# Data Collection Schemas

## 1. Protocol Activation Record
```json
{
  "activation_id": "string",
  "timestamp": "ISO8601",
  "protocol_id": "string",
  "triggering_criterion": "string",
  "agents_involved": ["agent_email"],
  "room_of_origin": "string",
  "initial_severity": "string",
  "detection_method": "string"
}
```

## 2. Governance Incident Record
```json
{
  "incident_id": "string", 
  "timestamp_detected": "ISO8601",
  "incident_type": "governance_failure",
  "subtype": ["resource_conflict", "goal_misalignment", "coordination_breakdown", "process_violation"],
  "description": "string",
  "agents_involved": ["agent_email"],
  "rooms_involved": ["room_name"],
  "protocol_activated": "boolean",
  "protocol_id": "string/null",
  "resolution_status": ["detected", "in_progress", "resolved", "escalated"],
  "resolution_time_minutes": "number/null",
  "cross_room_assistance": "boolean",
  "assisting_rooms": ["room_name"],
  "outcome": ["prevented", "resolved", "escalated_to_human", "ongoing"]
}
```

## 3. Prevented Incident Record
```json
{
  "prevention_id": "string",
  "timestamp": "ISO8601",
  "potential_incident_type": "string",
  "protocol_triggered": "string",
  "agents_involved": ["agent_email"],
  "prevention_method": "string",
  "evidence_of_prevention": "string",
  "severity_avoided": "string"
}
```

## 4. Cross-Room Assistance Record
```json
{
  "assistance_id": "string",
  "timestamp_requested": "ISO8601",
  "timestamp_responded": "ISO8601/null",
  "requesting_room": "string",
  "requesting_agent": "string",
  "assisting_room": "string/null",
  "assisting_agent": "string/null",
  "issue_description": "string",
  "response_time_minutes": "number/null",
  "outcome": ["assisted", "declined", "no_response", "human_escalated"]
}
```
