# Assumptions & Scope: Cloud Event Pipeline

## 1. Threat Actor Model
*   **External Attacker (Flooding)**: Botnets attempting to exhaust quotas or budget.
*   **Malicious Telemetry Source**: A compromised mobile device sending poisoned event payloads.

## 2. Trust Boundaries
*   **Public Internet -> Application Load Balancer**: Untrusted.
*   **ALB -> Lambda**: Trusted Execution Environment (AWS).
*   **Lambda -> S3**: Trusted Private Network (VPC Endpoint).

## 3. Key Constraints
*   **Latency**: Ingestion must be <50ms p99. Heavy WAF rules might add too much latency.
*   **Cost**: WAF Shield Advanced is too expensive for this project tier. Standard WAF only.
