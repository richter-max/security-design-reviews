# Security Findings: Multi-Tenant SaaS

| ID | Threat | Category | Preconditions | Likelihood (1-5) | Impact (1-5) | Score | Risk Band | Detection Strategy | Mitigation Ref |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | **Tenant Hopping (IDOR)** | Broken Access Control | Valid Account on Tenant A | 4 (Likely) | 5 (Critical) | **20** | **Critical** | Anomaly Detection (User A accessing Resource B pattern) | [M-01](./mitigations.md#m-01-enforcement-of-tenant-isolation) |
| **TH-02** | **Noisy Neighbor DoS** | Resource Exhaustion | Valid Account, Scripting capability | 4 (Likely) | 3 (Moderate) | **12** | **High** | APM Spikes, DB CPU Alerts per User | [M-02](./mitigations.md#m-02-rate-limiting--quotas) |
| **TH-03** | **S3 Data Leak** | Information Disclosure | Knowledge of S3 Bucket Name | 4 (Likely) | 4 (Severe) | **16** | **High** | AWS GuardDuty (S3 Public Access) | [M-03](./mitigations.md#m-03-pre-signed-urls-for-s3-access) |
| **TH-04** | **Admin Account Takeover** | Identification & Auth | Phishing / Weak Password | 3 (Plausible) | 5 (Critical) | **15** | **High** | UEBA (Impossible Travel, Strange User-Agent) | [M-04](./mitigations.md) (MFA) |
