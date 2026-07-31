arXiv is now an independent nonprofit! Learn more ×
License: arXiv.org perpetual non-exclusive license 
arXiv:2607.25656v1 [cs.AI] 28 Jul 2026
# OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation
Zhenzhen Ren1, 2, Jiyan He2, Xinpeng Zhang1, Zhenxing Qian1, Ke Han3, Shuxin Zheng2, GuoBiao Li1, Xiaoqing Zhang2\corresponding
###### Abstract
Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation. Starting from real-world tasks, OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies, with controlled sizes and degrees of parallelism. Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios. A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions, achieving a Pearson correlation of r=0.816, while requiring only of the tokens and of the wall-clock time. Across diverse planners and workflow scales, we find that preserving task-critical information is more important than simply increasing the number of agents, and the benefits of parallelism diminish as coordination failures accumulate. These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.
Figure 1: Comparison between conventional end-to-end MAS evaluation and OrchBench. Instead of executing the complete multi-agent system, OrchBench evaluates orchestration plans with a deterministic simulator, isolating orchestration quality from execution-related factors while enabling fast, low-cost, and reproducible evaluation.
## Introduction
Multi-agent systems (MAS) have emerged as a powerful paradigm for solving complex tasks by coordinating multiple specialized agents (Guo et al. 2024; Hong et al. 2024; Wang et al. 2025b; Fourney et al. 2024). As these systems become increasingly sophisticated, their performance depends not only on the capability of individual agents, but also on the orchestration strategy, i.e., how a workflow is organized across multiple agents. Even with the same task and the same set of agents, different orchestration strategies can lead to substantially different outcomes (Yu et al. 2025; Kim et al. 2023; Zhuge et al. 2024). This growing importance raises a fundamental question: how can orchestration itself be evaluated?
However, evaluating orchestration itself remains challenging. Existing benchmarks primarily evaluate the end-to-end task performance of MAS in realistic environments (Liu et al. 2023; Mialon et al. 2023; Zhou et al. 2023; Jimenez et al. 2023; Xie et al. 2024; Koh et al. 2024; Drouin et al. 2024; Yoran et al. 2024; Xu et al. 2026b; Deng et al. 2023). The resulting performance conflates orchestration quality with execution-related factors (Ma et al. 2024; Ke et al. 2026; Tsang et al. 2026), making it difficult to attribute success or failure to orchestration itself, as illustrated in Figure . Moreover, end-to-end evaluation is computationally expensive, making systematic comparison across orchestration strategies increasingly impractical as workflow scale grows. Consequently, a practical evaluation framework that isolates orchestration from worker execution remains absent.
To address this issue, we introduce OrchBench, a _simulation-based_ benchmark for evaluating multi-agent orchestration independently of worker execution. Our key insight is that orchestration can be evaluated without executing the complete multi-agent system. Instead of evaluating end-to-end task performance, we require the model to generate only an orchestration plan. Worker execution is then replaced by a deterministic simulator, which removes the influence of worker reasoning, tool execution, and environmental noise from the evaluation while enabling different orchestration strategies to be compared under identical conditions. To enable systematic analysis of orchestration across different workflow scales, OrchBench contains semantically grounded dependency workflows ranging from 10 to 1,000 subtasks. Beyond producing evaluation scores, the simulator explicitly identifies coordination failures, providing interpretable diagnoses for improving orchestration strategies.
Using OrchBench, we conduct the first systematic study of orchestration strategies produced by language models. Our experiments uncover a previously hidden coordination bottleneck: as workflow scale increases, orchestration quality becomes increasingly constrained by information preservation rather than agent count and the benefits of parallelism decrease as coordination failures accumulate. These failures are largely obscured by conventional end-to-end evaluation but become directly observable through our simulator.
We further validate that the simulator faithfully reflects real-world orchestration quality. Across Claude Code executions, simulator scores achieve a strong correlation with real execution quality (Pearson r=0.816), while requiring only of the tokens and of the wall-clock time. Beyond evaluation, simulator-guided diagnosis consistently improves real multi-agent execution by identifying missing information transfers. Our contributions are threefold:
  * •
We identify the need to evaluate multi-agent orchestration independently of worker execution and formulate it as a standalone benchmark problem.
  * •
We introduce OrchBench, a scalable benchmark that combines semantically grounded task workflows with a deterministic simulator for efficient and reproducible orchestration evaluation.
  * •
We conduct a systematic study of orchestration strategies across workflows containing up to 1,000 subtasks, revealing previously hidden coordination failures and showing that OrchBench closely reflects real execution while significantly reducing evaluation time and token cost.


Figure 2: Benchmark design overview. OrchBench first constructs a DAG from a raw seed question, then asks the planner model to produce an orchestration plan. The deterministic simulator executes the plan and obtains the score.
## Related Work
##### End-to-End Evaluation of Agent Systems.
Most existing agent benchmarks test whether systems can complete tasks in external environments. AgentBench covers web browsing, databases, operating systems, games, and embodied tasks ; GAIA evaluates multi-step assistant tasks requiring reasoning, information retrieval, and tool use ; and WebArena, SWE-bench, and OSWorld evaluate agents in realistic web, software-engineering, and computer-use environments (Zhou et al. 2023; Jimenez et al. 2023; Xie et al. 2024). ToolLLM studies large-scale API use , while -bench evaluates agents that interact with simulated users and domain-specific tools . MultiAgentBench extends end-to-end evaluation to multi-agent systems by measuring task completion and collaboration quality under different coordination protocols . MAST analyzes execution traces from multiple MAS frameworks and identifies system design, inter-agent misalignment, and task verification as major failure sources . These benchmarks are useful for evaluating deployed systems, but their results mix the effects of planning, worker performance, tools, and environments. It is therefore hard to tell whether success or failure comes from the orchestration plan.
##### Evaluation of Planning and Multi-Agent Orchestration.
Existing studies fall into three groups. The first evaluates planning and workflow structure. PlanBench tests formal action planning, FlowBench evaluates workflow-guided tool planning, and WorFBench compares generated workflows with reference sequences or graphs (Valmeekam et al. 2023; Xiao et al. 2024; Qiao et al. 2025). Unlike OrchBench, they test structural correctness but do not simulate execution after tasks are assigned to agents. The second group evaluates specific aspects of MAS orchestration. MASBENCH studies when MAS execution outperforms a single agent, PerspectiveGap evaluates information and prompt assignment across roles, and OrchRM focuses on MAS training (Ke et al. 2026; Sun et al. 2026; Tsang et al. 2026). In contrast, OrchBench evaluates a complete orchestration plan without executing workers. The third group studies distributed information use. HiddenBench and Silo-Bench test whether agents can communicate and combine information from separate contexts (Li et al. 2025; Zhang et al. 2026). They evaluate coordination during interaction, whereas OrchBench evaluates task assignment, dependency scheduling, information transfer, and context compression beforehand.
## Problem Formulation
In this work, we study orchestration planning under fixed task dependencies. Given a task DAG and resource constraints, the planner assigns subtasks to agents and specifies how required dependency information is transferred and retained across agents. Task decomposition and dependency structure are treated as fixed inputs rather than orchestration decisions.
Let 𝒟\mathcal{D} denote the pool of raw tasks. Each generated task instance consists of a directed acyclic graph G=(V,E) and a per-agent context limit . Each node represents a subtask, and each edge (u,v)\in E indicates that requires information produced by . The number of subtasks is . Each subtask is associated with a description , input, execution, and output token budgets (,,)(x^{\mathrm{in}}_{v},x^{\mathrm{exec}}_{v},x^{\mathrm{out}}_{v}), a time budget , and a compression-sensitivity class ∈{robust,balanced,fragile}c_{v}\in\\{\mathrm{robust},\mathrm{balanced},\mathrm{fragile}\\}. specifies the maximum number of tokens that each agent can retain in its working context. The task decomposition and dependency graph remain fixed throughout evaluation.
Given , , and a maximum agent budget A_{\max}, the evaluated planner produces an orchestration plan \pi=(\alpha,\mathcal{R}). The assignment function α:\alpha:V\rightarrow\\{1,\ldots,A_{\max}\\} specifies which agent executes each subtask, while ℛ\mathcal{R} specifies cross-agent information transfers. For a dependency edge (u,v)\in E, if \alpha(u)=\alpha(v), the output of is reused locally. If \alpha(u)\neq\alpha(v) and the plan specifies \mathcal{R}(u,v)=e, where e\in(0,1], the output of is transferred to the agent executing with retention ratio . A required cross-agent transfer omitted by the plan is recorded as a missing transfer, whereas a declared transfer that does not correspond to an edge in is treated as invalid. A deterministic simulator evaluates under the task and context constraints and returns the final result quality , makespan , and total token cost .
## Methodology
##### Overview.
As shown in Figure , OrchBench has three stages: first, real-world seed tasks are transformed into dependency DAGs. Given a DAG, context limit, and agent budget, the planner produces the orchestration plan. The simulator then evaluates the plan and produces an orchestration score.
### DAG Construction
DAG Construction turns a suitable seed task into a DAG that requires multi-agent coordination. We measure its natural parallelism as k_{99}/n, where  
| =min⁡{k:≤+0.01​}.k_{99}(G)=\min\\{k:\mathrm{ms}_{k}(G)\leq C(G)+0.01(W(G)-C(G))\\}.  |  
| --- |  
Here, is the serial execution time of all subtasks, is the critical-path time, and \mathrm{ms}_{k}(G) is the makespan with workers. Thus, is the fewest workers needed to achieve of the maximum possible reduction in makespan. A larger k_{99}/n indicates greater natural parallelism. We sample a seed task from the problem pool 𝒟\mathcal{D} and remove unsuitable tasks using a seed judge. A refiner then constructs a DAG with a target number of subtasks and a target k_{99}/n. In each round, one judge checks the format, while another checks the task decomposition and parallelism. The refiner revises the DAG until both judges approve it. The detailed process is provided in Appendix E-II.
### Orchestration Planning
Given the DAG , context limit , and maximum agent budget A_{\max}, the tested planner F_{\theta} produces a workflow script . A deterministic interpreter then expands as the concrete plan \pi=(\alpha,\mathcal{R}). An example plan is provided in Appendix B-I. The assignment maps each subtask to an agent, and a subtask can start only after all of its dependencies have finished. When a dependency edge connects tasks assigned to different agents, the plan must include an information transfer \mathcal{R}(u,v)=e. Its retention ratio e\in(0,1] specifies how much of the output of upstream task is retained for downstream task . A larger preserves more information but increases communication and context usage. When the context limit of every agent is tight, the planner can reduce to save space. Because subtasks differ in their sensitivity to information loss, robust outputs can tolerate stronger compression, whereas fragile outputs require higher retention. The planner must therefore choose task assignments and transfer ratios jointly to balance information quality, communication cost, and context usage.
### Deterministic Simulation
The simulator draws on the six-stage lifecycle used by real execution frameworks: dependency resolution, agent scheduling, context acquisition, context management, subtask execution, and state updates. Given , \pi=(\alpha,\mathcal{R}), and , the simulator initializes each agent’s clock and memory and processes subtasks in topological order. For each subtask , it determines the start time, collects and manages the required context, computes the output quality and finish time, and updates the agent state. The updated state is then used by downstream subtasks. After all subtasks finish, the simulator computes the final quality, makespan, and token usage. This alignment helps the simulator capture the execution consequences of each plan. Please refer to Appendix B-II for the detailed simulation process.
##### Dependency resolution
In real execution, a subtask can begin only after all its dependencies are complete. Specifically, we preserve this by ensuring that every u∈Parents​u\in\text{Parents}(v) has finished before subtask v starts. This does not mean that all tasks are serialized; in fact, independent subtasks can be assigned to different agents to achieve parallelism.
##### Agent scheduling
In real execution, a subtask must also wait until its assigned agent is available. The simulator maintains a logical clock for each agent. For assigned to a=\alpha(v), its start time is  
| =max⁡(,maxu∈Parents⁡⁡),s_{v}=\max\left(c_{a},\,\max_{u\in\operatorname{Parents}(v)}f_{u}\right),  |  
| --- |  
where is the finish time of parent . Tasks assigned to the same agent run sequentially, while different agents can work in parallel. If several tasks are ready on one agent, the simulator follows a fixed topological order of the DAG.
##### Context acquisition
A subtask can use only the information available to its assigned agent in real execution. The simulator reconstructs the effective input of by tracing how each parent result reaches a=\alpha(v). Results produced by the same agent are reused locally. For cross-agent dependencies, the simulator checks the transfer map ℛ\mathcal{R}, applies the declared compression ratio, and records the communication tokens and retained quality. If transfer is missing, the simulator records a missing-transfer event and sets the parent’s effective quality to \lambda q, where \lambda\in[0,1] is a penalty factor.
##### Context management
Real agents operate under finite context limits: retaining more information may improve quality but increases token cost and context pressure. The simulator maintains a local memory for each agent . Before executing , its input and available parent results are added to ; if |M_{a}|>L, the stored results are compressed until they fit. Let be the context usage of the agent and the retained quality of the current subtask. Compressing it gives  
| ,=⁡,n^{\prime}_{v}=\left\lceil e\,n_{v}\right\rceil,\qquad q^{\prime}_{v}=\max\\!\left(q_{\min},q_{v}e_{s_{v}}\right),  |  
| --- |  
where e\in(0,1] is the context retention ratio, denotes the compression sensitivity of , and denotes the quality retention ratio. More fragile information requires gentler compression, but consumes more context, creating a trade-off situation for the model.
##### Subtask execution
After dependencies, agent availability, and input context are resolved, the simulator executes deterministically from its task metadata. For a non-root task, let \widetilde{q}_{uv} denote the quality of parent ’s package available to . Let denote the geometric mean of the available parent qualities. The result quality of is  
| \displaystyle q_{v}  | =clip⁡,\displaystyle=\operatorname{clip}_{[q_{\min},1]}\left(\bar{q}e_{s_{v}}\right),  |  
| --- | --- |  
where is the compression ratio for subtask , if compression is applied. The result is clipped to [q_{\min},1].
##### State updates
After execution, the simulator finishes the subtask with quality score and stores it in the local memory of agent \alpha(v). The finish time includes the task time and any post-execution context-compression delay:  
| =,,f_{v}=s_{v}+\tau_{v}+\Delta_{v}^{\mathrm{post}},\qquad c_{\alpha(v)}\leftarrow f_{v},  |  
| --- |  
where \Delta_{v}^{\mathrm{post}} is the delay caused by compression. The simulator then releases packages that no remaining subtask needs.
## Experiment Settings
##### Data.
We construct the problem pool 𝒟\mathcal{D} from four source datasets: Finance Agent , DS-1000 , Qasper , and BIRD-SQL . Using problems sampled from 𝒟\mathcal{D}, we generate 240 task DAGs for the main experiments. To study scalability, we additionally construct larger DAGs with n∈{200,500,1000}n\in\\{200,500,1000\\} nodes. We use MultiAgentBench , an established benchmark for multi-agent systems, to evaluate the agreement between simulation metrics and real-world execution results. Appendix E-I provides an overview of our DAG dataset and demonstrates that it is comprehensive and balanced. Appendix E-III analyzes DAG construction failure cases, and in Appendix E-IV we conduct experiments to show that our DAGs are of high quality.
##### Other Settings.
For benchmark validation, we evaluate six models: GLM-5.1, DeepSeek-V4-Pro, DeepSeek-V4-Flash, Qwen3.6-35B-A3B, Kimi-K2.6, and Doubao-Seed-2.0-Mini (Zeng et al. 2026; Xu et al. 2026a; Yang et al. 2025; Moonshot AI 2026; ByteDance Seed 2026). Our main evaluation covers these six models and three frontier models: Gemini-3.1-Pro-Preview, Claude-Opus-4.8, and GPT-5.5 (Google DeepMind 2026; Anthropic 2026; OpenAI 2026). For real-world execution experiments, we run Claude Code under the dynamic-workflow setting (Anthropic 2025). For the hyperparameters, we set A_{max}=100 and \lambda=0.5 (Appendix F-III). Other detailed settings are provided in Appendix G.  
| Group  | Metric  | Spearman   |  
| --- | --- | --- |  
| Scale  | DA  | 0.973  | 0.001  | 1.000  | 0.003  |  
| CA  | 0.749  | 0.090  | 0.829  | 0.058  |  
| SA  | 0.829  | 0.056  | 0.714  | 0.136  |  
| Structure  | SDT  | 0.928  | 0.011  | 0.943  | 0.017  |  
| PU  | 0.768  | 0.035  | 1.000  | 0.003  |  
| WD  | 0.887  | 0.028  | 0.771  | 0.103  |  
| ILR  | 0.664  | 0.157  | 0.600  | 0.242  |  
Table 1: Simulation-to-real correlation on MultiAgentBench (OrchBench vs. Claude Code). Figure 3: Correlations between OrchBench and real quality across frameworks. Upper/lower triangles report Pearson/Spearman coefficients.
##### Metrics.
We evaluate each execution plan in terms of output quality, scheduling efficiency, and token efficiency. Let 𝒯={∣=0}\mathcal{T}=\\{w\in V\mid\operatorname{outdeg}_{G}(w)=0\\} be the set of terminal tasks, and let q_{w}\in[0,1] be the task-specific quality score of . Overall quality is the macro-average over terminal tasks:  
| Q=\frac{1}{|\mathcal{T}|}\sum_{w\in\mathcal{T}}q_{w}.  |  
| --- |  
Let and denote the weighted critical-path length and observed makespan. Let be the total token consumption and TsingleT_{\mathrm{single}} that of the single-agent serial baseline. We define  
| =,=min⁡{1,}.E_{\mathrm{time}}=\min\left\\{1,\frac{C}{M}\right\\},\qquad E_{\mathrm{token}}=\min\left\\{1,\frac{T_{\mathrm{single}}}{T}\right\\}.  |  
| --- |  
Here, E_{\mathrm{time}} measures proximity to the critical-path lower bound, while E_{\mathrm{token}} measures token efficiency relative to the serial baseline.
The final score is the arithmetic mean of the three metrics:  
| Score=Q++3.\mathrm{Score}=\frac{Q+E_{\mathrm{time}}+E_{\mathrm{token}}}{3}.  |  
| --- |  
We also report makespan, token use, agent count, and missing transfers for diagnostic analysis.   
| Metric  | Spearman   |  
| --- | --- |  
| Final score  | 0.816  | 0.047  | 0.771  | 0.103  |  
| Time  | -0.264  | 0.633  | -0.314  | 0.564  |  
| Token usage  | -0.607  | 0.206  | -0.371  | 0.497  |  
Table 2: Correlations between our metrics and real outcomes.  
| Setting  |  
| --- |  
| Original  | 0.816  | 0.047  | 0.771  | 0.103  |  
| w/o DeepSeek-V4-Flash  | 0.677  | 0.183  | 0.600  | 0.350  |  
| w/o DeepSeek-V4-Pro  | 0.682  | 0.192  | 0.900  | 0.083  |  
| w/o Doubao-Mini  | 0.421  | 0.500  | 0.600  | 0.350  |  
| w/o GLM-5.1  | 0.949  | 0.033  | 0.900  | 0.083  |  
| w/o Kimi-K2.6  | 0.790  | 0.108  | 0.900  | 0.083  |  
| w/o Qwen3.6-A3B  | 0.719  | 0.167  | 0.600  | 0.350  |  
Table 3: Leave-one-model-out correlations between simulated scores and real task quality under Claude Code.  
| Model  | #Agents  | Miss.↓\downarrow  | Token   | Speed   | Qual.   | Score   |  
| --- | --- | --- | --- | --- | --- | --- |  
| GPT-5.5  | 6.42  | 0.12  | 0.735  | 0.951  |  
| Gemini-3.1-Pro  | 6.40  | 0.730  | 0.714  | 0.801  |  
| GLM-5.1  | 6.40  | 0.43  | 0.740  | 0.735  | 0.917  | 0.797  |  
| DeepSeek-V4-Pro  | 6.18  | 0.05  | 0.739  | 0.676  | 0.928  | 0.781  |  
| Claude-Opus-4.8  | 6.48  | 0.721  | 0.656  | 0.779  |  
| DeepSeek-V4-Flash  | 6.36  | 0.24  | 0.722  | 0.660  | 0.925  | 0.769  |  
| Qwen3.6-35B-A3B  | 6.00  | 0.25  | 0.739  | 0.650  | 0.916  | 0.768  |  
| Kimi-K2.6  | 5.85  | 0.43  | 0.647  | 0.914  | 0.768  |  
| Doubao-Seed-2.0-Mini  | 6.28  | 0.25  | 0.731  | 0.635  | 0.919  | 0.761  |  
| Model  | #Agents  | Miss.↓\downarrow  | Token   | Speed   | Qual.   | Score   |  
| --- | --- | --- | --- | --- | --- | --- |  
| GLM-5.1  | 12.15  | 0.58  | 0.693  | 0.893  |  
| Gemini-3.1-Pro  | 12.33  | 0.682  | 0.638  | 0.743  |  
| GPT-5.5  | 11.80  | 0.75  | 0.691  | 0.643  | 0.876  | 0.737  |  
| Claude-Opus-4.8  | 12.02  | 0.10  | 0.685  | 0.616  | 0.892  | 0.731  |  
| DeepSeek-V4-Pro  | 11.74  | 0.79  | 0.674  | 0.612  | 0.826  | 0.704  |  
| Doubao-Seed-2.0-Mini  | 11.55  | 3.47  | 0.704  | 0.628  | 0.777  | 0.703  |  
| Qwen3.6-35B-A3B  | 11.00  | 3.60  | 0.633  | 0.733  | 0.694  |  
| Kimi-K2.6  | 10.72  | 2.97  | 0.689  | 0.593  | 0.756  | 0.679  |  
| DeepSeek-V4-Flash  | 12.12  | 1.16  | 0.562  | 0.500  | 0.695  | 0.586  |  
| Model  | #Agents  | Miss.↓\downarrow  | Token   | Speed   | Qual.   | Score   |  
| --- | --- | --- | --- | --- | --- | --- |  
| Claude-Opus-4.8  | 29.65  | 0.43  | 0.635  | 0.484  |  
| Gemini-3.1-Pro  | 31.02  | 0.627  | 0.494  | 0.804  | 0.642  |  
| GPT-5.5  | 30.87  | 0.67  | 0.619  | 0.491  | 0.807  | 0.639  |  
| GLM-5.1  | 29.48  | 4.42  | 0.654  | 0.755  | 0.637  |  
| Qwen3.6-35B-A3B  | 29.68  | 6.45  | 0.652  | 0.485  | 0.647  | 0.595  |  
| Kimi-K2.6  | 30.45  | 5.83  | 0.621  | 0.471  | 0.660  | 0.584  |  
| DeepSeek-V4-Flash  | 29.64  | 3.55  | 0.603  | 0.447  | 0.647  | 0.566  |  
| Doubao-Seed-2.0-Mini  | 30.70  | 9.18  | 0.474  | 0.561  | 0.564  |  
| DeepSeek-V4-Pro  | 31.17  | 1.43  | 0.564  | 0.420  | 0.662  | 0.548  |  
| Model  | #Agents  | Miss.↓\downarrow  | Token   | Speed   | Qual.   | Score   |  
| --- | --- | --- | --- | --- | --- | --- |  
| Gemini-3.1-Pro  | 63.23  | 0.614  |  
| GLM-5.1  | 63.50  | 5.53  | 0.629  | 0.410  | 0.651  | 0.563  |  
| GPT-5.5  | 62.40  | 6.32  | 0.611  | 0.650  | 0.558  |  
| DeepSeek-V4-Pro  | 60.72  | 7.58  | 0.631  | 0.401  | 0.609  | 0.547  |  
| Claude-Opus-4.8  | 62.61  | 0.75  | 0.605  | 0.388  | 0.639  | 0.544  |  
| Qwen3.6-35B-A3B  | 58.23  | 14.37  | 0.406  | 0.492  | 0.514  |  
| DeepSeek-V4-Flash  | 59.65  | 4.53  | 0.599  | 0.379  | 0.564  | 0.514  |  
| Doubao-Seed-2.0-Mini  | 63.80  | 22.70  | 0.644  | 0.394  | 0.443  | 0.493  |  
| Kimi-K2.6  | 59.07  | 13.00  | 0.585  | 0.364  | 0.508  | 0.485  |  
Table 4: Main results across DAG sizes. Each panel reports results for DAGs with tasks.
## Results and Discussion
We first establish the fidelity of our simulator by demonstrating strong agreement between simulated metrics and real executions. Using the validated simulator, we then study multi-agent orchestration at scale. Our results show that preserving task-critical information is more important than simply increasing the number of agents: as coordination failures accumulate, parallel execution yields diminishing returns. Ablation studies further support our transfer and compression designs, with additional results provided in Appendix A. 
### Benchmark Validation
Structural alignment. Table reports model-level correlations between simulated orchestration metrics and the corresponding metrics from real Claude Code workflows on MultiAgentBench. For scale, DA measures agreement in the number of declared subagents, SA in the number of launched subagents, and CA in the number of subagents that return results. For structure, SDT, PU, WD, and ILR measure agreement in delegation tendency, subagent parallelism, dependency depth, and missing information transfers, respectively. The correlations across both categories indicate that OrchBench captures key orchestration behaviors. The strongest agreement appears in both scale and structure, demonstrating consistent alignment with real-world orchestration patterns. Detailed metric definitions are provided in Appendix D-I.
Outcome alignment. Table shows that simulated scores strongly correlate with real task quality (Pearson r=0.816; Spearman \rho=0.771). This correlation remains positive in all leave-one-model-out settings and reaches r=0.949 without GLM-5.1 (Table ). We assign each subtask time and token costs during DAG generation. These controlled costs test how planners balance quality and efficiency, making the time and token scores meaningful for planner comparison. However, real time and token consumption are framework-dependent and cannot be reliably predicted (Appendix D-II), which explains their lower simulation-to-real correlations.
Cross-framework robustness. Figure evaluates the agreement between OrchBench simulations and real executions using four agent frameworks: Claude Code (Anthropic 2025), SWE-mini , OpenHands , and Crush (Charmbracelet 2025). OrchBench maintains positive correlations across all four frameworks, indicating that its predictions are not tied to a particular implementation. These results support using OrchBench for initial screening, followed by validation in the target framework.
### Evaluating Orchestration
We evaluate the six validation models together with GPT-5.5, Gemini-3.1-Pro-Preview, and Claude-Opus-4.8 on DAGs with n∈{10,20,50,100}n\in\\{10,20,50,100\\} tasks. In Table , #Agents and Miss. denote the average numbers of declared agents and missing information transfers, respectively. Token, Speed, Qual., and Score denote token efficiency, scheduling efficiency, output quality, and the aggregate score defined in Equation . As the workflows grow, information routing becomes increasingly challenging: the range of average missing transfers widens from [0.00,0.43][0.00,0.43] at to [0.07,22.70][0.07,22.70] at . No model achieves the highest aggregate score at every scale: GPT-5.5 leads at , GLM-5.1 at , Claude-Opus-4.8 at , and Gemini-3.1-Pro-Preview at . Additional analysis is provided in Appendix F-I.
##### Transfer Coverage Matters More Than Agent Count.
Table reports correlations between agent count, transfer coverage, and performance. Agents– and Agents–Score measure the effect of agent count on quality score and the final score, while Coverage– measures the effect of successful transfers. Agent count is nearly uncorrelated with quality (-0.021) at , whereas Coverage is consistently more informative across scales (–), showing that more agents do not necessarily improve orchestration.
Figure 4:  Max-agent-cap sweep averaged across the six base planners.  Figure 5:  Extreme-scale results under A_{\max}=100.  
| n  | Agents–Score  |  
| --- | --- |  
| 10  | 0.468  | 0.952  | -0.481  |  
| 20  | 0.720  | 0.807  | 0.218  |  
| 50  | 0.470  | 0.829  | -0.189  |  
| 100  | -0.021  | 0.614  | -0.676  |  
Table 5: Pearson correlations between orchestration diagnostics and scores. denotes quality.  
| Quality  | Final score  |  
| --- | --- |  
| Single  | Multi  | Single  | Multi  |  
| 16\mathrm{k}  | 0.423  | 0.725  | 0.535  | 0.650  |  
| 32\mathrm{k}  | 0.649  | 0.821  | 0.613  | 0.684  |  
| 64\mathrm{k}  | 0.792  | 0.852  | 0.662  | 0.692  |  
| 128\mathrm{k}  | 0.852  | 0.859  | 0.682  | 0.693  |  
Table 6: Single/multi-agent performance under different .
##### Orchestration Reliability Diverges at Scale.
To test how this information-flow bottleneck scales, we evaluate Gemini-3.1-Pro-Preview, Claude-Opus-4.8, and DeepSeek-V4-Flash on DAGs with , , and n=1{,}000, under A_{\max}=100. As shown in Figure , from to 1{,}000 tasks, transfer coverage falls from to for Claude and from to for DeepSeek, producing and missing transfers. Gemini retains complete coverage and substantially higher quality. The degradation reflects coordination failures that accumulate as the numbers of dependencies and handoffs increase.
##### More Agents Yield Diminishing Returns.
We next ask whether increasing the agent budget improves orchestration. Figure summarizes the results across six base planners and 50 DAGs. A larger A_{\max} initially reduces compression pressure and improves quality and score. However, these gains quickly saturate: increasing A_{\max} from to more than doubles agent count while leaving scores nearly unchanged.
#### When Do More Agents Help?
We also compare MAS and single-agent execution on the same 50 DAGs to show when a single agent outperforms the MAS. Table shows that at L=16\mathrm{k}, multi-agent execution yields a 0.302 improvement in quality by avoiding repeated single-agent compression. The advantage falls to at 128\mathrm{k}, where single-agent quality is already higher on the 10-, 20-, and 50-task DAGs. Additional agents are therefore most useful when the working state exceeds one context window; once it fits, coordination can become pure overhead. Detailed per-model performance results can be found in Appendix F-II.  
| Selection  | Spearman  | Pair accuracy  |  
| --- | --- | --- |  
| OrchBench  |  
| Random  | 0.176  | 0.613  |  
Table 7: Model-ranking agreement under limited real-execution budgets for five tasks.  
| Benchmark  | Tokens (real/ours)  | Time (real/ours)  |  
| --- | --- | --- |  
| WideSearch  | /44.61​K17.35\mathrm{M}/44.61\mathrm{K}  |  56.13/0.5156.13/0.51 min  |  
| MultiAgentBench  | 383.09​K/5.16​K383.09\mathrm{K}/5.16\mathrm{K}  |  5.61/0.585.61/0.58 min  |  
Table 8: Average resource consumption per task.  
| Evaluation  | Metric  |  
| --- | --- |  
| Simulation  | Quality  | 0.1452  |  
| Speed  | 0.9231  |  
| Token  | 0.6858  |  
| Real execution  | Score  | 3.754  |  
Table 9:  Simulator-guided workflow refinement results. 
##### Simulation Enables Cost-Efficient Evaluation and Selection.
Beyond diagnosis, OrchBench helps allocate limited real-execution budgets. We rank tasks by cross-model disagreement in their simulated scores and execute only the five tasks with the highest disagreement. As shown in Table , our method achieves a Spearman correlation of and pairwise accuracy of , surpassing random selection and substantially reducing the number of executions needed for model comparison. We also demonstrate the use of task-difficulty estimation and model selection in Appendix C.
##### Simulation Cuts Token and Runtime by at least and 9.7\times.
Our approach is practical because simulation is substantially cheaper than real execution. Table shows reductions of 389\times in token and 110\times in time on WideSearch, and and 9.7\times on MultiAgentBench. This efficiency enables cost-effective plan screening, large-scale stress testing, and controlled parameter sweeps before targeted real executions.
##### Simulator-guided Refinement Improves Quality.
We evaluate simulator-guided workflow refinement on 20 MultiAgentBench tasks, using DeepSeek-V4-Flash as the execution model and DeepSeek-V4-Pro as the evaluator. For each baseline workflow (), the refined workflow () adds one simulator-selected cross-role handoff while keeping all other components fixed; if no handoff improves the simulation, . As shown in Table , the mean real-execution score increases from 3.754 to 4.150 out of .
## Conclusion
We introduced OrchBench, a benchmark for evaluating multi-agent orchestration through lightweight simulation. Our results show that good orchestration depends less on the number of agents than on preserving information across dependent tasks. Additional agents help relieve context pressure, but also introduce diminishing returns and coordination failures. The simulated results also correlate with real execution, supporting OrchBench as an efficient tool for screening orchestration plans before framework-specific validation.
## References
  * Anthropic (2025) Claude code.  Note: https://github.com/anthropics/claude-codeGitHub repository
  * Anthropic (2026) Claude Opus 4.8 System Card.  Note: Accessed: 2026-07-11. External Links: 
  * A. Bigeard, L. Nashold, R. Krishnan, and S. Wu (2025) Finance agent benchmark: benchmarking llms on real-world financial research tasks.  arXiv preprint arXiv:2508.00828. 
  * ByteDance Seed (2026) Seed2.0 Model Card: Towards Intelligence Frontier for Real-World Complexity.  External Links: 
  * M. Cemri, M. Z. Pan, S. Yang, L. A. Agrawal, B. Chopra, R. Tiwari, K. Keutzer, A. Parameswaran, D. Klein, K. Ramchandran, et al. (2025) Why do multi-agent llm systems fail?.  arXiv preprint arXiv:2503.13657. 
  * Charmbracelet (2025) Note: https://github.com/charmbracelet/crushGitHub repository
  * P. Dasigi, K. Lo, I. Beltagy, A. Cohan, N. A. Smith, and M. Gardner (2021) A dataset of information-seeking questions and answers anchored in research papers.  In Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,  pp. 4599–4610. 
  * X. Deng, Y. Gu, B. Zheng, S. Chen, S. Stevens, B. Wang, H. Sun, and Y. Su (2023) Mind2web: towards a generalist agent for the web.  Advances in Neural Information Processing Systems 36,  pp. 28091–28114. 
  * A. Drouin, M. Gasse, M. Caccia, I. H. Laradji, M. Del Verme, T. Marty, L. Boisvert, M. Thakkar, Q. Cappart, D. Vazquez, et al. (2024) WorkArena: how capable are web agents at solving common knowledge work tasks?.  arXiv preprint arXiv:2403.07718. 
  * A. Fourney, G. Bansal, H. Mozannar, C. Tan, E. Salinas, F. Niedtner, G. Proebsting, G. Bassman, J. Gerrits, J. Alber, et al. (2024) Magentic-one: a generalist multi-agent system for solving complex tasks.  arXiv preprint arXiv:2411.04468. 
  * Google DeepMind (2026) Gemini 3.1 Pro Model Card.  Google DeepMind.  External Links: 
  * T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N. V. Chawla, O. Wiest, and X. Zhang (2024) Large language model based multi-agents: a survey of progress and challenges.  arXiv preprint arXiv:2402.01680. 
  * S. Hong, M. Zhuge, J. Chen, X. Zheng, Y. Cheng, J. Wang, C. Zhang, S. Yau, Z. Lin, L. Zhou, et al. (2024) MetaGPT: meta programming for a multi-agent collaborative framework.  In International Conference on Learning Representations,  Vol. 2024,  pp. 23247–23275. 
  * C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan (2023) SWE-bench: can language models resolve real-world github issues?.  arXiv preprint arXiv:2310.06770. 
  * Z. Ke, Y. Ming, A. Xu, R. Chin, X. Nguyen, P. Jwalapuram, J. Wang, S. Yavuz, C. Xiong, and S. Joty (2026) Mas-orchestra: understanding and improving multi-agent reasoning through holistic orchestration and controlled benchmarks.  arXiv preprint arXiv:2601.14652. 
  * S. Kim, S. Moon, R. Tabrizi, N. Lee, M. W. Mahoney, K. Keutzer, and A. Gholami (2023) An llm compiler for parallel function calling.  arXiv preprint arXiv:2312.04511. 
  * J. Y. Koh, R. Lo, L. Jang, V. Duvvur, M. Lim, P. Huang, G. Neubig, S. Zhou, R. Salakhutdinov, and D. Fried (2024) Visualwebarena: evaluating multimodal agents on realistic visual web tasks.  In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 
  * Y. Lai, C. Li, Y. Wang, T. Zhang, R. Zhong, L. Zettlemoyer, W. Yih, D. Fried, S. Wang, and T. Yu (2023) DS-1000: a natural and reliable benchmark for data science code generation.  In International Conference on Machine Learning,  pp. 18319–18345. 
  * J. Li, B. Hui, G. Qu, J. Yang, B. Li, B. Li, B. Wang, B. Qin, R. Geng, N. Huo, X. Zhou, C. Ma, G. Li, K. C. Chang, F. Huang, R. Cheng, and Y. Li (2023) Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls.  In Advances in Neural Information Processing Systems,  Vol. 36,  pp. 42330–42357.  External Links: 
  * Y. Li, A. Naito, and H. Shirado (2025) HiddenBench: assessing collective reasoning in multi-agent llms via hidden profile tasks.  arXiv preprint arXiv:2505.11556. 
  * X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng, Z. Du, C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun, M. Huang, Y. Dong, and J. Tang (2023) AgentBench: evaluating llms as agents.  arXiv preprint arXiv:2308.03688. 
  * C. Ma, J. Zhang, Z. Zhu, C. Yang, Y. Yang, Y. Jin, Z. Lan, L. Kong, and J. He (2024) Agentboard: an analytical evaluation board of multi-turn llm agents.  Advances in neural information processing systems 37,  pp. 74325–74362. 
  * G. Mialon, C. Fourrier, C. Swift, T. Wolf, Y. LeCun, and T. Scialom (2023) GAIA: a benchmark for general ai assistants.  arXiv preprint arXiv:2311.12983. 
  * Moonshot AI (2026) Kimi K2.6 Tech Blog: Advancing Open-Source Coding.  External Links: 
  * OpenAI (2026) GPT-5.5 System Card.  Note: Updated April 24, 2026. Accessed: 2026-07-11. External Links: 
  * S. Qiao, R. Fang, Z. Qiu, X. Wang, N. Zhang, Y. Jiang, P. Xie, F. Huang, and H. Chen (2025) Benchmarking agentic workflow generation.  In International Conference on Learning Representations,  Vol. 2025,  pp. 69679–69703. 
  * Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang, B. Qian, et al. (2023) Toolllm: facilitating large language models to master 16000+ real-world apis.  In The twelfth international conference on learning representations, 
  * Y. Sun, X. Ren, K. Zhang, X. Liu, and J. Guo (2026) PerspectiveGap: a benchmark for multi-agent orchestration prompting.  arXiv preprint arXiv:2606.08878. 
  * K. Y. Tsang, Z. Zhao, V. Venkataramani, H. Shi, Z. Ke, S. Yavuz, S. Joty, and H. Wang (2026) Reward modeling for multi-agent orchestration.  arXiv preprint arXiv:2606.13598. 
  * K. Valmeekam, M. Marquez, A. Olmo, S. Sreedharan, and S. Kambhampati (2023) Planbench: an extensible benchmark for evaluating large language models on planning and reasoning about change.  Advances in Neural Information Processing Systems 36,  pp. 38975–38987. 
  * X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, et al. (2025a) Openhands: an open platform for ai software developers as generalist agents.  In International Conference on Learning Representations,  Vol. 2025,  pp. 65882–65919. 
  * Y. Wang, Z. Wu, J. Yao, and J. Su (2025b) Tdag: a multi-agent framework based on dynamic task decomposition and agent generation.  Neural Networks 185,  pp. 107200. 
  * R. Xiao, W. Ma, K. Wang, Y. Wu, J. Zhao, H. Wang, F. Huang, and Y. Li (2024) Flowbench: revisiting and benchmarking workflow-guided planning for llm-based agents.  In Findings of the Association for Computational Linguistics: EMNLP 2024,  pp. 10883–10900. 
  * T. Xie, D. Zhang, J. Chen, X. Li, S. Zhao, R. Cao, T. J. Hua, Z. Cheng, D. Shin, F. Lei, et al. (2024) Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments.  Advances in Neural Information Processing Systems 37,  pp. 52040–52094. 
  * A. Xu, B. Lin, B. Xue, B. Wang, B. Xu, B. Wu, B. Zhang, C. Lin, C. Dong, C. Ling, et al. (2026a) Deepseek-v4: towards highly efficient million-token context intelligence.  arXiv preprint arXiv:2606.19348. 
  * F. F. Xu, Y. Song, B. Li, Y. Tang, K. Jain, M. Bao, Z. Wang, X. Zhou, Z. Guo, M. Cao, et al. (2026b) Theagentcompany: benchmarking llm agents on consequential real world tasks.  Advances in Neural Information Processing Systems 38. 
  * A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao, C. Huang, C. Lv, et al. (2025) Qwen3 technical report.  arXiv preprint arXiv:2505.09388. 
  * J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024) SWE-agent: agent-computer interfaces enable automated software engineering.  In Advances in Neural Information Processing Systems,  External Links: 
  * S. Yao, N. Shinn, P. Razavi, and K. Narasimhan (2024) -Bench: a benchmark for tool-agent-user interaction in real-world domains.  arXiv preprint arXiv:2406.12045. 
  * O. Yoran, S. J. Amouyal, C. Malaviya, B. Bogin, O. Press, and J. Berant (2024) Assistantbench: can web agents solve realistic and time-consuming tasks?.  In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,  pp. 8938–8968. 
  * J. Yu, Y. Ding, and H. Sato (2025) Dyntaskmas: a dynamic task graph-driven framework for asynchronous and parallel llm-based multi-agent systems.  In Proceedings of the International Conference on Automated Planning and Scheduling,  Vol. 35,  pp. 288–296. 
  * A. Zeng, X. Lv, Z. Hou, Z. Du, Q. Zheng, B. Chen, D. Yin, C. Ge, C. Huang, C. Xie, et al. (2026) Glm-5: from vibe coding to agentic engineering.  arXiv preprint arXiv:2602.15763. 
  * Y. Zhang, F. Liu, Y. Shan, X. Huang, X. Yang, Y. Zhu, X. Cheng, C. Liu, K. Zeng, T. J. Zhang, et al. (2026) Silo-bench: a scalable environment for evaluating distributed coordination in multi-agent llm systems.  In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp. 29379–29398. 
  * S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, T. Ou, Y. Bisk, D. Fried, U. Alon, and G. Neubig (2023) WebArena: a realistic web environment for building autonomous agents.  arXiv preprint arXiv:2307.13854. 
  * K. Zhu, H. Du, Z. Hong, X. Yang, S. Guo, D. Z. Wang, Z. Wang, C. Qian, R. Tang, H. Ji, et al. (2025) Multiagentbench: evaluating the collaboration and competition of llm agents.  In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp. 8580–8622. 
  * M. Zhuge, W. Wang, L. Kirsch, F. Faccio, D. Khizbullin, and J. Schmidhuber (2024) Gptswarm: language agents as optimizable graphs.  In Forty-first International Conference on Machine Learning, 

Table 10: Mechanism ablations for Gemini and Doubao. Gaps are Gemini minus Doubao.  
| Setting  | Gemini Q  | Doubao Q  | Gemini Score  | Doubao Score  |  
| --- | --- | --- | --- | --- |  
| Full benchmark  | 0.690  | 0.443  | 0.247  | 0.573  | 0.493  | 0.079  |  
| No missing penalty  | 0.698  | 0.686  | 0.011  | 0.575  | 0.575  | 0.001  |  
| Auto-completion  | 0.697  | 0.663  | 0.035  | 0.575  | 0.555  | 0.020  |  
| Auto-completion + lossless  | 0.933  | 0.933  | 0.653  | 0.645  | 0.008  |  
##  Appendix A A. Ablation Study
To validate the effectiveness of the mechanisms introduced in our benchmark, we compare Gemini 3.1 Pro and Doubao Seed 2.0 Mini under controlled ablations. The two models represent a strong and a weak planner, respectively. If removing the proposed mechanisms makes their performance nearly indistinguishable, the benchmark loses its ability to discriminate orchestration capability.
We replay the same valid plans while keeping the DAGs, task assignments, agent budgets, and context limits fixed. Quality measures the information quality retained at the terminal tasks after cross-agent transfer and context compression. Score is the equal-weight average of quality, speed, and token efficiency. We report =−\Delta Q=Q_{\text{Gemini}}-Q_{\text{Doubao}} and =ScoreGemini−ScoreDoubao\Delta\mathrm{Score}=\mathrm{Score}_{\text{Gemini}}-\mathrm{Score}_{\text{Doubao}} as direct measures of model separation.
In Table , the _no missing penalty_ setting removes the quality penalty for an omitted cross-agent transfer without introducing additional time or token costs. The _auto-completion_ setting instead inserts a normal handoff for every omitted cross-agent dependency and charges its communication tokens, handoff time, and context cost. The combined setting applies auto-completion and additionally makes context compression lossless: compression still reduces context size and incurs its normal time and token costs, but it no longer reduces package quality.
Under the full benchmark, Gemini outperforms Doubao by in quality and in score. Removing the missing-transfer penalty reduces these gaps to and , while automatically completing omitted transfers reduces them to and . This shows that transfer coverage is a major source of model separation.
The combined ablation further amplifies this effect. When omitted transfers are automatically completed and context compression becomes lossless, both models obtain a quality score of approximately . The quality gap becomes effectively zero, and the score gap falls to . Thus, once both transfer omissions and context-compression losses are neutralized, the strong and weak planners become nearly indistinguishable. This result confirms that the two mechanisms jointly prevent score saturation and preserve the benchmark’s discriminative power.
Deterministic simulation of an orchestration plan
1:Input: problem package P=(G,L), concrete plan \pi=(\alpha,\mathcal{R}), max-agent cap A_{\max}, missing-transfer factor 
2:Each subtask has: input tokens, execution tokens, result tokens, time cost, and compression class. 
3:Each result package has: a token size and a quality value. 
4:if misses tasks, uses too many agents, has invalid task IDs, or has illegal transfers then
5: return ZeroScore​(invalid​-​plan)\mathrm{ZeroScore}(\mathrm{invalid\mbox{-}plan})
7:initialize each agent’s clock and memory 
8:initialize total tokens, finish times, and result qualities 
9:for all v∈TopologicalOrder​v\in\mathrm{TopologicalOrder}(G) do
10: a\leftarrow the agent assigned to subtask 
11: wait until all parent subtasks of are finished and agent is idle 
12: for all u∈Parents​u\in\mathrm{Parents}(v) do
13: if and are assigned to the same agent then
14: reuse ’s result with no transfer cost or quality loss 
15: else if ℛ\mathcal{R} declares a transfer from to then
16: copy ’s result into agent ’s memory using the declared compression ratio 
17: add transfer tokens and record the retained quality 
19: record a missing-transfer event 
20: multiply ’s contribution quality by 
23: add ’s input context to agent ’s memory and token count 
24: if agent ’s memory exceeds then
25: compress stored packages until the memory fits 
26: add compression tokens and record the quality loss 
28: execute ; add execution tokens, result tokens, and time cost 
29: compute ’s result quality from the available parent information 
30: store ’s result package in agent ’s memory 
31: if agent ’s memory exceeds then
32: compress stored packages until the memory fits 
33: add compression tokens and record the quality loss 
35: record ’s finish time 
36: release parent packages that no future subtask needs 
38:return final quality, makespan, total tokens, and diagnostics 
2"agent_pools":[
3{"name":"workers","count":2},
4{"name":"final","count":1}
8"match":{"stage":"Analysis"},
9"pool":"workers",
10"strategy":"round_robin"
13"match":{"stage":"Synthesis"},
14"pool":"final",
15"strategy":"dependency_locality"
19"pool":"workers",
20"strategy":"load_balance"
22"transfer_rules":[
24"parent_match":{"stage":"Analysis"},
25"child_match":{"stage":"Synthesis"},
26"cross_agent_only":true,
27"compression":0.80
Figure 6: An example workflow script.
##  Appendix B B. Planning and Simulation Process
### I. Planning instance
At the planning stage, each model outputs a JSON-formatted workflow_script that declaratively specifies how the input DAG should be executed. The script defines agent pools, ordered task-matching rules, a default rule for unmatched tasks, and dependency-based transfer rules. The matching rules determine which pool and assignment strategy are used for each task, whereas the transfer rules specify which intermediate results should be sent across agents and how much information is retained after compression. The script does not contain executable code or enumerate every task assignment explicitly. Instead, the benchmark interpreter applies the rules in topological order and deterministically expands the compact script into concrete agent assignments and transfer steps. Figure shows an example workflow script.
### II. Simulation Process
The simulator receives the problem package P=(G,L) and the concrete orchestration plan \pi=(\alpha,\mathcal{R}). It first checks whether the plan covers every subtask, respects the maximum agent budget, and contains only valid assignments and transfers. Invalid plans receive zero score. After this check, the simulator executes the plan without calling the planner model again.
The simulator processes subtasks in a deterministic topological order. For each subtask , its assigned agent waits until all parent subtasks have finished and the agent itself is idle. If a parent is assigned to the same agent, its result is reused directly without communication. If is assigned to another agent and the plan declares a transfer, the simulator copies the result using the specified compression ratio and records the communication cost and retained quality. If the required transfer is missing, the simulator records a missing-transfer event and reduces the contribution of by the factor .
Before executing , the simulator adds its input context to the assigned agent’s memory. If the memory exceeds , stored packages are compressed until they fit, incurring additional token cost and information loss. The simulator then executes , charges its token and time costs, computes its result quality from the available parent information, and stores the resulting package in the agent’s memory. The context limit is checked again after execution, and parent packages are released once they are no longer needed.
After all subtasks have completed, the simulator returns the final quality, makespan, total token cost, and diagnostic events. Because the execution order and all state updates follow fixed rules, the same problem and orchestration plan always produce the same result.
Table 11: Utility of OrchBench for model selection on MultiAgentBench.  
| Strategy  | Scenario  | Top-1 Cov.  | Top-1 Reg.  | Top-2 Cov.  | Top-2 Reg.  | Top-3 Cov.  | Top-3 Reg.  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| OrchBench  | Overall  | 61.5%  | 0.071  | 74.4%  | 0.033  | 81.8%  | 0.024  |  
| Historical best  | Overall  | 38.6%  | 0.142  | 73.3%  | 0.053  | 82.2%  | 0.023  |  
| OrchBench  | Negotiation  | 66.7%  | 0.067  | 86.7%  | 0.027  | 93.3%  | 0.009  |  
| Historical best  | Negotiation  | 46.7%  | 0.120  | 93.3%  | 0.009  | 93.3%  | 0.004  |  
| OrchBench  | Coding  | 50.0%  | 0.090  | 61.5%  | 0.038  | 57.1%  | 0.061  |  
| Historical best  | Coding  | 28.6%  | 0.232  | 46.7%  | 0.127  | 60.0%  | 0.057  |  
| OrchBench  | Research  | 64.3%  | 0.062  | 73.3%  | 0.036  | 93.3%  | 0.004  |  
| Historical best  | Research  | 40.0%  | 0.080  | 80.0%  | 0.022  | 93.3%  | 0.009  |  
(a) Predictors  
| Predictor  | MAE ↓\downarrow  | Pearson   | Spearman   |  
| --- | --- | --- | --- |  
| Scenario mean  | 0.088  | 0.725  | 0.614  |  
| Complexity linear  | 0.088  | 0.726  | 0.691  |  
(b) Feature correlations  
| Feature  | Pearson  | Spearman  |  
| --- | --- | --- |  
| Mean sim. makespan  | -0.754  | -0.832  |  
| Complexity index  | -0.761  | -0.823  |  
| Tool calls  | -0.754  | -0.819  |  
| Tool-task ratio  | -0.758  | -0.819  |  
| Total tokens  | -0.729  | -0.773  |  
| Task count  | -0.717  | -0.701  |  
Table 12: Task difficulty estimation from lightweight benchmark signals.
##  Appendix C C. Simulation-Guided Applications
### I. Task-conditioned Model Selection
Task-conditioned model selection asks whether OrchBench can recommend a suitable model for a specific task before running all candidate models in the real environment. For each task, OrchBench ranks the six models from the simulated orchestration signals. Top- coverage measures whether the true best real-run model appears in the recommended top- set, and Top- regret measures the score gap between the best model in that set and the true best model.
We compare OrchBench with a historical-best baseline, which ranks models by their real scores on all other tasks. This baseline is strong because it uses real execution history, but it is also expensive and unavailable for a newly introduced task suite. Table shows that OrchBench is more useful when the goal is to choose one model or a small candidate set. Overall Top-1 coverage improves from 38.6% to 61.5%, and coding improves from 28.6% to 50.0%. At Top-3, the historical baseline becomes competitive, suggesting that global model strength is helpful once the candidate set is wide. Thus, the main value of OrchBench in this setting is task-conditioned early filtering without requiring prior real executions for the target task.
### II. Task Difficulty Estimation
Task difficulty estimation asks whether OrchBench can predict how hard a task is before full real evaluation. We define task difficulty by the real average score of observed models on the task: a higher score means an easier task, and a lower score means a harder task. For each task, we compute a complexity index by averaging four normalized quantities: task count, total tokens, tool calls, and mean simulated makespan. A task is therefore more complex if it has more steps, uses more tokens or tools, or takes longer in simulation. We then use leave-one-task-out validation: each time, we train a simple linear predictor on 44 tasks and predict the real average score of the held-out task.
Table reports the results. The scenario mean is already a useful predictor of task difficulty. Adding structural complexity keeps MAE the same and improves rank correlation, with Spearman increasing from 0.614 to 0.691. The feature correlations are negative because the target is real score, where higher means easier, while the features measure task complexity. Thus, larger makespan, more tool use, more tokens, and more subtasks are associated with lower real scores. This suggests that OrchBench can provide useful task-difficulty estimates before running full real evaluation.  
| Metric  | Pearson  | Spearman  |  
| --- | --- | --- |  
| Cross-framework time  | -0.104  | -0.086  |  
| Cross-framework token  | 0.071  | 0.600  |  
| SWE-mini time-token  | 0.341  | 0.086  |  
| Claude Code time-token  | -0.126  | -0.314  |  
Table 13: Framework dependence of time and token usage. Correlations are computed on shared model-level results.
##  Appendix D D. Simulation-to-Real Validation
### I. Metric Definition
We compute every metric at the run level and then average it over runs from the same model before comparing models. Declared Agents (DA) measures how many agents the planner intended to use: in simulation, this is the value of plan.num_agents, while in the real workflow it is obtained by counting the agent(...) calls in the generated script. Started Agents (SA) and Completed Agents (CA) use the number of active agents in simulation, namely the number of distinct agents that receive at least one subtask. Their real counterparts are obtained from the workflow journal by counting the unique agent identifiers that produce a started event and a result event, respectively. Subagent Delegation Tendency (SDT) compares the simulated declared-agent count with the fraction of landed real runs that actually invoke the workflow tool. Parallel Utilization (PU) is the fraction of the available agent capacity used in simulation, Aactive/A_{\mathrm{active}}/A_{\max}. For real runs, it is computed from the subagent time intervals: we sum the active time of all subagents and divide it by the maximum possible active time, given by the maximum number of overlapping subagents multiplied by the total workflow span. Workflow Depth (WD) captures how many dependent stages the workflow contains. In simulation, it is the length of the longest dependency chain in the task DAG, normalized by the number of tasks. In real workflows, we first infer handoff edges by checking whether keywords from an earlier subagent’s output appear in a later subagent’s prompt; and the longest path in this inferred graph is then normalized by the number of subagents. Information-Loss Rate (ILR) measures how often information is not explicitly passed between agents. In simulation, it is the number of implicit reread events divided by the total number of explicit handoffs and implicit rereads. In real workflows, it is one minus the inferred handoff density, i.e., the fraction of possible earlier-to-later subagent pairs for which no handoff is detected. Pearson’s and Spearman’s are computed over the model-level averages; the former compares their numerical values, whereas the latter compares their rankings. The reported -values come from two-sided exact permutation tests over the six models.
### II. Framework Dependence
We also test whether time and token usage are stable across execution frameworks. Table reports four diagnostic correlations on the shared set of models. Cross-framework time and token measure whether model-level resource usage is consistent between SWE-mini and Claude Code dynamic workflow. The two time-token rows measure whether models that use more tokens also take more time within each framework. Time is almost uncorrelated across frameworks, and the relation between time and token usage is also inconsistent. This suggests that time and token usage are strongly affected by framework-specific execution behavior, so we use final score as the main sim-to-real validation target and treat time and token metrics as diagnostics.
Figure 7: Variance of benchmark mean scores under different task counts.  Figure 8: Structural profile of the generated DAG pool. The radar chart reports normalized structural metrics across target task-count groups, and the table gives the three-level reference ranges used for interpretation. The lower panels show the distribution of each normalized metric over the generated DAGs. Refinement-based problem generation
1:Input: raw problem pool 𝒟\mathcal{D}, target subtask count , target parallelism bucket , retry budget 
2:Output: accepted problem package P=(G,L), or no problem 
3:Each generated subtask has: description, input tokens, execution tokens, result tokens, time cost, and compression class. 
5: sample a raw seed task from 𝒟\mathcal{D}
6: ask the seed judge whether is suitable for DAG decomposition 
7:until the seed judge accepts 
8:ask the generator to build an initial semantic DAG from , , and 
9:for i=0,\ldots,K do
10: run the format judge on 
11: run the semantic judge on ; keep its repair advice 
12: if both judges accept, has subtasks, and k_{99}(G_{i})/n\in b then
13: set the context limit from the generated token budgets 
14: return the accepted problem package P=(G_{i},L)
16: ask the generator to revise using the judge failures and repair advice 
17: call the revised graph 
19:return no problem if no refined graph passes within rounds 
(a) Large-scale DAG.
(b) High-parallelism DAG.
(b) Layered pipeline DAG.
(a) Irregular DAG. Figure 11: Representative generated DAG structures, continued. The examples illustrate large scale, high parallelism, long dependency depth, regular layered execution, and irregular cross-stage dependency patterns.
##  Appendix E E. Benchmark Construction
### I. Overview
#### Task Count Stability
We also check whether the current number of tasks per scenario is sufficient to give a stable benchmark estimate. For each scenario, we fix the 60 tasks scored by Deepseek-V4-Flash and use each task’s final score as one observation. In each repeat, we sample 60 tasks with replacement from this pool. We then take the first n∈{5,10,20,30,60}n\in\\{5,10,20,30,60\\} tasks from the sampled sequence and compute their mean final score. This process is repeated 10 times, giving 10 benchmark means for each scenario and each task count. We report the unbiased sample variance of these 10 means. Figure shows that the variance generally decreases as the number of tasks increases. The reduction is clear in all four scenarios, although paper writing decreases more slowly than the other categories. At the full 60-task setting, the estimated variance is small in every scenario, with the largest value being 3.75\times 10^{-4}. This suggests that 60 tasks per scenario provide a stable estimate of model performance for our benchmark.  
|  Original task  |   |  
| --- | --- |  
|  Dropped branches before final synthesis  |  Identify the French foreign name of a black-border creature card illustrated by Matthew D. Wilson.  |  The LLM judge reports that several group-aggregation branches never reach the final analysis or delivery node.  |  The DAG is executable, but part of the searched information is silently lost before the final answer.  |  
|  Artificial over-decomposition  |  Identify the district with the second-highest number of crimes in 1995 and count male clients in that district.  |  A small SQL-style task is expanded into many near-identical query, counting, and correlation subtasks.  |  The graph reaches the target size, but the decomposition is not natural for the original task.  |  
|  Redundant verification or repeated templates  |  Compile all singers, episodes, and songs performed in the Chinese TV show I Am a Singer/Singer from 2013 to 2024.  |  The DAG contains a large verification layer that nearly mirrors the extraction layer.  |  Verification is useful, but duplicating most extraction tasks adds size without adding much orchestration structure.  |  
|  Arbitrary split not grounded in the seed  |  Apply MinMaxScaler to columns A2 and A3 grouped by month in a pandas DataFrame.  |  The DAG introduces specific months that are not required by the original task.  |  The graph looks detailed, but some details are not grounded in the seed task.  |  
|  Artificial global synchronization  |  Complete a large multi-domain web research task with several independent research requests.  |  The LLM judge identifies a global bottleneck where independent domains must wait for a shared synchronization task.  |  Large DAGs may become wide but still unnatural if they add unnecessary barriers between independent branches.  |  
|  Too-fine shallow subtasks  |  Produce a detailed research paper on supervised topic models for classification and regression from crowds.  |  The granularity diagnostic flags many short literature-review nodes as too small or underspecified.  |  The task boundaries become dominated by bookkeeping rather than meaningful subtasks.  |  
Table 14: Representative DAG generation failure modes.  
|  Original task  |  Failure pattern  |  
| --- | --- |  
|  Claude Opus 4.8  |  Produce a detailed research paper on supervised topic models for classification and regression from crowds.  |  The model uses 62 active agents for a low-parallelism problem. It has no missing transfers, but triggers 93 compression events and 97 warnings. Quality drops to 0.206 and final score is 0.409.  |  Claude usually writes complete transfers, but can over-fragment low-parallelism writing tasks. The resulting context pressure causes heavy compression and lowers quality.  |  
|  DeepSeek-V4-Flash  |  Analyze Airbnb’s gross booking value per room night from FY2022 to FY2024.  |  The model uses 75 active agents for the DAG with a target natural parallelism of 33 and declares 135 transfers, but the simulator records 60 implicit reads and 73 warnings. Quality is 0.511.  |  The plan exploits parallelism, but misses many required dependency transfers. The simulator must fall back to penalized reads, so quality is lower than the speed score suggests.  |  
|  Analyze Airbnb’s gross booking value per room night from FY2022 to FY2024.  |  The model uses 61 active agents and declares 135 transfers, but still has 57 implicit reads. Quality is 0.530 and final score is 0.619.  |  Kimi is stronger than most models overall, but this case shows the same transfer-coverage weakness: assigning dependent subtasks to different agents is not enough unless all required information is explicitly passed.  |  
|  Analyze Airbnb’s gross booking value per room night from FY2022 to FY2024.  |  The model uses 85 active agents for the DAG with a target natural parallelism of 33, declares only 123 transfers, and produces 73 implicit reads. Quality is 0.329.  |  Doubao tends to over-launch agents while under-specifying communication. This creates high coordination overhead and severe information loss.  |  
Table 15: Representative orchestration failures in simulation.
#### Data profile.
Figure profiles the generated DAG pool along five structural metrics. The choice of these metrics follows the way recent agent benchmarks and workflow-generation studies frame multi-agent difficulty. MultiAgentBench (ACL 2025) emphasizes that multi-agent evaluation should capture coordination and interaction structure, not only final task completion. WorFBench / Benchmarking Agentic Workflow Generation (ICLR 2025) is especially relevant because it treats agentic workflows as graph-structured subtask dependencies and evaluates workflow quality at both chain and graph levels. TheAgentCompany (NeurIPS 2025 Datasets and Benchmarks) and OdysseyBench (2025) similarly stress realistic, long-horizon work settings where agents must coordinate across tools, subtasks, and dependencies. Motivated by this view, we characterize each generated problem as a DAG and measure the structural properties that directly affect orchestration difficulty.
Specifically, depth measures the number of topological dependency layers and captures the sequential horizon of a problem. Branching factor is the average out-degree over non-terminal tasks, reflecting how broadly a problem decomposes into downstream subtasks. Average parallelism measures total work divided by critical-path length , which is the standard work-over-critical-path measure used in DAG scheduling to estimate exploitable concurrency. Dependency density normalizes the number of dependency edges by the number of tasks and measures average coupling strength. Edge count measures the total number of precedence constraints and captures the overall dependency volume. Together, these metrics cover the main structural sources of orchestration difficulty: long dependency chains, broad decomposition, parallel execution opportunities, and dense cross-task constraints.
For readability, we convert each metric into three reference regimes: Low, Medium, and High. This three-level discretization is used only for interpretation and normalization in the figure; it is not used to rebalance the dataset or force a uniform distribution. The thresholds are simple structural reference points: for example, already indicates a long sequential horizon, indicates substantial exploitable parallelism, and E/N>2.0 indicates a strongly coupled dependency graph. Values above the High threshold are clipped to the outer ring of the radar chart, so reaching the boundary should be interpreted as entering the high-complexity regime rather than matching the single largest DAG.
The labels T10, T20, T50, T100, and T200+ denote target task-count groups used during generation. T10 contains DAGs generated around the 10-task scale, T20 around the 20-task scale, and similarly for T50 and T100. T200+ aggregates larger target scales starting from 200 tasks, since these large-scale settings are generated less densely but are important for showing the upper structural range. The radar curves show how structural difficulty changes across task scales, while the lower distribution panels show the overall spread of normalized metric values across the generated DAG pool. The figure therefore demonstrates that the dataset is not concentrated in a single graph pattern, but covers diverse levels of depth, branching, dependency volume, coupling strength, and parallel execution potential.
Figure complements the aggregate statistics with representative DAG layouts drawn from the original generated problem graphs. The selected examples make the structural range visually explicit: the large-scale DAG demonstrates thousand-node orchestration, the high-parallelism DAG exposes many concurrently schedulable branches, the deep DAG highlights long dependency chains and multi-step progression, the layered pipeline DAG shows regular batched fan-out and fan-in, and the irregular DAG illustrates heterogeneous cross-stage dependencies. Together, these examples reinforce the aggregate profile by showing that the generated problems cover diverse graph sizes, dependency depths, structural patterns, and parallel execution opportunities.  
| Target size  | Judge  | Overall  | Coverage  | Missing  | Dependency  | Redundancy  | Parallelism  |  
| --- | --- | --- | --- | --- | --- | --- | --- |  
| 10  | Rule-based  | 83.00  | 97.00  | 98.00  | 94.00  | 92.00  | 96.00  |  
| 10  | Gemini  | 98.40  | 99.30  | 99.50  | 99.30  | 96.50  | 98.00  |  
| 10  | GLM  | 84.50  | 88.10  | 86.80  | 87.70  | 80.90  | 85.40  |  
| 20  | Rule-based  | 63.81  | 99.02  | 99.50  | 75.43  | 89.36  | 100.00  |  
| 20  | Gemini  | 95.12  | 97.00  | 98.50  | 96.38  | 90.00  | 96.88  |  
| 20  | GLM  | 77.44  | 87.22  | 88.33  | 73.11  | 67.22  | 83.00  |  
| 50  | Rule-based  | 77.69  | 98.78  | 99.80  | 97.90  | 81.01  | 97.60  |  
| 50  | Gemini  | 97.33  | 99.00  | 99.67  | 98.83  | 92.83  | 98.50  |  
| 50  | GLM  | 82.50  | 89.00  | 85.20  | 86.70  | 69.20  | 86.00  |  
| 100  | Rule-based  | 63.06  | 98.68  | 99.79  | 87.30  | 75.71  | 87.40  |  
| 100  | Gemini  | 89.67  | 97.83  | 97.83  | 93.33  | 83.83  | 88.83  |  
| 100  | GLM  | 76.11  | 88.00  | 90.11  | 78.33  | 62.33  | 80.00  |  
| 200  | Rule-based  | 86.15  | 100.00  | 100.00  | 93.53  | 92.25  | 99.42  |  
| 200  | Gemini  | 95.75  | 97.88  | 98.12  | 94.50  | 93.88  | 96.75  |  
| 200  | GLM  | 85.00  | 90.78  | 89.22  | 83.67  | 79.44  | 89.67  |  
| 500  | Rule-based  | 67.92  | 90.12  | 99.76  | 75.39  | 75.12  | 67.14  |  
| 500  | Gemini  | 71.50  | 95.00  | 97.50  | 97.50  | 57.50  | 75.00  |  
| 500  | GLM  | 75.75  | 85.50  | 78.75  | 87.50  | 64.00  | 74.50  |  
| 1000  | Rule-based  | 85.20  | 100.00  | 100.00  | 79.33  | 77.89  | 99.13  |  
| 1000  | Gemini  | 93.00  | 98.00  | 95.00  | 92.00  | 85.00  | 96.00  |  
| 1000  | GLM  | 80.60  | 89.60  | 91.60  | 76.70  | 69.40  | 88.50  |  
Table 16: Validation results for generated DAGs. Higher is better.  
| Setting  | Accuracy  | Average  |  
| --- | --- | --- |  
| w/o DAG  | 2/10 (20.00%)  | 3.300  | –  | –  |  
| w/ DAG  | 3/10 (30.00%)  | 3.575  | +10.00 pp  | +0.275  |  
Table 17: Effect of providing DAGs in actual agent runs.
### II. DAG Generation
Algorithm describes how OrchBench builds DAG problems from real seed tasks. We first sample a seed task from the problem pool 𝒟\mathcal{D}. A seed judge filters out tasks that are not suitable for DAG generation. For each accepted seed, the generator produces a DAG with a target number of subtasks and a target level of natural parallelism. Natural parallelism measures how many agents a DAG can use effectively. We define it as k_{99}/n. Here is the smallest number of workers whose schedule gets within one percent of the critical-path lower bound:  
| =min⁡{k:≤+0.01​}.k_{99}(G)=\min\\{k:\mathrm{ms}_{k}(G)\leq C(G)+0.01(W(G)-C(G))\\}.  |  
| --- |  
In this equation, is the sum of all task execution times, is the critical-path time, and \mathrm{ms}_{k}(G) is the makespan of a deterministic list schedule with workers. A larger k_{99}/n means the graph has more useful parallelism.
Generation then proceeds as a refinement loop. The structural judge checks whether the DAG is well formed. The semantic judge checks whether the DAG is a meaningful decomposition of the seed task and whether its natural parallelism matches the target. The generator revises the DAG using judge feedback until both judges accept it. The final package contains the accepted DAG and its context limit , which are passed to the simulation stage.
### III. Generation Failure Cases
We analyze failure cases from two sides. The first is DAG generation: whether the generated graph is a meaningful decomposition of the original task. The second is orchestration simulation: whether the tested model writes a plan that uses agents, transfers, and compression properly. These failures help explain both the limitations of the generated benchmark problems and the common weaknesses of current models when they are asked to orchestrate multiple agents.
#### DAG Generation Failures
Most generated DAGs pass basic structural checks, such as schema validity, acyclicity, and terminal reachability. The remaining failures are mainly semantic. They happen when the graph reaches the target size but does so in a way that is not fully faithful, natural, or useful for orchestration evaluation. The failure modes in Table are not mutually exclusive: a DAG may contain several issues at the same time.
To avoid making overlapping failure modes look like independent failure rates, we report normalized frequencies. We first compute the DAG-level failure rate over the 70 sampled DAGs: 24 DAGs are rejected by at least one successful LLM judge, giving ==p_{\mathrm{fail}}=24/70=34.3\%. We then count how often each failure mode appears among the failed-case annotations, giving total error mentions. For a failure mode with count , the reported frequency is p_{\mathrm{fail}}\cdot c_{m}/C. Thus the frequencies in Table decompose the overall failed-case mass and sum to , rather than exceeding 100% because of co-occurring errors.
These cases show that DAG generation is less likely to fail at the level of graph syntax, and more likely to fail at the level of task semantics. In particular, large DAGs tend to expose more redundancy and less clean dependency structure, while smaller DAGs are more likely to preserve the original task boundary.
#### Orchestration Simulation Failures
We also inspect workflow plans written by tested models. Here the DAG is fixed, so failures mainly come from the model’s orchestration decisions. Common problems include launching too many agents, splitting dependent subtasks across agents without declaring transfers, using compression too aggressively, and creating plans that look parallel but lose important upstream information. Table gives representative cases.
### IV. DAG Validation
The generated DAGs are the basis of OrchBench, since every orchestration plan is evaluated on top of their dependency structure. It is necessary to check whether these DAGs are structurally valid and semantically reasonable. We evaluate them along six dimensions: structure; coverage; missing-subtasks; dependency correctness; redundancy; and parallelism plausibility. The six validation dimensions are evaluated using both deterministic rules and LLM-based judging. For the rule-based evaluation, each generated DAG is scored independently. Let be the actual number of subtasks in the DAG. For each dimension, the checker counts the affected task nodes and additional structural violations, and converts them into a percentage using 100×()100\times(1-\text{issues}/N), with the number of issues capped at . The values reported in Table are the average percentages over the sampled DAGs at each target size. Thus, these values are not pass rates. The Overall score is also not the arithmetic mean of the other columns: it combines the task-level issues and structural penalties from all six dimensions, including structure, coverage, missing subtasks, dependency correctness, redundancy, and parallelism plausibility. Structure is included in the overall score but is not shown as a separate column in the table.
The structure dimension checks whether the generated object is a valid DAG with a reasonable size and complete task metadata. The task count is considered valid when it falls within of the target count, with at least one task of tolerance. The checker then verifies that task identifiers are unique, every dependency refers to an existing task, no task depends on itself, the graph is acyclic, there is exactly one terminal task, and every task can reach that terminal task. It also checks that input, execution, and result token counts and time costs are positive, and that compression and tool fields use valid values. Any task involved in one of these violations contributes to the structure penalty; graph-level violations such as a cycle, an incorrect terminal count, or a task-count mismatch are added as additional penalties.
Coverage measures whether the generated subtasks preserve the content of the original task. The rule-based checker extracts the 40 most frequent non-stopword tokens from the original seed prompt, dataset name, and summary, and computes the fraction that appear in the generated title, goal, stages, descriptions, or tool fields. A keyword coverage of at least is required. The checker also assigns each subtask coarse functional roles, such as acquisition, analysis, validation, synthesis, and delivery, and verifies that all category-specific required roles are present. The coverage score penalizes the gap below the keyword threshold and each missing required role.
Missing-subtasks measures whether the DAG omits an essential part of the workflow. The rule-based proxy flags tasks that do not lead to the terminal task, missing category-specific roles, and graphs with an incorrect terminal structure. Therefore, this score mainly captures missing workflow stages and disconnected parts of the graph; it is not based on counting every subtask that could have been generated.
Dependency correctness evaluates whether the edges form a plausible prerequisite structure. The graph must contain at least edges, which is the minimum required to connect tasks into a tree-like dependency structure. For each edge, the checker infers a coarse role order from the task descriptions, using acquisition, analysis, validation, synthesis, and delivery as progressively later stages. An edge is treated as a backward edge when its parent appears more than one role stage later than its child. The affected endpoints of such edges are penalized, and the backward-edge rate must not exceed . The checker also limits extreme fan-in and fan-out: the proxy limits are max⁡(10,)\max(10,\lceil 0.45N\rceil) incoming edges and max⁡(10,)\max(10,\lceil 0.90N\rceil) outgoing edges for a task.
Redundancy measures whether different subtasks repeat essentially the same work. Descriptions are normalized before comparison. The checker counts exact duplicate descriptions and near-duplicate pairs, where a pair is considered near-duplicate when its normalized text similarity reaches after token-overlap checks. Descriptions referring to different explicit objects, such as different years, quarters, or partitions, are not treated as duplicates. The near-duplicate pair ratio is the number of near-duplicate pairs divided by the number of comparable pairs, and it must not exceed . The checker additionally forms a structural signature from the stage, tool type, dependency list, and the beginning of the description; repeated signatures are also penalized.
Parallelism plausibility measures whether the DAG exposes useful and coherent parallel work. The checker uses deterministic list scheduling based on the task time costs to compute the critical path, total work, layer widths, and , the smallest number of agents whose estimated makespan reaches of the attainable scheduling gain. The resulting must fall inside the target parallelism range, which is derived from the declared parallelism bucket or target agent count. The DAG must also contain a downstream merge node when its target shape requires parallel branches, and the widest layer must not contain excessive near-duplicate tasks; for this last check, the pair-ratio threshold is .
The Gemini and GLM rows use the same metric names but are produced by LLM-as-judge rather than by these deterministic rules. The judge assigns each dimension an integer quality score from 0 to 100, where higher values indicate better coverage, more plausible dependencies, less redundancy, fewer missing stages, and more reasonable parallelism. The Overall judge score is a holistic quality assessment rather than a deterministic average of the five individual scores. The exact judge prompt, DAG representation supplied to the judge, and response normalization procedure are described in the dedicated judge-prompt subsection.
Table summarizes the results. The scores tend to fluctuate up and down and vary across sizes. The main failure comes from redundancy and dependency quality, while coverage and missing-subtask scores remain high in most settings. This suggests that the generated DAGs usually preserve the main task content, although larger DAGs contain more overlap and less clean dependency structure. We further test whether the generated DAGs are useful in actual agent runs. We compare two settings on 10 tasks: one gives the model only the original task description, and the other gives the generated 500-subtask DAG. In both settings, DeepSeek-V4-Pro runs under Claude Code dynamic workflow mode. The DAG setting improves accuracy from 20.00% to 30.00% and slightly increases the average score, as shown in Table .  
| Bucket  | Active agents  | Transfer coverage  | Missing transfer  | Quality  | Speed  | Final score  |  
| --- | --- | --- | --- | --- | --- | --- |  
| Low  | 39.25  | 0.858  | 23.47  | 0.568  | 0.509  | 0.585  |  
| Medium  | 62.53  | 0.973  | 6.26  | 0.584  | 0.353  | 0.509  |  
| High  | 79.58  | 0.992  | 1.77  | 0.540  | 0.336  | 0.494  |  
Table 18: 100-task results by natural-parallelism bucket.  
| Context  | System  | Quality  | Speed  | Token  | Final Score  |  
| --- | --- | --- | --- | --- | --- |  
| 16\mathrm{k}  | Single-agent  | 0.423  | 0.181  | 1.000  | 0.535  |  
| DeepSeek-V4-Flash  | 0.799  | 0.562  | 0.668  | 0.676  |  
| DeepSeek-V4-Pro  | 0.764  | 0.550  | 0.670  | 0.661  |  
| Doubao-Seed-2.0-Mini  | 0.651  | 0.533  | 0.684  | 0.623  |  
| GLM-5.1  | 0.790  | 0.547  | 0.671  | 0.669  |  
| Kimi-K2.6  | 0.721  | 0.526  | 0.691  | 0.646  |  
| Qwen3.6-35B-A3B  | 0.624  | 0.546  | 0.706  | 0.626  |  
| Multi-agent average  | 0.725  | 0.544  | 0.682  | 0.650  |  
| 32\mathrm{k}  | Single-agent  | 0.649  | 0.190  | 1.000  | 0.613  |  
| DeepSeek-V4-Flash  | 0.883  | 0.562  | 0.669  | 0.705  |  
| DeepSeek-V4-Pro  | 0.861  | 0.579  | 0.664  | 0.701  |  
| Doubao-Seed-2.0-Mini  | 0.699  | 0.552  | 0.682  | 0.644  |  
| GLM-5.1  | 0.908  | 0.563  | 0.657  | 0.709  |  
| Kimi-K2.6  | 0.803  | 0.539  | 0.681  | 0.674  |  
| Qwen3.6-35B-A3B  | 0.769  | 0.555  | 0.676  | 0.667  |  
| Multi-agent average  | 0.821  | 0.558  | 0.671  | 0.684  |  
| 64\mathrm{k}  | Single-agent  | 0.792  | 0.193  | 1.000  | 0.662  |  
| DeepSeek-V4-Flash  | 0.918  | 0.581  | 0.661  | 0.720  |  
| DeepSeek-V4-Pro  | 0.904  | 0.568  | 0.652  | 0.708  |  
| Doubao-Seed-2.0-Mini  | 0.750  | 0.550  | 0.664  | 0.655  |  
| GLM-5.1  | 0.925  | 0.580  | 0.650  | 0.718  |  
| Kimi-K2.6  | 0.799  | 0.540  | 0.678  | 0.672  |  
| Qwen3.6-35B-A3B  | 0.818  | 0.550  | 0.659  | 0.675  |  
| Multi-agent average  | 0.852  | 0.561  | 0.661  | 0.692  |  
| 128\mathrm{k}  | Single-agent  | 0.852  | 0.195  | 1.000  | 0.682  |  
| DeepSeek-V4-Flash  | 0.893  | 0.581  | 0.659  | 0.711  |  
| DeepSeek-V4-Pro  | 0.906  | 0.554  | 0.655  | 0.705  |  
| Doubao-Seed-2.0-Mini  | 0.784  | 0.553  | 0.667  | 0.668  |  
| GLM-5.1  | 0.927  | 0.563  | 0.652  | 0.714  |  
| Kimi-K2.6  | 0.834  | 0.548  | 0.671  | 0.684  |  
| Qwen3.6-35B-A3B  | 0.813  | 0.547  | 0.676  | 0.678  |  
| Multi-agent average  | 0.859  | 0.558  | 0.663  | 0.693  |  
Table 19: Quality, speed, token, and final scores under different context limits. All values are averaged over the 50 sampled problems. Table 20: Sensitivity to the missing-transfer factor . Q_{\mathrm{aff}} averages the plans containing missing transfers; \sigma_{Q} is computed across all model means, and \Delta Q_{\mathrm{G-D}} is the Gemini–Doubao quality gap.  
| Quality  | Final  | Q_{\mathrm{aff}}  | \Delta Q_{\mathrm{G-D}}  |  
| --- | --- | --- | --- |  
| 0.00  | 0.504  | 0.515  | 0.244  | 0.117  | 0.341  |  
| 0.25  | 0.527  | 0.522  | 0.311  | 0.105  | 0.317  |  
 |  
| 0.75  | 0.608  | 0.550  | 0.550  | 0.046  | 0.150  |  
| 1.00  | 0.689  | 0.576  | 0.785  | 0.022  | 0.011  |  
##  Appendix F F. Additional Results
### I. Detailed Discussion of the Main Results
Table reports the main results of OrchBench across target sizes. Here we provide additional analysis of it.
##### Transfer coverage matters more than agent count.
A central finding is that using more agents is not the same as better orchestration. Models with similar active-agent counts can have very different quality because their transfer coverage differs. For example, on 100-task DAGs, gemini-3.1-pro-preview and doubao-seed-2-0-mini both use about 63 active agents, but their missing-transfer counts are 0.07 and 22.70, and their quality scores are 0.690 and 0.443. The difference is not how many agents are used, but whether the information needed by downstream subtasks is passed forward.
##### Orchestration Depends on Structure and Trade-offs.
The results also show different orchestration styles. claude-opus-4.8 is a conservative handoff model: it rarely misses transfers and preserves quality, but does not always achieve the best final score because final score also includes speed and token efficiency. By contrast, gpt-5.5, glm-5.1, and gemini-3.1-pro-preview often achieve stronger scores by balancing quality against speed and token cost. For example, on 100-task DAGs, deepseek-v4-pro has lower quality than claude-opus-4.8, but a slightly higher final score because its speed and token scores are higher. Thus, the final score should be read as a Pareto-style summary, not as a pure quality ranking.
Source structure further changes which model is best. No model dominates every source family: gpt-5.5 leads on company research, gemini-3.1-pro-preview leads on compiler pipelines and data pipelines, and glm-5.1 leads on paper writing. The gaps are also small: the top-two gap is only 0.0052 on company research, 0.0014 on compiler pipelines, 0.0007 on data pipelines, and 0.0008 on paper writing. This indicates that OrchBench is not measuring a single abstract notion of model strength. It is also measuring whether a model can adapt its orchestration plan to different DAG structures and information-flow patterns.
Finally, task count alone does not explain difficulty. Table shows the 100-task results by natural-parallelism bucket. Low-parallelism DAGs have the most missing transfers, but still obtain the highest final score because their speed and token scores are better. High-parallelism DAGs have almost perfect transfer coverage, but lower final scores because the larger number of agents does not fully compensate for coordination cost. This suggests two different failure modes in large DAGs: low-parallelism graphs mainly fail through broken information chains, while high-parallelism graphs mainly expose the cost of coordinating many distributed branches.
Overall, the main result is that better orchestration is not equivalent to launching more agents. The stronger models are those that can distribute work while keeping dependency information available to downstream subtasks, and that can choose when the quality gain from additional coordination is worth the speed and token cost. This is the behavior that OrchBench is designed to isolate.
### II. Context-Limit Sweep
Table shows that the benefit of multi-agent orchestration is conditional on context pressure rather than universal. As the context limit increases from 16\mathrm{k} to 128\mathrm{k}, the average multi-agent quality advantage shrinks from +0.302 to +0.007, while its final-score advantage falls from +0.116 to +0.011. Under tight context, distributing intermediate state across agents avoids the repeated compression suffered by a single agent; under large context, this benefit disappears, while multi-agent execution continues to incur communication-token and information-transfer costs. Consequently, at 128\mathrm{k}, Doubao, Kimi, and Qwen already have lower average quality than the single-agent baseline, and multi-agent quality is lower in of all model–problem pairs. The slightly positive overall average is driven by the 100-subtask problems, for which the single agent still undergoes compression events on average and multi-agent quality remains higher. For the 10-, 20-, and 50-subtask problems, multi-agent quality is already lower at 128\mathrm{k}. These results indicate that multi-agent orchestration is most useful when it prevents context overflow; once the working state fits within a single context window, the single-agent system generally preserves information more reliably without paying coordination costs.
### III. Missing-transfer Sweep
We sweep λ∈{0,0.25,0.5,0.75,1}\lambda\in\\{0,0.25,0.5,0.75,1\\} by replaying existing plans, without making additional model calls. For each missing cross-agent transfer, the upstream quality contribution is multiplied by ; thus, \lambda=0 applies the strongest penalty, while \lambda=1 removes the quality penalty entirely. Since the plans and their speed and token costs remain fixed, the experiment isolates the effect of this parameter. As shown in Table , increasing mechanically raises Quality and Final but steadily reduces model separation. At \lambda=0 and , the mean quality of affected plans is only and . Conversely, at \lambda=1, \sigma_{Q} falls to , and the Gemini–Doubao quality gap nearly disappears at . With \lambda=0.5, affected-plan quality reaches , while \sigma_{Q}=0.081 and a quality gap of are retained. It therefore provides a meaningful penalty without obscuring the broader differences among models, making it a balanced default.
##  Appendix G G. Other Settings
##### Context and agent budgets.
Each standard benchmark instance retains the maximum agent budget A_{\max}=100 stored in its problem package. The per-agent context limit is fixed before orchestration planning and is independent of the evaluated planner. We estimate the active working set from task inputs, retained parent packages, task outputs, and a fraction of accumulated execution history. The raw estimate is the maximum of times the 90th-percentile active working set, twice the 95th-percentile package size, and an amortized per-agent estimate of cumulative execution and package tokens adjusted by the proportion of compression-fragile tasks. It is then mapped to the smallest accommodating window in {,,,}\\{16\mathrm{k},32\mathrm{k},64\mathrm{k},128\mathrm{k}\\}, with 128\mathrm{k} as the upper cap. This policy avoids assigning an artificially restrictive context window while preserving meaningful context pressure.
##### Planner inference and output handling.
All planner models receive the same serialized problem representation and the same planning instructions, without model-specific prompt tuning. We use a decoding temperature of and a maximum completion length of 16{,}000 tokens. Each model–problem pair receives one primary planning call. If the response cannot be parsed or fails plan validation, the model receives one repair call containing the validation errors and its previous response. We do not manually edit or complete model-generated workflows. Plans that remain invalid after this repair attempt are treated as invalid according to the rule in Appendix B. Agent identifiers are deterministically compacted after script expansion, so unused agent slots do not contribute to the reported active-agent count or simulation cost.
##### Compression and cost accounting.
For the robust, balanced, and fragile compression classes, retaining a fraction of a package preserves quality according to e^{\gamma}, with γ∈{0.35,0.85,1.25}\gamma\in\\{0.35,0.85,1.25\\}, respectively. Their minimum admissible retention ratios are , , and . When an agent exceeds , the simulator repeatedly compresses eligible memory items, prioritizing large and compression-robust packages while protecting fragile information. Each compression event adds token cost equal to of the package size before that event and one unit of simulated time. A handoff of retained tokens contributes communication tokens and max⁡\max(1,\lceil x/5000\rceil) units of time. Each active agent additionally incurs 1{,}200 startup tokens and two units of startup time.
##### Missing transfers and controlled sweeps.
Unless otherwise specified, an omitted cross-agent dependency is modeled as a quality-only missing transfer with \lambda=0.5: the upstream contribution is discounted by this factor without adding communication tokens, execution time, or stored context. This isolates information loss from additional resource penalties. Shared LLM- and tool-rate-limit waiting is disabled in the reported isolated-orchestration experiments, although the corresponding metadata are retained for optional contention studies. The agent-cap sweep uses ∈{1,2,4,8,16,32,64}A_{\max}\in\\{1,2,4,8,16,32,64\\}, while the context sweep uses L∈{,,,}L\in\\{16\mathrm{k},32\mathrm{k},64\mathrm{k},128\mathrm{k}\\}. Both sweeps reuse the same 50 problems, sampled once with seed 2026071020260710 and allocated as evenly as possible across the four nominal task scales. The extreme-scale study uses ten fixed problems at each of n∈{200,500,1000}n\in\\{200,500,1000\\} and A_{\max}=100. Since simulation is deterministic, no repeated simulator runs are required for a fixed problem and plan.
##  Appendix H H. Prompt Example
### I. DAG Generation Prompt
This subsection provides the illustrative examples of the prompts adopted used in OrchBench. At runtime, the concrete seed record, current DAG, judge feedback, target task count, target parallelism bucket, and schema fields are inserted into these templates.
#### Seed Filtering Prompt
`   
#### Refinement Prompt
 
 `   
#### Semantic Judge Prompt
 
 `   
#### Planner Evaluation Prompt
 
 `   
### II. DAG Validation Prompt
 
 
The LLM judge evaluates semantic validity that is difficult to capture with deterministic rules. The judge does not receive the full JSON for large DAGs. Instead, we compact the DAG into problem metadata, graph statistics, stage counts, largest layers, a rule-based validation snapshot, and representative task rows. Small DAGs are shown nearly in full. For large DAGs, task rows are sampled from the topology head, topology tail, widest layer, stage representatives, and stride samples. The hidden row count is included only for prompt-budget accounting and is not treated as missing subtasks.
 
 
 ` `
`
`
`
`
