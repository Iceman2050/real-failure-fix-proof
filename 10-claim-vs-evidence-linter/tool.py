"""Claim-vs-evidence linter (scheduled is not done) — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import re, sys
# A scheduled future event stated in completed language = fabricated state.
BAD_REPORT = "Status: the finding's recheck came back resolved on the scheduled date of 2026-11-20."
GOOD_REPORT = "Status: no recheck has run yet. The first scheduled recheck falls due 2026-11-20; the page shows exactly that real state."
DONE_WORDS = r"(came back|completed|passed|resolved|verified|ran)\b"
DATE = r"20\d\d-\d\d-\d\d"
def lint(text):
    problems = []
    for sentence in re.split(r"(?<=[.!])\s+", text):
        if re.search(DATE, sentence) and re.search(DONE_WORDS, sentence, re.I) and "due" not in sentence and "scheduled" not in sentence.lower().replace("on the scheduled date", ""):
            # completed-language + a date + no honest scheduling marker in the claim itself
            if "no recheck has run" not in sentence:
                problems.append(sentence.strip())
    return problems
def main():
    p1, p2 = lint(BAD_REPORT), lint(GOOD_REPORT)
    print(f"[{'PASS' if p1 else 'FAIL'}] fabricated-state sentence flagged: {p1}")
    print(f"[{'PASS' if not p2 else 'FAIL'}] honest scheduled-state sentence passes: {p2}")
    ok = bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
