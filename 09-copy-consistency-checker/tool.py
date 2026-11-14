"""Marketing-copy vs directory consistency checker — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import sys
DIRECTORY_FAMILIES = ["Agent Control", "Business Protection", "AI Governance", "Commerce", "Creative"]  # the directory's real count: five
WORDS = {4: "four", 5: "five", 6: "six"}
STALE_COPY = "The fleet groups into four families."
FIXED_COPY = "The fleet groups into five families."
def check(copy, families):
    claimed = [w for n, w in WORDS.items() if f" {w} families" in copy]
    if not claimed: return ["no family-count claim found"]
    return [] if claimed[0] == WORDS[len(families)] else [f"copy claims '{claimed[0]} families' but the directory lists {len(families)}"]
def main():
    p1, p2 = check(STALE_COPY, DIRECTORY_FAMILIES), check(FIXED_COPY, DIRECTORY_FAMILIES)
    print(f"[{'PASS' if p1 else 'FAIL'}] stale hub copy caught: {p1}")
    print(f"[{'PASS' if not p2 else 'FAIL'}] corrected copy agrees with the directory count ({len(DIRECTORY_FAMILIES)})")
    ok = bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
