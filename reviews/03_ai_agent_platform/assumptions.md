# Assumptions & Scope: AI Agent Platform

## 1. Threat Actor Model
*   **External Attacker (Indirect)**: Inserting malicious prompts into public websites, emails, or documents that the agent consumes.
*   **Malicious Insider**: Employee trying to use the agent to bypass access controls or exfiltrate data.

## 2. Trust Boundaries
*   **User -> Orchestrator**: Trusted (Authenticated corp user).
*   **Orchestrator -> LLM (Azure OpenAI)**: Trusted Pipe, Untrusted Content. The LLM's output is *untrusted* and must be sanitized.
*   **Orchestrator -> Tools (Browse, SQL)**: Untrusted. Tools are high-privilege and can operate on chaotic inputs.

## 3. Tool Permission Model (Sandboxing)
*   **Browse Tool**: Ephemeral container. Destroyed after use. No persistence.
*   **SQL Tool**: Read-Only DB User. Low timeout (5s). row-limit=100.
*   **Python Tool**: E2B Sandbox. No network access allowed.

## 4. Key Constraints
*   **Model limitations**: We cannot fine-tune the model for safety due to cost/velocity. We must rely on Prompt Engineering and Guardrails.
*   **Latency**: HITL (Human in the Loop) adds significant friction but is non-negotiable for safety.
