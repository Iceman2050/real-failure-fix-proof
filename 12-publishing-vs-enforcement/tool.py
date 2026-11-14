"""Publishing-vs-enforcement honesty checker — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import json, sys
POLICY = {"agents": [{"id": "shopping-agent", "access": "allow", "actions": ["read_catalog"], "terms": "attribution required"}]}
OVERCLAIM = "Our site enforces agent access rules: only listed agents can use it, and terms are enforced automatically."
HONEST_CLAIM = "Our site publishes a machine-readable agent policy at /.well-known/agent-policy.json. Publishing states the rules; it does not by itself enforce them — enforcement happens in the serving layer, which this document does not test."
def check(policy, claim):
    problems = []
    valid = isinstance(policy.get("agents"), list) and all("id" in a and "access" in a for a in policy["agents"])
    if not valid: problems.append("policy document invalid: agents[] entries need id + access")
    low = claim.lower()
    if "enforc" in low and "does not by itself enforce" not in low and "not tested" not in low and "publishing states" not in low:
        problems.append("claim asserts enforcement from a published document alone — publishing != enforcement")
    return problems, valid
def main():
    p1, valid = check(POLICY, OVERCLAIM)
    p2, _ = check(POLICY, HONEST_CLAIM)
    print(f"[INFO] fixture policy document parses and is structurally valid: {valid} (that is ALL publishing proves)")
    print(f"[{'PASS' if p1 else 'FAIL'}] enforcement overclaim caught: {p1}")
    print(f"[{'PASS' if not p2 else 'FAIL'}] honest publishing claim passes")
    ok = valid and bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
