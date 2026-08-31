March 17, 2026

Advances made through No Language Left Behind (NLLB) have demonstrated that high-quality machine translation (MT) scale to 200 languages. Later Large Language Models (LLMs) have been adopted for MT, increasing in quality but not necessarily extending language coverage. Current systems remain constrained by limited coverage and a persistent generation bottleneck: while crosslingual transfer enables models to somehow understand many undersupported languages, they often cannot generate them reliably, leaving most of the world’s 7,000 languages—especially endangered and marginalized ones—outside the reach of modern MT. Early explorations in extreme scaling offered promising proofs of concept but did not yield sustained solutions. We present Omnilingual Machine Translation (OMT), the first MT system supporting more than 1,600 languages. This scale is enabled by a comprehensive data strategy that integrates large public multilingual corpora with newly created datasets, including manually curated MeDLEY bitext, synthetic backtranslation, and mining, substantially expanding coverage across long-tail languages, domains, and registers. To ensure both reliable and expansive evaluation, we combined standard metrics with a suite of evaluation artifacts: BLASER 3 quality estimation model (reference-free), OmniTOX toxicity classifier, BOUQuET dataset (a newly created, largest-to-date multilingual evaluation collection built from scratch and manually extended across a wide range of linguistic families), and Met-BOUQuET dataset (faithful multilingual quality estimation at scale). We explore two ways of specializing an LLM for machine translation: as a decoder-only model (OMT-LLaMA) or as a module in an encoder–decoder architecture (OMT-NLLB). The former consists of a model built on LLaMA3, with multilingual continual pretraining and retrieval-augmented translation for inference-time adaptation. The latter is a model built on top of a multilingual aligned space (OmniSONAR, itself also based on LLaMA3), and introduces a training methodology that can exploit non-parallel data, allowing us to incorporate the decoder-only continuous pretraining data into the training of an encoder–decoder architecture. Notably, all our 1B to 8B parameter models match or exceed the MT performance of a 70B LLM baseline, revealing a clear specialization advantage and enabling strong translation quality in low-compute settings. Moreover, our evaluation of English-to-1,600 translations further shows that while baseline models can interpret undersupported languages, they frequently fail to generate them with meaningful fidelity; OMT-LLaMA models substantially expand the set of languages for which coherent generation is feasible. Additionally, OMT models improve in cross-lingual transfer, being close to solving the “understanding” part of the puzzle in MT for the 1,600 evaluated. Beyond strong out-of-the-box performance, we find that finetuning and retrieval-augmented generation offer additional pathways to improve quality for the given subset of languages when targeted data or domain knowledge is available. Our leaderboard and main humanly created evaluation datasets (BOUQuET and Met-BOUQuET) are dynamically evolving towards Omnilinguality and freely available.

लेखक

Omnilingual MT Team

Belen Alastruey

Niyati Bafna

Andrea Caciolai

Kevin Heffernan

Artyom Kozhevnikov

Christophe Ropers

Eduardo Sánchez

Charles-Eric Saint-James

Ioannis Tsiamas

Chierh CHENG

Joe Chuang

Paul-Ambroise Duquenne

Mark Duppenthaler

Nate Ekberg

Cynthia Gao

Pere Lluís Huguet Cabot

João Maria Janeiro

Jean Maillard

Gabriel Mejia Gonzalez

Edan Toledo

Arina Turkatenko

Albert Ventayol-Boada

Rashel Moritz

Alexandre Mourachko

Surya Parimi

Mary Williamson

Shireen Yates

David Dale

Marta R. Costa-jussa

Publisher

arXiv

Research Topics

July 29, 2026

RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforward: just add execution time to the reward. But in practice, once timing drives the reward, small problems in measurement noise, reward sparsity, or GRPO instability overwhelm the signal and make RL fail: generated solutions are barely faster, and more of them can fail. We make execution time learnable through three stages: (1) how code is tested, by building DMC-Optim with large optimization tests and a calibrated sandbox; (2) how speed is turned into reward, by composing correctness and speed in the RL environment and using an offline simulator to predict the most promising configurations; and (3) how the model learns from that reward, by adapting GRPO and evaluation to the sparser, noisier timed-execution setting. On DMC-Optim, the strongest optimization-aware configurations improve strict top-50% pass@1 from 18.0% to 31.3% on Qwen 2.5 7B and from 30.7% to 50.4% on CWM 32B. These gains further increase at stricter percentiles such as top-30%, with 125% relative improvement for CWM 32B, while preserving pure-correctness scores. When the timing sandbox is degraded, robust optimization RL reaches up to 100%-200% improvement over standard RLVR, depending on the evaluation criterion. On LCB, CWM 32B wins up to 83% of median-sample speed comparisons against standard RLVR. Relative to the fastest correct human submissions per problem, it reaches about half the human rate of complexity-class improvements (14% vs. 28%).

Pierre Chambon, Kunhao Zheng, Juliette Decugis, Benoît Sagot, Gabriel Synnaeve

July 17, 2026

Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then fine-tunes the policy model via reinforcement fine-tuning methods with retrieved analogous demonstrations, so the model learns to leverage reasoning traces under verifiable outcome rewards. We further analyze the diversity of retrieved contexts and find that reasoning-aware retrieval surfaces complementary solution strategies that provide distinct reasoning scaffolds for individual problems. Across challenging mathematical reasoning benchmarks, RA-RFT consistently outperforms standard reinforcement fine-tuning methods. For example, it improves AIME 2025 average@32 accuracy by 7.1 and 2.8 points over GRPO for Qwen3-1.7B and Qwen3-4B respectively -- suggesting that reasoning-aware retrieval is a complementary axis of improvement and orthogonal to advances in reward design or training curricula.

Zilin Xiao, Qi Ma, Jason Chen, Xintao Chen, Avinash Atreya, Hanjie Chen, Vicente Ordonez

July 13, 2026

As wearable devices enable continuous first-person recording, AI assistants must reason across long time horizons to recall past experiences-a capability known as episodic memory. Current benchmarks often rely on offline evaluation with access to entire video files, failing to simulate the streaming reality of wearable intelligence. We introduce S-EMBER (Streaming Egocentric Memory Benchmark for Episodic Retrieval), a large-scale benchmark comprising 3,141 videos totaling 388 hours of organic activity captured via Ray-Ban Meta smart glasses. S-EMBER formalizes grounded streaming episodic retrieval, a paradigm shift from global offline search to causal, active recall triggered by visual events in a continuous stream. We provide 9,448 QA pairs requiring manual visual proof through precise temporal localization and supporting flexible response lengths to simulate natural human-AI interaction. Our extensive benchmarking of frontier models uncovers a localization paradox: while semantic reasoning improves with parameter scale, temporal grounding precision remains a stagnant architectural bottleneck that does not benefit from brute-force increases in model size, resolution, or frame density. S-EMBER establishes a hardware-authentic foundation for developing grounded, reliable episodic memory in the next generation of wearable AI agents.

Xiaodong Wang, Xuanyi Zhao, Pedro Rodriguez, Devendra Singh Sachan, Barlas Oguz, Seungwhan Moon, Shang-Wen Li, Gargi Ghosh, Xin Dong, Wen-Tau Yih

July 03, 2026

A long-standing question in physical reasoning is whether video models rely on factorized physical state variables, or on task-specific distributed representations. We present the first mechanistic interpretability study of physical variables inside large-scale video encoders, combining layerwise probing, subspace geometry, patch-level decoding, and targeted attention ablations to characterize where and how physical information is organized. Across architectures, we identify a sharp intermediate-depth transition, the Physics Emergence Zone, at which physical variables become linearly accessible. Scalar speed and acceleration are available from early layers, whereas motion direction emerges only at the Physics Emergence Zone, mirroring the V1 to MT motion hierarchy in primate visual cortex. Direction is encoded as a circular high-dimensional population code: dozens of orthogonal probe dimensions must be steered jointly to change the decoded direction, orders of magnitude more than the low-dimensional steering interventions seen in language models. These findings argue against compact physics-engine state variables and support distributed, hierarchically-organized, “brain-like” representations that are nonetheless sufficient for making physical predictions.

Sonia Joseph, Quentin Garrido, Randall Balestriero, Matthew Kowal, Thomas Fel, Shahab Bakhtiari, Blake Richards, Mike Rabbat