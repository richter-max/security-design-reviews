# Secure Design Review Lab

> **"Security is not a feature, it's a state of being."**

Welcome to the **Secure Design Review Lab**. This repository serves as a comprehensive portfolio of structured security architecture reviews, threat models, and risk assessments for complex software systems.

## 🎯 Purpose

This project demonstrates a rigorous, engineering-first approach to application security. It moves beyond automated scanner outputs and checklist compliance to focus on:
*   **Systems Thinking**: Understanding complex interactions and emergent behaviors.
*   **Threat Modeling**: systematically identifying design flaws (STRIDE, Attack Trees).
*   **Risk Realism**: Evaluating risk based on concrete likelihood and impact, not FUD (Fear, Uncertainty, Doubt).
*   **Defensive Design**: Proposing architectural mitigations that are practical and effective.

## 🧠 Core Philosophy

1.  **Design over Tools**: Tools find bugs; humans find design flaws. This repo focuses on the latter.
2.  **Context is King**: A vulnerability in one context is a feature in another. We analyze threats within the specific business and technical context.
3.  **Communication is Key**: Security artifacts must be readable by developers, architects, and stakeholders.

## 📂 Project Portfolio

### [Review 01: Multi-Tenant B2B SaaS](./reviews/01_multi_tenant_saas/architecture.md)
**Scenario**: A legacy HR platform moving to the cloud.
*   **Key Challenge**: Enforcing tenant isolation in a shared-schema database.
*   **Highlight**: Analysis of "Tenant Hopping" risks and ORM-level mitigations.

### [Review 02: Cloud Event Ingestion](./reviews/02_cloud_event_pipeline/architecture.md)
**Scenario**: High-scale telemetry pipeline handling 50k events/sec.
*   **Key Challenge**: Denial of Wallet & Injection attacks in log data.
*   **Highlight**: Cost-based circuit breakers and immutable storage for audit logs.

### [Review 03: Enterprise AI Agent Platform](./reviews/03_ai_agent_platform/architecture.md)
**Scenario**: Internal RAG-based agent with tool execution capabilities.
*   **Key Challenge**: Indirect Prompt Injection and Excessive Agency.
*   **Highlight**: Human-in-the-Loop design patterns for high-stake actions.

## 🛠 Methodology Overview

Our review process follows a structured lifecycle:
1.  **Discovery**: Gather architecture diagrams, data flows, and asset inventories.
2.  **Threat Modeling**: Apply STRIDE to identify potential threats at trust boundaries.
3.  **Attack Path Analysis**: Map out realistic steps an attacker would take to exploit the system.
4.  **Risk Assessment**: Score risks using our [standard model](docs/risk-scoring-model.md).
5.  **Mitigation & Residual Risk**: Propose controls and evaluate what risk remains.

## 🚀 Getting Started

Explore the reviews to see this methodology in action. Start with the **Multi-Tenant SaaS** review for a classic example of isolation challenges, or check out the **AI Agent Platform** for emerging threats in LLM systems.

---
*Built by a Security Engineer for Security Engineers.*
