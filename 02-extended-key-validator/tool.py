"""Extended public key (xpub/zpub) validator + re-serializer — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import hashlib, sys
ALPH = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
VERSIONS = {0x0488B21E: "xpub (BIP44, legacy)", 0x04B24746: "zpub (BIP84, native segwit)", 0x049D7CB2: "ypub (BIP49)"}
def b58decode(s):
    n = 0
    for c in s: n = n * 58 + ALPH.index(c)
    raw = n.to_bytes((n.bit_length() + 7) // 8, "big")
    pad = len(s) - len(s.lstrip("1"))
    return b"\x00" * pad + raw
def b58check_encode(payload):
    chk = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    data = payload + chk; n = int.from_bytes(data, "big"); out = ""
    while n: n, r = divmod(n, 58); out = ALPH[r] + out
    return "1" * (len(data) - len(data.lstrip(b"\x00"))) + out
def parse(key):
    raw = b58decode(key)
    payload, chk = raw[:-4], raw[-4:]
    assert hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4] == chk, "bad checksum"
    assert len(payload) == 78, f"payload {len(payload)} bytes, expected 78"
    return int.from_bytes(payload[:4], "big"), payload
def reserialize(key, target_version):
    _, payload = parse(key)
    return b58check_encode(target_version.to_bytes(4, "big") + payload[4:])
def main():
    # Deterministic synthetic 78-byte payload (NOT a real wallet key) wearing zpub version bytes.
    payload = bytes.fromhex("04b24746") + bytes(range(74))
    zpub = b58check_encode(payload)
    ver, _ = parse(zpub)
    print(f"[INFO] fixture key classifies as: {VERSIONS.get(ver, hex(ver))}")
    xpub = reserialize(zpub, 0x0488B21E)
    ver2, payload2 = parse(xpub)
    same = payload2[4:] == payload[4:]
    print(f"[{'PASS' if same else 'FAIL'}] zpub->xpub re-serialization keeps the 74 key bytes identical: {same}")
    print(f"[{'PASS' if ver2 == 0x0488B21E else 'FAIL'}] re-serialized key classifies as xpub for stacks that reject zpub version bytes")
    ok = same and ver2 == 0x0488B21E
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
