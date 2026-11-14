# 04 — The file that lost its tail (disk-quota truncation)

**Real failures (same fault class, twice):** a disk-quota write fault truncated `boundaryvault/app/main.py` from 3,654 → 3,263 lines, losing the file tail (recovered from the pristine deploy-branch tip; restored entry verified byte-identical by diff; suite 216 passed — source: `hidden_files/GSC-IMPLEMENT-CHECKPOINT-2026-11-13.md`); and a restore command truncated DomainGuard's `report_waiting.html` to 0 bytes mid-lane (restored byte-identical from the GitLab remote copy and proven by the live read-back — source: `hidden_files/TIM-GABE-CAPSTONE-NITS-CHECKPOINT-2026-11-13.md`).

**This tool** is the guard the incidents argue for: never trust a restored file — compare length, tail sentinel and SHA-256 against the pristine reference. Fixtures are simulated file bodies with the real fault shape. Run: `python3 tool.py`.
