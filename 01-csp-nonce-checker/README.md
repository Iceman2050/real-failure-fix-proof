# 01 — The signup form that could not be solved (CSP nonce)

**Real failure:** DomainGuard's signup ran a bare inline ALTCHA solver script under a strict nonce Content-Security-Policy. The browser refused to execute it, so signup was dead. **Fix:** one-line change so the solver carries the request nonce (commit `64067c7f`, deployed, live re-proof passed — nonce pair matched; solved signup reaches the mail wall). Source: `hidden_files/HANDBACK-RECOVERY-2026-11-11.md`.

**This tool** parses an HTML page against a nonce CSP and flags inline scripts with no matching nonce — the exact failure shape. Fixtures are simulated pages modelled on the incident. Run: `python3 tool.py`.
