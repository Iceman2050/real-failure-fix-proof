"""Resolved-state routing checker — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import sys
# Case fixtures: (tracked_in_workspace, has_lifecycle_event) -> expected HTTP status
CASES = [
    ({"tracked": True,  "has_event": True},  200),  # live change page
    ({"tracked": False, "has_event": True},  200),  # RESOLVED mode: was tracked, migrated away, event on record
    ({"tracked": False, "has_event": False}, 404),  # genuinely unknown to this workspace
    ({"tracked": True,  "has_event": False}, 200),  # tracked, no event yet
]
def buggy_route(c):   # the pre-fix rule: 404 whenever not currently tracked
    return 200 if c["tracked"] else 404
def fixed_route(c):   # the shipped rule: 404 only when no signal AND no lifecycle event
    return 404 if (not c["tracked"] and not c["has_event"]) else 200
def run(route):
    return [(c, exp, route(c)) for c, exp in CASES]
def main():
    b = run(buggy_route); f = run(fixed_route)
    b_bad = [r for r in b if r[1] != r[2]]; f_bad = [r for r in f if r[1] != r[2]]
    print(f"[{'PASS' if b_bad else 'FAIL'}] pre-fix rule fails {len(b_bad)} case(s): resolved state (untracked, event on record) returned 404 after a successful migration")
    print(f"[{'PASS' if not f_bad else 'FAIL'}] fixed rule matches all {len(CASES)} expected states (resolved renders 200, truly unknown still 404)")
    ok = bool(b_bad) and not f_bad
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
