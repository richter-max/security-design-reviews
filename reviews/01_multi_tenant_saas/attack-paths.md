# Attack Path Analysis: Multi-Tenant SaaS

## Scenario 1: Horizontal Privilege Escalation (Tenant Hopping)

**Goal**: Access confidential PII of a competing tenant.
**Precondition**: Attacker has a valid account on Tenant A.

### Kill Chain Steps
1.  **Reconnaissance**: Attacker logs in and inspects API traffic.
    *   *Observation*: API calls use sequential integers for IDs: `GET /api/v1/employees/1001`.
2.  **Fuzzing**: Attacker modifies the ID parameter to `1002`.
    *   *Test*: Does the API return a 403 Forbidden or 200 OK?
3.  **Exploitation**: The API returns 200 OK with the data of an employee from Tenant B.
    *   *Result*: Full IDOR (Insecure Direct Object Reference).
4.  **Scaling**: Attacker writes a script to iterate from `1` to `10000`, dumping the entire database.

**Feasibility**: HIGH. This is a common flaw in multi-tenant apps where `WHERE tenant_id = ?` is forgotten.

---

## Scenario 2: Remote Code Execution via CSV Import

**Goal**: Execute arbitrary code on the backend worker to access env vars (DB creds).
**Precondition**: Attacker has access to limits-enabled employee import feature.

### Kill Chain Steps
1.  **Discovery**: Attacker finds the "Import Employees from CSV" feature.
    *   *Observation*: The system accepts `.csv` files and processes them asynchronously.
2.  **Weaponization**: Attacker constructs a "CSV Injection" (Formula Injection) or attempts a Polyglot file.
    *   *Attempt A*: Spreadsheet formula `=cmd|' /C calc'!A0` (targeting admin viewing the file).
    *   *Attempt B*: Renaming a malicious binary to `import.csv` hoping for a parser vulnerability (Buffer Overflow - Unlikely in Python/Pandas).
3.  **Alternative Pivot**: Attacker notices the CSV parser uses an outdated library vulnerable to a known CVE or allows external entity expansion (if XML/XLSX support was hidden).
4.  **Action on Objectives**: If successful, the worker process runs the code. The attacker dumps `os.environ` to an external server.
    *   *Result*: DB Credentials exposed. Full database compromise.

**Feasibility**: MODERATE. Depends on the strictness of the file parser and input validation.
