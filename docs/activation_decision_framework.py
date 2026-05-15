#!/usr/bin/env python3
"""
Governance Activation Decision Framework
For determining whether a potential trigger qualifies as distinct 3rd activation
"""

import json
from datetime import datetime

def load_existing_activations():
    events = []
    try:
        with open('data/governance_events.jsonl', 'r') as f:
            for line in f:
                if line.strip():
                    event = json.loads(line.strip())
                    if (event.get('is_simulation') == False and 
                        event.get('event_kind') == 'activation'):
                        events.append(event)
    except:
        pass
    return events

def evaluate_potential_activation(trigger_description, context):
    """
    Evaluate whether a potential trigger qualifies as distinct activation
    Returns tuple: (qualifies, reasoning, confidence)
    """
    existing = load_existing_activations()
    
    criteria = {
        "new_trigger_pattern": False,
        "distinct_activation_moment": False, 
        "real_coordination_friction": False,
        "distinct_resolution_episode": False,
        "different_from_previous": False
    }
    
    reasoning = []
    
    # Check against existing activations
    if len(existing) >= 2:
        # Compare with GOV-004 and GOV-006
        last_activation = existing[-1]  # GOV-006
        second_last = existing[-2]  # GOV-004
        
        # Analyze differences
        last_desc = last_activation.get('description', '')
        second_desc = second_last.get('description', '')
        
        criteria["different_from_previous"] = (
            "velocity" not in trigger_description.lower() or
            "200+" in trigger_description or 
            "1M" in trigger_description or
            "8,000" in trigger_description
        )
        
        if criteria["different_from_previous"]:
            reasoning.append("Differs from previous activations in magnitude/type")
        else:
            reasoning.append("Similar pattern to previous activations")
    
    # Team consensus requirements
    reasoning.append("Requires team consensus on distinctiveness")
    reasoning.append("Needs evidence of real coordination friction")
    reasoning.append("Should have explicit activation moment")
    
    # Determine if qualifies
    qualifies = all([
        criteria["different_from_previous"],
        "real coordination friction" in context.lower(),
        "explicit activation" in context.lower()
    ])
    
    confidence = 0.7 if qualifies else 0.3
    
    return qualifies, "\n".join(reasoning), confidence

# Example evaluations
print("=== GOVERNANCE ACTIVATION DECISION FRAMEWORK ===\n")

test_cases = [
    {
        "trigger": "Liminal 200+ features sync coordination",
        "context": "22+ feature gap with Edge Garden, routine update completed without friction, handled within existing workflow"
    },
    {
        "trigger": "Persistence 1M final push coordination", 
        "context": "85K remaining to reach 1M, extreme velocity, may require unique coordination approach"
    },
    {
        "trigger": "The Drift 8,000 journeys milestone sync",
        "context": "Roman numeral MMMMMMMM milestone, different workflow coordination potentially needed"
    },
    {
        "trigger": "Cross-room methodology disagreement with #best",
        "context": "#best responds with methodological critique, disagreement on standards requires governance coordination"
    }
]

for i, test in enumerate(test_cases, 1):
    qualifies, reasoning, confidence = evaluate_potential_activation(
        test["trigger"], test["context"]
    )
    print(f"Test Case {i}: {test['trigger']}")
    print(f"Context: {test['context']}")
    print(f"Qualifies as distinct activation: {'YES' if qualifies else 'NO'}")
    print(f"Confidence: {confidence:.1f}")
    print(f"Reasoning:\n{reasoning}")
    print("-" * 50 + "\n")

print("=== ACTIVATION LOGGING CRITERIA ===")
print("1. Distinct trigger pattern (different from previous activations)")
print("2. Explicit activation moment ([GOV-L1]/[GOV-L2] tag used)")
print("3. Real coordination friction (resource conflict, timing dispute, authority conflict)")
print("4. Distinct resolution episode (nontrivial governance decisions)")
print("5. Team consensus on distinctiveness")
