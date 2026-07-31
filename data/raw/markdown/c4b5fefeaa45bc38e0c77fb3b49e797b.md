arXiv is now an independent nonprofit! Learn more ×
License: CC BY 4.0 
arXiv:2607.25877v1 [cs.AI] 28 Jul 2026
11institutetext: University of Hull, Hull HU6 7RX, UK 11email: bart_custers@hotmail.com 22institutetext: 22email: k.aslansefat@hull.ac.uk
# Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks
Bart Custers  Koorosh Aslansefat 
###### Abstract
This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.
Actuarial Modelling
##  Introduction
Over the past decades, artificial intelligence (AI) has become increasingly important in the insurance industry, particularly for predictive modelling and automation . Accurate risk estimation is central to insurance, as insurers rely on predictions of future claims to determine premiums and ensure both profitability and solvency. Risk modelling aims to capture differences in risk across policyholders, as these differences directly influence pricing decisions. For example, characteristics such as age or driving experience can significantly affect claim frequency, making accurate risk differentiation essential. Despite ongoing technological progress, actuarial risk modelling remains a resource-intensive process that requires substantial manual effort.
Recent advances in large language models (LLMs) have enabled the development of AI agents capable of performing complex reasoning tasks . These agents can potentially automate actuarial workflows, which typically involve data preparation, model development, validation, and interpretation. However, the use of LLM-based agents in actuarial risk modelling remains largely unexplored. A key challenge in adopting such systems is their lack of transparency. AI models are often perceived as “black boxes,” and LLM-based agents introduce additional concerns, including hallucinations and variability across runs . For actuaries, this is problematic, as transparency and explainability are essential in a highly regulated environment .
The safety implications of LLM-based multi-agent systems are particularly important in insurance risk modelling, where automated decisions may directly affect pricing, customer fairness, and financial accessibility. Errors introduced by a single agent could propagate to subsequent workflow stages, potentially leading to incorrect or biased outcomes that may be difficult to detect. Existing approaches do not sufficiently address how errors or uncertainty arise and propagate in multi-step, agent-based workflows. In addition to incorporating explainability techniques such as concept-based explanations and fairness assessments, this work therefore introduces a novel uncertainty modelling approach. We propose a runtime safety-monitoring framework for LLM-based multi-agent systems in high-stakes insurance workflows. The main contribution lies in combining token-level log probabilities from LLM outputs with a Bayesian Network that captures dependencies between workflow stages. As a result, the framework provides a structured representation of uncertainty, and a safety mechanism that may help identify unsafe workflows states.
##  Background
###  2.1 Multi-Agent Systems
Multi-agent systems (MAS) extend the concept of single LLM-based agents by enabling multiple agents to collaborate on shared tasks. This collaborative setup is particularly useful for complex problem-solving, where tasks can be decomposed into smaller, specialized components, which improves overall system performance . In addition, MAS can enhance robustness, since failures in one component may be mitigated by other agents within the system . Frameworks such as AutoGen and AgentVerse , for example, show how various agents are able to collaborate on complex tasks. Applications of MAS in the insurance domain, particularly for actuarial tasks, remain relatively limited. Existing studies primarily focus on the use of LLMs for specific tasks, such as processing unstructured data or supporting actuarial analysis . Despite all advances, MAS face several challenges. LLM-based agents are not inherently trained to collaborate, which may result in unpredictable behaviour or inconsistent reasoning . Furthermore, issues such as hallucination and sensitivity to prompts persist in multi-agent settings.
Evaluating LLM-based MAS is challenging due to their dynamic and probabilistic nature. Traditional evaluation metrics, which focus on task-specific performance, are often insufficient for capturing the broader behaviour of agent systems. Recent research therefore emphasizes holistic evaluation approaches that consider multiple aspects of system performance . One such framework distinguishes between evaluation objectives and evaluation processes . Evaluation objectives define what should be assessed, including dimensions such as agent behaviour, capabilities, reliability, and safety or alignment. Despite these developments, several limitations remain. Many evaluation approaches still focus on narrow aspects such as task accuracy or tool usage, while neglecting system-level properties like robustness and interaction dynamics .
###  2.2 Uncertainty quantification
A key consideration in deploying MAS is the handling of uncertainty. In autoregressive language models, uncertainty arises from the probability distribution over possible next tokens during text generation . Token-level log probabilities provide a model-internal confidence-related signal, but not a direct probability of correctness. The use of log probabilities ("logprobs") has been demonstrated by , where the authors propose Logprobs to monitor LLM updates. Furthermore, use logprobs to calculate uncertainty and reduce LLM hallucinations. However, such uncertainty estimates do not capture how uncertainty accumulates across the workflow. In MAS, decisions are interdependent, meaning that the output of one agent influences subsequent steps. This leads to a distinction between intrinsic uncertainty, which reflects uncertainty at a single step, and extrinsic uncertainty, which captures uncertainty propagated from earlier decisions . Sampling-based approaches, such as Monte Carlo methods, have been proposed to approximate uncertainty propagation by generating multiple reasoning trajectories . Although these methods can provide insights, they are computationally intensive and may be difficult to interpret. An alternative approach is to represent dependencies explicitly using a Bayesian Network, where nodes correspond to agent decisions and edges represent their relationships . This allows uncertainty to be modeled in a structured and interpretable way.
##  Multi-agent system design
The framework, shown in Fig. , follows a centralised star topology . A Central Hub coordinates four specialised agents through message passing, avoiding direct agent-to-agent communication and enabling controlled workflow oversight. The Data Preparation Agent performs data ingestion, cleaning, and encoding. The Modelling Agent develops predictive models. The Reviewing Agent evaluates data preparation and modelling outputs. The Explanation Agent supports interpretability and guardrails. Each agent records outputs and metadata, while shared memory stores information from previous workflow stages.
The Central Hub routes tasks based on agent feedback. If the Reviewing Agent detects issues, the workflow can be revised or terminated. To reduce prompt complexity, each agent task is divided into layers such as planning, code generation, evaluation, and explanation. The Reviewing Agent checks performance, consistency, and modelling decisions. The Explanation Agent assesses internal beliefs, concept alignment, and fairness. Concept alignment is measured using Testing with Concept Activation Vectors , while fairness is assessed through group-level comparisons between predicted and observed outcomes for sensitive attributes such as age and population density.
Figure 1: Sketch of the application’s architecture
The framework supports three LLM backends, all relatively small in size, as the aim was to invoke backends that can be quickly run on local machines. The three models, Llama 2 7B, and Llama 3.1 8B , and Qwen2.5 7B , can all be characterized as decoder-only transformer models and are all available as open source model.
##  Uncertainty quantification
###  4.1 Log probabilities and uncertainty estimation
Autoregressive language models generate outputs token-by-token from a predictive distribution conditioned on the input prompt. Given an input and model parameters , the predictive distribution over outputs can be written as p_{\theta}(y\mid x), and for a generated sequence of outputs y=(z_{1},\ldots,z_{L}) with length , the probability can be decomposed into conditional token probabilities:  
| =p_{\theta}(y|x)=\prod_{t=1}^{L}p_{\theta}(z_{t}|z_{<t},x)  |  
| --- |  
Taking the logarithm yields the log probability of the sequence:  
| =​\log p_{\theta}(y|x)=\sum_{t=1}^{L}\log p_{\theta}(z_{t}|z_{<t},x)  |  
| --- |  
Log probabilities (’logprobs’) therefore provide a systematic approach to quantify how likely a particular outcome is according to the model, and they are directly derived from the predictive distribution. Because the text length of an input prompt can influence the magnitude of the log probability, it is common to apply length normalization to ensure fair comparison between responses of different lengths . Hence, the normalized log probability \bar{\ell}(y) is computed as:  
| =​​\bar{\ell}(y)=\frac{1}{L}\sum_{t=1}^{L}\log p_{\theta}(z_{t}|z_{<t},x)  |  
| --- |  
Although log probabilities provide useful confidence-related signals, they do not directly represent the probability that an agent successfully completed its task, since LLMs may assign high likelihood to fluent but incorrect outputs. Therefore, the proposed framework treats log-probability summaries as uncertainty features rather than direct success probabilities. For agent , the length-normalised log-probability summary is computed as  
| =​​,s_{i}=\frac{1}{L_{i}}\sum_{t=1}^{L_{i}}\log p_{\theta}(z_{t}|z_{<t},x),  |  
| --- |  
which is transformed into a bounded confidence feature q_{i}=\exp(s_{i}). The probability of successful task completion is then estimated as  
| P​(=s​u​c​c​e​s​s∣)=P(X_{i}=success\mid q_{i})=f_{\mathrm{cal}}(q_{i})  |  
| --- |  
where f_{\text{cal}} denotes a calibration function estimated using validation runs. The calibrated value is then incorporated into the Bayesian Network as probabilistic evidence.
###  4.2 Bayesian Networks
In this MAS approach, uncertainty propagation is represented using a Bayesian Network that models the dependencies between agents. Each stage of the workflow is modelled as a node, and dependencies between stages are captured through directed edges, as shown in Fig. . Token-level log probabilities are used to quantify uncertainty at each node, which is then propagated through the network to estimate overall system uncertainty. Bayesian Networks (BNs) are probabilistic graphical models that represent the joint probability distribution of a set of random variables using a directed acyclic graph . Each node in the graph corresponds to a random variable, and directed edges represent conditional dependencies between variables. Let X=\\{X_{1},...,X_{n}\\} that denotes workflow tasks. For example, may represent successful data preparation, the successful review of the data, and the successful training of a model. The defining property of a Bayesian Network is that the joint distribution factorizes according to the structure of the graph:  
| =P(X_{1},...,X_{n})=\prod_{i=1}^{n}P(X_{i}|\mathrm{Pa}(X_{i}))  |  
| --- |  
where \mathrm{Pa}(X_{i}) denotes the set of parent nodes of . Each conditional probability term is specified through a conditional probability table (CPT). These tables quantify how the probability of a node depends on its parents. Hence, Bayesian Networks are suitable frameworks to visualize how conditional dependence and uncertainty accumulate through a network. In the context of the agent workflow, each node in the Bayesian Network represents the successful execution of a task performed by an agent. The confidence score obtained from the log probabilities of the agent’s response is used to parametrize the prior probability of that node, where denotes the output produced by agent is P​(=success)=P(X_{i}=\text{success})=c(y_{i}).
Figure 2: Bayesian Network representation of the actuarial workflow, including posteriors for each phase success (1) or failure (0).
The Bayesian Network used in this study represents an abstracted execution trace of the workflow rather than the full control logic of the agentic system. We do not model temporal ordering beyond direct parent-child dependencies, nor do we explicitly represent task priority, repeated execution, feedback loops, or iterative revision cycles. If an agent requests a revision, the final accepted output of that stage is used as the evidence for the corresponding node. This assumption keeps the graph acyclic and interpretable, which is appropriate for the present proof-of-concept study. Extending the model to dynamic Bayesian Networks or influence diagrams is left for future work. These values form the initial probability assignments for nodes that do not have parent variables. For nodes that depend on preceding steps in the workflow, the confidence score contributes to the conditional probability tables. As a CPT example, Fig. shows that the relationship between WorkflowOK and its three parent nodes can be characterized as an "AND" gate, implying that WorkflowOK can only be true if all parent nodes are true. The CPT on the right shows the probability of WorkflowOK being true (1) for each combination of parent outcomes. When all parent nodes are true, the probability of WorkflowOK being true is equal to its prior (0.99), or posterior when evidence is gathered during the workflow process.
Figure 3: CPT example of WorkflowOK, depending on three parent nodes. The “AND” gate label indicates that WorkflowOK succeeds only if all parent nodes pass.
Along the workflow run, new evidence is included in the network, and posterior probabilities are updated. The resulting network provides a dependency graph of uncertainty propagation within the workflow, as visualized in Fig. . An important advantage of a Bayesian Network is its interpretability. The graphical structure makes it possible to identify which components of the workflow contribute most to overall uncertainty. If a particular node shows high uncertainty or strongly influences downstream tasks, it could be flagged as a potential problem in the workflow.
###  4.3 Inference and uncertainty quantification
Once the Bayesian Network structure and conditional probability tables are defined, probabilistic inference can be performed to estimate posterior probabilities across the workflow. The objective of this inference is to determine how uncertainty in individual agent outputs affects the reliability of the final workflow outcome. The Bayesian Network for the actuarial workflow stores prior probabilities, CPTs, and holds functions to update the network and for inference. Throughout the workflow, the agents log the uncertainty measurements in the metadata, which is then extracted by the Central Hub that updates the Bayesian Network accordingly. At the end of the workflow, this results in a Bayesian Network graph with conditional probabilities on workflow subtasks.
Table 1: Scenario-based probability of successful workflow execution.  
 |  
|  |  
|  Safe scenario: low temperature (0.2) for all agents  |  
|  Mixed scenario: low temperature (0.2) for data prep and modelling agent, medium temperature (0.7) for reviewing and explanation agent  |  
|  Moderate scenario: medium temperature (0.7) for all agents (default)  |  
|  Risky scenario: high temperature (1.2) for one agent  |  
Fig. shows an example of the Bayesian Network graph produced by the actuarial workflow. It visualizes for each step or agent in the workflow the inferred average and standard deviation of the logprobs, based on the underlying dependencies. Here, most steps in the workflow show a certainty around 80%. However, the Bayesian Network also shows the propagation of uncertainty, as combining multiple agent outputs to finish the workflow results in a final certainty of 55% in this presented example, which is significantly less compared to the individual agent certainties. To further test uncertainty propagation, the workflow can be tested with different settings, such as the structure (e.g. sequential), or LLM temperature. The scenarios for tests with different temperature settings for the LLM backends are shown in Table . By testing with different LLM temperatures, the amount of randomness in the agent’s responses is varied, which has a direct effect on uncertainty. The scenarios in Table illustrate how increased randomness and uncertainty propagate through the network and reduce the probability that the overall workflow succeeds (1). In a conservative scenario (A), all agents operate with a low temperature (0.2). As expected, the probabilities of success are high across the network and the final WorkflowOK node shows the highest reliability. Scenario B introduces a mixed configuration: low temperature for the Data Preparation and Modelling agents, but medium temperature for Reviewing and Explanation agents. This increases variability in some tasks and leads to a decline in the probability that the workflow succeeds. Scenario C applies a moderate temperature (0.7) to all agents, thereby representing the default settings of the LLM backends. Finally, Scenario D maintains moderate temperatures but increases the temperature of the Explanation agent (1.2), showing how higher uncertainty in a single component can significantly reduce the reliability of the overall workflow. Hence, this approach provides useful insights into workflow certainty and possible weak elements in the workflow.
##  Evaluation
The evaluation of the MAS focuses on four key dimensions: agent behaviour, consistency, agent capabilities (including error detection and adaptability), and safety. The analysis is based on repeated executions of the workflow using three LLM backends. Each backend was tested on the original dataset (10 runs) and on 20 systematically perturbed datasets designed to introduce controlled errors. Results are summarized in Table . In terms of general performance and agent behaviour, the MAS achieved a high task success rate, with at least 80% of runs completed successfully across all backends. The predictive performance, measured using RMSE, was comparable to a baseline model, indicating that the MAS reliably reproduced standard actuarial results. While the Llama models performed similarly to the baseline, the Qwen backend achieved slightly better average performance. However, workflow certainty, derived from a Bayesian Network, varied significantly across backends, suggesting differences in how confidently each model evaluated its own outputs. Additionally, agent decisions differed across backends: Llama 2 tended to approve workflows more easily, while Llama 3.1 and Qwen more frequently included critical notes, highlighting variability in agent judgement despite identical prompts.
Table 2: Workflow performance metrics, perturbed test metrics, and agent-level uncertainty comparison of LLM backends
Main workflow metrics Task Success Rate Baseline model RMSE Mean RMSE Mean workflow uncertainty Test perturbed dataset metrics Error Detection Rate Mean RMSE Mean workflow uncertainty Agent-level uncertainty scores Data Preparation Agent Reviewing Agent Modelling Agent Explanation Agent Overall Workflow
A key focus of the evaluation was error detection and adaptability under perturbed datasets. Here, substantial differences between backends emerged. The Qwen model achieved a high error detection rate (90%), significantly outperforming Llama 2 (45%) and Llama 3.1 (65%). It also showed better predictive performance under perturbations and demonstrated a stronger tendency to adapt by retraining models or changing strategies. In contrast, the Llama models often failed to detect severe issues and rarely adjusted their approach. Further analysis showed that the MAS was particularly sensitive to distributional changes (population shifts), while other perturbations, such as missing values or sparsity, were less reliably detected. This highlights specific weaknesses in the validation process and suggests areas for improvement. Regarding safety, the Explanation Agent acts as a guardrail by evaluating belief consistency, interpretability (via TCAV), and fairness. The uncertainty tracking through the Bayesian Network provided useful insights. Table , the third part shows the average uncertainty scores per agent, and the combined uncertainty over the whole workflow. These results highlight how, even with high individual uncertainty scores for the agents, the propagation through the workflow can significantly reduce the score.
Table 3: Overview of test datasets, severity indicators and uncertainty scores
T1 Missing values - low na na na T2 Missing values - high na na na T3 Missing rows - low na na T4 Missing rows - high na na T5 Missing column - low na na na na na 0.6033 T6 Missing column - high na na na na na 0.5737 T7 Data increase - low na na T8 Data increase - high na na T9 Extra column - var1 na na na na na 0.5648 T10 Extra column - var2 na na na na na 0.5837 T11 Inject feature noise - var1 na na na na T12 Inject feature noise - var2 na na na na T13 Inject label noise - low na na na na T14 Inject label noise - high na na na na T15 Distribution shift - var1 na na T16 Distribution shift - var2 na na T17 Fairness test - low na na na na T18 Fairness test - high na na na na T19 Counterfactual test 1 na na na na na T20 Counterfactual test 2 na na na na na
Each backend was also tested on 20 perturbed datasets to assess error detection and handling. Table summarises these perturbations and reports the uncertainty score for each run, with derivations in Appendix . Following , these scores help examine how dataset characteristics relate to workflow uncertainty.
Appendix compares the uncertainty distributions of default and perturbed runs for the Qwen backend, which showed the strongest error detection and adaptability. Runs with detected issues may fall outside the default distribution, while the scenarios in Table are shown as individual points. Large deviations, for example measured using conformal prediction, could serve as warning signals for further review.
##  Conclusion
This work presented a runtime uncertainty-monitoring framework for LLM-based multi-agent systems in actuarial risk prediction. The system uses specialised agents for data preparation, modelling, review, and explanation, coordinated through a central hub. Its main contribution is the use of calibrated token-level log-probability signals together with a Bayesian Network to model how uncertainty propagates across agent outputs and workflow stages. Rather than assessing each agent in isolation, the framework traces uncertainty through the full workflow, helping to identify weak points and cases where human review may be needed. This is particularly important in actuarial settings, where unreliable outputs may lead to incorrect risk assessment, unfair pricing, or regulatory concerns.
The results show that the MAS can reproduce baseline actuarial modelling performance while providing additional insight into workflow-level confidence. However, the effectiveness of the approach depends on the selected LLM backend, with differences observed in error detection, adaptability, and uncertainty behaviour. The proposed Bayesian Network should therefore be interpreted as a runtime uncertainty-propagation monitor, not as a proof of output correctness.
This study has several limitations. The Bayesian Network abstracts the workflow as a directed acyclic dependency model and does not explicitly represent execution sequence, task priority, repeated revisions, or feedback loops between agents. These aspects are handled operationally by the central hub, while the Bayesian Network uses the final accepted output of each stage as evidence. Future work will extend the framework to better distinguish intrinsic and extrinsic uncertainty , introduce symptom layers for identifying the causes of uncertainty , and explore dynamic Bayesian Networks to capture temporal behaviour and iterative repair cycles.
####  6.0.1 Data and Code Availability
Regarding research reproducibility, the Python implementation, datasets, and evaluation notebooks supporting this paper are publicly available on GitHub: https://github.com/bart-custers/actuarial_agents
####  6.0.2 \discintname
The authors have no competing interests.
## References
  * [1] T. Chauvin, E. L. Merrer, F. Taïani, and G. Tredan (2025-12) Log probability tracking of llm apis.  arXiv 2512.03816.  External Links: 
  * [2] W. Chen, Y. Su, J. Zuo, C. Yang, C. Yuan, C. Chan, H. Yu, Y. Lu, Y. Hung, C. Qian, Y. Qin, X. Cong, R. Xie, Z. Liu, M. Sun, and J. Zhou (2023-10) AgentVerse: facilitating multi-agent collaboration and exploring emergent behaviors.  arXiv 2308.10848.  External Links: 
  * [3] L. Donaldson, C. Walker, K. Aslansefat, and Y. Papadopoulos (2026) Bayesian uncertainty propagation for agentic rag pipelines: a proof-of-concept study on multi-hop question answering.  arXiv preprint arXiv:2607.00972. 
  * [4] J. Duan, J. Diffenderfer, S. Madireddy, T. Chen, B. Kailkhura, and K. Xu (2025-06) UProp: investigating the uncertainty propagation of llms in multi-step agentic decision-making.  arXiv 2506.17419.  External Links: 
  * [5] S. Hatzesberger and I. Nonneman (2025-06) Advanced applications of generative ai in actuarial science: case studies beyond chatgpt.  arXiv 2506.18942.  External Links: 
  * [6] X. He, D. Wu, Y. Zhai, and K. Sun (2025) SentinelAgent: graph-based anomaly detection in multi-agent systems.  arXiv 2505.24201.  External Links: 
  * [7] Z. Hu, T. Zheng, and H. Huang (2024-10) A bayesian approach to harnessing the power of llms in authorship attribution.  arXiv 2410.21716.  External Links: 
  * [8] International Actuarial Association (2024) Artificial intelligence governance framework - general actuarial practice.  https://actuaries.org/paper/artificial-intelligence-governance-framework/ [Accessed 3/12/25]. 
  * [9] B. Kim, M. Wattenberg, J. Gilmer, C. Cai, J. Wexler, F. Viegas, and R. Sayres (2017-06) Interpretability beyond feature attribution: quantitative testing with concept activation vectors (tcav).  arXiv 1711.11279.  External Links: 
  * [10] Z. Liu, Y. Liu, B. Cai, and C. Zheng (2015) An approach for developing diagnostic bayesian network based on operation procedures.  Expert Systems with Applications 42 (4),  pp. 1917–1926.  External Links: ISSN 0957-4174, 
  * [11] A. Malinin and M. Gales (2020-02) Uncertainty estimation in autoregressive structured prediction.  arXiv 2002.07650.  External Links: 
  * [12] Meta AI (2024-07) Introducing llama 3.1.  https://ai.meta.com/blog/meta-llama-3-1/ [Accessed 25/1/2026]. 
  * [13] M. Mohammadi, Y. Li, J. Lo, and W. Yip (2025-08) Evaluation and benchmarking of llm agents: a survey.  In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2,  pp. 6129–6139.  External Links: 
  * [14] A. Nafar, K. B. Venable, Z. Cui, and P. Kordjamshidi (2025-08) Extracting probabilistic knowledge from large language models for bayesian network parameterization.  arXiv 2505.15918.  External Links: 
  * [15] D. Oreski, S. Oreski, and B. Klicek (2017-03) Effects of dataset characteristics on the performance of feature selection techniques.  Applied Soft Computing 52,  pp. 109–119.  External Links: ISSN 15684946
  * [16] E. Owens, B. Sheehan, M. Mullins, M. Cunneen, J. Ressel, and G. Castignani (2022-12) Explainable artificial intelligence (xai) in insurance.  External Links: ISSN 22279091
  * [17] Probabilistic reasoning in intelligent systems.  Morgan Kaufmann Publishers Inc., San Francisco, USA.  External Links: 
  * [18] Qwen2.5-7b-instruct (model card).  https://huggingface.co/Qwen/Qwen2.5-7B-Instruct [Accessed 25/1/2026]. 
  * [19] R. Sapkota, K. I. Roumeliotis, and M. Karkee (2025-05) AI agents vs. agentic ai: a conceptual taxonomy, applications and challenges.  arXiv 2505.10468.  External Links: 
  * [20] K. Tran, D. Dao, M. Nguyen, Q. Pham, B. O’Sullivan, and H. D. Nguyen (2025-01) Multi-agent collaboration mechanisms: a survey of llms.  arXiv 2501.06322.  External Links: 
  * [21] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, W. X. Zhao, Z. Wei, and J. Wen (2024-12) A survey on large language model based autonomous agents.  Frontiers of Computer Science 18.  External Links: ISSN 20952236
  * [22] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, A. H. Awadallah, R. W. White, D. Burger, and C. Wang (2023-10) AutoGen: enabling next-gen llm applications via multi-agent conversation.  arXiv 2308.08155.  External Links: 
  * [23] M. Xu, Q. Gan, Z. Zhu, and H. Qin (2025-07) Logprobs know uncertainty: fighting llm hallucinations.  In Proceedings of the ACM SIGSOFT Symposium on the Foundations of Software Engineering,  pp. 1242–1243.  External Links: ISBN 9798400712760, ISSN 15397521
  * [24] Y. Yang, Q. Peng, J. Wang, Y. Wen, and W. Zhang (2024-12) LLM-based multi-agent systems: techniques and business perspectives.  arXiv 2411.14033.  External Links: 
  * [25] A. Yehudai, L. Eden, A. Li, G. Uziel, Y. Zhao, R. Bar-Haim, A. Cohan, and M. Shmueli-Scheuer (2025-03) Survey on evaluation of llm-based agents.  arXiv 2503.16416.  External Links: 


##  Appendix 0.A Appendix: Dataset severity indicators
To quantify how strongly a dataset has changed between a baseline dataset and a perturbed dataset , several indicators were computed. These indicators capture structural, statistical, and distributional changes between the datasets.
###  0.A.1 Row Change
The row change indicator measures the relative change in the number of observations between the baseline and perturbed dataset.  
| RowChange=\text{RowChange}=\frac{|n_{p}-n_{b}|}{n_{b}}  |  
| --- |  
where:
  * •
is the number of rows in the baseline dataset,
  * •
is the number of rows in the perturbed dataset.


###  0.A.2 Column Change
The column change indicator measures the relative change in the number of features (columns).  
| ColChange=\text{ColChange}=\frac{|p_{p}-p_{b}|}{p_{b}}  |  
| --- |  
where:
  * •
is the number of columns in the baseline dataset,
  * •
is the number of columns in the perturbed dataset.


###  0.A.3 Missing values
The missing value indicator measures how the total number of missing values changes between datasets relative to the number of cells. It is computed as:  
| Missingness=||\text{Missingness}=\frac{|M(D_{p})-M(D_{b})|}{n_{b}p_{b}}  |  
| --- |  
where:
  * •
M(D_{p}) is the number of missing values in the perturbed dataset,
  * •
M(D_{b}) is the number of missing values in the baseline dataset.


###  0.A.4 Target Shift
Target shift measures the standardized difference in the mean of the target variable between datasets. Let denote the target variable (in this case the number of claims). Define the mean of the target value as \mu_{b}=\mathbb{E}{D_{b}}[Y] and \mu_{p}=\mathbb{E}{D_{p}}[Y]. The target shift is then defined as:  
| TargetShift=\text{TargetShift}=\frac{|\mu_{p}-\mu_{b}|}{\sigma_{b}}  |  
| --- |  
where:
  * •
is the mean target value in the perturbed dataset,
  * •
is the mean target value in the baseline dataset,
  * •
sigma_{b} is the standard deviation of the target value in the baseline dataset.


###  0.A.5 Sparsity
Sparsity measures the proportion of elements that are either zero or missing. Let the number of zero values and the number of missing values be defined by:  
| =,=Z(D)=\sum_{i=1}^{n}\sum_{j=1}^{p}\mathbf{1}(x_{ij}=0),\qquad M(D)=\sum_{i=1}^{n}\sum_{j=1}^{p}\mathbf{1}(x_{ij}=\text{NA})  |  
| --- |  
The sparsity of dataset is defined as:  
| Sparsity​=\text{Sparsity}(D)=\frac{Z(D)+M(D)}{np}  |  
| --- |  
where is the total number of elements in the dataset.
###  0.A.6 Population Shift
Population shift is measured using a population stability index (PSI), which quantifies changes in the distribution of a variable between datasets. First, the baseline variable is divided into quantile-based bins. Let N^{b}_{k} and N^{p}_{k} be the numbers of observations from the base and perturbed datasets, respectively, that fall into bin . The corresponding proportions are  
| ,,.p^{b}_{k}=\frac{N^{b}_{k}}{n_{\text{b}}},\qquad p^{p}_{k}=\frac{N^{p}_{k}}{n_{\text{n}}},\quad k=1,\dots,K.  |  
| --- |  
The PSI is then defined as  
| PSI=​\text{PSI}=\sum_{k=1}^{K}(p^{p}_{k}-p^{b}_{k})\log\left(\frac{p^{p}_{k}}{p^{b}_{k}}\right)  |  
| --- |  
A higher PSI indicates stronger distributional drift.
###  0.A.7 Correlation Shift
Correlation shift is measured by how much the correlation structure between the numeric columns of two data sets changes. It computes the correlation matrix of all numeric variables in each dataset and then returns the Euclidean (L2) norm of the difference between these two correlation matrices (i.e., a single number summarizing the overall shift in pairwise correlations):  
| CorrShift=\text{CorrShift}=\left\|R_{p}-R_{b}\right\|  |  
| --- |  
where:
  * •
R_{b}=\text{corr}(D_{b}) is the correlation matrix of the baseline dataset,
  * •
R_{p}=\text{corr}(D_{p}) is the correlation matrix of the perturbed dataset,
  * •
\left\|.\right\| is the default matrix 2-norm.


##  Appendix 0.B Appendix: Uncertainty distribution
Figure 4: Uncertainty distribution, compared between original (default) and test datasets, for workflow runs with Qwen backend. The four individual points represent the uncertainty outcomes from the test scenarios in Table .
