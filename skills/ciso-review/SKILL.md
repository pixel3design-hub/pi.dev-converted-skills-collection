---
name: "ciso-review"
description: "Challenge a plan touching customer data, compliance or prod access. Use when asked or /skill:ciso-review."
---

# /skill:ciso-review — CISO Forcing Questions

## Running the Python tools

Run a tool with `python3 scripts/<tool>.py`. If `python` is blocked in this environment, put the same
arguments after `uv run --no-project python`. If `uv` is missing or blocked as well, stop and ask the
user to install it from https://docs.astral.sh/uv/getting-started/installation/.

**Command:** `/skill:ciso-review <plan>`

The risk-paranoid threat-modeler. Six questions before any production change that touches customer data or compliance scope.

## When to Run

- Before deploying any system that touches PII / PHI / cardholder data
- Before signing a new vendor with data access
- Before a compliance audit (SOC 2, ISO 27001, HIPAA, GDPR)
- Before any architecture decision crossing trust boundaries
- After any near-miss incident

## The Six CISO Questions

### 1. Threat Model
**What's the STRIDE threat model for this system, and which threat is most likely?**
- Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege.
- Pick the top 3 by likelihood × impact.

### 2. Blast Radius
**If this is fully compromised, what data is exposed and how many users are affected?**
- Worst case in plain English.
- Quantify in dollars via FAIR-based ALE.

### 3. Detection
**What signals indicate compromise, and how long until they're triggered (MTTD)?**
- Logs alone are not detection.
- Define the detection rule, the alert, and the on-call.

### 4. Response
**Is there an IR runbook for this scenario, and has it been tabletop-tested?**
- If no runbook: build one before ship.
- If untested: tabletop before ship.

### 5. Regulatory Window
**What's the regulator notification window if this scenario occurs?**
- GDPR: 72h. HIPAA: 60d. State breach laws vary.
- Pre-write the customer comms template.

### 6. Vendor & Supply Chain
**Which third-party vendors are in scope, and what's their security posture?**
- Subprocessor list current?
- DPAs in place?
- Last security review per vendor?

## Workflow

```bash
python3 ../ciso-advisor/scripts/risk_quantifier.py
python3 ../ciso-advisor/scripts/compliance_tracker.py
```

## Output Format

```markdown
# CISO Review: <plan>
**Date:** YYYY-MM-DD

## Threat Model
- Top threat: <STRIDE category> — <description>
- Likelihood: H/M/L | Impact: H/M/L
- ALE: $X / year

## Blast Radius
- Data exposed (worst case): <description>
- Users affected: N
- Estimated cost: $X

## Detection
- MTTD target: X hours
- Current MTTD: X hours
- Detection rule: <name>

## Response
- IR runbook: ✅ / ❌
- Last tabletop: <date>

## Regulatory
- Frameworks in scope: SOC 2 / ISO 27001 / HIPAA / GDPR
- Notification window: X hours/days

## Vendors
- New vendors added: N
- DPAs signed: N / N
- Security reviews complete: N / N

## Verdict
🟢 SHIP | 🟡 MITIGATE THEN SHIP | 🔴 BLOCK
```

## Routing

- `/skill:cto-review` — architecture alignment
- `/skill:gc-review` — DPA, regulatory implications
- `/skill:decide` — log risk acceptance
- `/skill:boardroom` — for CRITICAL risks

## Related

- Agent: [`cs-ciso-advisor`](../../agents/cs-ciso-advisor.md)
- Skill: [`ciso-advisor`](../ciso-advisor/SKILL.md)
- Compliance: `../../../ra-qm-team/`

---

**Version:** 1.0.0
