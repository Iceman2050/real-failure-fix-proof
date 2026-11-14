"""Truncated-file guard (byte-identity restore checker) — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import hashlib, sys
PRISTINE = ("line-%04d\n" % 0) + "".join("line-%04d\n" % i for i in range(1, 2000)) + "TAIL-SENTINEL: end of file\n"
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def check(candidate, pristine):
    problems = []
    if len(candidate) < len(pristine): problems.append(f"shorter: {len(candidate)} < {len(pristine)} bytes (truncation shape)")
    if "TAIL-SENTINEL" not in candidate: problems.append("tail sentinel missing (file tail lost)")
    if digest(candidate) != digest(pristine): problems.append("hash differs from pristine reference")
    return problems
def main():
    truncated = PRISTINE[: len(PRISTINE) * 3 // 4]  # the disk-quota fault shape: tail lost
    p1 = check(truncated, PRISTINE)
    print(f"[{'PASS' if p1 else 'FAIL'}] truncated copy is caught: {p1}")
    restored = PRISTINE  # restored from the pristine branch tip / remote copy
    p2 = check(restored, PRISTINE)
    print(f"[{'PASS' if not p2 else 'FAIL'}] restored copy verifies byte-identical (sha256 match, tail sentinel present)")
    ok = bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
