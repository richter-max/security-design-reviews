# Assumptions & Scope: Multi-Tenant B2B SaaS

## 1. Threat Actor Model
*   **External Attacker (Opportunistic)**: Script kiddies, bots scanning for known CVEs.
*   **External Attacker (Targeted)**: Competitors or criminals seeking specific tenant data (PII/IP).
*   **Malicious Insider (Tenant)**: A valid user from Tenant A trying to access Tenant B's data (Horizontal Escalation).
*   **Compromised Administrator**: An Acme admin account taken over via phishing.

## 2. Trust Boundaries
*   **User Browser <-> API Gateway**: Untrusted. All inputs must be validated.
*   **API Gateway <-> App Service**: Trusted (mTLS or VPC private link).
*   **App Service <-> Database**: High Trust. The App Service holds the "Golden Key" (DB Credentials).

## 3. Out of Scope
*   **Physical Security**: AWS/Azure data center security is assumed managed by the CSP.
*   **Corporate Laptop Security**: Endpoint security of Acme employees is out of scope for *this* application review.
*   **DDoS Protection**: Assumed covered by Cloudflare/AWS Shield at the edge.

## 4. Key Constraints
*   **Shared Schema**: Migration to "Database-per-tenant" is not feasible due to cost/operational complexity.
*   **Performance**: Tenant isolation checks must not add >10ms latency per request.
