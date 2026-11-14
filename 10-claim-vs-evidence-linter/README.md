# 10 — The recheck that hadn't happened (scheduled ≠ done)

**Real failure:** in the Phase 4 Second-Visit work, a status line presented DomainGuard's first scheduled recheck — due **2026-11-20** — in language that read as settled state. The checkpoint retracted it to the honest form: "No recheck data is fabricated — for the capstone's example.com report, whose first scheduled recheck falls due 2026-11-20, the page shows exactly its real state," with explicit render states for *no recheck yet* vs *verified resolved* vs *still live*. Source: `hidden_files/TIM-GABE-PHASE4-CHECKPOINT-2026-11-13.md`.

**This tool** lints status text for the failure shape: a dated, future/scheduled event written in completed language. It is a wording linter over fixture sentences — it judges language, not live data, and says so. Run: `python3 tool.py`.
