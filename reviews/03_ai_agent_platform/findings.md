# Security Findings: AI Agent Platform

| ID | Threat | Category | Preconditions | Likelihood (1-5) | Impact (1-5) | Score | Risk Band | Detection Strategy | Mitigation Ref |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | **Indirect Prompt Injection** | LLM Vulnerability | Agent reads untrusted content | 5 (Trivial) | 5 (Critical) | **25** | **Critical** | Prompt Guard / LLM-as-Judge (Output Analysis) | [M-03](./mitigations.md#m-03-system-prompt-hardening) |
| **TH-02** | **SSRF (Metadata Access)** | Network Security | "Browse" tool enabled | 4 (Likely) | 4 (Severe) | **16** | **High** | Network Egress Logs (blocked IPs) | [M-02](./mitigations.md#m-02-tool-sandboxing) |
| **TH-03** | **Excessive Agency** | Authorization | User approves action blind | 3 (Plausible) | 5 (Critical) | **15** | **High** | Audit Logs (Action Approval Rates) | [M-01](./mitigations.md#m-01-human-in-the-loop-hitl) |
| **TH-04** | **Data Exfiltration** | Info Disclosure | Agent has "Email" tool | 3 (Plausible) | 4 (Severe) | **12** | **High** | DLP scanning on outgoing emails | [M-01](./mitigations.md) (HITL) |
