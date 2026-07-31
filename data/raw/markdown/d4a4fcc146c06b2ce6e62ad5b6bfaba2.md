arXiv is now an independent nonprofit! Learn more ×
License: arXiv.org perpetual non-exclusive license 
arXiv:2607.25446v1 [cs.AI] 28 Jul 2026
# Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm
Huan Chen1, Xiang Song1, Jian Jin1, Pan Ren1, Liang-Jie Zhang2
###### Abstract
Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: _who_ is on the team (organization), _how_ members align (coordination), and _which_ algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. Classic organizational theory (Belbin roles, Mintzberg coordination, RACI accountability) becomes executable, validated configuration, and the framework places six published collaboration algorithms behind a common interface while exposing roles, coordination, and accountability as independently configurable factors. We use this separation to conduct controlled comparisons in which organizational assignments vary while the collaboration protocol is held fixed. It also turns protocol choice into a variable that can be _learned_ : Adaptive Org Routing, a contextual-bandit meta-protocol, selects a protocol per task under an explicit quality–cost trade-off, outperforms every fixed protocol in a controlled study, and trains online on real benchmark and LLM-judge rewards. The ablations expose a mechanism. Accountability placement changes outcomes exactly when the protocol routes the deliverable through the accountable agent, and the winning placement flips across model families, so organizational design cannot be hard-coded; it must be re-validated, or learned, for each model binding.
## Introduction
Large language models (LLMs) have moved from single-shot prompting to _multi-agent_ collaboration, in which multiple model instances critique and build on one another’s reasoning. A growing toolbox of collaboration algorithms now exists—Mixture-of-Agents (Wang et al. 2025), Multi-Agent Debate (Du et al. 2024), Self-Consistency (Wang et al. 2023b), LLM-Blender (Jiang, Ren, and Lin 2023), Plan-and-Execute (Hong et al. 2024), Reflexion (Shinn et al. 2023)—alongside agent frameworks such as AutoGen, CAMEL, and MetaGPT.
#### The entanglement problem.
Despite this progress, most frameworks _tangle_ three logically independent concerns into one implementation:
  1. 1.
Organization (WHO): which agents exist, what roles they play, which models back them, and who is accountable.
  2. 2.
Coordination (HOW): the mechanism by which members align, whether informal mutual adjustment, a supervisor issuing orders, or standardized procedures and outputs.
  3. 3.
Collaboration protocol (the ALGORITHM): the procedure that fuses individual contributions into a result, such as debate, voting, or planning.


When these are fused, swapping the aggregation algorithm means rewriting the team. The cost is threefold: teams cannot be reconfigured without touching algorithms; decades of organizational theory (Belbin 2010; Mintzberg 1979) cannot be applied as a first-class design surface; and collaboration algorithms cannot be compared on an equal organizational footing, since each ships its own implicit team.
#### Our thesis: decouple the three concerns.
We argue these concerns are _orthogonal_ and model them as independently swappable layers. IMACS (Intelligent Multi-Agent Collaboration System) realizes this: organizations are declared in YAML and grounded in Belbin’s nine roles ; coordination is one of Mintzberg’s five mechanisms (Mintzberg 1979); and the collaboration protocol is a pluggable object behind a single interface. RACI is a cross-cutting tag with a validated at-most-one-Accountable constraint, and any layer can be replaced without touching the others (Proposition ). To show the organization layer is culturally pluggable, IMACS ships three presets: belbin (default), adhocracy, and three-departments (the Tang-dynasty ministry system in Belbin terms).
#### Why decouple?
Once the three factors are independently swappable, organizational variables (roles, coordination, RACI) can be held fixed or ablated while the protocol stays constant; to our knowledge, no prior multi-agent LLM framework supports such controlled ablation of _who_ and _how_ independent of _which algorithm_. Protocol choice also becomes a free variable. We exploit both consequences in this paper.
#### Adaptive Org Routing.
With protocol choice freed, we cast it as an online decision problem. Adaptive Org Routing featurizes each task into an interpretable 7-dimensional vector and uses a LinUCB contextual bandit (Li et al. 2010) to select, per task, the protocol that maximizes a cost-adjusted reward r=quality−r=\text{quality}-\lambda\cdot\text{cost}, updating online via rank-1 Sherman–Morrison updates. Over a task stream it traces a quality/cost Pareto frontier, spending on expensive protocols only when they earn their cost.
#### Contributions.
  * •
A decoupled architecture and formalization (our core contribution). We separate organization, coordination, and collaboration into orthogonal layers, formalize an organization as O=(\mathcal{R},\mu,\kappa,\rho) and a protocol as π:(Task,Team,Blackboard)→Result\pi:(\text{Task},\text{Team},\text{Blackboard})\\!\to\\!\text{Result}, and prove an orthogonality property on which the controlled ablations and the router below both rest.
  * •
A systematic study of the organization dimension. Holding the protocol fixed and varying the organization, controlled RACI ablations replicated three times show accountability matters _exactly when_ the protocol routes the deliverable through the accountable agent, and only by changing which model does the work; a natural cross-dataset conjecture proves _unstable across repeats and model bindings_. We also stress-test a catalog of evidence-backed (organization, protocol) recipes on five real benchmarks.
  * •
Adaptive Org Routing, an online organization-aware meta-protocol that selects a protocol per task via a contextual bandit over task features, evaluated on a controlled oracle ( routing accuracy, beating all six fixed baselines) and trained on real objective and LLM-judge rewards.
  * •
A modular, reproducible framework, released with this paper: a unified pluggable implementation of the six protocols above on AgentScope 2.0, with gateway key isolation, a transparent blackboard runtime, and seeded benchmarks.


A note on scope: the framework is the primary contribution and the router a method instance built on it. The router’s headline number comes from a controlled simulated oracle; the real-benchmark, real-reward, and RACI results are small-, reported as direction and mechanism (see Discussion).
## Related Work
#### Multi-agent LLM frameworks.
Prior frameworks couple roles, coordination, and aggregation (Guo et al. 2024): conversational systems like AutoGen, CAMEL, and AgentVerse fix the dialogue loop as the protocol (Wu et al. 2024; Li et al. 2023; Chen et al. 2024), while MetaGPT and ChatDev bind roles to a fixed software-company pipeline (Hong et al. 2024; Qian et al. 2024). A complementary line optimizes the communication topology itself—GPTSwarm learns over agent graphs (Zhuge et al. 2024), DyLAN prunes dynamic agent networks (Liu et al. 2024)—but _within_ one algorithmic family, without declarative roles or accountability. Purpose-built evaluations have followed: MultiAgentBench scores collaboration across coordination topologies with milestone KPIs (Zhu et al. 2025); AgentsNet poses formally verifiable coordination problems over agent networks (Grötschla et al. 2025). IMACS instead treats organization, coordination, and collaboration as orthogonal layers over a generic runtime (we build on AgentScope 2.0 (Gao et al. 2024)), so a team and an algorithm combine freely.
#### Collaboration algorithms.
We treat published collaboration algorithms as interchangeable _protocols_ : Mixture-of-Agents (Wang et al. 2025) (proposer/aggregator layers), Multi-Agent Debate (Du et al. 2024) (critique-revise rounds), Self-Consistency (Wang et al. 2023b) (sample-and-vote), LLM-Blender (Jiang, Ren, and Lin 2023) (rank-and-fuse), Plan-and-Execute in the Plan-and-Solve / MetaGPT line (Wang et al. 2023a; Hong et al. 2024) (decompose-then-execute), and Reflexion (Shinn et al. 2023) (verbal self-feedback). IMACS ships each behind a common interface, so they can be compared on the same team and selected automatically per task.
#### Organizational theory.
Belbin identifies nine team roles (thought-, people-, action-oriented) a balanced team covers; Mintzberg (Mintzberg 1979) identifies five coordination mechanisms and forms such as the adhocracy; RACI assigns Responsible/Accountable/Consulted/Informed tags, classically one Accountable per deliverable. While agent “personas” are common, IMACS makes these theories a _first-class, declarative, validated_ design surface, with cultural pluggability via the _three-departments_ preset (the Tang ministry system; Fei, Guo, and Xiao 2026 also cast historical institutions as agent topologies, but as fixed architectures, not a swappable layer).
#### Bandits for model and protocol selection.
LinUCB (Li et al. 2010) is the canonical linear-payoff contextual bandit (Auer, Cesa-Bianchi, and Fischer 2002; Chu et al. 2011) with \tilde{O}(\sqrt{T}) regret. Adjacent selection problems use the same machinery, routing _queries to models_ (Chen, Zaharia, and Zou 2024; Shnitzer et al. 2024; Ong et al. 2025; Poon et al. 2026) or across agent _communication_ standards (A2A, ACP, ANP) (Du et al. 2026). IMACS routes at a different layer, to our knowledge unaddressed: its arms are entire _collaboration algorithms_ over a declared organization, its context an interpretable 7-dimensional task featurization, and the problem is well-posed only because organization and protocol are decoupled (Proposition ).
## The IMACS Framework
Figure 1: The seven-layer IMACS stack. Inside the dashed region, the organization (WHO/HOW) and the collaboration protocol (ALGORITHM) meet only through the runtime’s Team and Blackboard interfaces, so any organization composes with any protocol (Proposition ). The adaptive router is itself an L4 protocol that selects among the others.
IMACS is organized as a stack of seven layers (Figure ). Lower layers provide atomic capabilities; upper layers compose them. The three middle layers (organization, collaboration, and the runtime that hosts them) are where the decoupling lives.
### Layers
L1 Atomic capabilities. Model adapters, tools, MCP servers, and the provider-facing _ModelGateway_. The ModelGateway owns provider credentials and resolves opaque model handles, keeping credentials below the agent boundary. Models are restricted to an author-defined experimental registry: callable through available provider APIs, compatible with the common AgentScope chat interface, and spanning distinct provider families. It is an implementation allowlist, not an external certification or quality endorsement. An offline deterministic stand-in keeps tests and demos running without credentials or network access.
L2 Agent. A role-typed wrapper binding a model handle, a system prompt, and tools; agents act via a ReAct-style reason-act loop (Yao et al. 2023) when tools are involved.
L3 Organization (WHO/HOW). A declarative team: Belbin-typed roles, each bound to a registered model and a RACI tag, plus a Mintzberg coordination mechanism. Loaded from YAML presets and formalized below (Definition ).
L4 Collaboration protocol (ALGORITHM). The pluggable fusion algorithm behind the single interface of Definition . Ships voting, MoA, blender, debate, reflexion, plan-execute, and the _adaptive_ meta-protocol (Adaptive Org Routing).
L5 Runtime. A _Conductor_ instantiates a Team from an organization and drives a protocol over a shared _Blackboard_ on which every intermediate message is posted, a transparent room with human-in-the-loop and SSE hooks.
L6 API Gateway. A FastAPI boundary exposes the L5 Conductor through REST and streams Blackboard events through SSE. It delegates model resolution to L1’s ModelGateway and does not expose provider credentials to applications.
L7 Application. A Vue application provides two canonical demos: an _arena_ (models compete per query) and a _project_ (a task decomposed across roles).
### Formalization
######  (Organization).
An organization is a tuple O=(\mathcal{R},\mu,\kappa,\rho) where
  * •
\mathcal{R}=\\{r_{1},\dots,r_{n}\\} is a set of _roles_ , each r_{i}\in\mathcal{B} drawn from Belbin’s nine team roles ℬ\mathcal{B};
  * •
\mu:\mathcal{R}\to\mathcal{M} is a _model binding_ from roles to the configured model registry ℳ\mathcal{M} (the gateway guarantees \mathrm{im}(\mu)\subseteq\mathcal{M});
  * •
\kappa\in\mathcal{K} is a single _coordination mechanism_ from Mintzberg’s five mechanisms 𝒦\mathcal{K};
  * •
\rho:\mathcal{R}\to\\{\mathsf{R},\mathsf{A},\mathsf{C},\mathsf{I}\\} is the RACI _assignment_ , subject to the single-owner constraint ||≤1\bigl|\\{r\in\mathcal{R}:\rho(r)=\mathsf{A}\\}\bigr|\leq 1.


Here 𝖱\mathsf{R}, 𝖠\mathsf{A}, 𝖢\mathsf{C}, and 𝖨\mathsf{I} denote Responsible, Accountable, Consulted, and Informed; Greek symbols name organization components rather than reusing these RACI initials. The single-owner constraint is validated at load time. A _Team_ is the instantiation of : a set of agents \\{a_{i}\\} where wraps model \mu(r_{i}) under role , sharing a coordination context derived from .
######  (Collaboration protocol).
A collaboration protocol is a function  
| π:(𝑇𝑎𝑠𝑘,𝑇𝑒𝑎𝑚,𝐵𝑙𝑎𝑐𝑘𝑏𝑜𝑎𝑟𝑑)⟶𝑅𝑒𝑠𝑢𝑙𝑡,\pi:\ (\mathit{Task},\ \mathit{Team},\ \mathit{Blackboard})\ \longrightarrow\ \mathit{Result},  |  
| --- |  
that, given a task, an instantiated team, and a shared blackboard, executes a fusion algorithm and returns a result, while posting every intermediate utterance to the blackboard. The set of protocols is extensible: a new algorithm is a new \pi\in\Pi registered by name.
A protocol is deliberately _agnostic_ to which roles populate the team and to ; it sees a pool of role-typed agents, never a fixed cast. Conversely, an organization carries no commitment to any .
######  (Orthogonality of the three layers).
Let 𝒪\mathcal{O} be the set of valid organizations and the protocols. The system’s behavior is a well-defined map run:→𝑅𝑒𝑠𝑢𝑙𝑡\mathrm{run}:\mathcal{O}\times\Pi\times\mathit{Task}\to\mathit{Result} on the full product \mathcal{O}\times\Pi: any organization O\in\mathcal{O} composes with any protocol \pi\in\Pi. Hence replacing one component leaves the interfaces of the others invariant: for fixed , varying (roles, models, coordination , or RACI assignment ) requires no change to ; and for fixed , varying requires no change to .
###### Proof sketch.
depends on only through the _Team_ interface (a pool of role-typed agents) and the _Blackboard_ interface, neither of which exposes specific roles, model identities, , or . depends on through no interface at all; it is a static declaration consumed by the runtime, not by . Therefore the two are free coordinates of the design space, and run\mathrm{run} is total on \mathcal{O}\times\Pi. The coordination mechanism is likewise a property of surfaced to agents as context, independent of . ∎
Proposition lets the three presets (belbin, adhocracy, three-departments) and the protocol library be reused combinatorially, and it makes the routing problem of Adaptive Org Routing well-posed: the router chooses a point in while is held fixed.
## Adaptive Org Routing
Decoupling protocols from organizations (Proposition ) makes protocol choice a free variable. The right choice is task-dependent: cheap voting suffices for factual lookups, debate helps reasoning, and plan-and-execute suits decomposable work, but each step up costs more model calls. _Adaptive Org Routing_ learns this mapping online.
### Task featurization
Routing must be cheap relative to the protocols it selects, so featurization uses no model call. A goal string is mapped to an interpretable vector x\in\mathbb{R}^{7} whose coordinates are an intercept and six features— _length_ , _#questions_ , _#subtasks_ , _reasoning_ , _factoid_ , _has_code_ —each bounded to by normalized counts (token length, ? count, decomposition/reasoning/factoid keyword densities, and a code indicator). These features are the _context_ that lets the policy generalize across tasks of the same type.
### Bandit formulation
We cast per-task protocol selection as a contextual bandit. The arms are the six base protocols 𝒜={voting,moa,blender,debate,reflexion,plan-execute}\mathcal{A}=\\{\text{voting},\text{moa},\text{blender},\text{debate},\text{reflexion},\text{plan-execute}\\}. On task with feature vector , the router plays arm \pi_{t}\in\mathcal{A}, runs that protocol over the (fixed) organization, observes a quality estimate q_{t}\in[0,1] from an evaluator agent, and forms a _cost-adjusted reward_  
| =,=,r_{t}\;=\;q_{t}\;-\;\lambda\cdot\tilde{c}(\pi_{t}),\qquad\tilde{c}(\pi)=\frac{c(\pi)}{\max_{\pi^{\prime}}c(\pi^{\prime})},  |  
| --- |  
where is the protocol’s relative model-call multiplicity (voting , MoA/blender , reflexion , plan-execute , debate ) and \lambda\geq 0 tunes cost aversion.
We use LinUCB (Li et al. 2010). Each arm maintains A_{a}\in\mathbb{R}^{d\times d} (initialized to , ) and b_{a}\in\mathbb{R}^{d}. Its payoff estimate is \hat{\theta}_{a}=A_{a}^{-1}b_{a} and the router selects  
| =arg⁡⁡(+),\pi_{t}\;=\;\arg\max_{a\in\mathcal{A}}\ \Bigl(\hat{\theta}_{a}^{\top}x_{t}\;+\;\alpha\sqrt{x_{t}^{\top}A_{a}^{-1}x_{t}}\,\Bigr),  |  
| --- |  
the upper-confidence bound on cost-adjusted utility, with exploration coefficient . After observing it updates A_{\pi_{t}}\\!\mathrel{+}=x_{t}x_{t}^{\top}, b_{\pi_{t}}\\!\mathrel{+}=r_{t}x_{t}. We maintain A_{a}^{-1} directly via the Sherman–Morrison rank-1 update,  
| ←−​,A^{-1}\leftarrow A^{-1}-\frac{(A^{-1}x)(A^{-1}x)^{\top}}{1+x^{\top}A^{-1}x},  |  
| --- |  
giving O(d^{2}) per-step learning with no matrix inversion. The full per-task meta-protocol is given as pseudocode in the supplement.
### Persistence and online observability
The router’s entire learned state is the per-arm pair (A_{a}^{-1},b_{a}) plus a pull count, a few small dense matrices () that serialize compactly to JSON, so a policy can be checkpointed and restored to resume learning rather than cold-start; restoration validates the arm set and feature dimension. Because learning is fully online, rolling routing accuracy and cumulative regret stream per round (Figure ): train once, persist, keep improving.
### Regret and “org-awareness”
Equation () is LinUCB on a -dimensional context with bounded rewards, which under the standard linear-payoff assumption enjoys \tilde{O}(\sqrt{dT}) cumulative regret (Li et al. 2010); our setting satisfies the assumptions by construction (full statement and sketch in the supplement), so per-round regret against the cost-adjusted optimum vanishes as \tilde{O}(\sqrt{d/T}). The router holds fixed and chooses over , but by Proposition the arm set extends to (protocol, coordination) pairs or per-role model bindings with the same machinery (only |\mathcal{A}| grows); we evaluate the protocol-selection instance and leave the joint space to future work.
## Scenario Recommendations
Proposition guarantees that any organization composes with any protocol, but not _which_ combination to pick. This section closes that gap with a small catalog of evidence-backed (organization, protocol) recipes (Table ), each naming a public benchmark so the recommendation is falsifiable, shipped as a one-call API and an auto-recommender.
### From evidence to recipes
The recipes follow established results: self-consistency voting for verifiable arithmetic (Wang et al. 2023b); multi-agent debate for open-ended reasoning and factuality (Du et al. 2024); Mixture-of-Agents (Wang et al. 2025) and ranking-fusion (Jiang, Ren, and Lin 2023) for open-ended generation; Reflexion for code with executable feedback (Shinn et al. 2023); and role-specialized planning for complex, decomposable tasks (Hong et al. 2024).  
 |  
|  |  
| Factual lookup  | belbin  | voting  |  
| Math reasoning  | belbin  | voting  |  
| Open reasoning  | belbin  | debate  |  
| Code generation  | belbin  | reflexion  |  
| Open-ended gen.  | adhocracy  | moa  |  
| Candidate fusion  | belbin  | blender  |  
| Complex decomp.  | three-departments  | plan-execute  |  
Table 1: Evidence-backed scenario recipes. Each pairing is the default IMACS recommendation for its scenario, tested against a public benchmark; evidence cited in the text.
Collaboration is not universally beneficial: heavy protocols can over-think simple tasks and coordination failures can reduce quality (Cemri et al. 2025). Recipes therefore encode structural role division rather than persona strings, which do not reliably improve objective accuracy (Zheng et al. 2024), and serve as priors for the adaptive router.
### From asserted to validated recommendations
We test these priors on five public benchmarks: GSM8K (Cobbe et al. 2021) exact-match, HumanEval (Chen et al. 2021) pass@1, HotpotQA token-F1, and AgentsNet (Grötschla et al. 2025) formal validity use task-intrinsic, model-free scoring; open-ended AlpacaEval uses a disclosed LLM-judge win-rate. Runs also log latency and answer length, isolate item-level transport failures, and record data source and generation mode. Every table cell is generated from its evaluation record, so Table is a directly auditable quality/cost frontier rather than a manually transcribed summary.  
 |  
|  |  
| exact-match  | pass@1  | token-F1  | win-rate  | validity  |  
| Voting  | 0.60  | 0.33  | 0.90  |  
| Debate  | 0.36  | 1.00  |  
| Reflexion  | 0.50  | 0.21  | –  |  
| Plan-Execute  | –  |  
| Best solo  | 0.90  | 1.00  | 0.53  | 1.00  | 1.00  |  
Table 2: Real-benchmark evaluation, items/cell, real models (belbin org). Each column is scored by its objective metric (exact-match / pass@1 / token-F1 / formal validity) or, for the inherently open-ended AlpacaEval, an LLM-judge win-rate vs. a reference baseline (judge = GLM-5.2; a model judge carries length/style biases). Best protocol per objective column in bold. At , reported AlpacaEval scores are near the ceiling and AgentsNet scores equal , so we read cost there. “–”: not run. Bottom row: the strongest _single_ model per dataset answering alone (mean over the three solo runs in the organization-dimension study; single run for AlpacaEval and AgentsNet).
#### Findings.
At /cell, HotpotQA supports Plan-and-Execute (, also lowest latency), while GSM8K favors Plan-and-Execute and Debate () over the Voting recipe (). At , all reported HumanEval and AgentsNet cells equal , leaving cost as the useful axis: Plan-and-Execute is respectively 4.2\times and 2.3\times faster than Debate. Reported AlpacaEval scores are near the ceiling (–); MoA reaches the top observed win-rate at the lowest latency ( s versus s for Blender and s for Debate). No protocol exceeds the strongest solo model on quality, and that model changes by dataset. Thus task type and model binding jointly determine the winner: recipes are falsifiable priors, not guarantees, motivating adaptive selection. These small- runs are directional rather than leaderboard claims. Objective metrics are used wherever possible; the open-ended judge, its biases, and the synthetic/real boundary are explicitly disclosed. AgentsNet is evaluated as a whole-graph deliverable because its checker is intrinsic to the output; framework-coupled interaction metrics are excluded (supplement).
### The organization dimension
The findings above vary the protocol while holding the organization fixed. We now cross the two. Table (a) evaluates a partial 3\times 2 organization–protocol grid on GSM8K: no organization is uniformly best, the protocol preference varies with the organization (_belbin_ and _three-departments_ favor debate, 0.60/0.800.60/0.80 and 0.50/0.900.50/0.90, while _adhocracy_ is even at 0.70/0.700.70/0.70), and a fixed protocol moves by up to exact-match across organizations. This is direct evidence for Proposition in practice: the organization is a real, independent lever whose best choice interacts with the protocol.
#### Does accountability placement matter? A controlled RACI ablation.
Because the three presets differ on many axes at once, a raw grid cannot isolate _RACI_ , so we add a controlled ablation (Table (b)): three variants of the _same_ belbin team (identical roles, models, and coordination) differing only in the Accountable tag (Chair, Critic, or none). Voting and debate never read the tag, so for them the three variants are functionally identical, which lets this grid double as a noise calibration. Over three independent repeats, the variant _means_ agree within (voting –; debate –) while the _single-run_ cross-variant spread reaches 0.17±0.050.17\pm 0.05: single-run differences of that size are generation noise, the yardstick for the Blender effect below. With three repeats (all are population std over repeats), we report sign consistency and paired effect sizes rather than significance tests. We report this near-null result as is: _where_ accountability sits barely moves objective accuracy, consistent with evidence that role/persona tags alone do not lift objective performance (Zheng et al. 2024) and with the framing above that a recipe’s value is structural.
#### When RACI _does_ bite: a mechanistic prediction, tested.
The null on voting/debate does not mean accountability is inert; those protocols simply never read the Accountable tag. Reading the control flow predicts when RACI matters: LLM-Blender hands the final fusion to the team’s accountable agent (first agent when none is tagged), so the _fuser is the accountable agent_ ; moving Accountable from the Chair (glm-5.2) to the Critic (deepseek) reroutes the final write to a different model. MoA instead aggregates at its coordinator role and consults the Accountable tag only as a fallback, so its aggregator stays the Chair regardless of RACI. This yields a falsifiable prediction, _RACI should move Blender but not MoA_ , and a natural follow-up conjecture, that Blender’s winning variant should use the stronger fuser model. We test both across three independent repeats with a solo-model baseline (Table (c) and Table ). The prediction holds in the repeated data: on HotpotQA, Blender’s paired CriticChair gap is positive in _every_ repeat (±0.02+0.08\pm 0.02 in the fuser grid; 0.34±0.060.34\pm 0.06 vs. 0.48±0.050.48\pm 0.05 cross-dataset), while the MoA control, whose aggregator is identical in all three variants, shows an unsigned spread of comparable magnitude ( per repeat) whose _ordering shuffles_ across repeats. The effect is stable in sign; the control varies without one. GSM8K moves the same way when it moves (0.70±0.000.70\pm 0.00 vs. 0.77±0.090.77\pm 0.09) and all HumanEval cells equal in this sample. The follow-up conjecture, by contrast, has _no stable direction_ : across the repeats the winning fuser matched the stronger _solo_ model in , , and of 3 datasets, and shifts again under a different model binding (supplement). The claim that survives is precise: accountability placement affects outcomes exactly when the protocol routes the deliverable through the accountable agent (a replicated, sign-consistent effect), it operates by changing which model does the work, and its direction is not predictable a priori. The optimal placement must therefore be found empirically, an argument for an adaptive router over (organization, protocol) rather than a static rule.  
| Organization  |  
| --- |  
| _(a) org protocol — presets_  |  
| adhocracy  | 0.70  | 0.70  |  
| three-departments  | 0.50  |  
| _(b) RACI ablation (3 repeats)_  |  
| Chair  |  
| Critic  |  
| none  |  
| _(c) HotpotQA fuser ablation (3 repeats)_  |  
| Chair  |  
| Critic  |  
| none  |  
Table 3: Organization dimension (exact-match / token-F1, /cell, real models; (b–c) meanstd over three repeats). _(a)_ GSM8K: no organization is uniformly best and the protocol preference varies with the organization — a real, independent lever that interacts with the protocol. _(b)_ Voting and debate never read the Accountable tag, so these variants are functionally identical: means agree within , single-run spread reaches 0.17±0.050.17\pm 0.05 (the measured noise floor). _(c)_ Blender’s fuser _is_ the accountable agent: its paired CriticChair gap is positive in repeats (±0.02+0.08\pm 0.02), while the MoA control (identical aggregator) shuffles across repeats. The gap keeps its sign; the control does not.  
 |  
|  |  
 |  
| glm fuser  | deepseek fuser  |  
| GSM8K  |  
| HumanEval  |  
| HotpotQA  |  
Table 4: RACI Blender cross-dataset attribution, meanstd over 3 independent repeats (/cell, real models). Moving Accountable from Chair (glm-5.2 fuser) to Critic (deepseek fuser) reroutes who writes the final answer. The winning fuser matched the stronger _solo_ model in 1, 3, 1 of 3 datasets per repeat: no stable direction, so the optimal placement must be found empirically.
## Experiments
We study whether Adaptive Org Routing _learns_ to send each task to its cost-adjusted optimal protocol, and whether the learned policy beats every fixed protocol. Because the goal is to measure routing/regret behavior against _known_ ground truth, not to estimate absolute LLM quality, we evaluate against a controlled simulated oracle (motivated in the Discussion).
### Setup
Task stream. A mixed suite of factual, reasoning, complex-decomposition, code, and open-ended tasks (e.g., “What is the capital of France?”). Each round draws a task uniformly at random; tasks carry a type tag used only to define the oracle, never seen by the router.
Simulated quality oracle. Each (task-type, protocol) pair has a latent mean quality in plus bounded Gaussian noise (\sigma{=}0.03). The latent profile encodes established literature trends: factual tasks peak at _voting_ ; reasoning peaks at _debate_ (Du et al. 2024); code peaks at _reflexion_ (Shinn et al. 2023); complex/decomposable tasks peak at _plan-execute_ (Hong et al. 2024); open-ended generation peaks at _MoA_ (Wang et al. 2025). After cost adjustment (Eq. ) each type has one clearly separated optimal arm, giving a learnable signal and a well-defined regret target.
Router and baselines. LinUCB with , \alpha{=}0.6. We compare against the six fixed-protocol baselines (always play one arm), an _oracle_ upper bound (always play the cost-adjusted optimal arm, no noise), and a _context-free_ bandit ablation (LinUCB fed a constant intercept-only feature, i.e., no task context). Reward is cost-adjusted (Eq. ); unless noted \lambda{=}0.3 and T{=}400. Routing accuracy is the fraction of the last 50 tasks routed to the cost-adjusted optimal arm. All runs are seeded and reproducible (supplement).
Model versions. The controlled study above uses no LLM calls. All real-model runs use this registry and pin exact versions: DeepSeek-V4 (deepseek-v4-pro, deepseek-v4-flash), Qwen3.7 (qwen3.7-plus), GLM-5.2 (glm-5.2), and MiniMax-M3 (MiniMax-M3); the AlpacaEval judge is glm-5.2.
#### Main result: the router approaches the oracle.
Table reports mean cost-adjusted reward at T{=}400, \lambda{=}0.3. The router attains , beating _all six_ fixed-protocol baselines (best fixed, MoA, ) and recovering of the best-fixedoracle headroom (oracle ); final routing accuracy is , with sublinear regret and an accuracy plateau (Figure ).  
| Method  | Mean reward  |  vs. router  |  
| --- | --- | --- |  
| Adaptive Org Routing (LinUCB)  | —  |  
| Oracle (upper bound)  | 0.754  |  
| MoA (best fixed)  | 0.669  |  
| Blender  | 0.652  |  
| Voting  | 0.629  |  
| Reflexion  | 0.621  |  
| Plan-Execute  | 0.550  |  
| Debate  | 0.519  |  
| Context-free bandit (ablation)  | 0.628  |  
Table 5: Mean cost-adjusted reward over T{=}400 mixed tasks (\lambda{=}0.3). The router beats all six fixed baselines and approaches the oracle; the context-free ablation collapses to always-voting, below the best fixed arm. Figure 2: Online learning (\lambda{=}0.3, T{=}400). _Left:_ cumulative regret vs. the cost-adjusted oracle grows sublinearly and flattens as the policy converges (consistent with the \tilde{O}(\sqrt{T}) LinUCB bound). _Right:_ last-50 routing accuracy climbs toward its plateau (dashed: final ).
The learned arm counts, in turn, show what the router learned: cheap _MoA_ (142/400) and _voting_ (111) carry the open-ended and factual mass, _reflexion_ (73) fires on code tasks, and the expensive arms (_plan-execute_ 29, _blender_ 23, _debate_ 22) are played only where their edge survives the cost penalty.
#### Ablation: task context.
The context-free bandit (constant feature) collapses to mean reward , the level of always-voting () and _below_ the best fixed arm (MoA, ). Without features it can only learn one global arm, so the gain comes from context, not from the bandit machinery.
#### Ablation: cost-aversion .
The -sweep (λ∈{0.1,0.3,0.5}\lambda\in\\{0.1,0.3,0.5\\}) shows the router beats best-fixed at every setting: accuracy rises as cost pressure separates the cost-adjusted optima (, , ) while absolute reward falls with the heavier penalty.
### From synthetic oracle to real rewards
We now run the _same_ router on _real_ rewards: each round draws an item from a mixed real-benchmark stream, the chosen protocol runs with real models, and the objective score (exact-match / pass@1 / token-F1) forms r=score−r=\text{score}-\lambda\,\tilde{c}(\pi). With no oracle for real quality we report realized reward and score, not a regret curve. Over an 18-round mixed stream (\lambda{=}0.3, belbin) the router trains end-to-end with no errors: mean task score , reward (HumanEval , GSM8K , HotpotQA ). We read this as a feasibility result (, with the arm distribution concentrated on one cost-efficient protocol): the central mechanism now runs unchanged on genuine outcomes.
#### Judge-based rewards integrate on the same scale.
Mixing AlpacaEval into the stream (reward an LLM-judge win-rate against a reference baseline), a 20-round four-dataset run trains with no errors (mean task score , reward ): judge-scored items land in on the same scale as exact-match/F1, so the bandit needs no special-casing. As a small- artifact the policy again concentrates on one cheap arm (here voting): a subjective, judge-derived reward drops into the same online loop.
## Discussion and Limitations
#### The synthetic oracle is a controlled stand-in.
The regret/accuracy study uses a _simulated_ oracle calibrated to literature trends (Du et al. 2024; Shinn et al. 2023; Hong et al. 2024): learning under known ground truth with exact regret; real-benchmark and real-reward results supply absolute quality.
#### Linearity, arms, and scale.
LinUCB assumes payoffs approximately linear in the 7 features; kernelized or neural bandits could capture nonlinear structure at higher cost. Extending arms to (protocol, coordination) or per-role bindings is well-defined under Proposition but enlarges exploration; our real runs are small- feasibility runs, not tuned policies.
#### Cost and statistical scope.
The router uses model-call multiplicity rather than provider-specific billing, so deployment costs require local recalibration. Real-model cells contain only items and the RACI study only three repeats; we therefore report latency, dispersion, sign consistency, and paired effects instead of leaderboard or significance claims. The process-global policy is suited to sequential learning; concurrent services should isolate or synchronize updates.
#### Benchmark and deployment scope.
The evaluated tasks score final deliverables; they do not cover long-horizon tool use, human approval loops, or failures caused by changing external state. AgentsNet is posed as a whole-graph team deliverable rather than through its native partial-visibility harness, which preserves task-intrinsic scoring but narrows the coordination claim. Online runs also depend on provider availability and a unified proxy, so their latency is environment-specific even when quality metrics are reproducible. Finally, the current feature map is intentionally lightweight and English-centric. Richer semantic features, persistent policies across deployments, and joint routing over organization and per-role model bindings remain open evaluations rather than claims established here.
#### Scope of orthogonality.
Proposition guarantees _interfaces_ compose, not that every combination is equally _effective_ ; the router exists to discover effective combinations empirically.
#### Model-binding dependence.
Recipe winners and the direction of the RACI effect flip across model bindings (supplement), so organizational conclusions need not transfer across model families. Re-validation must therefore be cheap, or learned online; this is the framework’s central argument.
## Conclusion
Most multi-agent LLM frameworks hard-wire _who_ collaborates into _how_ results are fused. IMACS separates these concerns: organizational theory becomes executable configuration, controlled ablations expose mechanisms, and protocol choice becomes learnable. Adaptive Org Routing outperforms every fixed protocol in the controlled study and trains online on real rewards. Roles, coordination, and accountability can thus be optimized alongside fusion algorithms, enabling inspectable comparisons across organizations, protocols, and model bindings.
## References
  * Auer, Cesa-Bianchi, and Fischer (2002) Auer, P.; Cesa-Bianchi, N.; and Fischer, P. 2002.  Finite-time Analysis of the Multiarmed Bandit Problem.  _Machine Learning_ , 47: 235–256. 
  * Belbin (2010) Belbin, R. M. 2010.  _Management Teams: Why They Succeed or Fail_.  Oxford, UK: Butterworth-Heinemann, 3rd edition.  First edition 1981. 
  * Cemri et al. (2025) Cemri, M.; Pan, M. Z.; Yang, S.; Agrawal, L. A.; Chopra, B.; Tiwari, R.; Keutzer, K.; Parameswaran, A.; Klein, D.; Ramchandran, K.; Zaharia, M.; Gonzalez, J. E.; and Stoica, I. 2025.  Why Do Multi-Agent LLM Systems Fail?  In _Advances in Neural Information Processing Systems (NeurIPS)_ , volume 38. 
  * Chen, Zaharia, and Zou (2024) Chen, L.; Zaharia, M.; and Zou, J. 2024.  FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance.  _Transactions on Machine Learning Research (TMLR)_. 
  * Chen et al. (2021) Chen, M.; Tworek, J.; Jun, H.; Yuan, Q.; et al. 2021.  Evaluating Large Language Models Trained on Code.  _arXiv preprint arXiv:2107.03374_. 
  * Chen et al. (2024) Chen, W.; Su, Y.; Zuo, J.; Yang, C.; Yuan, C.; Chan, C.-M.; Yu, H.; Lu, Y.; Hung, Y.-H.; Qian, C.; Qin, Y.; Cong, X.; Xie, R.; Liu, Z.; Sun, M.; and Zhou, J. 2024.  AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors.  In _Proceedings of ICLR_. 
  * Chu et al. (2011) Chu, W.; Li, L.; Reyzin, L.; and Schapire, R. 2011.  Contextual Bandits with Linear Payoff Functions.  In _Proceedings of AISTATS_ , 208–214. 
  * Cobbe et al. (2021) Cobbe, K.; Kosaraju, V.; Bavarian, M.; Chen, M.; Jun, H.; Kaiser, L.; Plappert, M.; Tworek, J.; Hilton, J.; Nakano, R.; Hesse, C.; and Schulman, J. 2021.  Training Verifiers to Solve Math Word Problems.  _arXiv preprint arXiv:2110.14168_. 
  * Du et al. (2026) Du, H.; Su, J.; Li, J.; Ding, L.; Yang, Y.; Han, P.; Tang, X.; Zhu, K.; and You, J. 2026.  Which LLM Multi-Agent Protocol to Choose?  In _Proceedings of ICML_. 
  * Du et al. (2024) Du, Y.; Li, S.; Torralba, A.; Tenenbaum, J. B.; and Mordatch, I. 2024.  Improving Factuality and Reasoning in Language Models through Multiagent Debate.  In _Proceedings of ICML_ , 11733–11763. 
  * Fei, Guo, and Xiao (2026) Fei, C.; Guo, H.; and Xiao, Y. 2026.  When Agents Evolve, Institutions Follow.  _arXiv preprint arXiv:2604.27691_. 
  * Gao et al. (2024) Gao, D.; Li, Z.; Pan, X.; Kuang, W.; Ma, Z.; Qian, B.; Wei, F.; Shen, W.; Dou, Y.; Li, W.; Ding, B.; and Zhou, J. 2024.  AgentScope: A Flexible yet Robust Multi-Agent Platform.  _arXiv preprint arXiv:2402.14034_. 
  * Grötschla et al. (2025) Grötschla, F.; Müller, L.; Tönshoff, J.; Galkin, M.; and Perozzi, B. 2025.  AgentsNet: Coordination and Collaborative Reasoning in Multi-Agent LLMs.  _arXiv preprint arXiv:2507.08616_. 
  * Guo et al. (2024) Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N. V.; Wiest, O.; and Zhang, X. 2024.  Large Language Model Based Multi-Agents: A Survey of Progress and Challenges.  In _Proceedings of IJCAI_. 
  * Hong et al. (2024) Hong, S.; Zhuge, M.; Chen, J.; Zheng, X.; Cheng, Y.; Zhang, C.; Wang, J.; Wang, Z.; Yau, S. K. S.; Lin, Z.; et al. 2024.  MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework.  In _International Conference on Learning Representations (ICLR)_. 
  * Jiang, Ren, and Lin (2023) Jiang, D.; Ren, X.; and Lin, B. Y. 2023.  LLM-Blender: Ensembling Large Language Models with Pairwise Ranking and Generative Fusion.  In _Proceedings of ACL_ , 14165–14178. 
  * Li et al. (2023) Li, G.; Hammoud, H. A. A. K.; Itani, H.; Khizbullin, D.; and Ghanem, B. 2023.  CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society.  In _Advances in Neural Information Processing Systems (NeurIPS)_ , volume 36, 51991–52008. 
  * Li et al. (2010) Li, L.; Chu, W.; Langford, J.; and Schapire, R. E. 2010.  A Contextual-Bandit Approach to Personalized News Article Recommendation.  In _Proceedings of WWW_ , 661–670. 
  * Liu et al. (2024) Liu, Z.; Zhang, Y.; Li, P.; Liu, Y.; and Yang, D. 2024.  A Dynamic LLM-Powered Agent Network for Task-Oriented Agent Collaboration.  In _Proceedings of COLM_. 
  * Mintzberg (1979) Mintzberg, H. 1979.  _The Structuring of Organizations: A Synthesis of the Research_.  Englewood Cliffs, NJ: Prentice-Hall. 
  * Ong et al. (2025) Ong, I.; Almahairi, A.; Wu, V.; Chiang, W.-L.; Wu, T.; Gonzalez, J. E.; Kadous, M. W.; and Stoica, I. 2025.  RouteLLM: Learning to Route LLMs from Preference Data.  In _The Thirteenth International Conference on Learning Representations (ICLR)_. 
  * Poon et al. (2026) Poon, M.; Dai, X.; Liu, X.; Kong, F.; Lui, J. C.; and Zuo, J. 2026.  Online Multi-LLM Selection via Contextual Bandits under Unstructured Context Evolution.  In _Proceedings of the 40th AAAI Conference on Artificial Intelligence_ , volume 40, 24855–24863. 
  * Qian et al. (2024) Qian, C.; Liu, W.; Liu, H.; Chen, N.; Dang, Y.; Li, J.; Yang, C.; Chen, W.; Su, Y.; Cong, X.; Xu, J.; Li, D.; Liu, Z.; and Sun, M. 2024.  ChatDev: Communicative Agents for Software Development.  In _Proceedings of ACL_ , 15174–15186. 
  * Shinn et al. (2023) Shinn, N.; Cassano, F.; Berman, E.; Gopinath, A.; Narasimhan, K.; and Yao, S. 2023.  Reflexion: Language Agents with Verbal Reinforcement Learning.  In _Advances in Neural Information Processing Systems (NeurIPS)_ , volume 36, 8634–8652. 
  * Shnitzer et al. (2024) Shnitzer, T.; Ou, A.; Silva, M.; Soule, K.; Sun, Y.; Solomon, J.; Thompson, N.; and Yurochkin, M. 2024.  Large Language Model Routing with Benchmark Datasets.  In _Proceedings of COLM_. 
  * Wang et al. (2025) Wang, J.; Wang, J.; Athiwaratkun, B.; Zhang, C.; and Zou, J. 2025.  Mixture-of-Agents Enhances Large Language Model Capabilities.  In _The Thirteenth International Conference on Learning Representations (ICLR)_. 
  * Wang et al. (2023a) Wang, L.; Xu, W.; Lan, Y.; Hu, Z.; Lan, Y.; Lee, R. K.-W.; and Lim, E.-P. 2023a.  Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models.  In _Proceedings of ACL_ , 2609–2634. 
  * Wang et al. (2023b) Wang, X.; Wei, J.; Schuurmans, D.; Le, Q.; Chi, E.; Narang, S.; Chowdhery, A.; and Zhou, D. 2023b.  Self-Consistency Improves Chain of Thought Reasoning in Language Models.  In _International Conference on Learning Representations (ICLR)_. 
  * Wu et al. (2024) Wu, Q.; Bansal, G.; Zhang, J.; Wu, Y.; Li, B.; Zhu, E.; Jiang, L.; Zhang, X.; Zhang, S.; Liu, J.; Awadallah, A. H.; White, R. W.; Burger, D.; and Wang, C. 2024.  AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.  In _Proceedings of COLM_. 
  * Yao et al. (2023) Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; and Cao, Y. 2023.  ReAct: Synergizing Reasoning and Acting in Language Models.  In _International Conference on Learning Representations (ICLR)_. 
  * Zheng et al. (2024) Zheng, M.; Pei, J.; Logeswaran, L.; Lee, M.; and Jurgens, D. 2024.  When “A Helpful Assistant” Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models.  In _Findings of the Association for Computational Linguistics: EMNLP 2024_ , 15126–15154. 
  * Zhu et al. (2025) Zhu, K.; Du, H.; Hong, Z.; Yang, X.; Guo, S.; Wang, Z.; Wang, Z.; Qian, C.; Tang, X.; Ji, H.; and You, J. 2025.  MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents.  In _Proceedings of ACL_. 
  * Zhuge et al. (2024) Zhuge, M.; Wang, W.; Kirsch, L.; Faccio, F.; Khizbullin, D.; and Schmidhuber, J. 2024.  GPTSwarm: Language Agents as Optimizable Graphs.  In _Proceedings of ICML_. 


