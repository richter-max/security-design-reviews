# Security Review Checklist

## Authentication & Authorization
- [ ] Is MFA enforced for administrative actions?
- [ ] Are API tokens rotated automatically?
- [ ] Is there proper validation of `User-ID` on every object access (IDOR check)?
- [ ] Are permissions checked serverside (not just UI hidden)?

## Data Protection
- [ ] Is PII encrypted at rest?
- [ ] Is TLS 1.2+ enforced everywhere?
- [ ] Are secrets excluded from code/git? (Use Vault/Secrets Manager)
- [ ] Are backups encrypted and tested?

## Input Validation
- [ ] Is there a global Input Validation Filter?
- [ ] Are SQL queries parameterized?
- [ ] Is HTML output encoded (XSS Prevention)?
- [ ] Are file uploads restricted by type and size?

## Logging & Monitoring
- [ ] Are security events logged (Auth failures, extensive queries)?
- [ ] Are PII and Secrets REDACTED from logs?
- [ ] Is there alerting for suspicious activity patterns?
