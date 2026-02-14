# Mitigation Strategy: Multi-Tenant SaaS

## 1. Proposed Controls

### M-01: Enforcement of Tenant Isolation (Addressed TH-01)
*   **Type**: Prevention
*   **Implementation**:
    *   **Middleware**: Implement a global strict middleware `EnforceTenantContext` in the Go App Service.
    *   **Logic**: Extract `TenantID` from the JWT. Inject this ID into the SQL context.
    *   **ORM Hook**: Configure GORM/Ent to automatically append `WHERE tenant_id = <ctx.ID>` to *every* query.
    *   **Test**: Add regression tests that attempt to query across tenants.

### M-02: Rate Limiting & Quotas (Addressed TH-02)
*   **Type**: Prevention
*   **Implementation**:
    *   **Gateway**: Configure Nginx/Kong to limit requests/sec per `TenantID` header.
    *   **Worker**: Implement "Fair Queueing" so one tenant cannot clog the job queue.
    *   **DB**: Set `statement_timeout` on Postgres roles to prevent long-running analytical queries from efficiently killing the DB.

### M-03: Pre-Signed URLs for S3 Access (Addressed TH-03)
*   **Type**: Prevention
*   **Implementation**:
    *   **Change**: Do NOT make the bucket public. Block all public access.
    *   **Logic**: App Service generates a temporary (15-min) Pre-Signed URL for authorized users only.
    *   **Audit**: Enable S3 Server Access Logging.

## 2. Trade-off Analysis

### Performance vs. Isolation (M-01)
*   **Trade-off**: Adding RLS or mandatory `WHERE` clauses adds slight overhead to query planning.
*   **Decision**: Security Priority. The risk of data leakage is existential for a B2B SaaS. We accept the <5ms latency penalty.

### User Experience vs. Security (M-02)
*   **Trade-off**: Strict rate limits might block legitimate power users during end-of-month reporting.
*   **Decision**: Balanced. We will set soft limits at 2x normal peak and implement "Burst" capacity. We will return `429 Too Many Requests` with a `Retry-After` header.
