# Mitigations: Event Pipeline

## 1. Input Validation (Events)
*   **Schema Validation**: Enforce strict JSON Schema at the Gateway (API Gateway) or initial Lambda. Drop unknown fields.
*   **Sanitization**: Treat all log data as untrusted. Ensure downstream dashboards (Splunk, Kibana, Internal Tools) use context-aware encoding.

## 2. Infrastructure Protection
*   **Rate Limiting**:
    *   Per IP limit at ALB/WAF.
    *   Global "Circuit Breaker" to stop Lambda triggers if cost/velocity exceeds threshold.
*   **Networking**:
    *   Place Lambda in private subnet.
    *   Use VPC Endpoints for S3 and Kinesis (keep data off public internet).

## 3. Data Integrity
*   **Immutable Storage**: Enable S3 Object Lock (Compliance Mode) for raw logs to prevent tampering/deletion by attackers covering tracks.
