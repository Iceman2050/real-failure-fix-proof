# 03 — The rename that ran backwards (EvalScope vs EvalEgress)

**Real failure:** an audit report assumed the canonical name was *EvalScope* and the hub's *EvalEgress* tile was the error. Live verification reversed it: the product's own About page is titled "About EvalEgress" and states "EvalEgress was formerly called EvalScope" — the stale labels were in the directory, JSON-LD, portfolio and footer, and were all fixed toward EvalEgress (17 display replacements). Source: `hidden_files/TIM-GABE-PHASES-1-3-CHECKPOINT-2026-11-13.md`.

**This tool** encodes the lesson: the product's own live site is ground truth; every other surface is audited against it, never the reverse. Fixture labels are the real pre-fix state. Run: `python3 tool.py`.
