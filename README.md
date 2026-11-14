# real-failure-fix-proof

Twelve real failures from a live SaaS fleet — each with the fix that shipped and a small runnable tool that catches the failure class. Every incident below is documented in the fleet's own checkpoint records; each folder's README names its source.

This repo is the companion-asset set for the video series **"Real Failure → Fix → Proof"** (merged with "Build, Break, Fix, Prove"): every episode shows the real failure, the fix that was built, and the proof artifact — and links here so a viewer can run the checker themselves.

## Verdict honesty — read this first

- The **incidents are real** and sourced per folder. The **tools run on fixtures**: simulated inputs modelled on each incident's failure shape. No tool touches a live system, a real wallet, a real mailbox or a real customer account, and none claims to.
- A `PASS` from a tool means "this checker correctly flags the broken fixture and accepts the fixed fixture" — nothing more.
- One synthetic extended key appears in folder 02, built from bytes 0–73 for the re-serialization proof. It is not a real wallet key and controls no funds.

## The twelve

| # | Failure | The fix that shipped | Run |
|---|---|---|---|
| 01 | Signup killed by a bare inline script under a nonce CSP (DomainGuard) | Solver carries the request nonce (commit `64067c7f`) | `python3 01-csp-nonce-checker/tool.py` |
| 02 | BTCPay could not parse the wallet's zpub version bytes | Re-serialized zpub→xpub, key bytes identical, derivation verified | `python3 02-extended-key-validator/tool.py` |
| 03 | A rename audit ran backwards (EvalScope vs EvalEgress) | The product's own site is ground truth; 17 stale labels fixed toward EvalEgress | `python3 03-name-direction-audit/tool.py` |
| 04 | Disk-quota faults truncated live source files | Restored byte-identical from pristine copies, hash/diff-verified | `python3 04-truncated-file-guard/tool.py` |
| 05 | Account delete 500'd for key-holding accounts (HomeShield) | Child rows deleted before the parent (commit `80ea2af3`) | `python3 05-fk-delete-checklist/tool.py` |
| 06 | A successful migration ended at a 404 (ModelMinder) | Resolved mode renders; 404 only for the truly unknown | `python3 06-resolved-state-404-checker/tool.py` |
| 07 | Mail provider blocked (Mailjet 401 mj-0001) | Manual-fulfilment doctrine: no "sent" claim without a verified success response | `python3 07-mail-fallback-planner/tool.py` |
| 08 | FOUNDING coupon discounted the wrong plan ($129 vs ruled $99) | Per-plan coupon math verified against the ruled targets before go-live | `python3 08-coupon-math-verifier/tool.py` |
| 09 | Hub copy said "four families"; the directory listed five | Copy corrected to the directory count, verified live | `python3 09-copy-consistency-checker/tool.py` |
| 10 | A scheduled recheck (due 2026-11-20) was stated as settled state | Retracted to honest states: not run yet / verified / still live | `python3 10-claim-vs-evidence-linter/tool.py` |
| 11 | IndexNow 403: the host was bound to a different key | Resubmitted under the host's own key → 200 | `python3 11-indexnow-host-checker/tool.py` |
| 12 | "We enforce agent rules" — from a published document alone | AgentGate's conformance tester states publishing ≠ enforcement on its face | `python3 12-publishing-vs-enforcement/tool.py` |

## Run everything

```bash
git clone https://github.com/Iceman2050/real-failure-fix-proof
cd real-failure-fix-proof
python3 run_all.py   # 12/12 self-checks; Python 3.9+, standard library only, no network
```

## License

MIT. Built by Ingenious AI — https://getingeniousai.com

## Ingenious AI platforms

Built by Ingenious AI. The fleet — every platform does one job:

- [Agent Auth Gateway](https://authgateway.getingeniousai.com) · [MandateGuard](https://mandateguard.getingeniousai.com) · [Agentic Receipts](https://agentic-receipts.getingeniousai.com) · [Agent Flight Recorder](https://flightrecorder.getingeniousai.com) · [TrustGate](https://trustgate.getingeniousai.com) · [BoundaryVault](https://boundaryvault.getingeniousai.com) · [Rogue-Agent Defense](https://rogue-defense.getingeniousai.com) · [AgentGate](https://agentgate.getingeniousai.com) · [Agent Passport](https://agentpassport.getingeniousai.com) · [HomeShield](https://homeshield.getingeniousai.com) · [AgentBlock](https://agentblock.getingeniousai.com) · [ChatBreaker](https://chatbreaker.getingeniousai.com) · [EvalEgress](https://evalscope.getingeniousai.com) · [CompanionGuard](https://companionguard.getingeniousai.com)
- [DomainGuard](https://domainguard.getingeniousai.com) · [BreachHunter](https://breachhunter.getingeniousai.com) · [TakedownCoop](https://takedowncoop.getingeniousai.com) · [WireWatch](https://wirewatch.getingeniousai.com) · [CallbackShield](https://callbackshield.getingeniousai.com) · [Vibe-Code Audit](https://vibe-audit.getingeniousai.com)
- [DisclosureGuard](https://disclosureguard.getingeniousai.com) · [ProvenanceGuard](https://provenanceguard.getingeniousai.com) · [ADMT](https://admt.getingeniousai.com) · [ReviewDesk](https://reviewdesk.getingeniousai.com) · [CRAClock](https://craclock.getingeniousai.com) · [AI Audit Exchange](https://auditexchange.getingeniousai.com) · [TermsWatch](https://termswatch.getingeniousai.com) · [ModelMinder](https://modelminder.getingeniousai.com) · [ReviewProof](https://reviewproof.getingeniousai.com) · [EInvoice](https://einvoice.getingeniousai.com) · [DueLadder](https://dueladder.getingeniousai.com) · [OutcomeMeter](https://outcomemeter.getingeniousai.com)
- [AgentReady](https://agentready.getingeniousai.com) · [Store Audit](https://storeaudit.getingeniousai.com) · [ContentCraft AI](https://contentcraft.getingeniousai.com) · [GEOFixer](https://geofixer.getingeniousai.com)
- Full directory: https://getingeniousai.com/platforms
