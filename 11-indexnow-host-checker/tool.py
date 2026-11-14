"""IndexNow host-key + sitemap-homepage checker — companion asset for Real Failure -> Fix -> Proof.
Stdlib only. Run: python3 tool.py  (self-check on bundled fixtures; exit 0 = tool behaves as specified)
Verdict honesty: fixtures are SIMULATED inputs modelled on the real incident; no live system is touched.
"""

import sys
SITEMAP_MISSING = '<?xml version="1.0"?><urlset><url><loc>https://breachhunter.getingeniousai.com/pricing</loc></url></urlset>'
SITEMAP_OK = '<?xml version="1.0"?><urlset><url><loc>https://breachhunter.getingeniousai.com/</loc></url><url><loc>https://breachhunter.getingeniousai.com/pricing</loc></url></urlset>'
def sitemap_problems(xml, homepage):
    return [] if f"<loc>{homepage}</loc>" in xml else [f"homepage {homepage} absent from sitemap"]
def key_problems(served_key_body, submitted_key, host_bound_key):
    problems = []
    if served_key_body.strip() != submitted_key: problems.append("key file body != submitted key (host verification cannot pass)")
    if host_bound_key and host_bound_key != submitted_key: problems.append("host is already bound to a DIFFERENT key -> IndexNow 403 UserForbiddedToAccessSite; resubmit under the host's own key")
    return problems
def main():
    sp1 = sitemap_problems(SITEMAP_MISSING, "https://breachhunter.getingeniousai.com/")
    sp2 = sitemap_problems(SITEMAP_OK, "https://breachhunter.getingeniousai.com/")
    print(f"[{'PASS' if sp1 else 'FAIL'}] sitemap missing its homepage is caught: {sp1}")
    print(f"[{'PASS' if not sp2 else 'FAIL'}] sitemap containing the homepage passes")
    kp = key_problems("fleetkey123", "fleetkey123", "domainguardsownkey")
    print(f"[{'PASS' if kp else 'FAIL'}] fleet key submitted to a host bound to its own key predicts the real 403: {kp}")
    kp2 = key_problems("domainguardsownkey", "domainguardsownkey", "domainguardsownkey")
    print(f"[{'PASS' if not kp2 else 'FAIL'}] resubmitting under the host's own key is clean (the applied fallback -> HTTP 200)")
    ok = bool(sp1) and not sp2 and bool(kp) and not kp2
    print("SELF-CHECK:", "PASS" if ok else "FAIL"); return 0 if ok else 1
if __name__ == "__main__": sys.exit(main())
