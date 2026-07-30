arXiv is now an independent nonprofit! Learn more ×
License: arXiv.org perpetual non-exclusive license 
arXiv:2607.25369v1 [cs.AI] 28 Jul 2026
# ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning
Jiaqi Zhang  The University of QueenslandBrisbaneAustralia Tong Chen  The University of QueenslandBrisbaneAustralia Junliang Yu  Griffith UniversityGold CoastAustralia Quoc Viet Hung Nguyen  Griffith UniversityGold CoastAustralia and  Hongzhi Yin  The University of QueenslandBrisbaneAustralia
(2018)
###### Abstract.
Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users. However, unlike natural-world tasks that assume well-defined instructions, human-centered scenarios are characterized by ambiguous requests that lead to large, open-ended solution spaces. Decoding users’ personalized preferences is therefore essential for narrowing the candidate solution space. This introduces a new challenge, personalized agentic reasoning, which requires agents to transform ambiguous user requests into concrete needs to deliver personalized services. In this paper, we present ODYSSE, a Reinforced Fine-Tuning (RFT) framework for personalized agentic reasoning. At its core, ODYSSE proposes Episode-wise GRPO (ESPO), a novel extension of Group Relative Policy Optimization (GRPO) designed to address long action horizons and strong cross-step dependencies in personalized agentic reasoning. Rather than optimizing individual steps independently, ESPO introduces an episode-level reward mechanism together with episodic advantage estimation, enabling upstream evidence to effectively guide downstream personalized decisions and allowing agents to progressively resolve ambiguous user requests across multiple interaction steps. We further propose an episodic batch sampler that groups actions from the same episode into unified training batches, facilitating coherent optimization under ESPO. We evaluate ODYSSE on realistic long-horizon personalized GUI reasoning tasks. Experimental results demonstrate that ODYSSE consistently outperforms both specialist and general-purpose LVLMs, highlighting its effectiveness for personalized agentic reasoning.
††copyright: acmlicensed††doi: XXXXXXX.XXXXXXX††conference: Make sure to enter the correct conference title from your rights confirmation email; June 03–05, 2018; Woodstock, NY††isbn: 978-1-4503-XXXX-X/2018/06
##  1. Introduction
Agentic systems based on Large Vision-Language Models (LVLMs) have recently demonstrated strong capabilities in multimodal understanding, instruction following, and complex reasoning, making them increasingly promising for real-world decision-making tasks (Wei et al., 2026; Li et al., 2024, 2026). Powered by representative reasoning backbones such as GPT-o series (Achiam et al., 2023), Google Gemini (Comanici et al., 2025), and DeepSeek-R1 , agentic systems are being deployed beyond simplified experimental environments into more realistic, adaptive, and human-centered service scenarios. Such real-world applications span diverse domains, including digital personal assistants (Zhang et al., 2026; Wang et al., 2026a, c), web agents (Wu et al., 2026; He et al., 2024; Chae et al., 2025), household service robots (Szot et al., 2021; Puig et al., 2024; Yenamandra et al., 2023), etc.
Across these scenarios, the role of agentic systems shifts from executing predefined instructions to inferring personalized goals for a particular user. In many real-world services, users do not approach an agent with a fully determined task plan. Instead, they seek assistance to clarify available options, identify relevant trade-offs, and settle on their preferences. This uncertainty often leads to an initial ambiguous request. Decoding such requests places new demands on real-world agent design. We refer to this capability as personalized agentic reasoning, where agents transform an ambiguous user request into concrete personalized needs by narrowing the candidate solution space with user feedback.
However, existing agent designs are not aligned with such personalized requirements. Most agents are designed to follow either clear instructions grounded in natural-world observations (Luo et al., 2025; Huang et al., 2024), or user requests pre-specified as direct commands (Zhang et al., 2026; Zhao et al., 2025). This formulation works when the user’s goal is explicit, but becomes insufficient when agents must handle ambiguous requests. For example, if a user asks to locate “Hilton New York Midtown at 1335 Avenue of the Americas”, any existing GUI agent can do so by directly typing keywords and returning the unique result. Yet intuitively, such a request is far from how real users behave. A real request would simply be “I am going to New York, any hotels?” Such an ambiguous request leaves an open-ended solution space, where the appropriate response varies with different users’ personalized preferences. As a result, existing agents lack effective mechanisms to perceive the personalized factor in ambiguous requests.
Another limitation arises from the optimization paradigm. Real-world reasoning rarely depends on a single observation or single-turn question answering . Instead, it requires agents to integrate signals across long-horizon interactions, where personalized needs often unfold through longer interaction steps and stronger cross-step dependencies (Zhou et al., 2024; Zhang et al., 2024). However, existing agents are not optimized towards such long-horizon reasoning. Firstly, many agents rely on outcome-based supervision, often using external functional rewards (Dong et al., 2026; Zhou et al., 2025; Da et al., 2025). This leaves optimization dominated by final-answer correctness, while the intermediate steps are underconstrained (Lightman et al., 2024; Setlur et al., 2025). Agents may forgo crucial intermediates or exploit shortcuts. Second, many agents adopt step-wise optimization, which assumes that each interaction step can be optimized independently (Deng et al., 2024; Chen et al., 2023; Sinha et al., 2026). This fragments cross-step dependencies, leaving agents struggle to connect upstream evidence with downstream personalized decisions (Wang et al., 2026d; Kim et al., 2025; Sinha et al., 2026). Overall, existing agents are ill-suited for coherent long-horizon reasoning.
In light of the deficiencies of existing solutions to personalized agentic reasoning, we present ODYSSE, which systematically reasons its way out of an initially brief and ambiguous user input to perform personalized actions. To bypass the coarse feedback signals in existing solutions, instead of assigning supervision only to final outcomes or isolated actions, we propose episode-wise relative policy optimization (ESPO), a novel RFT framework that allows ODYSSE to identify which exact steps are driving performance or causing error when eliciting personalized needs. Specifically, after warm-up training with SFT, ESPO organizes an episode-aware reward mechanism in three components. First, it introduces stage-specific verifiable rewards for individual action steps. These step-wise rewards provide reliable feedback for heterogeneous stages such as GUI execution, intent prediction, and personalized decision-making. Second, ESPO constructs a Chain-of-User-Thought (COUT) reward from two complementary perspectives on how the user’s ambiguous request is decoded: Intent Confidence evaluates the confidence in the user intent inferred from preceding GUI actions, while Intent Contribution evaluates the contribution of the inferred intent to the final personalized decision. Built upon this bidirectional dependency, the COUT reward enables traceable decoding of ambiguous user requests. Third, an episodic advantage estimation mechanism broadcasts each episode’s COUT advantage to its action steps and combines it with their step-wise advantages to form episode-wise advantages, thereby enabling cross-step intent alignment. Finally, the resulting episode-wise advantages are then used to update the policy. To support coherent ESPO, we further design an episodic batch sampler. During training, the sampler treats each episode as the minimum indivisible sampling unit and groups samples from the same episode into a unified training batch. This ensures that dependent action steps within the same episode are optimized together, allowing ESPO to compute COUT rewards and perform policy updates over the full interaction trajectory rather than isolated action steps.
Our contributions are summarized as follows:
  * •
We formulate personalized agentic reasoning, where agent systems must handle ambiguous requests from real-world users. We identify key limitations of existing agents, namely limited ability to decode ambiguous requests and fragmented outcome-/step-wise optimization, and analyze how they become particularly severe in personalized scenarios.
  * •
We put forward ODYSSE, a dedicated framework for personalized agentic reasoning. In ODYSSE, we propose a novel RFT method, namely ESPO that offers fine-grained, per-step feedback. With ESPO, ODYSSE decodes ambiguous user requests by executing basic GUI actions, inferring GUI-related intent, and generating personalized recommendations.
  * •
Experiments show that ODYSSE achieves superior performance compared with both specialist GUI agents and general-purpose LVLMs, demonstrating the effectiveness and broader potential of episode-wise optimization for long-horizon personalized agentic reasoning.


##  2. Related Work
###  2.1. Real-World Agentic Reasoning
Real-world agentic reasoning focuses on interacting with practical environments such as GUIs, Web Agents, and Coding Agents, rather than static image-text or video-text reasoning tasks (Wei et al., 2026; Li et al., 2024, 2026; Luo et al., 2025; Zhang et al., 2025a, b; Yang et al., 2024). SeeClick enables LVLM agents to identify and execute interface actions directly from screenshots and textual instructions, demonstrating the potential of multimodal LVLMs for real-world GUI control across various environments. GUI-R1 enables GUI agents with rule-based RL, improving long-horizon interaction planning and action reasoning in dynamic interface environments. SmartAgent presents a personal assistant agent that integrates GUI interaction and personalized recommendations, highlighting the importance of long-horizon personalization decision-making in real-world agentic systems.
ESPO organizes isolated action steps into episodes. The stacked and blocks represent rollout-level quantities.
Recent OpenClaw introduces an open-source agent framework that can serve as a virtual digital assistant on personal hardware. The variants of OpenClaw further extend agentic systems toward real-time and personal adaptation in deployed environments (Wang et al., 2026a; Ren et al., 2026; Zhu et al., 2026). For example, OpenClaw-RL proposes a real-time personal agent framework built on a server-client architecture, enabling online agent learning by leveraging user re-queries, corrections, and explicit feedback. Overall, existing real-world agents mainly extend agent-environment interaction, assuming simplified user instructions can be directly executed. Our work instead studies personalized agentic reasoning, where agents decode personalized needs from ambiguous requests through long-horizon interactions and generate personalized item recommendations.
###  2.2. Agentic Systems with Reinforcement Learning
Agentic systems learn to accomplish complex goals through autonomous environment perception and interaction. Unlike monolithic LLMs that typically perform CoT reasoning within a single forward generation process, agentic systems interact with evolving environments through iterative multi-turn actions, where each step corresponds to an environment-aware decision conditioned on updated observations (Yao et al., 2022; Schick et al., 2023; Wang et al., 2024). Early agentic systems mainly relied on prompting engineering and SFT training, often suffer from compounding error accumulation, limited generalization, and weak long-term planning capabilities (Chen et al., 2023; Yao et al., 2022; Schick et al., 2023). Recent works (Lambert et al., 2024; Luo et al., 2025; Singh et al., 2025) introduce Reinforcement Learning with Verifiable Rewards (RLVR). The RLVR setting improves interactive reasoning capabilities with deterministic reward functions, which are typically derived from executable environment feedback, such as task completion, correctness checking, or functional success signals. Existing methods have demonstrated that adapting RLVR to agentic systems through either step-wise rewards that assign verifiable supervision signals to intermediate interaction steps (Yang et al., 2024; Wang et al., 2026e), or outcome-oriented rewards that only evaluate final task success (Wang et al., 2026a; Lambert et al., 2024), can significantly improve agent reasoning and interaction capabilities in complex tasks. However, outcome-oriented rewards only supervise final success, while step-wise rewards optimize actions separately. Our work instead augments step-wise rewards with episodic supervision to capture cross-step dependencies in personalized agentic reasoning.
##  3. Problem Definition
In this work, we formulate Personalized Agentic Reasoning in the context of digital personal assistants (e.g., flight booking and product purchasing assistants). In this setting, an ambiguous request is resolved through agent-GUI (Graphical User Interface) interaction across heterogeneous action stages, including GUI execution, GUI-related user intent prediction, and personalized recommendation decision. The agent learns from user demonstrations of this process, in which humans interact with an environment by operating the GUI to identify target items \tau^{\ast} from its open-ended item pool 𝒯\mathcal{T}. Such a demonstration is represented as an interaction episode =e_{i}=\\{a_{1},a_{2},\ldots,a_{N}\\}, where each action step is generated based on the current GUI observation O_{j}\in\mathcal{O} and interaction history H_{j}\in\mathcal{H}. These demonstrations teach the agent how interaction evidence guides personalized decisions. Given a new ambiguous task, the agent is expected to: (1) generate appropriate actions a_{j}\in e_{i} to interact with the environment, and (2) search, retrieve, and recommend candidate items \tau\in\mathcal{T} that best satisfy the user’s intent.
##  4. Methodology
###  4.1. Preliminaries
Let \mathcal{D}=\\{e_{1},e_{2},\ldots,e_{M}\\} denote the full episode dataset. Given an action step a_{j}\in e_{i}, the corresponding training sample is denoted as (q,O_{j},H_{j},y^{\ast}_{j}), with y^{\ast}_{j}\in Y representing the corresponding ground-truth action. Existing works optimize the agent either through SFT, which maximizes the likelihood of the ground-truth action:  
| =−𝔼​[​],\mathcal{L}_{\text{SFT}}=-\mathbb{E}_{(q,O_{j},H_{j},y_{j})\sim\mathcal{D}}\left[\log\pi_{\theta}(y^{\ast}_{j}\mid q,O_{j},H_{j})\right],  |  
| --- |  
or through reinforcement learning, typically instantiated with GRPO . For each sample, GRPO draws a group of candidate actions \\{y_{1},y_{2},\dots,y_{G}\\} from the old policy \pi_{\theta_{\mathrm{old}}} and estimates their advantages using relative rewards. The GRPO objective is formulated as:  
| \displaystyle\mathcal{J}_{\text{GRPO}}(\theta)=  | 𝔼,[{\displaystyle\mathbb{E}_{x\sim D,\\{y_{i}\\}_{i=1}^{G}\sim\pi_{\theta_{\text{old}}}}\Bigg[\frac{1}{G}\sum_{i=1}^{G}\frac{1}{|y_{i}|}\sum_{t=1}^{|y_{i}|}\Bigg\\{  |  
| --- | --- |  
| min(​​,\displaystyle\min\Bigg(\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})}A_{i,t},  |  
| clip(​​,1−ϵ,1+ϵ))\displaystyle\text{clip}\Bigg(\frac{\pi_{\theta}(y_{i,t}|x,y_{i,<t})}{\pi_{\theta_{\text{old}}}(y_{i,t}|x,y_{i,<t})},1-\epsilon,1+\epsilon\Bigg)A_{i,t}\Bigg)  |  
| −β}],\displaystyle-\beta\mathbb{D}_{\mathrm{KL}}\left[\pi_{\theta}\|\pi_{\mathrm{ref}}\right]\Bigg\\}\Bigg],  |  
where balances reward maximization and KL regularization. The advantage term \hat{A}_{j} is derived from the step-wise rewards of the group of responses \\{R_{1},R_{2},\dots,R_{l}\\} and calculated as:  
| =−mean​std​.A_{i}=\frac{r_{i}-\mathrm{mean}(\\{r_{1},r_{2},\ldots,r_{G}\\})}{\mathrm{std}(\\{r_{1},r_{2},\ldots,r_{G}\\})}.  |  
| --- |  
###  4.2. Episode-wise Policy Optimization (ESPO)
Existing agents are not explicitly optimized for such personalized reasoning processes, and the step-wise paradigm further makes it difficult to accumulate interaction evidence across the full episode and use it to guide downstream personalized decisions. To bridge this gap, we propose Episode-wise Policy Optimization (ESPO), as illustrated in Figure . Specifically, ESPO preserves GRPO’s group-relative update and augments step-wise supervision with episodic signals that explicitly model the dependencies among different action steps. The overall training procedure is summarized in Algorithm , and comprises of three main phases: ESPO first derives stage-specific verifiable rewards from heterogeneous action types (lines 4-9), then aggregates them into a Chain-of-User-Thought (COUT) reward to decode ambiguous user requests (lines 10-12), and finally broadcasts the resulting episodic supervision through an episode-wise advantage estimation mechanism (lines 13-17). In what follows, we unfold the design details of ESPO.
####  4.2.1. Verifiable Rewards in Episodic Action Space
Different steps within an episode serve distinct roles in personalized reasoning. We therefore categorize action steps in each episode into three stages, including GUI task execution, GUI-related user intent prediction, and personalized decision. Each stage is associated with a specific action space and a corresponding verifiable reward. This enables fine-grained supervision beyond final outcomes.
For all action steps a_{j}\in e_{i}, we define a format reward RformatR_{\mathrm{format}} to verify whether the generated response follows the required format:  
| Rformat={if the format is correct,otherwise.R_{\mathrm{{format}}}=\left\\{\begin{array}[]{ll}0.5&\text{if the format is correct},\\\ 0.0&\text{otherwise}.\end{array}\right.  |  
| --- |  
For GUI task execution steps, we define RGUI​-​accuracyR_{\mathrm{GUI\text{-}accuracy}} in Eq. () as a fine-grained reward over the <action type> and <action value> parsed from the generated response.  
| RGUI​-​accuracy={if both are correct,if only <action type> is correct,if only <action value> is correct,otherwise.R_{\mathrm{GUI\text{-}accuracy}}=\left\\{\begin{array}[]{ll}\;\;0.5&\text{if both are correct},\\\ \;\;0.2&\text{if only {<action type>} is correct},\\\ -0.2&\text{if only {<action value>} is correct},\\\ -0.5&\text{otherwise}.\end{array}\right.  |  
| --- |  
Episode-wise GRPO (ESPO)
Input: Training dataset 𝒟\mathcal{D} with episode ids. 
Parameter: Policy \pi_{\theta}, training iterations , KL coefficient 
Output: Optimized policy \pi_{\theta}
fordo
Sample a mini-batch \mathcal{B}\in\mathcal{D} with complete episodes. 
for all episode e_{i}\in\mathcal{B}do
for all step do
Compute format reward RformatR_{\mathrm{format}}
Compute accuracy reward RaccuracyR_{\mathrm{accuracy}}
Compute step-wise reward Rstep​-​wiseR_{\mathrm{step\text{-}wise}}^{(j)} by Eq. (); 
Compute intent matching score I​n​t​e​n​Intent_{\mathrm{acc}} by Eq. (); 
Aggregate GUI action gate  by Eq. (); 
Aggregate decision gate  by Eq. (); 
Compute R_{\mathrm{COUT}} by Eq. (); 
for all step do
Compute step-wise advantage Astep​-​wise​A_{\mathrm{step\text{-}wise}}(a_{j}) by Eq. (); 
Broadcast R_{\mathrm{COUT}} to step  to obtain A_{\mathrm{COUT}}(e_{i}) by Eq. (); 
Compute episode-wise advantages Aepisode​-​wise​{A_{\mathrm{episode\text{-}wise}}^{(i,j)}}(e_{i}) by Eq. (); 
Update  using GRPO with KL regularization; 
return optimized policy \pi_{\theta}
For GUI-related user intent prediction steps, we define an intent matching reward I​n​t​e​n​Intent_{\mathrm{acc}} in Eq. () to measure whether the predicted intent matches the user’s ground-truth GUI intent y^{\ast}_{j}:  
| I​n​t​e​n​={if <action type> is correct andCosine​(<action value>,)≥τ,otherwise.Intent_{\mathrm{acc}}=\left\\{\begin{array}[]{ll}0.5&\begin{array}[]{@{}l@{}}\text{if {<action type>} is correct and}\\\ \mathrm{Cosine}(\texttt{<action value>},y^{\ast}_{j})\geq\tau,\end{array}\\\ 0.0&\text{otherwise}.\end{array}\right.  |  
| --- |  
For personalized decision steps, we define Rdec​-​accuracyR_{\mathrm{dec\text{-}accuracy}} in Eq. () to evaluate whether each item is correctly recommended. This stage imposes a stricter criterion, requiring both <action type> and <action value> to be correct for a positive reward:  
| Rdec​-​accuracy={if both <action type> and<action value> are correct,otherwise.R_{\mathrm{dec\text{-}accuracy}}=\left\\{\begin{array}[]{ll}\;\;0.5&\begin{array}[]{@{}l@{}}\text{if both {<action type>} and}\\\ \text{{<action value>} are correct}\end{array}\;,\\\ -0.5&\text{otherwise}.\end{array}\right.  |  
| --- |  
####  4.2.2. Chain-of-User-Thought (COUT) Reward
Based on the stage-specific verifiable rewards, ESPO constructs a Chain-of-User-Thought reward R_{\mathrm{COUT}} to evaluate whether an episode of actions coherently decodes an ambiguous request into a personalized need. Accordingly, we aggregate stage-level evidence into two gates to model cross-step dependencies. Specifically, the GUI-action gate summarizes the reliability of preceding GUI task execution actions for intent prediction, while the decision gate summarizes the extent to which the inferred intent contributes to the final personalized decision:  
| =σ​(k⋅RGUI​-​accuracyRGUI​-​accuracymax),\phi_{i}=\sigma\left(k\cdot\frac{\sum_{j}R_{\mathrm{GUI\text{-}accuracy}}^{(j)}}{R_{\mathrm{GUI\text{-}accuracy}}^{\max}}\right),  |  
| --- |  
| =σ​(k⋅Rdec​-​accuracyRdec​-​accuracymax),\psi_{i}=\sigma\left(k\cdot\frac{\sum_{j}R_{\mathrm{dec\text{-}accuracy}}^{(j)}}{R_{\mathrm{dec\text{-}accuracy}}^{\max}}\right),  |  
| --- |  
where is the temperature coefficient. With these gates, R_{\mathrm{COUT}} is formulated as two complementary components:  
| =​n​t​e​n​⏟Intent Confidence+​n​t​e​n​⏟Intent Contribution,R_{\mathrm{COUT}}^{(i)}=\underbrace{\phi_{i}\cdot Intent_{\mathrm{acc}}}_{\text{Intent Confidence}}+\underbrace{\psi_{i}\cdot Intent_{\mathrm{acc}}}_{\text{Intent Contribution}},  |  
| --- |  
where the two terms respectively correspond to Intent Confidence and Intent Contribution, as detailed below.
Intent Confidence. The term ​n​t​e​n​\phi\cdot Intent_{\mathrm{acc}} measures whether intent prediction is supported by reliable GUI task execution. Specifically, accurate intent prediction should receive a high reward only when the preceding GUI actions are trustworthy, as quantified by the GUI-action gate in Eq. ().
Intent Contribution. The term ​n​t​e​n​\psi\cdot Intent_{\mathrm{acc}} measures whether the predicted intent contributes to the final personalized decision. A correct intent prediction should receive a higher reward only when it further leads to a valid personalized decision, as quantified by the decision gate in Eq. ().
Together, these two components connect aggregated upstream GUI evidence with downstream personalized decision-making, encouraging the model to reason over the whole episode rather than optimizing each action independently.
####  4.2.3. Episodic Advantage Estimation
ESPO realizes episodic advantage estimation to assign the personalized credit encoded in R_{\mathrm{COUT}} to each step. Specifically, for each step a_{j}\in e_{i}, we preserve the original GRPO-style relative optimization by maintaining a stage-specific step-wise rewards and step-wise advantage:  
|  Rstep​-​wise={+RGUI​-​accuracy,if ​​ is GUI task step,+I​n​t​e​n​,if ​​ is user intent step,+Rdec​-​accuracy,if ​​ is personalized step,R_{\mathrm{step\text{-}wise}}^{(j)}=\left\\{\begin{array}[]{l}R_{\mathrm{format}}^{(j)}+R_{\mathrm{GUI\text{-}accuracy}}^{(j)},\,\text{if }a_{j}\text{ is GUI task step},\\\\[4.2679pt] R_{\mathrm{format}}^{(j)}+Intent_{\mathrm{acc}},\quad\;\text{if }a_{j}\text{ is user intent step},\\\\[4.2679pt] R_{\mathrm{format}}^{(j)}+R_{\mathrm{dec\text{-}accuracy}}^{(j)},\;\text{if }a_{j}\text{ is personalized step},\end{array}\right.  |  
| --- |  
| Astep​-​wise​=Rstep​-​wise−mean​({Rstep​-​wise}G)std​({Rstep​-​wise}G).A_{\mathrm{step\text{-}wise}}(a_{j,g})=\frac{R_{\mathrm{step\text{-}wise}}^{(j,g)}-\mathrm{mean}\left(\\{R_{\mathrm{step\text{-}wise}}^{(j,g)}\\}_{g=1}^{G}\right)}{\mathrm{std}\left(\\{R_{\mathrm{step\text{-}wise}}^{(j,g)}\\}_{g=1}^{G}\right)}.  |  
| --- |  
Then, we define the COUT advantage by broadcasting the R_{\mathrm{COUT}}^{(i)} to every rollout of each step :  
| =Broadcast⁡.A_{\mathrm{COUT}}(e_{i})=\operatorname{Broadcast}_{a_{j}\in e_{i},\;g=1,\ldots,G}\left(R_{\mathrm{COUT}}^{(i)}\right).  |  
| --- |  
The final episodic advantage for the -th rollout of step is then merged as:  
| Aepisode​-​wise=Astep​-​wise​+,,A_{\mathrm{episode\text{-}wise}}^{(i,j,g)}=A_{\mathrm{step\text{-}wise}}(a_{j,g})+w\cdot A_{\mathrm{COUT}}(e_{i}),\quad g=1,\ldots,G,  |  
| --- |  
where controls the influence of the COUT advantage. In this estimation, Astep​-​wise​A_{\mathrm{step\text{-}wise}}(a_{j,g}) provides local step-wise credit, while A_{\mathrm{COUT}}(e_{i}) broadcasts episode-level personalized signals to all steps, forming a personalized GRPO-style advantage.
####  4.2.4. ESPO Objective Function
After estimating the episodic advantage, ESPO updates the policy on episode-preserving mini-batches, where each step a_{j}\in e_{i} is associated with rollouts {y_{j,g}}_{g=1}^{G}. The overall objective of ESPO is formulated as:  
| \displaystyle\mathcal{J}_{\mathrm{ESPO}}(\theta)=  | 𝔼,∼[{\displaystyle\;\mathbb{E}_{\begin{subarray}{c}e_{i}\sim\mathcal{D},\;\\{y_{j,g}\\}_{g=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}\end{subarray}}\Bigg[\frac{1}{|e_{i}|}\sum_{a_{j}\in e_{i}}\frac{1}{G}\sum_{g=1}^{G}\frac{1}{|y_{j,g}|}\sum_{t=1}^{|y_{j,g}|}\Bigg\\{  |  
| --- | --- |  
| min(Aepisode​-​wise,\displaystyle\qquad\min\Bigg(\rho_{j,g,t}(\theta)A_{\mathrm{episode\text{-}wise}}^{(i,j,g)},  |  
| clip(,1−ϵ,1+ϵ)Aepisode​-​wise)\displaystyle\qquad\mathrm{clip}\Big(\rho_{j,g,t}(\theta),1-\epsilon,1+\epsilon\Big)A_{\mathrm{episode\text{-}wise}}^{(i,j,g)}\Bigg)  |  
| −β}],\displaystyle\qquad-\beta\,\mathbb{D}_{\mathrm{KL}}\left[\pi_{\theta}\|\pi_{\mathrm{ref}}\right]\Bigg\\}\Bigg],  |  
where \rho_{j,i,t}(\theta) is the importance ratio:  
| =​(∣)​(∣),\displaystyle\rho_{j,g,t}(\theta)=\frac{\pi_{\theta}\left(y_{j,g,t}\mid x_{j},y_{j,g,<t}\right)}{\pi_{\theta_{\mathrm{old}}}\left(y_{j,g,t}\mid x_{j},y_{j,g,<t}\right)},  |  
| --- |  
and, is the clipping parameter to constrain policy updates,and is the coefficient for the KL-divergence penalty term \mathbb{D}_{\mathrm{KL}}.
Compared with standard GRPO-style optimization over isolated action steps, ESPO performs episode-preserving optimization with personalized episodic advantage estimation. The former keeps steps from the same trajectory intact during policy updates, while the latter broadcasts episode-level personalized signals into the advantage. Therefore, ESPO encourages actions that are not only locally executable at the current GUI state but also beneficial to the overall personalized reasoning trajectory.
###  4.3. Episode-wise Training Strategy
####  4.3.1. RFT Training
ODYSSE follows a two-stage reinforced fine-tuning (RFT) pipeline. In the first stage, we perform SFT on expert action trajectories to cold-start the policy. This stage teaches the model to generate structured GUI actions conditioned on the user query, current observation, and execution history. The SFT objective follows Eq. (), where each sample is an action-level tuple (q,O_{j},H_{j},y_{j}^{\ast}) extracted from an episode.
In the second stage, we initialize the policy from the SFT checkpoint and optimize it with our ESPO. For each sampled episode, the model predicts actions conditioned on the current observation and action history, receives stage-specific verifiable rewards, and then obtains the episode-wise reward by Eq. (). These rewards are used to compute group-relative advantages and update the policy with the GRPO objective in Eq. (). Compared with directly applying GRPO to isolated steps, this RFT design preserves the stability of SFT while using episode-level feedback to improve long-horizon intent inference and personalized decision making.
####  4.3.2. Episodic Batch Sampler
Standard batch construction (Shao et al., 2024; Schulman et al., 2017; Engstrom et al., 2020) in GRPO-based training randomly shuffles individual action steps, which breaks the temporal structure required by episode-wise reward computation. To support ESPO, we design an in-batch episode sampler that treats each complete episode as the minimum sampling unit. Specifically, the sampler assigns each step an episode identifier indicating the episode to which it belongs. Based on these identifiers, the sampler first groups all steps belonging to the same episode, preserves their original temporal order, and then shuffles episodes rather than individual steps.
The sampler subsequently constructs a training batch by sampling one or more complete episodes. Formally, the resulting batch can be represented as:  
| ,,\mathcal{B}=\bigcup_{k=1}^{K}e_{k},\quad e_{i}\cap e_{j}=\varnothing,\quad i\neq j,  |  
| --- |  
where each sampled episode is represented as  
| =,e_{k}=\\{a_{1},a_{2},\ldots,a_{N_{k}}\\},  |  
| --- |  
and each action step belongs to exactly one episode, i.e.,  
| a_{j}\notin e_{m}\cap e_{n},\qquad m\neq n.  |  
| --- |  
where each episode remains intact throughout the sampling process. This preserves the integrity of each episode while preventing interference across different episodes, thereby enabling coherent episode-wise reward computation and credit assignment.
Table 1. Action spaces and output formats in SmartSpot.  
|   |  
| --- |  
|  ¡action type¿: GUI operation (e.g., {click}{type}); ¡action value¿: (e.g., “click point ¡0.23, 0.74¿, type ’Next Page”’)  |  
|  ¡action type¿: {pool_found}; ¡action value¿: Natural-language output (e.g., “The user needs an economy class flight from London to New York”)  |  
|  ¡action type¿: {recommendation}; ¡action value¿: {Yes/No}  |  
##  5. Experiments
In this section, we progressively evaluate ODYSSE by answering the following research questions:
  * •
RQ1:Is RFT superior to SFT for personalized reasoning?
  * •
RQ2:If so, can ODYSSE outperform existing LVLMs?
  * •
RQ3:Is ESPO responsible for ODYSSE’s gains?
  * •
RQ4: What drives the effectiveness of ESPO?


Furthermore, we investigate the sensitivity of ODYSSE to different hyperparameter settings. We also provide a case study in Appendix .
###  5.1. Experimental Setup
####  5.1.1. Datasets.
We conduct experiments on SmartSpot , a benchmark for long-horizon personalized reasoning. SmartSpot is organized into multiple episodes, each associated with an ambiguous user request expressing a real-world need, such as I am going to New York, any hotels? or find me some choices about flights to Sydney.
Comparison with Generalist LVLMs and Specialist Agents on SmartSpot.  
 |  
|  |  
|   |  
 |  
 |  
 |  
|  llava-v1.6-mistral-7b  |  
|  llava-v1.6-vicuna-7b  |  
 |  
 |  
 |  
|  Specialist Agents  |  
 |  
 |  
|   |   |  
An episode consists of a sequence of action steps, resulting in 1,713 steps across 102 episodes (an average of 17 steps per episode). Each episode spans three stages: Search steps for navigating and retrieving an item pool, an Item Pool step corresponding to a GUI page of the retrieved item list, and Recommend steps for deciding whether each candidate should be recommended. Across all steps, the agent receives an ambiguous user request, a GUI screenshot, and previous actions as input. The stage-specific action formats are summarized in Table . We split the dataset by episode with an 8:1:1 ratio. A representative data case is provided in Appendix .
####  5.1.2. Evaluation Settings.
Following SmartAgent , we evaluate model performance with two groups of metrics that progressively assess an agent’s capabilities from low-level GUI interaction to high-level personalized reasoning. Element Accuracy (EleAcc), Operation F1 Score (Op F1), and Step Success Rate (Step SR) measure GUI actions from GUI element grounding accuracy, overall action matching, and step success, respectively. Recommendation Accuracy (RecAcc) evaluates whether the agent makes the correct final recommendation decision.
Our RFT-based ODYSSE vs. its SFT variants.
####  5.1.3. Implementation Details.
We use Qwen2.5-VL-3B as our base model. We first perform one epoch of SFT, followed by six epochs of ESPO implemented with EasyR1 . We enable in-batch sampling with one episode per batch and apply both the temperature in Eqs. () and () and advantage weight in Eq. () to 1.0. All experiments are conducted on a single NVIDIA H100-80G GPU.
###  5.2. Preliminary Investigation (RQ1)
We first study whether RFT offers a better training foundation than SFT for personalized agentic reasoning. SFT is widely used for learning expert behaviors, but its local imitation objective provides limited supervision for delayed feedback and episode-level outcomes. Given the recent success of RFT in reasoning and agentic tasks, we evaluate whether ODYSSE benefits from reinforcement feedback beyond purely SFT.
We examine this question with two SFT-based variants. ODYSSE (Only SFT Cold-start) keeps only the SFT cold-start, isolating whether RFT provides learning signals beyond SFT imitation. ODYSSE (All SFT) extends the SFT stage to the same iterations as ODYSSE but without any RL stage, testing whether RFT is more effective than simply scaling the SFT counterpart. Together, these comparisons assess both the necessity of RL and the paradigm-level advantage of RFT over SFT.
As shown in Figure , the most pronounced gap appears between ODYSSE and ODYSSE (Only SFT Cold-start), which performs the worst among all variants, with both EleAcc and RecAcc being zero. This indicates that the SFT cold-start can help the model acquire basic response formats, but it still struggles to ground GUI actions to the correct elements, let alone make personalized final recommendations Compared with ODYSSE (Only SFT Cold-start), ODYSSE (All SFT) obtains further improvements, suggesting that additional SFT iterations can strengthen low-level GUI interaction ability. However, both SFT variants still fail to make any breakthrough on RecAcc. This indicates that high-level personalized perceiving remains beyond the capability of the SFT paradigm, even with additional SFT training iterations. In contrast, ODYSSE achieves the best performance across all metrics. The advantage is especially clear on RecAcc, where the RFT stage enables the policy to acquire personalized decision-making that cannot be obtained from the SFT paradigm. These results support our choice of building ODYSSE upon the RFT paradigm and motivate the following experiments to further examine how episode-wise optimization benefits personalized agentic reasoning.
###  5.3. Overall Performance (RQ2)
After establishing the advantage of RFT over pure SFT, we next benchmark ODYSSE on the SmartSpot dataset against existing LVLMs to evaluate its overall capability. To make this comparison comprehensive, we consider two complementary groups of baselines. Generalist LVLMs examine whether broad multimodal understanding alone is sufficient for personalized factor perception without task-specific adaptation. Specialist Agentsexamine whether optimization for specific environments alone is sufficient for capturing personalized factors. Together, these two groups test whether personalized agentic reasoning can be achieved by either general-purpose multimodal capability or environment-specific agents, thereby highlighting the effectiveness of ODYSSE.
Our ESPO vs. GRPO.
Specifically, the Generalist LVLMs group includes:
  * •
Qwen3-VL series , the latest Qwen model family, where we use 2B, 4B, and 8B variants to cover different scales.
  * •
LLaVA series , where we use three 7B variants with different language backbone.
  * •
InternVL3 series , where we evaluate its 1B, 2B, and 8B variants.


The Specialist Agents group includes:
  * •
SeeClick , a representative GUI-specialized visual agent designed around SFT-based GUI. We reproduce it under the same fine-tuning epoch setting as ours.
  * •
SmartAgent , a personalized agent that achieves state-of-the-art performance on the SmartSpot benchmark under the SFT paradigm.
  * •
GUI-R1 , a recent leading GUI agent and the first RFT-based framework for GUI action prediction. We fine-tune its 3B version to maintain a comparable scale with ours.


As shown in Table , ODYSSE achieves the best performance across all metrics. In particular, it improves the strongest baseline over on EleAcc and on Step SR, showing that ODYSSE can perform more accurate GUI element grounding and complete more successful steps. Built upon these stronger low-level interaction abilities, ODYSSE further achieves a RecAcc of 28.57\%, indicating its advantage in transferring GUI interaction evidence into final personalized recommendations.
Ablation study for ODYSSE before (left) and after (right) our ESPO optimization. The y-axis represents the final reward score.
General-purpose LVLMs show clear limitations. Although some of them obtain non-zero RecAcc, their GUI interaction performance remains unconvincing. For example, the LLaVA variants achieve relatively competitive RecAcc, but their EleAcc is consistently zero, suggesting that their final decisions are weakly grounded in accurate GUI element actions. Similarly, Qwen3-VL-8B and InternVL3-8B show stronger performance than their smaller variants, but they still lag behind ODYSSE on both EleAcc and Step SR.
Specialist agents perform better but remain substantially behind ODYSSE. The two SFT-based specialists, SeeClick and SmartAgent, show comparable performance on GUI action metrics, but both remain limited on RecAcc. This suggests that SFT-based adaptation for GUI interaction can improve certain low-level abilities, but it is still insufficient for personalized decision-making. The RFT-based GUI-R1 ranks second among nearly all baselines. In contrast, equipped with ESPO, ODYSSE better guides the policy to decode personalized factors from interaction evidence, leading to the best performance across all metrics.
###  5.4. In-Depth Analysis of ODYSSE (RQ3)
Following the comparison with existing baselines, we further examine whether ODYSSE’s gains are driven by its core optimization strategy, ESPO. To isolate the effect of this design, we compare two controlled variants under the same backbone model, SFT cold-start, and reward setting: one trained with vanilla GRPO and the other with ESPO.
As shown in Figure , replacing vanilla GRPO with ESPO brings consistent improvements across all metrics. These improvements indicate that episode-wise optimization benefits both low-level GUI interaction and high-level personalized decision-making. Specifically, the gains on EleAcc and Step SR suggest that ESPO helps the policy produce more reliable intermediate actions, while the improvement on RecAcc shows that these interaction gains are better translated into final personalized recommendations.
This comparison further explains why episode-wise optimization is necessary for long-horizon personalized agentic reasoning. Vanilla GRPO still optimizes actions in a more local manner, providing limited guidance on how each step contributes to the complete episode. In contrast, ESPO aligns intermediate GUI actions with episode-level outcomes, allowing the policy to better decode personalized interaction evidence across the trajectory.
Therefore, RQ3 further clarifies ESPO as the key source of ODYSSE’s advantage. Its improvement over vanilla GRPO confirms that episode-wise feedback is more effective for optimizing long-horizon personalized reasoning, which is consistent with the RFT advantage observed in RQ1 and further supports ODYSSE’s strong overall performance in RQ2.
###  5.5. Ablation Study (RQ4)
In this section, we conduct ablation studies to assess the contribution of each component and examine how ESPO reshapes their optimization dynamics. Specifically, we organize the analysis into two levels: a framework-level ablation that evaluates the necessity of the major training components, and an internal-level ablation that further examines how detailed reward design, Intent Confidence and Intent Contribution , inside R_{\mathrm{COUT}} contribute to ESPO.
Ablation study of Intent Contribution and Intent Confidence in R_{\mathrm{COUT}}. The y-axis presents the score relative to ODYSSE (%). Hyper-parameter sensitivity analysis of ODYSSE under different Epoch and settings.
####  5.5.1. Analysis of SFT Cold-start and R_{\mathrm{COUT}}
At the framework level, we investigate the effects of SFT cold-start and the proposed R_{\mathrm{COUT}} by constructing three variants: We construct three ablation variants, including No \bm{R}_{\bm{\mathrm{COUT}}}, No SFT Cold-start, and No All, and compare them against the complete ODYSSE framework. Figure presents their training dynamics by steps before and after applying ESPO. Several important observations can be drawn from the optimization dynamics:
  * •
First, the four ablation variants are roughly separated into two groups before applying ESPO, where the presence or absence of SFT cold-start forms the dominant performance gap. In contrast, after introducing ESPO, the reward trajectories of different ablation variants become clearly separated, indicating that episodic policy optimization substantially improves the optimization discriminability among different architectural and reward designs.
  * •
More importantly, without ESPO, the reward trajectories of complete ODYSSE and No \bm{R}_{\bm{\mathrm{COUT}}} remain largely intertwined, with no clear performance gap between them. With ESPO, however, the complete ODYSSE model becomes fully separated from No \bm{R}_{\bm{\mathrm{COUT}}} and achieves a significantly larger reward advantage. This demonstrates that broadcasting the episode-wise reward provides effective long-horizon supervisory signals beyond conventional step-wise ones.
  * •
Furthermore, under ESPO optimization, No SFT Cold-start noticeably surpasses No \bm{R}_{\bm{\mathrm{COUT}}}, despite the absence of SFT cold-start. This suggests that episode-wise supervision introduced by ESPO can provide stronger long-horizon optimization benefits than relying solely on step-wise rewards with SFT cold-start.
  * •
Finally, the No All variant consistently performs the worst after ESPO optimization. This indicates that the proposed components are not independently beneficial but instead work synergistically, jointly contributing to long-horizon personalized reasoning through complementary optimization effects.


####  5.5.2. Analysis of Intent Confidence and Intent Contribution
Since ESPO’s effectiveness mainly arises from R_{\mathrm{COUT}}, we further examine whether both components of R_{\mathrm{COUT}}, Intent Confidence and Intent Contribution, are necessary. Specifically, we construct two variants by separately removing the Intent Confidence term ​n​t​e​n​\phi\cdot Intent_{\mathrm{acc}} and the Intent Contribution term ​n​t​e​n​\psi\cdot Intent_{\mathrm{acc}}, respectively.
As shown in Figure , removing either term causes a cascading deterioration through the episode. Although the effect on EleAcc is relatively mild, the gap grows when moving to Op F1 and Step SR, ultimately causing at least a gap on RecAcc and even an collapse at epoch 3. This suggests that the bidirectional supervision slips toward a breakdown over the full episode. Consequently, the variants gradually lose control over early GUI actions and later recommendation actions, which tend to optimize toward their own local objectives rather than mutually constraining each other across the episode.
Together, these results show that Intent Confidence and Intent Contribution are both indispensable for preserving the cross-stage dependency between GUI interaction and final personalized recommendation in R_{\mathrm{COUT}}.
###  5.6. Hyperparameter Sensitivity Analysis
We further analyze the sensitivity of ODYSSE to two key hyperparameters: the training epoch and the temperature coefficient in R_{\mathrm{COUT}}. In ESPO, controls the sharpness of the sigmoid gates for GUI-stage and recommendation-stage rewards. A larger makes the gates more sensitive to accumulated rewards, thereby increasing the influence of R_{\mathrm{COUT}} on episode-wise optimization.
As shown in Figure , training ODYSSE for 6 epochs with yields leading results across all metrics. This indicates that a smoother gate provides a more stable R_{\mathrm{COUT}} for long-horizon optimization. Larger may make the ESPO process more sensitive to partial or negative steps. Some settings obtain isolated gains, such as higher EleAcc at epoch 3 with , but these improvements are limited to a single local metric and do not bring consistent benefits. Similarly, extending training from 6 to 9 epochs does not further improve overall performance and even degrades several settings, suggesting possible over-optimization toward specific reward signals.
##  6. Conclusion
In this paper, we propose ODYSSE, a novel RFT framework for personalized agentic reasoning. To address ambiguous user requests in real-world scenarios, ODYSSE learns to decode personalized needs across long-horizon interactions. ODYSSE introduces ESPO to move beyond outcome-/step-wise optimization by enabling episode-wise learning over coherent interaction trajectories. Extensive experiments show that ODYSSE outperforms both specialist and general-purpose LVLMs, underscoring the importance of episode-wise optimization for personalized agentic reasoning.
## References
  * J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat, et al. (2023) Gpt-4 technical report.  arXiv preprint arXiv:2303.08774. 
  * S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, et al. (2025) Qwen3-vl technical report.  arXiv preprint arXiv:2511.21631. 
  * H. Chae, N. Kim, K. Ong, M. Gwak, G. Song, J. Kim, S. Kim, D. Lee, and J. Yeo (2025) Web agents with world models: learning and leveraging environment dynamics in web navigation.  In International Conference on Learning Representations,  Vol. 2025,  pp. 63707–63738. 
  * B. Chen, C. Shu, E. Shareghi, N. Collier, K. Narasimhan, and S. Yao (2023) Fireact: toward language agent fine-tuning.  arXiv preprint arXiv:2310.05915. 
  * K. Cheng, Q. Sun, Y. Chu, F. Xu, L. YanTao, J. Zhang, and Z. Wu (2024) Seeclick: harnessing gui grounding for advanced visual gui agents.  In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp. 9313–9332. 
  * G. Comanici, E. Bieber, M. Schaekermann, I. Pasupat, N. Sachdeva, I. Dhillon, M. Blistein, O. Ram, D. Zhang, E. Rosen, et al. (2025) Gemini 2.5: pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities.  arXiv preprint arXiv:2507.06261. 
  * J. Da, C. Wang, X. Deng, Y. Ma, N. Barhate, and S. Hendryx (2025) Agent-rlvr: training software engineering agents via guidance and environment rewards.  arXiv preprint arXiv:2506.11425. 
  * Z. Deng, Z. Dou, Y. Zhu, J. Wen, R. Xiong, M. Wang, and W. Chen (2024) From novice to expert: llm agent policy optimization via step-wise reinforcement learning.  arXiv preprint arXiv:2411.03817. 
  * G. Dong, H. Mao, K. Ma, L. Bao, Y. Chen, Z. Wang, Z. Chen, J. Du, H. Wang, F. Zhang, G. Zhou, Y. Zhu, J. Wen, and Z. Dou (2026) Agentic reinforced policy optimization.  In The Fourteenth International Conference on Learning Representations, 
  * L. Engstrom, A. Ilyas, S. Santurkar, D. Tsipras, F. Janoos, L. Rudolph, and A. Madry (2020) Implementation matters in deep policy gradients: a case study on ppo and trpo.  arXiv preprint arXiv:2005.12729. 
  * D. Guo, D. Yang, H. Zhang, J. Song, P. Wang, Q. Zhu, R. Xu, R. Zhang, S. Ma, X. Bi, et al. (2025) DeepSeek-r1 incentivizes reasoning in llms through reinforcement learning.  Nature 645 (8081),  pp. 633–638. 
  * H. He, W. Yao, K. Ma, W. Yu, Y. Dai, H. Zhang, Z. Lan, and D. Yu (2024) Webvoyager: building an end-to-end web agent with large multimodal models.  In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),  pp. 6864–6890. 
  * J. Huang, S. Yong, X. Ma, X. Linghu, P. Li, Y. Wang, Q. Li, S. Zhu, B. Jia, and S. Huang (2024) An embodied generalist agent in 3d world.  In Proceedings of the 41st International Conference on Machine Learning,  pp. 20413–20451. 
  * J. Kim, S. Rhee, M. Kim, D. Kim, S. Lee, Y. Sung, and K. Jung (2025) Reflact: world-grounded decision making in llm agents via goal-state reflection.  In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,  pp. 33421–33453. 
  * N. Lambert, J. Morrison, V. Pyatkin, S. Huang, H. Ivison, F. Brahman, L. J. V. Miranda, A. Liu, N. Dziri, S. Lyu, et al. (2024) Tulu 3: pushing frontiers in open language model post-training.  arXiv preprint arXiv:2411.15124. 
  * J. Li, Y. Su, and M. R. Lyu (2026) From laboratory to real-world applications: benchmarking agentic code reasoning at the repository level.  arXiv preprint arXiv:2601.03731. 
  * Y. Li, H. Wen, W. Wang, X. Li, Y. Yuan, G. Liu, J. Liu, W. Xu, X. Wang, Y. Sun, et al. (2024) Personal llm agents: insights and survey about the capability, efficiency and security.  arXiv preprint arXiv:2401.05459. 
  * H. Lightman, V. Kosaraju, Y. Burda, H. Edwards, B. Baker, T. Lee, J. Leike, J. Schulman, I. Sutskever, and K. Cobbe (2024) Let’s verify step by step.  In International Conference on Learning Representations,  Vol. 2024,  pp. 39578–39601. 
  * H. Liu, C. Li, Q. Wu, and Y. J. Lee (2023) Visual instruction tuning.  Advances in neural information processing systems 36,  pp. 34892–34916. 
  * R. Luo, L. Wang, W. He, L. Chen, J. Li, and X. Xia (2025) Gui-r1: a generalist r1-style vision-language action model for gui agents.  arXiv preprint arXiv:2504.10458. 
  * X. Puig, E. Undersander, A. Szot, M. Dallaire Cote, T. Yang, R. Partsey, R. Desai, A. Clegg, M. Hlavac, S. Y. Min, et al. (2024) Habitat 3.0: a co-habitat for humans, avatars, and robots.  In International Conference on Learning Representations,  Vol. 2024,  pp. 15306–15336. 
  * X. Ren, R. Zhen, C. Li, Y. Song, Q. Hou, Y. Zhang, P. Liu, Q. Qi, Q. Zheng, Q. Wu, et al. (2026) X-omniclaw technical report: a unified mobile agent for multimodal understanding and interaction.  arXiv preprint arXiv:2605.05765. 
  * T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom (2023) Toolformer: language models can teach themselves to use tools.  Advances in neural information processing systems 36,  pp. 68539–68551. 
  * J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov (2017) Proximal policy optimization algorithms.  arXiv preprint arXiv:1707.06347. 
  * A. Setlur, C. Nagpal, A. Fisch, X. Geng, J. Eisenstein, R. Agarwal, A. Agarwal, J. Berant, and A. Kumar (2025) Rewarding progress: scaling automated process verifiers for llm reasoning.  In International Conference on Learning Representations,  Vol. 2025,  pp. 60808–60838. 
  * Z. Shao, P. Wang, Q. Zhu, R. Xu, J. Song, X. Bi, H. Zhang, M. Zhang, Y. Li, Y. Wu, et al. (2024) Deepseekmath: pushing the limits of mathematical reasoning in open language models.  arXiv preprint arXiv:2402.03300. 
  * J. Singh, R. Magazine, Y. Pandya, and A. Nambi (2025) Agentic reasoning and tool integration for llms via reinforcement learning.  arXiv preprint arXiv:2505.01441. 
  * A. Sinha, A. Arun, S. Goel, S. Staab, and J. Geiping (2026) The illusion of diminishing returns: measuring long horizon execution in LLMs.  In The Fourteenth International Conference on Learning Representations, 
  * A. Szot, A. Clegg, E. Undersander, E. Wijmans, Y. Zhao, J. Turner, N. Maestre, M. Mukadam, D. Chaplot, O. Maksymets, A. Gokaslan, V. Vondrus, S. Dharur, F. Meier, W. Galuba, A. Chang, Z. Kira, V. Koltun, J. Malik, M. Savva, and D. Batra (2021) Habitat 2.0: training home assistants to rearrange their habitat.  In Proceedings of the 35th International Conference on Neural Information Processing Systems,  NIPS ’21, Red Hook, NY, USA.  External Links: ISBN 9781713845393
  * L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, et al. (2024) A survey on large language model based autonomous agents.  Frontiers of Computer Science 18 (6),  pp. 186345. 
  * Y. Wang, X. Chen, X. Jin, M. Wang, and L. Yang (2026a) Openclaw-rl: train any agent simply by talking.  arXiv preprint arXiv:2603.10165. 
  * Y. Wang, T. Xie, K. Shen, M. Wang, and L. Yang (2026b) RLAnything: forge environment, policy, and reward model in completely dynamic rl system.  arXiv preprint arXiv:2602.02488. 
  * Y. Wang, F. Xu, Z. Lin, G. He, Y. Huang, H. Gao, Z. Niu, S. Lian, and Z. Liu (2026c) From assistant to double agent: formalizing and benchmarking attacks on openclaw for personalized local ai agent.  arXiv preprint arXiv:2602.08412. 
  * Z. Wang, F. Wu, H. Wang, X. Tang, B. Li, Z. Yin, Y. Ma, Y. Li, W. Sun, X. Chen, et al. (2026d) Why reasoning fails to plan: a planning-centric analysis of long-horizon decision making in llm agents.  arXiv preprint arXiv:2601.22311. 
  * Z. Wang, M. Gao, H. Yin, J. Yu, T. Chen, S. Sadiq, and T. Li (2026e) Self-distilled reinforcement learning for co-evolving agentic recommender systems.  arXiv preprint arXiv:2604.10029. 
  * T. Wei, T. Li, Z. Liu, X. Ning, Z. Yang, J. Zou, Z. Zeng, R. Qiu, X. Lin, D. Fu, et al. (2026) Agentic reasoning for large language models.  arXiv preprint arXiv:2601.12538. 
  * J. Wu, B. Li, R. Fang, W. Yin, L. Zhang, Z. Wang, Z. Tao, D. Zhang, Z. Xi, R. Tang, et al. (2026) Webdancer: towards autonomous information seeking agency.  Advances in Neural Information Processing Systems 38,  pp. 120957–120985. 
  * J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press (2024) Swe-agent: agent-computer interfaces enable automated software engineering.  Advances in Neural Information Processing Systems 37,  pp. 50528–50652. 
  * S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y. Cao (2022) React: synergizing reasoning and acting in language models.  arXiv preprint arXiv:2210.03629. 
  * S. Yenamandra, A. Ramachandran, K. Yadav, A. Wang, M. Khanna, T. Gervet, T. Yang, V. Jain, A. W. Clegg, J. Turner, et al. (2023) Homerobot: open-vocabulary mobile manipulation.  arXiv preprint arXiv:2306.11565. 
  * J. Zhang, Y. Cheng, Y. Ni, Y. Pan, Z. Yuan, J. Fu, Y. Li, J. Wang, and F. Yuan (2024) Ninerec: a benchmark dataset suite for evaluating transferable recommendation.  IEEE Transactions on Pattern Analysis and Machine Intelligence. 
  * J. Zhang, C. Gao, L. Zhang, Q. V. H. Nguyen, and H. Yin (2026) Smartagent: chain-of-user-thought for embodied personalized agent in cyber world.  In Proceedings of the AAAI Conference on Artificial Intelligence,  Vol. 40,  pp. 17993–18001. 
  * J. Zhang, J. Yu, Z. Wang, W. Yuan, T. Chen, Q. V. H. Nguyen, B. Cui, and H. Yin (2025a) Towards reasoning-aware recommender systems: a survey in the llm era.  Authorea Preprints. 
  * Y. Zhang, S. Qiao, J. Zhang, T. Lin, C. Gao, and Y. Li (2025b) A survey of large language model empowered agents for recommendation and search: towards next-generation information retrieval.  arXiv preprint arXiv:2503.05659. 
  * Y. Zhao, W. Shi, F. Feng, and X. He (2025) Appagent-pro: a proactive gui agent system for multidomain information integration and user assistance.  In Proceedings of the 34th ACM International Conference on Information and Knowledge Management,  pp. 6767–6771. 
  * Y. Zheng, J. Lu, S. Wang, Z. Feng, D. Kuang, and Y. Xiong (2025) Easyr1: an efficient, scalable, multi-modality rl training framework.  arXiv preprint arXiv:2501.12345. 
  * A. Zhou, K. Yan, M. Shlapentokh-Rothman, H. Wang, and Y. Wang (2024) Language agent tree search unifies reasoning, acting, and planning in language models.  In Proceedings of the 41st International Conference on Machine Learning,  pp. 62138–62160. 
  * Y. Zhou, S. Jiang, Y. Tian, J. Weston, S. Levine, S. Sukhbaatar, and X. Li (2025) Sweet-rl: training multi-turn llm agents on collaborative reasoning tasks.  arXiv preprint arXiv:2503.15478. 
  * J. Zhu, W. Wang, Z. Chen, Z. Liu, S. Ye, L. Gu, H. Tian, Y. Duan, W. Su, J. Shao, et al. (2025) Internvl3: exploring advanced training and test-time recipes for open-source multimodal models.  arXiv preprint arXiv:2504.10479. 
  * N. Zhu, H. Wang, J. Zhou, F. Chen, S. Zhang, G. Chen, C. Liu, J. Wu, W. Chen, X. Mou, et al. (2026) SemaClaw: a step towards general-purpose personal ai agents through harness engineering.  arXiv preprint arXiv:2604.11548. 


##  Appendix A Appendix
###  A.1. Detailed Prompt
Prompt designs of our ODYSSE You are a personal GUI agent. In this UI screenshot <image>, I want you to continue executing the command {goal}, with the previous actions being {previous_actions}. Please provide exactly one next action. The action must be one of: [’click’, ’type’, ’scroll up’, ’scroll down’, ’scroll left’, ’scroll right’, ’exit’, ’complete’, ’recommendation’]. Output the thinking process in <think> </think> tags, and the final answer in <answer> </answer> tags. The final answer must contain exactly one dictionary in the following format: <think> ... </think> <answer>[’action’: ACTION, ’point’: [x, y], ’input_text’: TEXT]</answer> Rules for each action: • output the click point [x, y] • input_text must be ’no input text’ • output the target point [x, y] • input_text must be the exact text to type 3. For ’scroll up’, ’scroll down’, ’scroll left’, ’scroll right’, ’exit’: • point must be [-100, -100] • input_text must be ’no input text’ 4. For ’pool_found’: • point must be [-100, -100] • input_text must be a short summary of the user’s final intent 5. For ’recommendation’: • point must be [-100, -100] • input_text must be exactly one English word: ’Yes’ or ’No’ • do not output any explanation, summary, or extra text Important constraints: • Output exactly one action. • Do not output multiple <think>/<answer> blocks. • Do not output multiple dictionaries. • For ’recommendation’, input_text must be exactly ’Yes’ or exactly ’No’. • For ’complete’, input_text must summarize the user’s GUI intent in natural language.
###  A.2. Case Study
Case Study of our proposed ODYSSE.
