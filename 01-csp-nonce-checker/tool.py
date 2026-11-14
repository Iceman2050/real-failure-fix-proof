"""CSP nonce checker — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import re, sys
CSP = "default-src 'self'; script-src 'self' 'nonce-TESTNONCE'"
def check(html, csp):
    nonce = re.search(r"'nonce-([A-Za-z0-9+/=]+)'", csp)
    bad = []
    for m in re.finditer(r"<script(?![^>]*\bsrc=)([^>]*)>(.*?)</script>", html, re.S):
        if nonce and f'nonce="{nonce.group(1)}"' not in m.group(1):
            bad.append(m.group(2).strip()[:40])
    return bad
BAD = '<html><head><script src="/static/app.js"></script></head><body><script>window.altchaSolver()</script></body></html>'
GOOD = '<html><head><script src="/static/app.js"></script></head><body><script nonce="TESTNONCE">window.altchaSolver()</script><script src="https://cdn.example/solver.js" async></script></body></html>'
def main():
    b, g = check(BAD, CSP), check(GOOD, CSP)
    print(f"[{'PASS' if b else 'FAIL'}] broken page: bare inline solver script detected -> {b}")
    print(f"[{'PASS' if not g else 'FAIL'}] fixed page: every inline script carries the CSP nonce -> {g}")
    print("SELF-CHECK:", "PASS" if b and not g else "FAIL"); return 0 if b and not g else 1
if __name__ == "__main__": sys.exit(main())
