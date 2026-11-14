"""Product-name direction audit — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import json, sys
# Fixture: what each source calls the product. The product's OWN live site is ground truth.
SOURCES = {
    "product_own_site_about_page": "EvalEgress",   # ground truth: 'EvalEgress was formerly called EvalScope'
    "hub_tile": "EvalEgress",
    "directory_listing": "EvalScope",              # stale label (the defect)
    "registry_canonical_name": "EvalScope",        # the report's assumed direction (reversed)
}
def audit(sources):
    truth = sources["product_own_site_about_page"]
    return truth, {k: v for k, v in sources.items() if v != truth}
def main():
    truth, stale = audit(SOURCES)
    print(f"[INFO] canonical name per the product's own site: {truth}")
    for k in stale: print(f"[FAIL] {k} still says '{stale[k]}' — rename direction is TOWARD '{truth}', not away from it")
    fixed = dict(SOURCES, directory_listing=truth, registry_canonical_name=truth)
    _, stale2 = audit(fixed)
    print(f"[{'PASS' if not stale2 else 'FAIL'}] after fixing labels to the ground-truth name: {len(stale2)} stale surfaces")
    ok = bool(stale) and not stale2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
