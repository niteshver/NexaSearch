arXiv is now an independent nonprofit! Learn more ×
License: arXiv.org perpetual non-exclusive license 
arXiv:2606.12109v2 [cs.RO] 28 Jul 2026
# InDex: Empowering VLA Models with Intent-Conditioned Arm–Hand Coordination for Dexterous Manipulation 
Chuanke Pang, Junyi Huang, Zhijun Zhao, Yaobing Wang, Kun Xu and Xilun Ding Kun Xu is with Faculty of Robotics Institute, Beihang University, Beijing, China. xk007@buaa.edu.cnRobotics Institute, Beihang University, Beijing, ChinaChina Academy of Space Technology, Beijing, China
###### Abstract
Pre-trained Vision-Language-Action (VLA) models provide useful semantic and spatial priors, yet their parallel-gripper action interfaces do not specify how those priors should be realized by a dexterous hand. Directly appending finger joints conflates two decisions with different structure: _when_ contact should be established and _how_ a morphology-specific hand trajectory should establish it. We introduce InDex, an intent-conditioned adaptation framework that separates these decisions without discarding full hand supervision. InDex derives a normalized grasp intent from retargeted demonstrations. A first stage predicts synchronized end-effector–intent chunks; conditioned on these predictions, VLA context, and proprioception, a diffusion decoder generates multi-joint hand actions. The scalar intent is therefore a temporal coordination interface rather than a compressed hand pose. Across four simulated tasks, three VLA backbones, and a physical arm–hand platform, InDex preserves the VLA’s reaching competence while markedly improving conversion from approach to stable grasp and task completion. Ablations isolate complementary roles: intent aligns the contact transition, whereas diffusion represents the multiple hand trajectories compatible with the same task-space plan. These results identify post-reach arm–hand coordination, rather than object localization alone, as the principal bottleneck in adapting parallel-gripper VLAs to dexterous manipulation.
##  Introduction
Vision-Language-Action (VLA) models acquire semantic and spatial priors from large robot datasets , most of which are collected with parallel grippers [ref_droid, ref_openx]. These priors remain valuable for dexterous manipulation: a VLA can interpret an instruction, localize an object, and approach it. Success after reaching, however, requires the arm and hand to coordinate contact onset, finger pre-shaping, grasp stabilization, and subsequent motion. A single parallel-jaw coordinate couples aperture and contact; a multi-finger hand instead admits many time-varying configurations for the same object and task phase.
This mismatch is structural, not merely dimensional. Appending hand joints to the end-effector (EEF) action leaves the grasp transition implicit and encourages deterministic decoders to average distinct hand trajectories. The resulting policy may reach reliably but close too early, too late, or with an incompatible hand shape. Such errors are partly hidden on Lift, where coarse localization can suffice, but compound on contact-rich, long-horizon tasks such as Nut Assembly. Dexterous transfer therefore requires both a temporal interface for _when to grasp_ and an expressive, morphology-specific model of _how to grasp_.
Figure 1: InDex augments pretrained VLA models with a grasp-intent interface that bridges parallel-gripper action priors and diffusion-based dexterous realization, enabling timing-aware, multimodal, and coordinated arm–hand manipulation.
InDex (Intent-conditioned nested Dexterous manipulation), illustrated in Fig. , makes this separation explicit. From each retargeted demonstration, it computes a normalized grasp intent \gamma\in[0,1] while retaining the complete 6-D EEF and 6-DoF hand commands. Stage 1 predicts synchronized EEF– chunks. Stage 2 uses these predictions, VLA context, and proprioception to generate the hand trajectory by conditional diffusion. Thus, aligns the contact phase without prescribing a finger configuration; the diffusion decoder realizes the many hand trajectories compatible with that intent. Sequential training first establishes task-space and intent alignment, then adapts hand control with low-rate upstream co-adaptation.
Experiments separate reaching, stable grasp, and task completion to locate where transfer succeeds or fails. Across four simulated tasks, native VLAs retain strong reaching and simple-manipulation behavior but lose trials at the reach-to-grasp transition. InDex preserves this spatial competence while substantially improving post-reach conversion, with the largest gain on Nut Assembly. Conditional-success ablations show that removing mainly impairs stable-grasp formation, whereas replacing diffusion with an MLP mainly impairs post-contact completion. Trajectory and intent visualizations further show that diverse approach modes can share a phase-consistent grasp transition. Cross-backbone and physical experiments test whether this interface extends beyond the primary simulation model and embodiment.
Our contributions are:
  1. 1.
A formulation of dexterous VLA adaptation that separates grasp-transition timing from morphology-specific hand realization while retaining full hand supervision.
  2. 2.
A sequential architecture that predicts EEF–intent chunks and generates synchronized, multimodal 6-DoF hand trajectories by conditional diffusion.
  3. 3.
Simulation, ablation, cross-backbone, and physical evidence that localizes the principal morphology-transfer gain to post-reach arm–hand coordination.


##  II Related Work
###  Dexterous Manipulation
Dexterous manipulation couples arm motion, hand morphology, and uncertain contact. Studies of integrated humanoid platforms and hand representations show that control abstractions cannot be separated from embodiment [ref_schmitz2010humanoids, ref_grothe2012humanoids, ref_tomita2012humanoids]. High-dimensional control under nonlinear contact exceeds parallel-gripper closure [ref_bai2014, ref_chen2022], while model-based and reinforcement-learning approaches must additionally address dynamics, reward design, and transfer [ref_kumar2014, ref_chen2022system, ref_zhao2020simtoreal]. InDex targets a different boundary: the interface between pretrained VLA priors and embodiment-specific joints. A low-dimensional cue represents contact progress, but the decoder retains the full hand action rather than reducing dexterity to binary open/close control.
###  Teleoperation and Imitation Learning
Teleoperation captures contact timing and finger coordination that are hard to specify analytically. Humanoid systems have studied dexterous interfaces and human-to-robot transfer [ref_to2012humanoids, ref_seo2023trill], while markerless vision reduces instrumentation [ref_anyteleop]. Deterministic cloning can average multimodal demonstrations [ref_pearce2023]; diffusion policies instead model action distributions [ref_diffusionpolicy, ref_reuss2023]. InDex conditions such a decoder on VLA features and retargeted intent, providing synchronized EEF, hand, and transition supervision without separate event annotation.
###  VLA Fine-tuning
VLA models bind visual-language context to robot actions [ref_rt2, ref_openvla, ref_pi05], but efficient fine-tuning does not define a parallel-gripper-to-hand interface. Pan et al. switch from OpenVLA arm motion to a task-specific diffusion grasp controller [ref_pan2024]. InDex instead retains a time-indexed intent condition throughout synchronized EEF–hand chunks within one policy. It is therefore a morphology-aware action interface, not a new foundation model or a trigger between separately executed controllers.
##  III Method
InDex factorizes dexterous control into a task-space transition plan and its embodiment-specific realization (Fig. ). A retargeted hand configuration yields \gamma\in[0,1] while the complete hand action remains supervised. Stage 1 predicts Cartesian EEF motion and grasp intent; Stage 2 generates the corresponding hand trajectory. Synchronized chunks preserve their temporal coupling, while sequential initialization establishes the upstream EEF–intent representation before learning downstream hand control.
Figure 2: InDex framework. Stage 1 predicts synchronized EEF motion and grasp intent. Conditioned on these predictions, VLA context, and proprioceptive history, the Stage-2 diffusion decoder generates 6-DoF hand-action chunks. The EEF and hand streams form the executed 12-D command; grasp intent is a decoder condition, not an executed action.
###  Problem Formulation
We learn an instruction-conditioned policy from demonstrations 𝒟={(,,,,)}N\mathcal{D}=\\{(\mathbf{o}_{i},\ell_{i},\mathbf{a}_{eef,i},\mathbf{a}_{hand,i},\gamma_{i})\\}_{i=1}^{N}, where \mathbf{o}_{i} contains global RGB, wrist RGB, and proprioception, and is the language instruction. Each executed command comprises a 6-D Cartesian EEF action \mathbf{a}_{eef}\in\mathbb{R}^{6} and a 6-DoF hand action \mathbf{a}_{hand}\in\mathbb{R}^{6}. The scalar , computed from the retargeted hand state in Section , conditions the decoder but is not executed. For a query at time , Stage 1 targets the synchronized sequence {(,)}\\{(\mathbf{a}_{eef,t+j},\gamma_{t+j})\\}_{j=0}^{H-1}, where each \gamma_{t+j} is computed from the demonstrated hand state at the same index. Stage 2 targets \\{\mathbf{a}_{hand,t+j}\\}_{j=0}^{H-1} using VLA context, proprioceptive history, and the Stage-1 predictions. These sequences form a 12-D chunk, whose prefix is executed before the next query. The EEF action is =[,,,,,]\mathbf{a}_{eef}=[\Delta x,\Delta y,\Delta z,\Delta r_{x},\Delta r_{y},\Delta r_{z}], with translation and axis-angle rotation increments in the robot base frame. At each index, \gamma_{t+j} specifies the intended contact progression of the corresponding EEF and hand commands, rather than an episode-level phase label. Table gives the prediction and execution horizons.
###  Task-Space Intent Realization
We derive \gamma\in[0,1] after Section retargets the human hand to robot configuration 𝐪\mathbf{q}. For the Fourier FDH-6 hand, the joint state is 𝐪=∈\mathbf{q}=[\mathbf{q}_{th}^{\top},\mathbf{q}_{f}^{\top}]^{\top}\in\mathbb{R}^{6}. Let =∈p_{th}=\operatorname{FK}_{th}(\mathbf{q})\in\mathbb{R}^{3} and =∈p_{f,i}=\operatorname{FK}_{f,i}(\mathbf{q})\in\mathbb{R}^{3} denote the thumb and opposing-finger fingertips, and let =\bar{p}_{f}=\frac{1}{4}\sum_{i=1}^{4}p_{f,i}. We define the virtual grasp aperture as  
| =,d_{v}(\mathbf{q})=\left\|p_{th}-\bar{p}_{f}\right\|_{2},  |  
| --- |  
which we normalize using task- and embodiment-specific bounds. Here, denotes the embodiment and the task.  
| γ=⁡(−−).\gamma=\operatorname{clip}_{[0,1]}\left(\frac{d_{\max}^{(e,\tau)}-d_{v}(\mathbf{q})}{d_{\max}^{(e,\tau)}-d_{\min}^{(e,\tau)}}\right).  |  
| --- |  
Thus, and denote task-specific open and closed references. The Inspire-Robots hand uses its own kinematics and bounds; therefore standardizes progress only within each calibrated setting. The decoder still outputs all six hand DoFs from VLA context, proprioception, EEF action, and . The cue consequently transfers the parallel-jaw notion of aperture without asserting a one-to-one mapping between gripper width and dexterous pose. Multiple hand configurations can share the same ; object context and proprioception disambiguate their finger-level realization. This many-to-one construction is deliberate: it exposes grasp progress while leaving contact geometry to the 6-DoF decoder.
###  Macro-Reaching Alignment and Intent Prediction
We build the macro-reaching and intent-prediction module on the \pi_{0.5} architecture, which pairs a VLM with a conditioned Action Expert for trajectory generation. The module retains the Cartesian EEF output and repurposes the parallel-jaw coordinate to predict . It therefore outputs (\hat{\mathbf{a}}_{eef},\hat{\gamma}), rather than a coarse hand configuration. The target \gamma^{*} is computed from the demonstrated hand configuration using Section . This preserves the backbone’s native separation between Cartesian motion and a gripper-like coordinate, but gives that coordinate an embodiment-calibrated target. The Stage-1 role is consequently limited to semantic approach and transition alignment; it is not trained to regress the dexterous joints.
We apply LoRA to the Action Expert and the staged VLM schedule in Table . Unlike the Native baseline’s 12-D flow-matching objective, Stage 1 separately supervises EEF translation 𝐩\mathbf{p}, rotation 𝐫\mathbf{r}, and grasp intent:  
| \displaystyle\mathcal{L}_{\mathrm{stage1}}={}  | ++​,\displaystyle\lambda_{pos}\mathcal{L}_{pos}+\lambda_{rot}\mathcal{L}_{rot}+\lambda_{intent}\mathcal{L}_{intent},  |  
| --- | --- |  
| \displaystyle\mathcal{L}_{pos}={}  | \displaystyle\mathbb{E}\\!\left[\left\|\mathbf{p}^{*}-\hat{\mathbf{p}}\right\|_{2}^{2}\right],  |  
| \displaystyle\mathcal{L}_{rot}={}  | \displaystyle\mathbb{E}\\!\left[\left\|\mathbf{r}^{*}-\hat{\mathbf{r}}\right\|_{2}^{2}\right],  |  
| \displaystyle\mathcal{L}_{intent}={}  | ​[BCElogit​].\displaystyle\mathbb{E}\\!\left[\mathrm{BCE}_{\mathrm{logit}}(\hat{s}_{\gamma},\gamma^{*})\right].  |  
Here, =\mathbf{a}_{eef}=[\mathbf{p}^{\top},\mathbf{r}^{\top}]^{\top}, denotes a target, and =sigmoid⁡\hat{\gamma}=\operatorname{sigmoid}(\hat{s}_{\gamma}). BCElogit\mathrm{BCE}_{\mathrm{logit}} supports continuous \gamma^{*}\in[0,1]. We set (,,)=(\lambda_{pos},\lambda_{rot},\lambda_{intent})=(500,10,1).
###  Intent-Conditioned Dexterous Adaptation
Stage 2 starts from the final Stage-1 checkpoint. The diffusion decoder is the primary trainable module, while the VLM and Action Expert remain in the graph at the lower learning rate in Table . The sequential initialization limits disruption of the learned EEF–intent alignment while still allowing low-rate co-adaptation; the upstream modules are not frozen.
The execution module is a conditional denoising diffusion model that synthesizes multi-joint hand-action sequences \mathbf{a}_{hand}. For compactness, let 𝐜=[,,,]\mathbf{c}=[\mathbf{z}_{VLA},\mathbf{q}_{hist},\hat{\mathbf{a}}_{eef},\hat{\gamma}] collect visual-language context, proprioceptive history, and the synchronized Stage-1 prediction sequences. Starting from ∼\mathbf{a}_{hand}^{K}\sim\mathcal{N}(0,I), a network \epsilon_{\theta} iteratively refines the sequence.  
| \displaystyle\mathbf{a}_{hand}^{k-1}={}  | ​[−​​(,𝐜,k)]\displaystyle\alpha_{k}\left[\mathbf{a}_{hand}^{k}-\eta_{k}\,\epsilon_{\theta}(\mathbf{a}_{hand}^{k},\mathbf{c},k)\right]  |  
| --- | --- |  
| \displaystyle+\sigma_{k}\boldsymbol{\xi}^{k},  |  
| \displaystyle\boldsymbol{\xi}^{k}\sim{}  | \displaystyle\mathcal{N}(0,I).  |  
where \alpha_{k}, , and \sigma_{k} define the variance schedule. The decoder is trained with the standard noise-prediction objective.  
| \displaystyle\tilde{\mathbf{a}}_{hand}^{k}={}  | +,\displaystyle\sqrt{\bar{\alpha}_{k}}\,\mathbf{a}_{hand}^{0}+\sqrt{1-\bar{\alpha}_{k}}\,\boldsymbol{\epsilon}^{k},  |  
| --- | --- |  
| \displaystyle\mathcal{L}_{\mathrm{diff}}={}  | ​[‖−​(,𝐜,k)‖22].\displaystyle\mathbb{E}_{k,\boldsymbol{\epsilon}^{k}}\\!\left[\left\|\boldsymbol{\epsilon}^{k}-\epsilon_{\theta}(\tilde{\mathbf{a}}_{hand}^{k},\mathbf{c},k)\right\|_{2}^{2}\right].  |  
The loss reaches the upstream modules through the predicted conditions at their lower learning rate. Training and deployment use the same prediction path; neither \hat{\mathbf{a}}_{eef} nor \hat{\gamma} is replaced by an oracle target. Diffusion can therefore sample distinct hand trajectories for the same context, while \hat{\gamma} aligns their state transitions with the EEF plan.
##  IV Data and Platforms
Operator measurements are first retargeted to each robot’s 6-DoF hand space; Section then computes aperture and . Each sample stores global and wrist RGB, proprioception, the 12-D action, and the auxiliary cue. Embodiment-specific kinematics thus determine both the supervised hand command and its intent condition.
###  Unified Vision-Based Teleoperation
An Intel RealSense D435i and AnyTeleop [ref_anyteleop] estimate hand keypoints, finger joints, wrist position, and orientation, then retarget them subject to joint and smoothness constraints. Relative wrist motion maps \mathbf{w}_{t}\in\mathbb{R}^{3} to EEF velocity =\dot{\mathbf{p}}_{eef}=\mathbf{K}(\mathbf{w}_{t}-\mathbf{w}_{t-1}), while wrist orientation maps as =​​\mathbf{R}_{eef}=\mathbf{R}_{cam}^{base}\mathbf{R}_{hand}\mathbf{R}_{align}. Here, \mathbf{R}_{cam}^{base} is the camera-to-base extrinsic and \mathbf{R}_{align} compensates for anatomical and mechanical axes. The operator-side D435i is distinct from the policy cameras. Retargeting produces 𝐪\mathbf{q} and \mathbf{a}_{hand}, then Section computes . Observations, arm motion, hand motion, and intent are timestamped together so the action chunks retain the transition timing demonstrated by the operator.
###  Simulation Platform and Corpus
Simulation uses robosuite [ref_robosuite], a fixed-base Fourier GR-1 upper body, and an FDH-6 hand. At 30 Hz, it records global and wrist RGB, proprioception, 12-D EEF–hand actions, and in HDF5. We collect 100 successful teleoperated episodes per task. Training and evaluation use this same embodiment and observation interface; evaluation varies task initial states rather than transferring simulator coordinates to hardware.
###  Simulation Tasks
We adapt four robosuite tasks to the Fourier arm–hand system: Lift raises a cube, Stack places one cube on another, Pick & Place transfers an object to its bin, and Nut Assembly seats a round nut on its peg. Success follows the corresponding official benchmark criterion.
###  Physical Platform and Corpus
The physical platform combines a Rokae xMate ER3 Pro arm and Inspire-Robots hand (Fig. , left). The D435i–AnyTeleop front end is unchanged, while workspace, EEF, retargeting, and aperture calibration are fitted to this embodiment. The policy again receives global RGB, wrist RGB, and proprioception. Recalibration changes the physical meaning of the hand joints and aperture bounds but leaves the learned EEF–intent–hand interface unchanged.
The corpus covers Pick & Place and Block Fit; the latter aligns, inserts, and extracts an interlocking block within one trial. Each task uses 50 successful demonstrations, and policies are trained on these hardware data rather than transferred zero-shot. A 1 kHz controller tracks the set-points selected from each action chunk.
##  Experiments
We compare simulation policies, ablate components, test backbone compatibility, and separately evaluate a second physical embodiment.
###  Evaluation Protocol
Baselines and controls. We compare BC-RNN [ref_mandlekar2021], ACT [ref_zhao2023], DP [ref_diffusionpolicy], OpenVLA [ref_openvla], UniVLA [ref_univla], and \pi_{0.5} . BC-RNN, ACT, and DP use 30k updates. Native VLAs retain their released decoder families for 12-D chunks and use 12k updates. Direct Projection instead trains a three-layer, 512-unit GELU MLP on the final hidden state for 30k updates using MSE and AdamW at . Full InDex follows Table .
Controls. Methods share observations, demonstrations, 12-D targets, and test episodes. Update budgets are not compute matched.
Metrics. SR_{\text{reach}} requires the EEF to enter a 3-cm sphere around the object; SR_{\text{grasp}} requires a secure hold for 30 simulator steps (1 s); and SR_{\text{task}} follows Section . Each final checkpoint is evaluated for 100 episodes per task, which serve as the denominator for all three rates. Pooled rates, conditional probabilities, and differences are computed from integer counts before being rounded once to one decimal place.
TABLE I: InDex interface and training configuration.  
 |  
|  |  
|  Global/wrist RGB + proprio.  |  
|   |  6-D EEF + 6-DoF hand  |  
|  Auxiliary condition  |  Computed scalar   |  
 |  
|  Reported checkpoint  |  Stage-2 final (60k)  |  
|   |  
|  Frozen: 0–5k; unfrozen: 5k–60k  |  
|  Trainable-module LR  |  (VLM after 5k)  |  
|   |  
|   |  
|  Diffusion optimizer  |  
|  Decoder learning rate  |  
|  VLM + Action Expert LR  |  
|  Prediction horizon  |  
|  Observation history  |  
|  Executed actions/query  |  
|  Inference denoising steps  |  
|  Training/inference GPUs  |   |  
###  Simulation Evaluation
####  Main Multi-Task Performance
Fig. shows representative successful InDex executions, while Fig. relates sampled task-space motion to grasp-intent evolution. For the latter, we execute 50 stochastic rollouts from a common nominal initialization for each visualized task and segment every trajectory into approach, grasp, and manipulation phases. One rollout is highlighted; the remaining trajectories are rendered translucently to expose the conditional spread. Grasp intent is recorded at each policy query and aligned with the same phase boundaries.
Figure 3: Representative successful InDex rollouts in simulation. Time proceeds from left to right; rows correspond to Lift, Stack, Pick & Place, and Nut Assembly. Figure 4: Task-space trajectories and grasp-intent evolution. (a) Lift and (b) Pick & Place task-space rollouts; translucent paths summarize 50 stochastic rollouts and the solid path highlights one execution. (c) Lift intent during approach, grasp, and elevation. (d) Pick & Place intent during approach, grasp, transfer, and release.
Table reports cumulative success. Without a VLA, BC-RNN, ACT, and DP obtain 8.5%, 34.5%, and 42.8% average task success. Action chunking and diffusion improve longer-horizon control, but DP still loses 21.8 points from reach to completion. Native VLAs show the opposite strength: their semantic priors support reaching and Lift, whereas the gap widens on Nut Assembly. Native \pi_{0.5} loses 20.0 points between reach and stable grasp, localizing its principal failure after object localization but before reliable contact.
TABLE II: Cumulative simulation success (%). Entries report SR_{reach} / SR_{grasp} / SR_{task}.  
 |  
|  |  
| 48.0 / 31.0 / 24.0  | 21.0 / 5.0 / 1.0  | 33.0 / 15.0 / 9.0  | 12.0 / 3.0 / 0.0  | 28.5 / 13.5 / 8.5  |  
| 78.0 / 65.0 / 61.0  | 53.0 / 33.0 / 27.0  | 65.0 / 45.0 / 41.0  | 35.0 / 15.0 / 9.0  | 57.8 / 39.5 / 34.5  |  
| 83.0 / 73.0 / 68.0  | 59.0 / 43.0 / 37.0  | 71.0 / 55.0 / 51.0  | 45.0 / 21.0 / 15.0  | 64.5 / 48.0 / 42.8  |  
| OpenVLA (Native)  | 85.0 / 69.0 / 63.0  | 41.0 / 23.0 / 17.0  | 59.0 / 41.0 / 34.0  | 46.0 / 19.0 / 13.0  | 57.8 / 38.0 / 31.8  |  
| UniVLA (Native)  | 87.0 / 75.0 / 69.0  | 47.0 / 29.0 / 23.0  | 65.0 / 49.0 / 42.0  | 51.0 / 21.0 / 17.0  | 62.5 / 43.5 / 37.8  |  
|  \pi_{0.5} (Native)  | 93.0 / 81.0 / 76.0  | 71.0 / 47.0 / 43.0  | 83.0 / 61.0 / 57.0  | 57.0 / 35.0 / 25.0  | 76.0 / 56.0 / 50.3  |  
|  \pi_{0.5}+InDex (Full)  | 98.0 / 97.0 / 95.0  | 91.0 / 86.0 / 83.0  | 95.0 / 91.0 / 89.0  | 87.0 / 79.0 / 76.0  | 92.8 / 88.3 / 85.8  |  
Figure 5: Pooled reach–grasp–task conversion. Cumulative success for native \pi_{0.5} and full InDex is shown together with P(G\mid R) and P(T\mid G), identifying the stage at which each policy loses successful trials.
For Fig. , integer counts are pooled over four 100-episode tasks before computing P(G\mid R)=N_{G}/N_{R} and P(T\mid G)=N_{T}/N_{G}. InDex improves reach from 76.0% to 92.8% and the two conditional rates from 73.7% to 95.1% and 89.7% to 97.2%. It improves Lift, Stack, Pick & Place, and Nut Assembly task success by 19, 40, 32, and 51 points. The increasing gain with contact complexity localizes the benefit to stable contact and compatible hand shape rather than localization alone.
Fig. provides the corresponding qualitative view. The trajectory samples preserve the multimodality of approach and transfer, while their intent traces remain aligned with manipulation phase. For Lift, rises near contact and remains closed during elevation; for Pick & Place, it rises for transport and falls at release. Thus, does not select a geometric path or encode a hand pose. It supplies a shared temporal reference under which the diffusion decoder can realize different finger trajectories. This coordination between grasp timing and hand shape is the key distinction from direct joint concatenation.
####  Ablation Study
Table separates interface, training order, and hand decoder. Vision-only removes the VLA-derived intent pathway; removes only the scalar prediction and condition; Coupled-12k omits Stage-1 initialization; and MLP Hand replaces diffusion with a 256–512–1024–512–256 MLP. Conditional rates locate each component’s effect within the execution funnel.
TABLE III: Simulation ablations and stage conversion (%).  
| Task Success (%)  | Conditional (%)  |  
| --- | --- |  
|   |   |  
|   |  
 |  
|  InDex: Vision-only  |  
|  InDex: Coupled-12k  |  
|   |  
|   |  
 |  
, and  denote reach, stable grasp, and task completion; P(G\mid R) and P(T\mid G) are pooled conditional success rates.
Direct Projection and Vision-only reach only 4.0% and 17.0% average success; neither high-dimensional projection nor a hand generator without transition context is sufficient. Coupled-12k reaches 21.5%, although its changed initialization, rates, and budget prevent isolating training order.
The two targeted controls expose complementary failure modes. Without , diffusion retains diverse hand generation but converts only 75.6% of reaches into stable grasps, versus 95.1% for Full; its degradation is largest on Nut Assembly, where closure timing is least forgiving. MLP Hand retains intent and converts 82.0% of reaches, but completes only 65.1% of stable grasps, versus 97.2% for Full. A scalar cue can align contact onset but cannot specify the multi-joint shape required after contact, while an expressive decoder without the cue lacks a reliable temporal reference. Their combination is therefore necessary: answers _when_ , and conditional diffusion realizes _how_.
To test synchronization, Fig. uses 50 Lift rollouts each for Full and w/o at 30 Hz, aligned to first contact (). Point-connected traces show one rollout; thick curves are five-sample Gaussian-smoothed means, and bands denote smoothed standard deviations.
Figure 6: Contact-aligned Lift coordination. Across 50 rollouts, time zero denotes first contact. Curves show smoothed means, bands show smoothed standard deviations, and point-connected traces show one rollout.
Full increases during late approach and maintains it through grasp and elevation. The hand closes before and accumulates contacts afterward; w/o approaches similarly but closes later and establishes fewer contacts. This attributes the reach-to-grasp gap to contact–hand synchronization rather than localization.
For Fig. , we shift by {,,…,12}\\{-12,-9,\ldots,12\\} control steps without changing EEF predictions. Each task and offset uses the same 50 initial conditions; at 30 Hz, adjacent offsets differ by 0.1 s and zero denotes the unmodified policy.
Figure 7: Grasp-intent timing intervention. Negative offsets advance and positive offsets delay while EEF predictions remain unchanged. Each point reports success over 50 trials.
Success peaks near zero shift, showing that intent must be aligned rather than merely large. Lift has the broadest tolerance; Stack and Pick & Place degrade faster, and Nut Assembly is most sensitive, particularly to delay.
Figure 8: Qualitative InDex failure and recovery rollouts. Time proceeds from left to right. Top: a Nut Assembly failure after reaching. Bottom: closed-loop Pick & Place recovery from an initially tilted object. Figure 9: Physical platform and representative successful executions. Left: the Rokae xMate ER3 Pro–Inspire-Robots platform. Right: Pick & Place and Block Fit executions, with time proceeding from left to right.
####  Failure and Recovery Analysis
In Nut Assembly, the arm may hover after reaching the socket; in Pick & Place, subsequent closed-loop chunks can correct an initially tilted can (Fig. ). These examples are qualitative diagnostics, not evidence of explicit replanning or force-feedback robustness.
####  Cross-Backbone Evaluation
We instantiate InDex with OpenVLA, UniVLA, and \pi_{0.5} (Table ). Within a backbone, variants share the checkpoint and protocol; the Stage-2 hand decoder is common. Direct Projection reaches only 2.5–4.0% average success, whereas InDex improves the respective Native models by 14.5, 14.8, and 35.5 points. The consistent gain supports compatibility across action representations. Its unequal magnitude, together with non-compute-matched decoder recipes, does not support a stronger claim of backbone invariance.
TABLE IV: Cross-backbone simulation task-success rates (%).  
| Task Success (%)  |  
| --- |  
|  OpenVLA (Direct Proj.)  |  
|   |  
|   |  
|  UniVLA (Direct Proj.)  |  
|   |  
 |  
|  \pi_{0.5} (Direct Proj.)  |  
|   |  
|  \pi_{0.5} + InDex (Full)  |  
###  Physical-Robot Evaluation
We evaluate DP and the Native and InDex variants of UniVLA and \pi_{0.5} on the Rokae–Inspire platform. Policies share 50 demonstrations, observations, 12-D actions, test initializations, and 50 trials per task. Table reports final-checkpoint success, and Fig. shows the platform and representative executions.
TABLE V: Physical task success (50 trials per task).  
| Successful Trials  |  
| --- |  
 |  
 |  
|   |  
 |  
|  \pi_{0.5} (Native)  |  
|   |  
The ordering matches simulation. InDex improves UniVLA from 54.0% to 70.0% and \pi_{0.5} from 71.0% to 83.0%, with six additional successes per task for the latter. Block Fit remains harder because it requires tighter alignment and sustained contact. Because all policies train on physical demonstrations, this experiment evaluates embodiment deployment rather than zero-shot sim-to-real transfer.
###  Discussion and Limitations
Simulation and separately trained hardware policies test architecture and deployment, respectively; their results are not pooled, and two physical tasks do not establish broad embodiment generalization. Moreover, encodes calibrated aperture progress rather than arbitrary manipulation phase. In-hand rotation, finger gaiting, and independent contacts may require richer intent. Without tactile or force feedback, recovery is also limited to errors observable through subsequent visual and proprioceptive queries.
##  VI Conclusion
InDex treats dexterous VLA adaptation as a coordination problem rather than an increase in action dimension. Aperture-derived intent provides a temporal reference for contact, while conditional diffusion preserves the full, multimodal hand trajectory. The reach–grasp–task funnel and targeted ablations show that these roles are complementary: intent improves the transition into stable contact, and expressive hand generation sustains a compatible grasp afterward. InDex consequently preserves the spatial priors of native VLAs while improving post-reach execution across simulation backbones and a physical arm–hand platform. The broader implication is that morphology transfer requires an interface between semantic task progress and embodiment-specific control. Extending this interface beyond aperture-dominated transitions will require richer intent representations, additional embodiments, and tactile feedback.
## References
