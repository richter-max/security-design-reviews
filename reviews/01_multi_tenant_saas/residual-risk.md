# Residual Risk Assessment

| ID | Threat | Initial Risk | Mitigations Applied | Residual Risk | Justification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | Tenant Hopping (IDOR) | **Critical** | Middleware Enforcement, Auto-Injection of ID | **Low** | The systemic fix (ORM hooks) removes developer error from the equation. |
| **TH-02** | Noisy Neighbor DoS | **High** | Rate Limiting, Fair Queueing | **Medium** | Burst traffic can still degrade performance, but total outage is unlikely. Accepted business risk. |
| **TH-03** | S3 Data Leak | **High** | Block Public Access, Pre-signed URLs | **Low** | Bucket is private by default. Access requires valid auth. |
| **TH-04** | Account Takeover | **High** | MFA (Optional) | **Medium** | We are NOT enforcing MFA for all tenants yet due to UX friction complaints. **This is an accepted risk for Q3.** |

## Open Questions / Follow-ups
1.  **MFA Enforcement**: When can we force MFA for admin accounts? (Target: Q4)
2.  **Encryption at Rest**: Are we using separate KMS keys per tenant? (Current: No, shared key. Future: Tenant-specific keys for Enterprise tier).
