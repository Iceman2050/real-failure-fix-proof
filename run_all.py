#!/usr/bin/env python3
"""Run every companion asset's self-check. Exit 0 only if all 12 pass."""
import glob, os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
tools = sorted(glob.glob(os.path.join(here, "*/tool.py")))
failed = []
for t in tools:
    print(f"\n=== {os.path.relpath(t, here)} ===")
    r = subprocess.run([sys.executable, t], capture_output=True, text=True)
    print(r.stdout, end="")
    if r.returncode != 0: failed.append(t)
print(f"\nTOTAL: {len(tools) - len(failed)}/{len(tools)} companion assets PASS")
sys.exit(1 if failed else 0)
