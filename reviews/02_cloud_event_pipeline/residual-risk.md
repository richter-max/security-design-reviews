# Residual Risk Assessment

| ID | Threat | Initial | Mitigations | Residual | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | Log Injection | Critical | Strict Schema + Sanitization | Low | Defense in depth reduces likelihood significantly. |
| **TH-02** | Denial of Wallet | High | WAF + Cost Monitoring | Medium | Extremely distributed attacks are hard to stop completely without affecting legitimate users. Risk accepted as "Cost of doing business". |
| **TH-03** | Public S3 Bucket | High | Public Access Block (Org Policy) | Low | Managed via Terraform + AWS Config Rules. |
