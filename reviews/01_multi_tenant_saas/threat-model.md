# Threat Model: Multi-Tenant SaaS Platform

| Methodology | Application |
| :--- | :--- |
| **Model** | STRIDE (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation) |
| **Scope** | Core App Service, API Gateway, Data Layer |
| **Trust Boundaries** | External/App, App/Data, Multi-Tenant Logic |

## 1. STRIDE Analysis

### Trust Boundary: Public Internet -> API Gateway
*   **Spoofing**: Attacker impersonates a valid user using stolen JWT.
    *   *Mitigation*: Short-lived tokens, Refresh Token Rotation.
*   **DoS**: Attacker floods API to degrade service for all tenants.
    *   *Mitigation*: Rate limiting per IP and per Tenant ID at Gateway level.

### Trust Boundary: App Service -> Database (The "Golden Key" Risk)
*   **Tampering**: SQL Injection allows modification of other tenants' data.
    *   *Mitigation*: Use ORM with parameterized queries ONLY. No raw SQL.
*   **Information Disclosure**: "Tenant Hopping" - User ID 123 accesses User ID 456's data.
    *   *Mitigation*: Row Level Security (RLS) in Postgres or mandatory filter clauses in ORM middleware.

### Trust Boundary: App Service -> Worker (Redis Queue)
*   **Tampering**: Attacker injects malicious job payload.
    *   *Mitigation*: Strict schema validation for job payloads.

## 2. Key Threats Identified

| ID | Category | Description | Impact | Likelihood | Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TH-01** | **E**levation | Tenant A modifies URL ID to access Tenant B resources (IDOR) | Critical | Likely | **Critical** |
| **TH-02** | **D**oS | "Noisy Neighbor" - One tenant exhausts DB connections | Moderate | Likely | **High** |
| **TH-03** | **I**nfo Disc | Leaked S3 URL allows public access to private docs | Severe | Plausible | **High** |
| **TH-04** | **S**poofing | Lack of MFA allows account takeover | Severe | Plausible | **High** |

## 3. Focus Areas for Attack Path Analysis
Based on this model, we will prioritize analyzing:
1.  **Horizontal Privilege Escalation (Tenant Hopping)**.
2.  **Resource Exhaustion (DoS)**.
