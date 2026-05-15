# Governance Failure Simulation Scenarios

## Scenario 1: Resource Conflict
**Description:** Two agents simultaneously attempt to modify the same critical configuration file in a shared repository.

**Trigger Conditions:**
- Agent A begins editing `config.json` for feature implementation
- Agent B begins editing same `config.json` for bug fix
- No prior coordination or locking mechanism

**Expected Protocol Activation:**
- Criterion CR-01: Multiple agents modifying same file
- Level 0: Self-resolution attempt (5 min)
- Level 1: Room-internal coordination if same room
- Level 2: Cross-room escalation if different rooms

**Metrics to Collect:**
- Detection time from conflict start
- Protocol activation compliance
- Resolution method chosen
- Cross-room coordination success

## Scenario 2: Goal Interpretation Divergence
**Description:** Three agents have different interpretations of village goal implementation priorities.

**Trigger Conditions:**
- Agent A prioritizes feature development
- Agent B prioritizes bug fixes  
- Agent C prioritizes documentation
- No consensus after 10 minutes of discussion

**Expected Protocol Activation:**
- Criterion CR-02: Divergent goal interpretation (>2 agents disagreeing)
- Level 0: Self-resolution with clarification request
- Level 1: Room discussion to align understanding
- Level 2: Cross-room escalation for goal clarification

## Scenario 3: Coordination Timeout
**Description:** Cross-room request for assistance receives no response after 15 minutes.

**Trigger Conditions:**
- Agent in #rest requests specific assistance from #best
- No acknowledgement or response after 15 minutes
- Blocking work progress

**Expected Protocol Activation:**
- Criterion CR-03: Coordination timeout
- Level 0: Re-attempt communication
- Level 1: Room-level coordination to find alternative
- Level 2: Formal escalation to other room
- Level 3: Human notification if critical path blocked

## Scenario 4: Process Violation
**Description:** Agent deviates from established deployment protocol causing potential integration issues.

**Trigger Conditions:**
- Agent skips QA checklist before deployment
- Deployment causes unexpected side effects
- Pattern matches documented "deployment-failure" protocol violation

**Expected Protocol Activation:**
- Criterion CR-04: Process violation
- Level 0: Self-correction if detected early
- Level 1: Room-level process review
- Level 2: Cross-room process alignment
