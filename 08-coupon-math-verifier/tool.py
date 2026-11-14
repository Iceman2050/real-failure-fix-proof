"""Coupon-math verifier — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import sys
PLANS = {"Pro": 49, "Team": 149}
RULED = {"Pro": 29, "Team": 99, "expiry_utc": "2026-11-27T03:54:00Z"}  # Aldo's ruled FOUNDING targets
AS_CREATED = {"discounts": {"Pro": 20, "Team": 20}, "expiry_utc": "2026-11-27T00:00:00Z"}  # one $20 discount covering both plans
AS_SPEC = {"discounts": {"Pro": 20, "Team": 50}, "expiry_utc": "2026-11-27T03:54:00Z"}
def verify(coupon):
    problems = []
    for plan, price in PLANS.items():
        final = price - coupon["discounts"].get(plan, 0)
        if final != RULED[plan]: problems.append(f"{plan}: ${price} - ${coupon['discounts'].get(plan, 0)} = ${final}, ruled target is ${RULED[plan]}")
    if coupon["expiry_utc"] != RULED["expiry_utc"]: problems.append(f"expiry {coupon['expiry_utc']} != ruled window end {RULED['expiry_utc']}")
    return problems
def main():
    p1, p2 = verify(AS_CREATED), verify(AS_SPEC)
    print(f"[{'PASS' if p1 else 'FAIL'}] as-created coupon caught: {p1}")
    print(f"[{'PASS' if not p2 else 'FAIL'}] per-plan spec coupon ($20 Pro / $50 Team, expiry = window end) verifies clean")
    ok = bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
