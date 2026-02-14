# Residual Risk Assessment

| ID | Threat | Initial | Mitigations | Residual | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | Indirect Prompt Injection | **Critical** | Prompt Hardening | **High** | Prompt Injection is an unsolved research problem. Hardening helps, but is not a guarantee. We rely on HITL (M-01) for safety. |
| **TH-02** | SSRF (Metadata) | **Critical** | Network Isolation | **Low** | Network policies are deterministic and effective. |
| **TH-03** | Excessive Agency | **High** | Human-in-the-Loop | **Medium** | Users might click "Approve" without reading ("Alert Fatigue"). |
