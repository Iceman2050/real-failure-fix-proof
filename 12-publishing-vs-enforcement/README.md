# 12 — Publishing a policy is not enforcing it (AgentGate)

**Real build (an honesty fix, shipped as a feature):** AgentGate's conformance tester was built to state, on its face, the distinction most tools blur — publishing a machine-readable agent policy at `/.well-known/agent-policy.json` states your rules; it does not enforce them. The live `/conformance` page carries the "publishing ≠ enforcement" card, verified live (200, card present, sitemap contains `/conformance`; suite 277 passed). Source: `hidden_files/tim-gabe-phase8-agentgate.md`.

**This tool** validates a policy document's structure and lints the claim made about it: any claim of enforcement drawn from publishing alone fails. Fixtures are a simulated policy + claim texts. Run: `python3 tool.py`.
