# 06 — "Your migration worked" → 404 (ModelMinder)

**Real failure:** after a user successfully migrated away from a deprecated model, ModelMinder's change page 404'd — the route treated "no longer tracked" as "does not exist", erasing the resolved state the user had earned. **Fix:** the page 404s only when there is no signal/model AND no lifecycle event for the workspace; untracked-but-recorded renders in resolved mode with the verification record (shipped in the Phase 5 Change Impact workflow, commit `22b46a76`; 6 new tests). Source: `hidden_files/tim-gabe-phase5-B-modelminder.md`.

**This tool** runs the routing rule against the four real state combinations as fixtures and shows the pre-fix rule failing exactly the resolved case. Run: `python3 tool.py`.
