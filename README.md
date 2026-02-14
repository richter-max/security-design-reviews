# Secure Design Review Lab

> **"Security is not a feature, it's a state of being."**

Welcome to the **Secure Design Review Lab**. This repository transforms vague security concepts into a structured, engineering-grade Security Design Review Framework. It demonstrates how to rigorously analyze complex systems, quantify risk, and design practical mitigations.

## 🧭 How to Navigate This Repository

| Directory | Purpose |
| :--- | :--- |
| [`/reviews`](./reviews) | **The Core Work.** Deep-dive security reviews of 3 distinct architectures. |
| [`/docs`](./docs) | **The Framework.** Methodology, Risk Scoring Model, and Templates. |
| [`/tools`](./tools) | **The Engineering.** Python scripts for automated validation and summary generation. |
| [`/.github`](./.github) | **The CI/CD.** Automated workflows ensuring artifact quality and consistency. |

## 🎯 Core Competencies Demonstrated

This repository is built to demonstrate specific senior security engineering skills:

*   **Threat Modeling**: Applied STRIDE and Attack Trees to finding logic flaws.
*   **Risk Governance**: Consistent, numeric [Risk Scoring](./docs/risk-scoring-model.md) (Likelihood × Impact).
*   **Cloud Security**: Deep dives into AWS/Azure architectures (S3, Lambda, Kinesis, OpenAI).
*   **AI Security**: Analysis of Prompt Injection and Excessive Agency in LLM agents.
*   **Engineering Rigor**: Automated validation (CI/CD) to ensure "Docs-as-Code" quality.

## 📂 Review Portfolio

| Review | Domain | Highest Risk | Key Themes | Status |
| :--- | :--- | :--- | :--- | :--- |
| **[01: Multi-Tenant SaaS](./reviews/01_multi_tenant_saas/summary.md)** | AppSec | **Critical (20)** | Tenant Isolation, IDOR, ORM Security | ✅ Complete |
| **[02: Cloud Event Pipeline](./reviews/02_cloud_event_pipeline/summary.md)** | CloudSec | **Critical (20)** | Injection, DoS ("Denial of Wallet") | ✅ Complete |
| **[03: AI Agent Platform](./reviews/03_ai_agent_platform/summary.md)** | AI Security | **Critical (25)** | Prompt Injection, SSRF, Sandboxing | ✅ Complete |

## 🛠 Methodology Overview

Our review process follows a structured 5-step lifecycle:
1.  **Discovery**: Architecture decomposition and Asset Inventory.
2.  **Threat Modeling**: STRIDE analysis at Trust Boundaries.
3.  **Attack Path Analysis**: Realistic "Kill Chain" mapping.
4.  **Risk Assessment**: Quantified scoring (L x I).
5.  **Mitigation**: Engineering-led controls (Middleware, Sandboxing, IaC).

## ✅ Definition of Done

Every review in this repository MUST contain:
*   `architecture.md`: System design and diagrams.
*   `threat-model.md`: Detailed STRIDE analysis.
*   `findings.md`: Structured, machine-readable table of risks.
*   `mitigations.md`: Proposed controls.
*   `summary.md`: Executive-level overview.

*This project is validated by CI/CD to ensure all artifacts are present and usually consistent.*

## 🚀 Getting Started

Explore the reviews to see this methodology in action. Start with the **Multi-Tenant SaaS** review for a classic example of isolation challenges, or check out the **AI Agent Platform** for emerging threats in LLM systems.

---
*Built by a Security Engineer for Security Engineers.*
