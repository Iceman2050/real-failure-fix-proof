"""Foreign-key delete-route checklist runner — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import re, sys
# Simulated route sources, modelled on the real defect: production DB enforces FKs, the test DB did not.
BUGGY = """
@app.delete('/account')
def delete_account(user):
    db.execute('DELETE FROM users WHERE id=?', user.id)
    return {'ok': True}
"""
FIXED = """
@app.delete('/account')
def delete_account(user):
    db.execute('DELETE FROM api_keys WHERE user_id=?', user.id)
    db.execute('DELETE FROM sessions WHERE user_id=?', user.id)
    db.execute('DELETE FROM users WHERE id=?', user.id)
    return {'ok': True}
"""
CHILD_TABLES = {"api_keys": "user_id", "sessions": "user_id"}  # tables holding FKs to users
def check(src):
    order = [m.start() for m in re.finditer(r"DELETE FROM (\w+)", src)]
    tables = re.findall(r"DELETE FROM (\w+)", src)
    problems = []
    if "users" in tables:
        parent_pos = tables.index("users")
        for child in CHILD_TABLES:
            if child not in tables: problems.append(f"child table {child} never deleted -> FK violation on key-holding accounts")
            elif tables.index(child) > parent_pos: problems.append(f"{child} deleted AFTER parent -> FK violation")
    return problems
def main():
    p1, p2 = check(BUGGY), check(FIXED)
    print(f"[{'PASS' if p1 else 'FAIL'}] buggy route caught: {p1}")
    print(f"[{'PASS' if not p2 else 'FAIL'}] fixed route deletes children before the parent row: {p2}")
    ok = bool(p1) and not p2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
