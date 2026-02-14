# Architecture: Cloud Event Ingestion Pipeline

## 1. System Overview
**EventFlow** is a high-throughput telemetry ingestion service.
*   **Scale**: 50,000 events/sec.
*   **Tech Stack**: Kinesis -> Lambda -> S3 Data Lake + Snowflake.
*   **Data Sensitivity**: Operational logs (Low), but occasionally contains debug dumps (High).

## 2. Data Flow Diagram

```mermaid
graph LR
    Client[Mobile/IoT Client] --HTTPS/JSON--> API[Ingestion API (ALB)]
    API --> Stream[Kinesis Data Stream]
    Stream --> Processor[Lambda Processor]
    Processor --Raw--> S3[S3 Raw Bucket]
    Processor --Transform--> Firehose[Kinesis Firehose]
    Firehose --> Snowflake[Snowflake DW]
    
    subgraph "VPC Boundary"
        Stream
        Processor
        Firehose
    end
```

## 3. Trust Boundaries
1.  **Public/VPC**: Clients sending data to ALB.
2.  **Compute/Storage**: Lambda writing to S3.
3.  **Cross-Account**: Firehose writing to Snowflake.
