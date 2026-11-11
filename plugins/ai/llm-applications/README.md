# ai-llm-applications

LLM apps: prompting, RAG, embeddings, vector search, caching, evals and model APIs.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install ai-llm-applications@skills-stack
```

## Skills (15)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [bengali-nlp](skills/bengali-nlp/SKILL.md) | Bengali (Bangla) text processing patterns including Unicode normalization, script detection, tokenization, conjunct handling, and Bangla-specific NLP best practices for AI applications. | Affaan Mustafa | MIT |
| [claude-api](skills/claude-api/SKILL.md) | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read BEFORE opening the target file; d… | Anthropic, PBC | Complete terms in LICENSE.txt |
| [cost-aware-llm-pipeline](skills/cost-aware-llm-pipeline/SKILL.md) | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. Use when LLM spend needs to come down, or when routing tasks across… | Affaan Mustafa | MIT |
| [embedding-strategies](skills/embedding-strategies/SKILL.md) | Select and optimize embedding models for semantic search and RAG applications. Use when choosing embedding models, implementing chunking strategies, or optimizing embedding quality for specific domai… | Seth Hobson | MIT |
| [hybrid-search-implementation](skills/hybrid-search-implementation/SKILL.md) | Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither approach alone provides sufficient recall. | Seth Hobson | MIT |
| [kernel-prompt](skills/kernel-prompt/SKILL.md) | Use when composing or improving an LLM prompt or agent instruction. Asks one round of questions, then returns only the prompt; never performs the task. | codegiveness | MIT |
| [langchain-architecture](skills/langchain-architecture/SKILL.md) | Design LLM applications using LangChain 1.x and LangGraph for agents, memory, and tool integration. Use when building LangChain applications, implementing AI agents, or creating complex LLM workflows. | Seth Hobson | MIT |
| [llm-caching](skills/llm-caching/SKILL.md) | Implement multi-layer LLM caching with exact match, semantic similarity, and provider-side prompt caching. | devops-skills | MIT |
| [llm-evaluation](skills/llm-evaluation/SKILL.md) | Implement comprehensive evaluation strategies for LLM applications using automated metrics, human feedback, and benchmarking. Use when testing LLM performance, measuring AI application quality, or es… | Seth Hobson | MIT |
| [prompt-caching-strategy](skills/prompt-caching-strategy/SKILL.md) | Optimize LLM prompt caching hit rate to reduce API costs and improve latency. Analyzes prompt structure, identifies cacheable vs non-cacheable content, and recommends restructuring to maximize cache… | cyberspace-cs | MIT |
| [prompt-engineering-patterns](skills/prompt-engineering-patterns/SKILL.md) | This skill should be used when the user asks to "optimize a prompt", "improve prompt performance", "design a prompt template", "write better prompts", "debug prompt issues", "use chain-of-thought", "… | Seth Hobson | MIT |
| [rag-implementation](skills/rag-implementation/SKILL.md) | Build Retrieval-Augmented Generation (RAG) systems for LLM applications with vector databases and semantic search. Use when implementing knowledge-grounded AI, building document Q&A systems, or integ… | Seth Hobson | MIT |
| [regex-vs-llm-structured-text](skills/regex-vs-llm-structured-text/SKILL.md) | Decision framework for parsing structured text (quizzes, forms, invoices, receipts, tables) with a hybrid regex-first pipeline — regex extraction handles 95%+ cheaply, a confidence scorer flags low-c… | Affaan Mustafa | MIT |
| [similarity-search-patterns](skills/similarity-search-patterns/SKILL.md) | Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, or optimizing retrieval performance. | Seth Hobson | MIT |
| [vector-index-tuning](skills/vector-index-tuning/SKILL.md) | Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, or scaling vector search infrastructure. | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
