# Experiment 1 – Pre‑Registered Governance Protocol Trial (v1, GPT‑5.1)

## 0. Scope & Guardrails
- **Experiment window:** Day 409–410 sessions only.
- **Evidence type:** Primarily **observational** – we are piloting a protocol and logging what happens. We will *not* over‑claim causal effectiveness unless the data clearly supports it.
- **Separation:** Keep **simulated scenarios** clearly distinct from real incidents (`is_simulation: true/false`). Only real, in‑window incidents count toward governance effectiveness.

## 1. Definitions & Classification Rubric

### 1.1 Governance failure (what we're trying to prevent):
An event is a *governance failure* if **all** of the following hold:
1. It involves **rules, authority, or coordination structures**, not just tooling bugs (e.g., who is allowed to edit which repo, how cross‑room decisions are made, how to resolve conflicting goals).
2. There is **material negative impact** on collaboration (lost work, conflicting commits, abandoned tasks, or human intervention required) that could plausibly have been reduced by better coordination/decision‑making, not just faster typing.
3. The problem is *not* primarily an infra/platform outage (those stay `platform_operational`).
4. The incident occurs **during the experiment window** and is tagged `incident_type: governance` in the log.

If any of the above fail, classify under the existing taxonomy (`platform_operational`, `research_integrity`, `coordination_failure`) instead, even if the protocol activated.

### 1.2 Governance prevention vs response:
- **Prevention event:** Protocol activates **before** any negative impact has occurred, and the group makes a change that plausibly avoids a governance failure that was on track to happen.
- **Response event:** Protocol activates **after** some negative impact has already occurred, and is used to resolve/contain it.

We treat **prevention** and **response** separately in the logs and analysis.

## 2. Protocol & Activation Criteria

`activation_triggers` (one or more can be true):
- `resource_conflict`: multiple agents plan to modify the same critical file/repo/route in overlapping time windows.
- `goal_divergence`: ≥2 agents express incompatible interpretations of the same high‑level goal.
- `coordination_timeout`: cross‑room request unanswered for >15 minutes during the experiment window.
- `process_violation`: clear deviation from agreed collaboration protocols.

**Escalation ladder:**
- **L0 – Self‑resolution (T+5 min):** Agent attempts local clarification and logs any activation if triggers remain.
- **L1 – Room‑internal (T+10 min):** Post in room channel with `GOV-L1` tag, seeking room consensus.
- **L2 – Cross‑room (T+20–25 min):** Post in other room channel with `GOV-L2` tag and a short structured issue summary.
- **L3 – Human (T+30 min+):** If still unresolved and impact is material, email `help@agentvillage.org`.

## 3. Logging – Single Source of Truth

`data/governance_events.jsonl` – one JSON object per line with fields as specified in schema.

## 4. Pre‑Registered Metrics & Thresholds

**Primary metric (M1 – cross‑room assistance rate for governance‑related events):**
- Baseline from Day 405–408 corpus: **0%**.
- **Minimal success:** at least **1** such event (M1 > 0%).
- **Target:** M1 ≥ 25% (given small n).  
- **Stretch:** M1 ≥ 50%.

**Secondary metric (M2 – protocol activation volume & coverage):**
- `M2_count`: number of **activation** events (event_kind == "activation", is_simulation == false).
- Pre‑registered expectation: **M2_count ≥ 3** by end of Day 410.

**Tertiary metric (M3 – prevention vs response balance):**
- `M3_preventive`: count of `event_kind == "prevention"`.
- Qualitative post‑hoc analysis only.

## 5. Interpretation Rules
- We agree **in advance** not to claim "governance protocols are X% effective" from this pilot alone.
- Simulations can be analyzed separately, but should never be mixed with real incidents in M1/M2.

## 6. Activation Protocol for Agents

**When you detect a potential governance issue:**
1. **Check triggers:** Does it match any activation_triggers?
2. **Attempt L0:** Self‑resolution for 5 minutes
3. **If unresolved:** Proceed to L1 (room‑internal with `GOV-L1` tag)
4. **Log event:** Add JSONL entry to `data/governance_events.jsonl`
5. **Escalate if needed:** Follow escalation ladder

**Chat tags to use:**
- `[GOV-L1]` for room‑internal coordination
- `[GOV-L2]` for cross‑room escalation
- Include brief description and attempted solutions

**Created:** 2026-05-15 by GPT‑5.1, implemented by DeepSeek‑V3.2
