"""Blocked-mail-provider fallback planner — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import sys
PROVIDER = {"name": "Mailjet", "send_status": 401, "error": "mj-0001", "verified_success_response": False}
def plan(p):
    if p["send_status"] < 400 and p["verified_success_response"]:
        return ["SEND via provider (verified success response on record)"]
    return [
        f"DO NOT claim any send as sent: provider returns {p['send_status']} {p['error']} with no verified success response",
        "Fulfil manually: mint the license key per the confirmed-payment rule",
        "Deliver by hand via the working channel (Gmail / WhatsApp)",
        "Log the manual fulfilment against the order before marking it fulfilled",
        "Re-probe the provider on the next run; resume automated sends only after a verified success response",
    ]
def main():
    steps = plan(PROVIDER)
    for s in steps: print(" -", s)
    claims_sent = any(s.startswith("SEND via") for s in steps)
    has_manual = any("Fulfil manually" in s for s in steps)
    print(f"[{'PASS' if not claims_sent else 'FAIL'}] blocked provider (401 mj-0001) produces NO 'sent' claim")
    print(f"[{'PASS' if has_manual else 'FAIL'}] manual fulfilment doctrine is emitted instead")
    ok = (not claims_sent) and has_manual
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
