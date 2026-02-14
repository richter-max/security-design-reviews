# Risk Scoring Model

We use a standard **Likelihood × Impact** matrix to score all security findings. This ensures we prioritize fixing the issues that matter most.

## 1. The Formula

$$ Risk Score = Likelihood \times Impact $$

*   **Likelihood**: How probable is it that this threat will be exploited? (1-5)
*   **Impact**: How bad is it if this threat is exploited? (1-5)

## 2. Likelihood Definitions

| Score | Rating | Definition |
| :--- | :--- | :--- |
| **1** | **Theoretical** | Requires a complex chain of unlikely events. No known exploit exists. |
| **2** | **Difficult** | Requires significant resources, insider access, or a specific window of opportunity. |
| **3** | **Plausible** | Determining the exploit is feasible for a skilled attacker. Tools may exist. |
| **4** | **Likely** | Exploit is straightforward. Automated tools likely exist. |
| **5** | **Trivial** | Exploit is trivial (e.g., browse to a URL). Fully automated exploitation is expected. |

## 3. Impact Definitions

| Score | Rating | Definition |
| :--- | :--- | :--- |
| **1** | **Minimal** | No sensitive data lost. Minor UI glitch. No business impact. |
| **2** | **Limited** | Nuisance to users. Minor data exposure (e.g., internal IDs). |
| **3** | **Moderate** | Service degradation. Exposure of non-critical user data. Brand damage. |
| **4** | **Severe** | Significant PII breach. Financial loss. Critical system downtime. |
| **5** | **Critical** | Full system compromise. Admin access. Massive data breach (Regulator fines). |

## 4. Risk Matrix

| Impact \ Likelihood | 1 (Theoretical) | 2 (Difficult) | 3 (Plausible) | 4 (Likely) | 5 (Trivial) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5 (Critical)** | Medium | High | Critical | Critical | Critical |
| **4 (Severe)** | Low | Medium | High | Critical | Critical |
| **3 (Moderate)** | Low | Low | Medium | High | High |
| **2 (Limited)** | Info | Low | Low | Medium | Medium |
| **1 (Minimal)** | Info | Info | Low | Low | Low |

## 5. Remediation SLAs

*   **Critical**: Fix immediately (within 24 hours). Block deployment.
*   **High**: Fix within current sprint (2 weeks).
*   **Medium**: Fix within next quarter.
*   **Low/Info**: Backlog or Accept.
