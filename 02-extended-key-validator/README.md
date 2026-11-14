# 02 — The wallet key the payment stack could not parse (zpub)

**Real failure:** the fleet BTCPay store held Aldo's wallet as a raw BIP84 **zpub** string; the stack cannot parse zpub version bytes, so crypto checkout derivation failed (`GET /v1/cryptos/BTC/derivations/<zpub>` → 400). **Fix:** the zpub was re-serialized to its xpub form — identical 74-byte key material, different version bytes — and derivation verified against the zpub-derived address set. Sources: `hidden_files/BTCPAY-REPAIR-CHECKPOINT-2026-11-12.md`, `hidden_files/masters-wave-2026-10-31/CRYPTO-READINESS-CHECKPOINT-2026-11-10.md`.

**This tool** classifies extended keys by version bytes, verifies the Base58Check checksum, and performs the same zpub→xpub re-serialization, proving the key bytes survive unchanged. The fixture key is synthetic (built from bytes 0–73); it is not a real wallet key. Run: `python3 tool.py`.
