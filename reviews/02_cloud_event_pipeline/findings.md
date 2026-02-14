# Security Findings: Cloud Event Pipeline

| ID | Threat | Category | Preconditions | Likelihood (1-5) | Impact (1-5) | Score | Risk Band | Detection Strategy | Mitigation Ref |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | **Log Injection (RCE/XSS)** | Injection | Payload reflected in Admin UI | 4 (Likely) | 5 (Critical) | **20** | **Critical** | Pattern Match (`<script>`, `${jndi:`) in Logs | [M-01](./mitigations.md#m-01-input-validation-events) |
| **TH-02** | **Denial of Wallet** | Resource Exhaustion | Distributed Botnet | 4 (Likely) | 3 (Moderate) | **12** | **High** | Cost Anomaly Detection (AWS Cost Explorer) | [M-02](./mitigations.md#m-02-infrastructure-protection) |
| **TH-03** | **S3 Public Bucket** | Config Error | Terraform Drift | 4 (Likely) | 4 (Severe) | **16** | **High** | AWS Config (s3-bucket-public-read-prohibited) | [M-03](./mitigations.md#m-03-data-integrity) |
