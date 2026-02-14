# Architecture: Enterprise AI Agent Platform

## 1. System Overview
**AgentCore** is an internal platform allowing employees to build LLM-powered agents that can execute tools (SQL, HTTP API, Python Code) on behalf of the user.
*   **Model**: GPT-4o via Azure OpenAI.
*   **Capabilities**: RAG (Vector DB), Tool Use (Sandboxed execution).
*   **Users**: 5,000+ internal employees.

## 2. Component Diagram

```mermaid
graph TD
    User[Employee] --HTTPS--> WebApp[Agent UI]
    WebApp --gRPC--> Orchestrator[Agent Orchestrator (Python)]
    
    subgraph "Trust Boundary: LLM Integration"
    Orchestrator --Prompt--> LLM[Azure OpenAI]
    end
    
    subgraph "Trust Boundary: Tool Execution"
    Orchestrator --Code--> Sandbox[E2B Sandbox / Firecracker]
    Orchestrator --SQL--> ReadOnlyDB[Replica DB]
    end
    
    subgraph "Data Context"
    Orchestrator --Vector Search--> Qdrant[Vector DB]
    end
```

## 3. Data Flow
1.  User sends prompt ("Summarize Q3 sales").
2.  Orchestrator fetches context from **Qdrant** (RAG).
3.  Orchestrator sends System Prompt + Context + User Prompt to **LLM**.
4.  LLM decides to call tool `sql_query`.
5.  Orchestrator executes `sql_query` against **ReadOnlyDB**.
6.  Results returned to LLM -> Final answer to User.
