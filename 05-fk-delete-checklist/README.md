# 05 — Delete my account → 500 (foreign keys)

**Real failure:** HomeShield's account-delete route returned 500 for any account holding API keys — the production database enforces foreign keys, the route deleted the parent row first, and the test harness's SQLite engine did not enforce FKs, so the suite could not reproduce it. **Fix:** delete child rows before the parent (commit `80ea2af3`, live-verified; suite 236 passed). Source: `hidden_files/READINESS-CHECKPOINT-2026-11-12.md`.

**This tool** statically checks a delete route (simulated source fixtures) for the child-before-parent ordering the production DB demands. It is a checklist runner, not a database test — labelled as such. Run: `python3 tool.py`.
