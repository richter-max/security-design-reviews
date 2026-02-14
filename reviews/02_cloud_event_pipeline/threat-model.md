# Threat Model: Cloud Event Ingestion

| Component | STRIDE | Threat Description | Risk |
| :--- | :--- | :--- | :--- |
| **Ingestion API** | **D**oS | Attacker floods endpoint with large payloads, exhausting quotas. | High |
| **Ingestion API** | **S**poofing | Attacker sends fake telemetry to pollute analytics. | Medium |
| **Lambda** | **T**ampering | Malformed JSON triggers deserialization exploity (Log4Shell style). | Critical |
| **S3 Raw** | **I**nfo Disc | S3 bucket misconfigured as public. | High |

## Key Risks identified
1.  **Injection Attacks in Logs**: Attacker injects CRLF or XSS payloads that trigger in admin dashboards (Log Injection).
2.  **Resource Exhaustion**: 1M small requests costing $$$ in Lambda triggers (Denial of Wallet).
