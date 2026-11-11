# ai-machine-learning

ML training, fine-tuning, MLOps, model serving, PyTorch and data science.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install ai-machine-learning@skills-stack
```

## Skills (26)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [checkpoint-promotion](skills/checkpoint-promotion/SKILL.md) | Gate fine-tuned checkpoints with drift budgets, paired comparison, and forgetting checks before promotion. Use after a training run produces a checkpoint, when deciding whether a tuned model ships, o… | Seth Hobson | MIT |
| [data-scientist](skills/data-scientist/SKILL.md) | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive modeling, and business intelligence. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [dataset-curation](skills/dataset-curation/SKILL.md) | Prepare, format, and validate datasets for supervised fine-tuning and preference training. Use when converting raw data into training format, applying chat templates, configuring sequence packing, ge… | Seth Hobson | MIT |
| [eval-harness-first](skills/eval-harness-first/SKILL.md) | Build the evaluation harness that gates every fine-tuning run — golden sets, per-failure-mode graders, judge calibration, and base-model baselines. Use when starting a fine-tuning effort, when conver… | Seth Hobson | MIT |
| [finetuning-method-selection](skills/finetuning-method-selection/SKILL.md) | Decide whether to fine-tune at all, and route to the right method (SFT, DPO/ORPO/KTO, GRPO/RLVR, continued pretraining) and base model. Use when starting any fine-tuning effort, when unsure whether R… | Seth Hobson | MIT |
| [grpo-rlvr-training](skills/grpo-rlvr-training/SKILL.md) | Train reasoning and verifiable-task behavior with GRPO and reinforcement learning from verifiable rewards (RLVR). Use when task success is algorithmically checkable (math, code, tool calls, structure… | Seth Hobson | MIT |
| [huggingface-datasets](skills/huggingface-datasets/SKILL.md) | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [huggingface-zerogpu](skills/huggingface-zerogpu/SKILL.md) | AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. | sickn33 and the agentic-awesome-skills contributors (copyri… | Apache-2.0 |
| [ito-inference](skills/ito-inference/SKILL.md) | Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend becomes available, hand off an explicitly confirmed serving manifest. Use after ito-comput… | Affaan Mustafa | MIT |
| [ito-training](skills/ito-training/SKILL.md) | Inspect the availability of ML training on a completed Itô compute booking and, when the canonical backend becomes available, hand off an explicitly confirmed training manifest. Use after ito-compute… | Affaan Mustafa | MIT |
| [llm-inference-scaling](skills/llm-inference-scaling/SKILL.md) | Auto-scale LLM inference clusters on Kubernetes using KEDA, custom GPU metrics, and horizontal pod autoscaling. | devops-skills | MIT |
| [lora-qlora-recipes](skills/lora-qlora-recipes/SKILL.md) | Configure LoRA and QLoRA supervised fine-tuning with current best-practice hyperparameters. Use when writing or reviewing a LoRA/QLoRA training configuration, choosing rank/alpha/target modules, or d… | Seth Hobson | MIT |
| [mac-mini-llm-lab](skills/mac-mini-llm-lab/SKILL.md) | Configure a Mac mini as a reliable local LLM server with remote access, observability, and power-safe operation. Use when building an always-on private AI inference server on Apple Silicon. | devops-skills | MIT |
| [ml-adoption-playbook](skills/ml-adoption-playbook/SKILL.md) | End-to-end methodology for AI agents and software engineers to add machine learning algorithms to existing non-ML codebases. Covers problem framing, data readiness, architectural decoupling, and base… | Affaan Mustafa | MIT |
| [ml-pipeline-workflow](skills/ml-pipeline-workflow/SKILL.md) | Build end-to-end MLOps pipelines from data preparation through model training, validation, and production deployment. Use when creating ML pipelines, implementing MLOps practices, or automating model… | Seth Hobson | MIT |
| [mle-workflow](skills/mle-workflow/SKILL.md) | Production machine-learning engineering workflow for data contracts, reproducible training, model evaluation, deployment, monitoring, and rollback. Use when building, reviewing, or hardening ML syste… | Affaan Mustafa | MIT |
| [model-serving-kubernetes](skills/model-serving-kubernetes/SKILL.md) | Deploy ML models on Kubernetes with KServe (formerly KFServing) and NVIDIA Triton Inference Server. | devops-skills | MIT |
| [preference-optimization](skills/preference-optimization/SKILL.md) | Align a fine-tuned model with preference data using DPO, ORPO, KTO, or SimPO. Use when preference pairs or thumbs-up/down feedback exist, when choosing between preference-optimization methods, or whe… | Seth Hobson | MIT |
| [pytorch-patterns](skills/pytorch-patterns/SKILL.md) | PyTorch deep learning patterns and best practices for building robust, efficient, and reproducible training pipelines, model architectures, and data loading. Use when writing or reviewing PyTorch tra… | Affaan Mustafa | MIT |
| [quantized-export](skills/quantized-export/SKILL.md) | Export a promoted fine-tuned model in the right deployment format — merged safetensors, LoRA-only, GGUF with imatrix, or FP8. Use after a checkpoint passes promotion, when choosing a quantization for… | Seth Hobson | MIT |
| [recsys-pipeline-architect](skills/recsys-pipeline-architect/SKILL.md) | Design composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect framework popularized by xAI's open-sourced X For You algorithm. Us… | Seth Hobson | MIT |
| [spark-environment-setup](skills/spark-environment-setup/SKILL.md) | Set up a working ML training/inference environment on NVIDIA DGX Spark (GB10, aarch64, CUDA 13). Use when installing PyTorch/Unsloth/TRL/vLLM on DGX Spark, hitting libcudart or wheel-ABI errors on aa… | Seth Hobson | MIT |
| [spark-memory-thermal-ops](skills/spark-memory-thermal-ops/SKILL.md) | Manage unified memory and thermals during long-running ML jobs on NVIDIA DGX Spark. Use when planning memory headroom for a training run on GB10, when a job OOMs on unified memory, or when monitoring… | Seth Hobson | MIT |
| [spark-training-gotchas](skills/spark-training-gotchas/SKILL.md) | Preflight and diagnose the ten known failure modes for ML training on NVIDIA DGX Spark. Use when a training run on DGX Spark fails to start, OOMs below the 128GB limit, slows down mid-run, or before… | Seth Hobson | MIT |
| [trace-to-training-data](skills/trace-to-training-data/SKILL.md) | Convert evaluation traces and production logs into SFT examples and preference pairs. Use when graded traces or failure examples exist and need to become training data, when applying rejection sampli… | Seth Hobson | MIT |
| [vision-sft](skills/vision-sft/SKILL.md) | Fine-tune vision-language models (VLMs) with supervised learning on image+text data. Use when adapting a VLM to a visual domain or task, configuring frozen-vision-tower LoRA, or debugging a VLM fine-… | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
