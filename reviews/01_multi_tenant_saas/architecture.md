# Architecture: Multi-Tenant B2B SaaS Platform

## 1. System Overview
**Acme SaaS** is a B2B platform allowing organizations to manage HR workflows.
*   **Tenancy Model**: Shared database, shared compute, logical isolation (discriminator column).
*   **Data Sensitivity**: High (PII, Salary Data, Performance Reviews).
*   **Key Requirement**: Strict tenant isolation. Tenant A must NEVER see Tenant B's data.

## 2. Context Diagram (C4 Level 1)

```mermaid
graph TD
    %% Context Diagram
    CustomerUser[Customer User] --Uses--> AcmeSaaS[Acme SaaS Platform]
    Admin[Acme Admin] --Administers--> AcmeSaaS
    
    AcmeSaaS --Authenticates via--> Auth0[Identity Provider (Auth0)]
    AcmeSaaS --Sends emails via--> EmailSystem[Email Service (SendGrid)]
    AcmeSaaS --Reads/Writes docs--> S3[Document Store (S3)]

    subgraph "Acme Corp"
        AcmeSaaS
        Admin
    end
```

## 3. Container Diagram (C4 Level 2)

```mermaid
graph TD
    %% Container Diagram
    User[User (Browser)] --HTTPS--> API_GW[API Gateway (Nginx)]
    
    subgraph "Acme Cluster"
        API_GW --gRPC--> AppSvc[App Service (Go)]
        AppSvc --Redis Queue--> Worker[Async Worker (Python)]
    end
    
    AppSvc --SQL--> DB[(Primary DB - Postgres)]
    AppSvc --TCP--> Cache[(Cache - Redis)]
    Worker --HTTPS--> S3[S3 Bucket]
```

## 4. Trust Boundaries & Data Flow
Key trust boundaries identified for Threat Modeling:

1.  **Public/DMZ**: Between User and API Gateway.
2.  **App/Data**: Between App Service and Database.
    *   *Risk*: If App Service is compromised, all tenant data is exposed.
3.  **Worker/External**: Between Worker and S3 (File parsing risks).
4.  **Inter-Service**: Between App Service and Redis/Queue.

## 5. Assets
*   **Tenant Data**: Salary info, PII. (Confidentiality: High)
*   **Authentication Tokens**: JWTs. (Integrity/Confidentiality: High)
*   **Infrastructure Secrets**: DB credentials, API keys. (Confidentiality: Critical)
*   **System Availability**: Uptime for customers. (Availability: High)
