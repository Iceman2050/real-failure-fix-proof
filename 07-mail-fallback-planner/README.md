# 07 — The mail provider said no (Mailjet mj-0001)

**Real failure:** the fleet Mailjet account was blocked for sends (401, error `mj-0001`, verified 2026-11-06; compliance ticket #4334604 still open at the time of writing) — signup verification mail fleet-wide went down with it. **Fix (doctrine, still in force):** no Mailjet send is claimed as sent without a verified success response, and fleet sale fulfilment is MANUAL — license key minted per the confirmed-payment rule, delivered by hand via Gmail/WhatsApp. Sources: `hidden_files/MAILJET-REPLY-CHECKPOINT-2026-11-10.md`, `hidden_files/MAILJET-CLARIFICATION-DRAFT-2026-11-12.md`, MEMORY.md "MAILJET BLOCK + MANUAL FULFILLMENT".

**This tool** turns the doctrine into a runnable planner: feed it a provider status fixture and it refuses to emit a "sent" claim for a blocked provider and emits the manual path instead. Run: `python3 tool.py`.
