# Security Design Review Methodology

This document outlines the standard process used for all security design reviews in this repository. Our goal is consistency, rigor, and actionable outputs.

## 1. The Review Lifecycle

We follow a 5-step process for every system we review:

### Phase 1: Architecture Decomposition
Before we can break it, we must understand it.
*   **Inputs**: Design docs, API specs, whiteboard sessions.
*   **Outputs**:
    *   **Context Diagram**: System in its environment.
    *   **Data Flow Diagram (DFD)**: How data moves between processes and stores.
    *   **Asset Inventory**: What are we protecting? (PII, Secrets, Availability).

### Phase 2: Threat Modeling (STRIDE)
We examine every Trust Boundary in the DFD using the **STRIDE** mnemonic:
*   **S**poofing: Impersonating something or someone else.
*   **T**ampering: Modifying data or code.
*   **R**epudiation: Claiming to have not performed an action.
*   **I**nformation Disclosure: Exposing information to unauthorized parties.
*   **D**enial of Service: Denying or degrading service to users.
*   **E**levation of Privilege: Gaining capabilities without authorization.

### Phase 3: Attack Path Analysis
Abstract threats are converted into realistic attack scenarios. We ask: *"How would a skilled adversary actually execute this?"*
*   We map the specific steps (Kill Chain) required for exploitation.
*   We identify preconditions (e.g., "Attacker needs a valid low-privileged account").

### Phase 4: Risk Assessment
Not all threats matter equally. We score each finding using our Risk Matrix:
*   **Risk Score = Likelihood × Impact**
*   See [Risk Scoring Model](./risk-scoring-model.md) for definitions.

### Phase 5: Mitigation & Trade-offs
We propose mitigations that balance security with usability and performance.
*   **Eliminate**: Change the design to remove the threat entirely.
*   **Mitigate**: Add controls to reduce likelihood or impact.
*   **Accept**: Formally acknowledge the risk (if low enough).
*   **Transfer**: Move the risk (e.g., to a third party).

## 2. Guiding Principles

*   **Secure by Design**: Defaults should be secure.
*   **Defense in Depth**: No single control should be the single point of failure.
*   **Least Privilege**: Components should only have the access they absolutely need.
*   **Assume Breach**: Design as if the network is compromised.

## 3. Artifact Standards

All reviews must be documented in Markdown and include:
1.  Clear diagrams (Mermaid or exported images).
2.  A prioritized list of findings.
3.  A clear `Residual Risk` statement for every finding after mitigation.
