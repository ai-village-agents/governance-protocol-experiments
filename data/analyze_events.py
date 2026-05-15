#!/usr/bin/env python3
"""
Governance Events Analysis Tool
Analyzes governance_events.jsonl for Experiment 1 metrics
"""

import json
from collections import defaultdict
from datetime import datetime

def load_events(filepath='governance_events.jsonl'):
    events = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                events.append(json.loads(line))
    return events

def analyze_metrics(events):
    """Calculate M1, M2, M3 metrics per pre-registered protocol"""
    
    # Separate simulations from real events
    real_events = [e for e in events if not e.get('is_simulation', False)]
    sim_events = [e for e in events if e.get('is_simulation', False)]
    
    # M1: Cross-room assistance rate for governance events
    gov_events = [e for e in real_events 
                  if e.get('incident_type') == 'governance' 
                  and e.get('window_status') == 'in-window']
    
    gov_with_assist = [e for e in gov_events if e.get('cross_room_assistance', False)]
    
    if gov_events:
        m1 = len(gov_with_assist) / len(gov_events) * 100
        m1_status = "MEASURED"
    else:
        m1 = None
        m1_status = "NO EMPIRICAL BASELINE (0 governance events)"
    
    # M2: Protocol activation count
    activations = [e for e in real_events if e.get('event_kind') == 'activation']
    m2_count = len(activations)
    m2_target = 3
    m2_status = "✅ MET" if m2_count >= m2_target else f"⏳ {m2_count}/{m2_target}"
    
    # M3: Prevention events
    preventions = [e for e in real_events if e.get('event_kind') == 'prevention']
    m3_count = len(preventions)
    
    return {
        'total_events': len(events),
        'real_events': len(real_events),
        'simulations': len(sim_events),
        'm1_rate': m1,
        'm1_status': m1_status,
        'm1_gov_events': len(gov_events),
        'm1_with_assist': len(gov_with_assist),
        'm2_count': m2_count,
        'm2_status': m2_status,
        'm3_preventions': m3_count,
        'by_level': defaultdict(int),
        'by_trigger': defaultdict(int),
        'by_room': defaultdict(int)
    }

def print_report(metrics):
    print("=" * 60)
    print("GOVERNANCE PROTOCOL EXPERIMENT 1 - METRICS REPORT")
    print("=" * 60)
    print(f"\n📊 EVENT SUMMARY:")
    print(f"   Total events logged: {metrics['total_events']}")
    print(f"   Real events: {metrics['real_events']}")
    print(f"   Simulations: {metrics['simulations']}")
    
    print(f"\n📈 M1 - CROSS-ROOM ASSISTANCE RATE:")
    if metrics['m1_rate'] is not None:
        print(f"   Rate: {metrics['m1_rate']:.1f}%")
        print(f"   Governance events: {metrics['m1_gov_events']}")
        print(f"   With cross-room assist: {metrics['m1_with_assist']}")
    else:
        print(f"   Status: {metrics['m1_status']}")
    
    print(f"\n📈 M2 - PROTOCOL ACTIVATIONS:")
    print(f"   Count: {metrics['m2_count']}")
    print(f"   Target: ≥3 by end of Day 410")
    print(f"   Status: {metrics['m2_status']}")
    
    print(f"\n📈 M3 - PREVENTION EVENTS:")
    print(f"   Count: {metrics['m3_preventions']}")
    print(f"   (Qualitative analysis only)")
    
    print("\n" + "=" * 60)

if __name__ == '__main__':
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else 'governance_events.jsonl'
    events = load_events(filepath)
    metrics = analyze_metrics(events)
    print_report(metrics)
