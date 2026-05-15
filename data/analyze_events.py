#!/usr/bin/env python3
"""
Governance Events Analysis Tool
Analyzes governance_events.jsonl for Experiment 1 metrics
"""

import json
import os
from collections import defaultdict
from datetime import datetime

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_events(filepath=None):
    if filepath is None:
        filepath = os.path.join(SCRIPT_DIR, 'governance_events.jsonl')
    events = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    continue  # Skip malformed lines
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
    cross_room_events = [e for e in gov_events if e.get('cross_room_assistance', False)]
    
    m1_numerator = len(cross_room_events)
    m1_denominator = len(gov_events)
    m1_rate = m1_numerator / m1_denominator if m1_denominator > 0 else None
    
    # M2: Real protocol activation count (target >= 3)
    real_activations = [e for e in real_events 
                        if e.get('event_kind') == 'activation'
                        and not e.get('is_simulation', False)]
    m2_count = len(real_activations)
    m2_target = 3
    m2_status = "✅" if m2_count >= m2_target else "⏳"
    
    # M3: Prevention events (qualitative)
    prevention_events = [e for e in real_events 
                         if e.get('governance_role') == 'prevention'
                         or e.get('event_kind') == 'prevention']
    
    return {
        'total_events': len(events),
        'real_events': len(real_events),
        'simulations': len(sim_events),
        'm1': {
            'cross_room_assisted': m1_numerator,
            'total_gov_events': m1_denominator,
            'rate': m1_rate,
            'status': 'undefined (no in-window incidents)' if m1_denominator == 0 else f'{m1_rate:.1%}'
        },
        'm2': {
            'count': m2_count,
            'target': m2_target,
            'status': f'{m2_status} {m2_count}/{m2_target}'
        },
        'm3': {
            'prevention_count': len(prevention_events),
            'events': [e.get('description', '')[:80] for e in prevention_events]
        }
    }

def print_report(metrics):
    """Print formatted analysis report"""
    print("=" * 60)
    print("GOVERNANCE EXPERIMENT 1 - METRICS ANALYSIS")
    print("=" * 60)
    print(f"\nTotal events logged: {metrics['total_events']}")
    print(f"  - Real events: {metrics['real_events']}")
    print(f"  - Simulations: {metrics['simulations']}")
    print(f"\n--- M1: Cross-Room Assistance Rate ---")
    print(f"Status: {metrics['m1']['status']}")
    print(f"  Cross-room assisted: {metrics['m1']['cross_room_assisted']}")
    print(f"  Total governance events: {metrics['m1']['total_gov_events']}")
    print(f"\n--- M2: Real Protocol Activations ---")
    print(f"Status: {metrics['m2']['status']} real activations")
    print(f"\n--- M3: Prevention Evidence ---")
    print(f"Prevention events: {metrics['m3']['prevention_count']}")
    for desc in metrics['m3']['events']:
        print(f"  - {desc}...")
    print("\n" + "=" * 60)

if __name__ == '__main__':
    import sys
    filepath = sys.argv[1] if len(sys.argv) > 1 else None
    events = load_events(filepath)
    metrics = analyze_metrics(events)
    print_report(metrics)
