# 08 — The coupon that discounted the wrong plan (FOUNDING)

**Real failure:** BreachHunter's FOUNDING coupon was created with one $20 discount covering both plans — Pro landed right ($49→$29) but Team composed to **$129 instead of the ruled $99** (the spec was $50 off Team), and its expiry was set to Nov 27 00:00 UTC instead of the window end 03:54 UTC. Source: `hidden_files/FREEMIUS-SETUP-CHECKPOINT-2026-11-13.md`.

**This tool** verifies coupon math before a coupon ever goes live: per-plan final prices against the ruled targets, plus expiry against the offer-window end. Prices and targets in the fixtures are the real recorded figures. Run: `python3 tool.py`.
