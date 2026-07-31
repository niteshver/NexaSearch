arXiv is now an independent nonprofit! Learn more ×
License: arXiv.org perpetual non-exclusive license 
arXiv:2607.24983v1 [cs.LG] 27 Jul 2026
# Generative Distributionally Robust Optimization
Jonathan Yu-Meng Li1 zzhan073@uottawa.ca jonathan.li@telfer.uottawa.ca 1Telfer School of Management, University of Ottawa 2Department of Electrical and Computer Engineering, Western University 
(July 27, 2026)
###### Abstract
Generative models are increasingly adopted in distributionally robust optimization (DRO), but existing approaches trade off model compatibility and adversarial structure: methods that accept arbitrary samplers do not restrict worst-case laws to a generator family, while generator-parameterized adversaries rely on model-specific access such as likelihoods, scores, or training data. We propose Generative Distributionally Robust Optimization (GDRO), a principled framework that accepts any sampleable conditional generator as the nominal model and restricts worst-case laws to a chosen conditional generator family. The key is the sampler–Sinkhorn pairing: samplers represent the conditional laws exactly, while Sinkhorn divergence compares their induced distributions without likelihood access and can be estimated from samples alone. The resulting population problem admits a direct finite-sample approximation and differentiable primal–dual implementation at the active decision context. For Lipschitz losses, the population Sinkhorn radius bounds downstream degradation. Across explicit and implicit generators, our method reduces rare-context inventory regret by 60% and SocialGAN navigation collisions by 50% relative to nominal decisions.
##  Introduction
Conditional generative models increasingly provide the predictive distributions used in downstream optimization. Given a current context , a pretrained model generates demand scenarios, trajectories, or other uncertain outcomes, and an optimizer chooses a decision from those samples. This interface is attractive because it accommodates rich, high-dimensional uncertainty, but it also passes any misspecification of the generator directly into the decision. The practical question is therefore not only how to generate realistic conditional outcomes, but how to robustify a downstream decision when the available generative model may be wrong.
Distributionally robust optimization (DRO) addresses model misspecification by optimizing against nearby alternative distributions (Mohajerin Esfahani and Kuhn, 2018; Rahimian and Mehrotra, 2022; Kuhn et al., 2024). Existing approaches, however, face a tradeoff between _model compatibility_ and _adversarial structure_. A predict-then-robustify approach samples any conditional generator at the active decision context and places a Wasserstein or Sinkhorn ambiguity set around the resulting nominal law (Mohajerin Esfahani and Kuhn, 2018; Wang et al., 2025b). It is likelihood-free and applies directly at the context where the decision is made; however, its adversary ranges over an ambient-space transport ball and is not required to follow the generator’s learned structure. High-dimensional outcomes often concentrate near lower-dimensional structure—a central premise of modern generative modeling (Song and Ermon, 2019)—so worst-case mass may leave the dependence, dynamics, or manifold structure encoded by the generator. The transport cost supplies geometry, but it does not impose membership in the chosen generator family.
Parametric DRO methods (Michel et al., 2021, 2022) and generative ambiguity-set methods, such as DRO with Generative Ambiguity Set (GAS-DRO) (Wen and Yang, 2026) and diffusion ambiguity-set DRO (Wen and Yang, 2025), take a complementary approach by representing the adversarial distribution with a parameterized model. This preserves a chosen form of parametric or generative structure, but representative formulations certify the adversary through model-specific quantities such as likelihood ratios, scores, reconstruction objectives, or losses evaluated on training data. Consequently, their stated formulations do not directly provide a common robustification layer for arbitrary implicit, proprietary, or otherwise frozen conditional generators available only through samples. Moreover, a certificate averaged over the training distribution of contexts—reconstruction loss, for example—need not control the conditional law at the particular where a decision is being made.
To address these limitations, we develop a DRO framework that (i) accepts any sampleable pretrained conditional generator as the nominal model, (ii) restricts the worst-case law to a chosen conditional generator family, and (iii) certifies proximity between the two conditional output laws at the active context. We call the resulting ambiguity set _generator-faithful_ : every admissible worst-case law is induced by the selected adversarial generator family, rather than being an arbitrary distribution in the ambient outcome space. When the nominal architecture is available, a natural choice is to use the same generator family for both nominal and adversarial models, thereby preserving its inductive structure. More generally, the framework accommodates any black-box nominal sampler and permits the adversarial generator family to be chosen independently.
Our key observation is that the right interface is the _sampler–Sinkhorn pairing_. Every sampleable conditional generative model exposes its law operationally through a sampler, regardless of whether it has a tractable likelihood, score, or density. Sinkhorn divergence is naturally compatible with this interface: it is a transport discrepancy between probability laws, can be estimated from samples alone, and is differentiable with respect to generated outputs (Cuturi, 2013; Genevay et al., 2018; Feydy et al., 2019). It also carries decision-level meaning: under bounded output support, Sinkhorn proximity controls Wasserstein proximity, and Kantorovich–Rubinstein duality then bounds the change in expected loss uniformly over Lipschitz objectives (Theorem ). Sinkhorn divergences have previously been used to learn generative models from samples; here we use them for a different purpose—to certify and optimize a worst-case conditional generator for a downstream decision. The sampler supplies broad model compatibility, while Sinkhorn supplies a likelihood-free, output-law transport certificate and a smooth route to adversarial optimization.
#### Generative distributionally robust optimization (GDRO).
Let P_{\hat{\phi}}(\cdot\mid x) denote the conditional law supplied by a pretrained nominal generator and \\{Q_{\psi}(\cdot\mid x):\psi\in\Psi\\} the conditional laws induced by a chosen adversarial generator family. Given a downstream loss f:\mathcal{W}\times\mathcal{Y}\rightarrow\mathbb{R}, let S_{\varepsilon} denote the debiased Sinkhorn divergence with regularization ε\varepsilon, and let be the ambiguity radius. Our central population problem is  
| ∈​supψ∈Ψ:(,)⩽ρ​.w_{\rho,\varepsilon}^{\star}(x)\in\arg\min_{w\in\mathcal{W}}\;\sup_{\psi\in\Psi:\,S_{\varepsilon}(Q_{\psi}(\cdot\mid x),P_{\hat{\phi}}(\cdot\mid x))\leqslant\rho}\mathbb{E}_{Y\sim Q_{\psi}(\cdot\mid x)}\\!\left[f(w,Y)\right].  |  
| --- |  
The generator family determines which perturbations are structurally admissible, Sinkhorn divergence controls their displacement from the nominal conditional output law, and conditioning throughout on aligns the stress test with the decision being made. Because both laws are induced by conditional samplers and Sinkhorn divergence can be estimated from their output samples, problem () admits a likelihood-free finite-sample approximation. Section gives the exact sampler reformulation, its empirical counterpart, and the resulting optimization algorithm.
#### Relation to prior work.
The distinction above positions GDRO between classical distribution-space DRO, including -divergence, Wasserstein, and Sinkhorn formulations (Mohajerin Esfahani and Kuhn, 2018; Blanchet and Murthy, 2019; Gao and Kleywegt, 2023; Gao et al., 2024; Rahimian and Mehrotra, 2022; Wang et al., 2025b; Yang et al., 2025), and structured adversaries based on parametric likelihood ratios, diffusion ambiguity sets, or GAS-DRO (Michel et al., 2021, 2022; Wen and Yang, 2025, 2026). FlowDRO (Xu et al., 2024; Kobyzev et al., 2021) uses a normalizing flow to parameterize a distribution-space Wasserstein adversary, but the Wasserstein ball—rather than membership in a chosen generator family—still defines which perturbations are admissible. Adversarial-environment reinforcement learning (Ren and Majumdar, 2022) likewise stress-tests decisions against generated environments, but perturbs inputs to a fixed simulator. Decision-focused learning (Donti et al., 2017; Elmachtoub and Grigas, 2022; Costa and Iyengar, 2023; Wang et al., 2025a; Ma et al., 2024) trains predictive models for downstream performance, whereas our object is a post-training ambiguity set around a frozen conditional sampler. Table isolates the combination that distinguishes our formulation.
Capabilities native to representative stated formulations. ✓\checkmark: present; : variant-dependent or requiring model-specific adaptation; : absent.  
|  Arbitrary frozen  |  Generator-family  |   |   |  
| --- | --- | --- | --- |  
|  Conditional Wasserstein /  |  
|  Parametric adversary DRO (Michel et al., 2021, 2022)  |  
|  Diffusion ambiguity-set DRO / GAS-DRO (Wen and Yang, 2025, 2026)  |  
| GDRO (ours)  |  
#### Contributions.
  * •
We introduce Generative Distributionally Robust Optimization (GDRO), a context-local ambiguity framework that combines an arbitrary sampleable nominal conditional generator with a generator-faithful adversarial family. To our knowledge, this is the first context-local DRO framework to restrict worst-case laws to a chosen conditional generator family and certify them by sample-based Sinkhorn proximity to an arbitrary frozen conditional sampler (Section ).
  * •
We establish the exact sampler representation of the population problem, derive its finite-sample approximation, and develop a differentiable primal–dual implementation. For Lipschitz losses, the population Sinkhorn radius controls downstream degradation, and we analyze convergence of the resulting optimization procedure (Section ).
  * •
Across explicit and implicit generators, the resulting robust decisions reduce rare-context inventory regret by and SocialGAN navigation collisions by relative to nominal decisions (Section ).


##  Generative Distributionally Robust Optimization (GDRO)
###  2.1 Conditional Population Formulation
Let 𝒳\mathcal{X} be the context space, 𝒴\mathcal{Y} the outcome space, \mathcal{W}\subseteq\mathbb{R}^{d} the decision set, and f:\mathcal{W}\times\mathcal{Y}\to\mathbb{R} the downstream loss. We fix the active decision context x\in\mathcal{X} throughout. Write  
| :=and:=,ψ∈Ψ,P_{0}^{x}:=P_{\hat{\phi}}(\cdot\mid x)\qquad\text{and}\qquad Q_{\psi}^{x}:=Q_{\psi}(\cdot\mid x),\quad\psi\in\Psi,  |  
| --- |  
for the nominal conditional law and a conditional law in the chosen adversarial generator family, respectively.
For \varepsilon>0, probability measures on 𝒴\mathcal{Y}, and a ground cost c:\mathcal{Y}\times\mathcal{Y}\to\mathbb{R}_{+}, entropically regularized optimal transport is  
| :={∫c​​​+},\operatorname{OT}_{\varepsilon}(P,Q):=\inf_{\pi\in\Pi(P,Q)}\left\\{\int c(y,y^{\prime})\,\mathrm{d}\pi(y,y^{\prime})+\varepsilon\,\operatorname{KL}\\!\left(\pi\,\middle\|\,P\otimes Q\right)\right\\},  |  
| --- |  
where \Pi(P,Q) contains all couplings with marginals and . The debiased Sinkhorn divergence (Feydy et al., 2019) is  
| :=−−.S_{\varepsilon}(P,Q):=\operatorname{OT}_{\varepsilon}(P,Q)-\tfrac{1}{2}\operatorname{OT}_{\varepsilon}(P,P)-\tfrac{1}{2}\operatorname{OT}_{\varepsilon}(Q,Q).  |  
| --- |  
By construction, S_{\varepsilon}(P,P)=0. For boundedly supported laws on a Euclidean outcome space and the squared-Euclidean cost =c(y,y^{\prime})=\|y-y^{\prime}\|_{2}^{2}, S_{\varepsilon}(P,Q)\geqslant 0 and →S_{\varepsilon}(P,Q)\to W_{2}^{2}(P,Q) as \varepsilon\downarrow 0 (Feydy et al., 2019; Peyré and Cuturi, 2019).
For an ambiguity radius \rho\geqslant 0, the conditional population problem is  
| :=sup​.V_{\rho,\varepsilon}(x):=\inf_{w\in\mathcal{W}}\sup_{\begin{subarray}{c}\psi\in\Psi:\\\ S_{\varepsilon}(Q_{\psi}^{x},P_{0}^{x})\leqslant\rho\end{subarray}}\mathbb{E}_{Y\sim Q_{\psi}^{x}}[f(w,Y)].  |  
| --- |  
The feasible laws in () are _generator-faithful_ : every one is induced by the selected conditional generator family. The natural choice, when the nominal architecture is available, is to use the same conditional architecture for the adversary and include the nominal parameter in ; then the ambiguity set is nonempty for every \rho\geqslant 0. A different adversarial family is also permitted, provided it contains at least one conditional law within radius of P_{0}^{x}.
###  2.2 Sampler Representation and Empirical Approximation
Let the nominal and adversarial conditional samplers be  
| ::.G_{\hat{\phi}}:\mathcal{Z}_{0}\times\mathcal{X}\to\mathcal{Y},\quad Z_{0}\sim\zeta_{0},\qquad G_{\psi}:\mathcal{Z}_{\mathrm{A}}\times\mathcal{X}\to\mathcal{Y},\quad Z_{\mathrm{A}}\sim\zeta_{\mathrm{A}}.  |  
| --- |  
Their conditional output laws are the pushforwards  
| =​,=.P_{0}^{x}=\bigl(G_{\hat{\phi}}(\cdot,x)\bigr)_{\\#}\zeta_{0},\qquad Q_{\psi}^{x}=\bigl(G_{\psi}(\cdot,x)\bigr)_{\\#}\zeta_{\mathrm{A}}.  |  
| --- |  
In the natural same-architecture case, the samplers may share the same latent space and base law. The notation in () also covers a black-box nominal sampler and a separately chosen adversarial family.
Substituting () into () gives the exact sampler representation  
| =sup​(,​)⩽ρ​[​].V_{\rho,\varepsilon}(x)=\inf_{w\in\mathcal{W}}\sup_{\begin{subarray}{c}\psi\in\Psi:\\\ S_{\varepsilon}((G_{\psi}(\cdot,x))_{\\#}\zeta_{\mathrm{A}},(G_{\hat{\phi}}(\cdot,x))_{\\#}\zeta_{0})\leqslant\rho\end{subarray}}\mathbb{E}_{Z_{\mathrm{A}}\sim\zeta_{\mathrm{A}}}\\!\left[f\\!\left(w,G_{\psi}(Z_{\mathrm{A}},x)\right)\right].  |  
| --- |  
Because the Sinkhorn constraint compares the induced output laws, this representation requires no likelihoods, scores, or pointwise pairing of generated outputs.
To obtain the finite-sample problem, draw  
| ,,.Y_{0,i}\stackrel{{\scriptstyle\mathrm{iid}}}{{\sim}}P_{0}^{x},\qquad Z_{{\mathrm{A}},i}\stackrel{{\scriptstyle\mathrm{iid}}}{{\sim}}\zeta_{\mathrm{A}},\quad i=1,\dots,M.  |  
| --- |  
They define the empirical conditional output laws  
| :=,:=​.\widehat{P}_{G_{\hat{\phi}},x}:=\frac{1}{M}\sum_{i=1}^{M}\delta_{Y_{0,i}},\qquad\widehat{P}_{G_{\psi},x}:=\frac{1}{M}\sum_{i=1}^{M}\delta_{G_{\psi}(Z_{{\mathrm{A}},i},x)}.  |  
| --- |  
The nominal and adversarial batches may be drawn independently. The adversarial latent draws are held fixed across during the sample-average optimization.
For empirical measures \alpha=M^{-1}\sum_{i}\delta_{a_{i}} and \beta=M^{-1}\sum_{j}\delta_{b_{j}}, let  
| :={:,}.\Pi_{M}:=\left\\{\pi\in\mathbb{R}_{+}^{M\times M}:\pi\mathbf{1}_{M}=M^{-1}\mathbf{1}_{M},\;\pi^{\top}\mathbf{1}_{M}=M^{-1}\mathbf{1}_{M}\right\\}.  |  
| --- |  
The empirical regularized transport term is  
| =⁡{+ε​​},\operatorname{OT}_{\varepsilon}(\alpha,\beta)=\min_{\pi\in\Pi_{M}}\left\\{\sum_{i,j=1}^{M}\pi_{ij}c(a_{i},b_{j})+\varepsilon\sum_{i,j=1}^{M}\pi_{ij}\log(M^{2}\pi_{ij})\right\\},  |  
| --- |  
with the convention 0\log 0=0. The two empirical self-transport terms in () are computed analogously. Since \sum_{i,j}\pi_{ij}=1, the regularizer in () equals ε​+\varepsilon\sum_{i,j}\pi_{ij}\log\pi_{ij}+2\varepsilon\log M. The additive constant appears in each of the three transport terms in () and therefore cancels from S_{\varepsilon}. Hence the empirical Sinkhorn divergence is unchanged under the common entropy convention ε​\varepsilon\sum_{i,j}\pi_{ij}\log\pi_{ij}.
The empirical objective is  
| :=​​(w,),\widehat{F}_{M}(w,\psi):=\frac{1}{M}\sum_{i=1}^{M}f\\!\left(w,G_{\psi}(Z_{{\mathrm{A}},i},x)\right),  |  
| --- |  
and the finite-sample GDRO problem is  
| :=sup​(,)⩽ρ.\widehat{V}_{M}(x):=\inf_{w\in\mathcal{W}}\sup_{\begin{subarray}{c}\psi\in\Psi:\\\ S_{\varepsilon}(\widehat{P}_{G_{\psi},x},\widehat{P}_{G_{\hat{\phi}},x})\leqslant\rho\end{subarray}}\widehat{F}_{M}(w,\psi).  |  
| --- |  
###  2.3 Primal–Dual Optimization
For fixed , set  
| :=​(,).\widehat{s}(\psi):=S_{\varepsilon}(\widehat{P}_{G_{\psi},x},\widehat{P}_{G_{\hat{\phi}},x}).  |  
| --- |  
The empirical inner problem is  
| subject to⩽ρ.\sup_{\psi\in\Psi}\widehat{F}_{M}(w,\psi)\quad\text{subject to}\quad\widehat{s}(\psi)\leqslant\rho.  |  
| --- |  
For a nonlinear generator this problem is generally nonconcave and its feasible set has no closed-form projection. Its Lagrangian is  
| :=−,.\widehat{\mathcal{L}}(w,\psi,\mu):=\widehat{F}_{M}(w,\psi)-\mu\bigl(\widehat{s}(\psi)-\rho\bigr),\qquad\mu\geqslant 0.  |  
| --- |  
The associated dual problem minimizes over \mu\geqslant 0 after maximizing over . Accordingly, we ascend in and use projected dual descent,  
| ,μ←[μ+]+.\psi\leftarrow\psi+\eta_{\psi}\nabla_{\psi}\widehat{\mathcal{L}},\qquad\mu\leftarrow\left[\mu+\eta_{\mu}\bigl(\widehat{s}(\psi)-\rho\bigr)\right]_{+}.  |  
| --- |  
The multiplier increases when \widehat{s}(\psi)>\rho and decreases otherwise. In computing \nabla_{\psi}\widehat{s}(\psi), the nominal samples are fixed; only the adversarial samples G_{\psi}(Z_{{\mathrm{A}},i},x) depend on . For \varepsilon>0 and a smooth ground cost, the empirical Sinkhorn divergence is differentiable in these generated samples, so the chain rule propagates the gradient through .
Primal–Dual GDRO
Context ; nominal sampling oracle Y\sim P_{0}(\cdot\mid x); adversarial sampler ; radius ; batch size ; step sizes \eta_{\psi},\eta_{\mu},\eta_{w}; iteration counts . 
Draw the nominal and adversarial batches in (); form \widehat{P}_{G_{\hat{\phi}},x}. 
Initialize w\in\mathcal{W}, \psi\in\Psi, and choose \mu^{(1)}>0. 
for t=1,\dots,T do
w^{(t)}\leftarrow w; \mu\leftarrow\mu^{(1)}. 
for k=1,\dots,K do
for j=1,\dots,J do
Form \widehat{P}_{G_{\psi},x} from the fixed adversarial latent draws. 
ψ←ψ+​​\psi\leftarrow\psi+\eta_{\psi}\nabla_{\psi}\widehat{\mathcal{L}}(w,\psi,\mu). 
Set \psi_{k}\leftarrow\psi and evaluate \widehat{s}(\psi_{k}). 
μ←[μ+]+\mu\leftarrow[\mu+\eta_{\mu}(\widehat{s}(\psi_{k})-\rho)]_{+}. 
←\widehat{g}_{k}\leftarrow\nabla_{w}\widehat{F}_{M}(w,\psi_{k}). 
w←​(w−​​)w\leftarrow\Pi_{\mathcal{W}}\\!\left(w-\eta_{w}K^{-1}\sum_{k=1}^{K}\widehat{g}_{k}\right). 
return =\overline{w}=T^{-1}\sum_{t=1}^{T}w^{(t)}. 
#### Model access and scope.
Algorithm queries the nominal conditional model only for output samples, which may be cached; it requires no likelihood, score, or gradient access to that model and therefore accommodates implicit or non-differentiable nominal generators. The gradient implementation does require an optimizable adversarial family, typically one whose outputs are differentiable with respect to . Because the empirical inner problem is nonconcave, the algorithm generally targets an approximate stationary solution rather than a certified global maximizer.
##  Theoretical Analysis
We establish four guarantees for Algorithm , all at a fixed context : a bound on the Sinkhorn ambiguity (Lemma ); a decision-alignment result linking the radius to downstream loss (Theorem ); convergence of the inner adversarial maximization (Theorem ); and joint convergence of the alternating procedure under outer convexity (Theorem ). Proofs are deferred to Appendix .
###  3.1 Setup
#### Standing assumptions.
Throughout, the context is fixed and:
  * (A1)
is -Lipschitz in , uniformly in ;
  * (A2)
\mathcal{W}\subset\mathbb{R}^{d} is convex and compact with diameter D_{\mathcal{W}};
  * (A3)
nominal and adversarial generator outputs are uniformly bounded: ⩽R\|G_{\hat{\phi}}(z_{0},x)\|_{2}\leqslant R for -almost every , and \|G_{\psi}(z_{\mathrm{A}},x)\|_{2}\leqslant R for every \psi\in\Psi and \zeta_{\mathrm{A}}-almost every z_{\mathrm{A}}.


All Sinkhorn and Wasserstein quantities in this section use the squared-Euclidean ground cost =c(y,y^{\prime})=\|y-y^{\prime}\|_{2}^{2}. Convexity of in is assumed only for joint convergence (Assumption ). We take \varepsilon>0 and throughout.
#### Notation.
At the population level, retain the notation P_{0}^{x} and Q_{\psi}^{x} from Section . For the optimization analysis, condition on the batches in () and abbreviate  
| :=,:=​,F(w,\psi):=\widehat{F}_{M}(w,\psi),\qquad F_{0}(w):=\frac{1}{M}\sum_{i=1}^{M}f(w,Y_{0,i}),  |  
| --- |  
| :=​(,),𝒜:=.s(\psi):=S_{\varepsilon}(\widehat{P}_{G_{\psi},x},\widehat{P}_{G_{\hat{\phi}},x}),\qquad\mathcal{A}:=\\{\psi\in\Psi:s(\psi)\leqslant\rho\\}.  |  
| --- |  
Let :=\phi(w):=\max_{\psi\in\mathcal{A}}F(w,\psi), :=\phi^{*}:=\min_{w\in\mathcal{W}}\phi(w), and ∈​\psi^{*}(w)\in\arg\max_{\psi\in\mathcal{A}}F(w,\psi). We assume these optima are attained and 𝒜\mathcal{A} is nonempty. Finally, write s_{k}:=s(\psi_{k}), {\gamma_{M}}:=\varepsilon\log M, B:=B:=\max\\{\rho,4R^{2}\\}, and let \mu^{(1)}>0 be the multiplier at the start of each inner block.
#### Sinkhorn–Wasserstein closeness.
For the two equally weighted -point empirical laws used by the algorithm, the comparison is explicit:  
| |−|⩽=.\bigl|S_{\varepsilon}(\alpha,\beta)-W_{2}^{2}(\alpha,\beta)\bigr|\leqslant{\gamma_{M}}=\varepsilon\log M.  |  
| --- |  
Indeed, an optimal unregularized permutation coupling has relative entropy , and the same bound applies to both self-transport terms. A proof is given in Appendix . Unlike a generic asymptotic interpolation-gap statement, () gives a uniform finite-sample comparison over generated empirical clouds, with an explicit error term \gamma_{M}=\varepsilon\log M.
###  3.2 Sinkhorn Bound and Decision Alignment
We first bound the Sinkhorn divergence between any adversarial conditional law and the nominal conditional law. This bound is the one problem-specific ingredient of the convergence analysis; everything downstream of it is standard.
######  (Uniform Sinkhorn upper bound).
Under (A3), any two nominal or adversarial output laws satisfy  
| 0⩽⩽.{0\leqslant S_{\varepsilon}(P,Q)\leqslant 4R^{2}.}  |  
| --- |  
In particular, 0\leqslant s(\psi)\leqslant 4R^{2} for every \psi\in\Psi.
###### Proof sketch.
The product coupling P\otimes Q has zero relative-entropy penalty and transport cost at most . Thus \operatorname{OT}_{\varepsilon}(P,Q)\leqslant 4R^{2}; subtracting the two nonnegative self-transport terms cannot increase the result. Nonnegativity is the standard positivity property of the debiased Sinkhorn divergence. This argument does not require a common latent space or paired draws. Full proof in Appendix . ∎
The next result formalizes the central claim of the introduction: the radius is a budget on downstream performance.
Let \mathcal{P}_{R} be the probability laws supported on the closed Euclidean ball of radius , and define  
| :=sup{:,}.\omega_{\varepsilon,R}(r):=\sup\\{W_{1}(P,Q):P,Q\in\mathcal{P}_{R},\ S_{\varepsilon}(P,Q)\leqslant r\\}.  |  
| --- |  
######  (Population decision alignment).
The function \omega_{\varepsilon,R} is finite and nondecreasing, and \omega_{\varepsilon,R}(r)\downarrow 0 as r\downarrow 0. Under (A1)–(A3), every \psi\in\Psi satisfying S_{\varepsilon}(Q_{\psi}^{x},P_{0}^{x})\leqslant\rho obeys  
| |−|⩽for every ​w∈𝒲.\left|\mathbb{E}_{Q_{\psi}^{x}}[f(w,Y)]-\mathbb{E}_{P_{0}^{x}}[f(w,Y)]\right|\leqslant L_{f}\,\omega_{\varepsilon,R}(\rho)\qquad\text{for every }w\in\mathcal{W}.  |  
| --- |  
###### Proof sketch.
On the compact space \mathcal{P}_{R}, Sinkhorn divergence is continuous, positive definite, and metrizes weak convergence; is also continuous. Compactness therefore implies \omega_{\varepsilon,R}(r)\downarrow 0. The loss bound then follows from Kantorovich–Rubinstein duality. Full proof in Appendix . ∎
######  (Empirical decision alignment).
Under (A1)–(A3), every \psi\in\mathcal{A} satisfies  
| ||⩽for every ​w∈𝒲.|F(w,\psi)-F_{0}(w)|\leqslant L_{f}\sqrt{\rho+{\gamma_{M}}}\qquad\text{for every }w\in\mathcal{W}.  |  
| --- |  
######  (Significance).
The radius is not an abstract divergence budget but a direct, loss-uniform bound on the downstream loss any adversary in 𝒜\mathcal{A} can extract, holding simultaneously for every Lipschitz objective. This makes an interpretable design parameter.
###  3.3 Inner Convergence
For fixed , the inner problem is a nonconcave maximization over a nonconvex feasible set, solved by the primal–dual scheme of Algorithm : at each of dual steps, ascent steps approximately solve ​\max_{\psi}\mathcal{L}(w,\psi,\mu_{k}), followed by a projected update of . The next result bounds the suboptimality in objective value, averaged over the dual iterates.
Because gradient ascent need not find a global maximizer of a nonconcave Lagrangian, the guarantee is stated under an explicit inner oracle condition:  
| ∈​.\psi_{k}\in\arg\max_{\psi\in\Psi}\widehat{\mathcal{L}}(w,\psi,\mu_{k}).  |  
| --- |  
An approximate oracle adds its average Lagrangian error to the bound below; in particular, an average error of order preserves the stated rate.
######  (Inner convergence).
Under (A1)–(A3) and (), use projected dual descent with \eta_{\mu}=\mu^{(1)}/(B\sqrt{K}). Then  
| −​⩽,F\bigl(w,\psi^{*}(w)\bigr)-\frac{1}{K}\sum_{k=1}^{K}F(w,\psi_{k})\;\leqslant\;{\frac{B\,\mu^{(1)}}{\sqrt{K}},}  |  
| --- |  
where ∈​\psi^{*}(w)\in\arg\max_{\psi\in\mathcal{A}}F(w,\psi).
The proof is the standard dual-subgradient analysis of constrained saddle-point problems (Zinkevich, 2003; Nedić and Ozdaglar, 2009): a projected-descent regret bound on the dual variable, into which the Sinkhorn bound (Lemma ) enters only through the constant . See Appendix .
###  3.4 Joint Convergence
The full algorithm alternates the inner primal–dual updates with an outer projected step along the averaged subgradient =\hat{g}^{(t)}=\frac{1}{K}\sum_{k=1}^{K}\hat{g}_{k}, ∈\hat{g}_{k}\in\partial_{w}F(w^{(t)},\psi_{k}). Coupling the two layers requires convexity of the downstream loss in .
######  (Outer convexity).
is convex in for every , and the outer subgradients used by the algorithm are assumed uniformly bounded, \|\hat{g}_{k}\|\leqslant G_{w}.
For fixed , let  
| :={+}.Q_{w}(\mu):=\sup_{\psi\in\Psi}\\{F(w,\psi)+\mu(\rho-s(\psi))\\}.  |  
| --- |  
######  (Dual regularity).
For every w\in\mathcal{W}, has a selected minimizer \mu^{*}(w)\geqslant 0 satisfying :=∞\overline{\mu}^{*}:=\sup_{w\in\mathcal{W}}\mu^{*}(w)<\infty.
The inner iterates need not be feasible; the next lemma controls their mean constraint violation using the standard long-term-constraint argument (Mahdavi et al., 2012), with an explicit comparison constant derived as in GAS-DRO (Wen and Yang, 2026).
######  (Average constraint slack).
Under the conditions of Theorem and Assumption ,  
| ⩽,=​(+),\frac{1}{K}\sum_{k=1}^{K}s_{k}\;\leqslant\;\rho+\frac{C_{K}}{\sqrt{K}},\qquad{C_{K}=\frac{\max\\{\rho,4R^{2}\\}}{\mu_{C}-\overline{\mu}^{*}}\Bigl(\tfrac{\mu^{(1)}}{2}+\tfrac{|\mu_{C}-\mu^{(1)}|^{2}}{2\mu^{(1)}}\Bigr),}  |  
| --- |  
where \mu_{C}>\overline{\mu}^{*} is fixed.
######  (Joint convergence).
Under (A1)–(A3), Assumptions and , and the inner-oracle condition (), run Algorithm for outer iterations with inner steps and outer step size \eta_{w}=D_{\mathcal{W}}/(G_{w}\sqrt{T}). Then the averaged iterate =\bar{w}=T^{-1}\sum_{t=1}^{T}w^{(t)} satisfies  
| \displaystyle\phi(\bar{w})-\phi^{*}\;\leqslant\;  | ++⏟slack\displaystyle\underbrace{\frac{D_{\mathcal{W}}G_{w}}{\sqrt{T}}}_{\textnormal{outer}}+\underbrace{\frac{B\mu^{(1)}}{\sqrt{K}}}_{\textnormal{inner}}+\underbrace{\frac{L_{f}C_{K}}{2\sqrt{(\rho+\gamma_{M})K}}}_{\textnormal{slack}}  |  
| --- | --- |  
| +comparison residual.\displaystyle+\underbrace{2L_{f}\sqrt{\rho+\gamma_{M}}}_{\textnormal{comparison residual}}.  |  
######  (Interpretation).
The first three terms are _optimization errors_ : outer projected subgradient descent, inner Lagrangian approximation, and accumulated average slack. These terms vanish as T,K\to\infty; for instance, taking makes the inner and slack terms , leaving the dominant optimization rate O(1/\sqrt{T}). The last term, 2L_{f}\sqrt{\rho+\gamma_{M}}, is a _comparison residual_ in the present proof. It has the same scale as the empirical decision-alignment bound in Corollary and arises from bounding the loss gap through Kantorovich–Rubinstein duality and the nominal empirical law. This term is independent of and in our analysis; we do not claim that it is intrinsic to the algorithm.
##  Experiments
#### Overview.
We evaluate GDRO on two downstream decision problems. The first is contextual newsvendor, where the decision is convex and the optimal order for a fixed scenario distribution has a weighted-quantile form. We study this task on a synthetic benchmark with controlled rare conditional tails and on the real M5 retail demand dataset (Makridakis et al., 2022). The second downstream problem is robot navigation among pedestrians, where the decision problem is nonconvex and the nominal model is the official implicit SocialGAN trajectory generator (Gupta et al., 2018). These two settings test GDRO under both explicit conditional generators and implicit black-box samplers.
#### Baselines.
For all tasks, Nominal optimizes the downstream decision using samples from the fitted nominal generator. KL performs finite-support KL reweighting over nominal samples, and therefore cannot create new outcomes outside the sampled support. W2 uses a finite-sample Wasserstein-2 perturbation of the sampled outcomes. For the newsvendor experiments, where the nominal model has an explicit conditional decoder, we also compare with GAS-DRO. For the synthetic benchmark only, we report an Oracle that optimizes using samples from the true data-generating process. Our method, GDRO, optimizes against adversarial generators constrained by a context-local Sinkhorn certificate around the nominal generator. Full implementation details and hyperparameters are given in Appendix .
#### Metrics.
For newsvendor, the primary decision-quality metrics are average realized cost and, when an oracle is available, regret relative to the oracle. Since the asymmetric newsvendor loss already encodes the underage–overage trade-off, lower tail losses or stockout rates alone do not necessarily indicate a better policy: they can also be obtained by systematically over-ordering. We therefore report Q95 loss, CVaR, stockout rate, and average order quantity as diagnostic metrics that reveal the risk–conservatism trade-off. For robot navigation, we report collision count, near-miss count, arrival count, evaluation loss, minimum realized pedestrian distance, and terminal goal error.
###  4.1 Contextual Newsvendor
#### Synthetic rare-tail benchmark.
The synthetic benchmark is designed so that most contexts follow a regular demand pattern, while rare contexts may activate a shifted tail component. This stresses a common failure mode of nominal generative models: the fitted generator can match the bulk of the conditional distribution while underrepresenting rare high-cost outcomes. The downstream decision is a multi-product order vector, and the realized loss is the asymmetric newsvendor cost.
Table reports results separately on frequent and rare contexts. On frequent contexts, GDRO obtains the lowest average cost and regret among non-oracle methods while keeping the average order close to the oracle. On rare contexts, GDRO again achieves the lowest non-oracle regret, improving substantially over the nominal policy, KL reweighting, W2, and GAS-DRO. KL achieves lower tail losses and stockout rates in some slices, but it does so with larger average orders and substantially higher average cost. This illustrates the risk–conservatism trade-off in newsvendor: tail-risk reductions are meaningful only when considered together with realized cost and order inflation. This supports the central mechanism of GDRO: rather than only reweighting nominal samples or freely perturbing support points, it searches over nearby generator-induced conditional laws that expose consequential tail scenarios.
Synthetic contextual newsvendor results. Avg. cost and regret are the primary decision-quality metrics. Q95 loss, CVaR, stockout, and average order are diagnostic metrics for the risk–conservatism trade-off.  
 |  
|  |  
| Oracle  | 422.99  | 0.00  | 801.89  | 1260.96  | 0.084  | 25.09  |  
| Nominal  | 436.55  | 13.55  | 947.01  | 1429.04  | 0.104  | 24.35  |  
| KL  | 451.43  | 28.44  | 754.84  | 1136.56  | 0.073  | 26.34  |  
| W2  | 436.73  | 13.74  | 846.07  | 1292.49  | 0.088  | 25.08  |  
| GAS-DRO  | 431.21  | 8.22  | 889.10  | 1358.03  | 0.094  | 24.68  |  
| 809.49  | 1257.77  | 0.084  | 25.16  |  
| Oracle  | 514.46  | 0.00  | 967.81  | 1799.44  | 0.084  | 28.35  |  
| Nominal  | 537.09  | 22.63  | 1291.28  | 2259.68  | 0.124  | 26.50  |  
| KL  | 541.09  | 26.63  | 1074.20  | 1903.99  | 0.101  | 28.25  |  
| W2  | 532.88  | 18.41  | 1205.79  | 2128.83  | 0.117  | 27.03  |  
| GAS-DRO  | 530.36  | 15.89  | 1236.14  | 2190.00  | 0.118  | 26.75  |  
| 1148.88  | 2064.01  | 0.107  | 27.26  |  
#### M5 retail demand.
We next apply the same newsvendor pipeline to the M5 retail demand dataset. We select 20 products with the fewest zero-demand observations to make conditional scenario generation stable. For each day , the context is a rolling window of the previous 10 days of demand, and the nominal CVAE–LSTM generator produces conditional scenarios for the next-day demand . The downstream decision is the order vector for that day, and all methods are evaluated out of sample on held-out rolling test windows. Unlike the synthetic benchmark, the true data-generating distribution is unknown, so performance is measured only against realized held-out demand. The robustness radius and inner-loop budget are adapted using a historical average-cost risk score, as described in Appendix .
GDRO achieves the lowest average realized cost on the M5 test set. It also improves the moderate-tail metrics Q and CVaR relative to the nominal policy while keeping the average order close to W2. KL and GAS-DRO reduce some extreme-tail or stockout metrics, but mainly by placing larger orders; in particular, GAS-DRO attains the lowest stockout rate with a much larger average order and the highest average cost. These results indicate that GDRO improves the primary decision objective without relying on excessive over-ordering.
Performance comparison on the held-out M5 contextual newsvendor test set. Average realized cost is the primary decision-quality metric; tail losses, stockout, and average order diagnose the risk–conservatism trade-off.  
| Method  | Avg. cost  | Stockout  | Avg. order  |  
| --- | --- | --- | --- |  
| Nominal  | 1230.30  | 1729.04  | 2634.58  | 2772.97  | 3440.73  | 0.1088  | 64.64  |  
| KL  | 1459.00  | 1951.36  | 2326.20  | 2607.80  | 3101.56  | 0.1070  | 71.33  |  
| W2  | 1212.91  | 1654.29  | 2400.24  | 2541.50  | 3093.66  | 0.0940  | 66.39  |  
| GAS-DRO  | 1712.35  | 2510.35  | 2592.51  | 2705.35  | 2859.42  | 0.0193  | 86.44  |  
| 1575.37  | 2354.47  | 2454.90  | 3035.12  | 0.0840  | 67.07  |  
###  4.2 Pedestrian-Conditioned Robot Navigation with SocialGAN
#### Setup.
To test GDRO with an implicit high-dimensional generator, we use the official pretrained SocialGAN model (Gupta et al., 2018). Given 8 observed frames of pedestrian motion, SocialGAN generates samples of the next 12 frames. We add a downstream robot navigation decision on top of this prediction task: the robot chooses a 12-step velocity plan to move from a sampled start point to a goal while avoiding pedestrians. During optimization, the robot only observes the past trajectory and SocialGAN-generated futures; the true future is used only for evaluation. In evaluation, a collision is counted when the robot comes within meters of any realized pedestrian trajectory, a near miss is counted using a larger -meter buffer, and arrival means that the robot reaches within meters of the goal within the planning horizon.
We construct 200 fixed decision tasks from 50 SocialGAN test contexts, with four start–goal queries per context. Queries are selected using only nominal-sample information so that the straight-line robot path has nontrivial predicted collision risk, while the start and goal are not initially occupied. This creates difficult but feasible navigation instances rather than trivially safe cases. Details of query construction, loss weights, adaptive radii, and optimization budgets are given in Appendix .
#### Results.
Figure shows the qualitative mechanism on a real SocialGAN test scene. Nominal and KL both collide with the realized pedestrian future: Nominal trusts the baseline forecast, while KL can only reweight the same nominal support. GDRO avoids the pedestrian while still reaching the goal. In contrast, W2 perturbs support points directly in trajectory space, which can move adversarial futures off the SocialGAN manifold and break the learned trajectory-interaction structure. The resulting robot plan is more distorted and not necessarily safer under realized evaluation.
Mechanism example on a real SocialGAN test scene. Nominal and KL plans collide with the realized pedestrian future. GDRO avoids the pedestrian while still reaching the goal, whereas W2 produces a distorted route after unconstrained output-space perturbation. 
Table confirms this pattern across 200 fixed test tasks. A collision is counted at m, a near miss at m, and arrival means reaching within m of the goal. GDRO reduces collisions from 22/200 to 11/200 and near misses from 106/200 to 55/200, while still arriving in 195/200 tasks. W2 achieves a larger average minimum distance, but has more collisions, a much lower arrival rate, and a larger terminal gap, showing that conservatism in the wrong geometry can be harmful.
SocialGAN robot navigation on 200 fixed test tasks. Collisions are counted at m, near misses at m, and arrivals at a m goal threshold.  
| Method  | Collisions  | Near misses  | Arrivals  | Eval. loss  | Min dist.  | Terminal gap  |  
| --- | --- | --- | --- | --- | --- | --- |  
| Nominal  | 22/200  | 106/200  | 200/200  | 35.48  | 0.800  | 0.010  |  
| KL  | 14/200  | 90/200  | 200/200  | 29.84  | 0.851  | 0.016  |  
| 195/200  | 0.925  | 0.035  |  
| W2  | 34/200  | 72/200  | 142/200  | 56.60  | 1.017  | 0.277  |  
#### Takeaway.
Across newsvendor and SocialGAN navigation, GDRO improves downstream robustness by stress-testing decisions through structured generator-level perturbations. The results show that robustness is not only about being more conservative, but about being conservative in the right geometry: GDRO preserves the simulator’s learned structure, whereas free output-space perturbations can produce misleading stress tests.
##  Conclusion
We proposed GDRO, a simulation-based distributionally robust optimization framework for decision-making with learned conditional generators. The core idea is to define robustness directly on generated samples at the active decision context. Instead of relying on likelihood ratios, reconstruction certificates, or global model-level discrepancies, GDRO compares nominal and adversarial output clouds through a sample-based Sinkhorn certificate. This makes the ambiguity set context-local, transport-based, and applicable even when the nominal model is only available as a sampler.
Theoretically, we showed that the Sinkhorn radius admits a downstream loss interpretation for Lipschitz objectives and proved a finite-time guarantee for the fixed empirical objective when the outer decision layer is convex, as in the newsvendor setting. Empirically, GDRO improves the primary decision objective in contextual newsvendor tasks and reduces realized collision risk in SocialGAN navigation, showing that the same sample-based framework can also be applied beyond convex decision problems to implicit pretrained generators. Together, these results highlight the central mechanism of GDRO: robustness is not merely about being more conservative, but about stress-testing the simulator in the right geometry. By constraining adversarial scenarios through generator-induced output laws, GDRO preserves sample-level structure that unrestricted support perturbations may destroy.
## References
  * Blanchet and Murthy [2019] Jose Blanchet and Karthyek Murthy.  Quantifying distributional model risk via optimal transport.  _Mathematics of Operations Research_ , 44(2):565–600, 2019.  doi: 10.1287/moor.2018.0936. 
  * Costa and Iyengar [2023] Giorgio Costa and Garud N. Iyengar.  Distributionally robust end-to-end portfolio construction.  _Quantitative Finance_ , 23(10):1465–1482, 2023.  doi: 10.1080/14697688.2023.2236148. 
  * Cuturi [2013] Marco Cuturi.  Sinkhorn distances: Lightspeed computation of optimal transport.  In _Advances in Neural Information Processing Systems_ , volume 26, 2013.  URL 
  * Donti et al. [2017] Priya L. Donti, Brandon Amos, and J. Zico Kolter.  Task-based end-to-end model learning in stochastic optimization.  In _Advances in Neural Information Processing Systems_ , volume 30, 2017.  URL 
  * Elmachtoub and Grigas [2022] Adam N. Elmachtoub and Paul Grigas.  Smart “predict, then optimize”.  _Management Science_ , 68(1):9–26, 2022.  doi: 10.1287/mnsc.2020.3922. 
  * Feydy et al. [2019] Jean Feydy, Thibault Séjourné, François-Xavier Vialard, Shun-ichi Amari, Alain Trouvé, and Gabriel Peyré.  Interpolating between optimal transport and MMD using sinkhorn divergences.  In _Proceedings of the Twenty-Second International Conference on Artificial Intelligence and Statistics_ , volume 89 of _Proceedings of Machine Learning Research_ , pages 2681–2690. PMLR, 2019.  URL 
  * Gao and Kleywegt [2023] Rui Gao and Anton J. Kleywegt.  Distributionally robust stochastic optimization with wasserstein distance.  _Mathematics of Operations Research_ , 48(2):603–655, 2023.  doi: 10.1287/moor.2022.1275. 
  * Gao et al. [2024] Rui Gao, Xi Chen, and Anton J. Kleywegt.  Wasserstein distributionally robust optimization and variation regularization.  _Operations Research_ , 72(3):1177–1191, 2024.  doi: 10.1287/opre.2022.2356. 
  * Genevay et al. [2018] Aude Genevay, Gabriel Peyré, and Marco Cuturi.  Learning generative models with sinkhorn divergences.  In _Proceedings of the Twenty-First International Conference on Artificial Intelligence and Statistics_ , volume 84 of _Proceedings of Machine Learning Research_ , pages 1608–1617. PMLR, 2018.  URL 
  * Gupta et al. [2018] Agrim Gupta, Justin Johnson, Li Fei-Fei, Silvio Savarese, and Alexandre Alahi.  Social GAN: Socially acceptable trajectories with generative adversarial networks.  In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , pages 2255–2264, 2018.  doi: 10.1109/CVPR.2018.00240. 
  * Hu and Hong [2013] Zhaolin Hu and L. Jeff Hong.  Kullback–leibler divergence constrained distributionally robust optimization.  _Optimization Online_ , 2013.  URL 
  * Kobyzev et al. [2021] Ivan Kobyzev, Simon J. D. Prince, and Marcus A. Brubaker.  Normalizing flows: An introduction and review of current methods.  _IEEE Transactions on Pattern Analysis and Machine Intelligence_ , 43(11):3964–3979, 2021.  doi: 10.1109/TPAMI.2020.2992934. 
  * Kuhn et al. [2024] Daniel Kuhn, Soroosh Shafiee, and Wolfram Wiesemann.  Distributionally robust optimization, 2024. 
  * Ma et al. [2024] Xutao Ma, Chao Ning, and Wenli Du.  Differentiable distributionally robust optimization layers.  In _Proceedings of the 41st International Conference on Machine Learning_ , volume 235 of _Proceedings of Machine Learning Research_ , pages 33880–33901. PMLR, 2024.  URL 
  * Mahdavi et al. [2012] Mehrdad Mahdavi, Rong Jin, and Tianbao Yang.  Trading regret for efficiency: Online convex optimization with long term constraints.  _Journal of Machine Learning Research_ , 13(81):2503–2528, 2012.  URL 
  * Makridakis et al. [2022] Spyros Makridakis, Evangelos Spiliotis, and Vassilios Assimakopoulos.  The m5 accuracy competition: Results, findings, and conclusions.  _International Journal of Forecasting_ , 38(4):1346–1364, 2022. 
  * Michel et al. [2021] Paul Michel, Tatsunori Hashimoto, and Graham Neubig.  Modeling the second player in distributionally robust optimization.  In _International Conference on Learning Representations_ , 2021.  URL 
  * Michel et al. [2022] Paul Michel, Tatsunori Hashimoto, and Graham Neubig.  Distributionally robust models with parametric likelihood ratios.  In _International Conference on Learning Representations_ , 2022.  URL 
  * Mohajerin Esfahani and Kuhn [2018] Peyman Mohajerin Esfahani and Daniel Kuhn.  Data-driven distributionally robust optimization using the wasserstein metric: Performance guarantees and tractable reformulations.  _Mathematical Programming_ , 171(1–2):115–166, 2018.  doi: 10.1007/s10107-017-1172-1. 
  * Namkoong and Duchi [2016] Hongseok Namkoong and John C. Duchi.  Stochastic gradient methods for distributionally robust optimization with f-divergences.  In _Advances in Neural Information Processing Systems_ , volume 29, 2016. 
  * Nedić and Ozdaglar [2009] Angelia Nedić and Asuman Ozdaglar.  Subgradient methods for saddle-point problems.  _Journal of Optimization Theory and Applications_ , 142(1):205–228, 2009. 
  * Peyré and Cuturi [2019] Gabriel Peyré and Marco Cuturi.  Computational optimal transport.  _Foundations and Trends in Machine Learning_ , 11(5–6):355–607, 2019.  doi: 10.1561/2200000073. 
  * Rahimian and Mehrotra [2022] Hamed Rahimian and Sanjay Mehrotra.  Frameworks and results in distributionally robust optimization.  _Open Journal of Mathematical Optimization_ , 3:1–85, 2022.  doi: 10.5802/ojmo.15. 
  * Ren and Majumdar [2022] Allen Z. Ren and Anirudha Majumdar.  Distributionally robust policy learning via adversarial environment generation.  In _Proceedings of the 2022 International Conference on Robotics and Automation_ , 2022. 
  * Sinha et al. [2018] Aman Sinha, Hongseok Namkoong, Riccardo Volpi, and John Duchi.  Certifying some distributional robustness with principled adversarial training.  In _International Conference on Learning Representations_ , 2018.  URL 
  * Song and Ermon [2019] Yang Song and Stefano Ermon.  Generative modeling by estimating gradients of the data distribution.  In _Advances in Neural Information Processing Systems_ , volume 32, pages 11895–11907, 2019. 
  * Wang et al. [2025a] Irina Wang, Bart Van Parys, and Bartolomeo Stellato.  Learning decision-focused uncertainty sets in robust optimization, 2025a. 
  * Wang et al. [2025b] Jie Wang, Rui Gao, and Yao Xie.  Sinkhorn distributionally robust optimization.  _Operations Research_ , 74(3):1581–1603, 2025b.  doi: 10.1287/opre.2023.0294. 
  * Wen and Yang [2025] Jiaqi Wen and Jianyi Yang.  Distributionally robust optimization via diffusion ambiguity modeling, 2025. 
  * Wen and Yang [2026] Jiaqi Wen and Jianyi Yang.  Distributionally robust optimization via generative ambiguity modeling.  In _International Conference on Learning Representations_ , 2026.  URL 
  * Xu et al. [2024] Chen Xu, Jonghyeok Lee, Xiuyuan Cheng, and Yao Xie.  Flow-based distributionally robust optimization.  _IEEE Journal on Selected Areas in Information Theory_ , 2024.  URL 
  * Yang et al. [2025] Yufeng Yang, Yi Zhou, and Zhaosong Lu.  Nested stochastic gradient descent for (generalized) sinkhorn distance-regularized distributionally robust optimization, 2025. 
  * Zinkevich [2003] Martin Zinkevich.  Online convex programming and generalized infinitesimal gradient ascent.  In _Proceedings of the 20th International Conference on Machine Learning (ICML)_ , 2003. 


##  Appendix A Proofs
This appendix contains full proofs for the results stated in Section . For convenience, each theorem or lemma is restated before its proof.
The population proof below concerns P_{0}^{x} and Q_{\psi}^{x} at the fixed context . All optimization proofs condition on the fixed Monte Carlo batches and use the empirical shorthand introduced in Section .
#### Basic assumptions.
We use the following basic assumptions throughout the theoretical analysis:
  1. (A1)
is -Lipschitz in uniformly in w\in\mathcal{W}.
  2. (A2)
\mathcal{W}\subset\mathbb{R}^{d} is convex and compact with diameter D_{\mathcal{W}}.
  3. (A3)
Nominal and adversarial generator outputs are uniformly bounded as stated in Section .


#### Notation.
For a fixed context , we use the following notation:
  * •
:=F(w,\psi):=\widehat{F}_{M}(w,\psi) denotes the empirical downstream loss under adversary ; this shorthand is used only in the fixed-batch optimization proofs.
  * •
:={ψ:​(,)⩽ρ}\mathcal{A}(\hat{\phi},\rho,x):=\left\\{\psi:S_{\varepsilon}\left(\widehat{P}_{G_{\psi},x},\widehat{P}_{G_{\hat{\phi}},x}\right)\leqslant\rho\right\\} denotes the Sinkhorn ambiguity set. When \hat{\phi}, , and are clear from context, we write simply 𝒜\mathcal{A}.
  * •
:=\phi(w):=\max_{\psi\in\mathcal{A}}F(w,\psi) denotes the robust outer objective, and :=\phi^{*}:=\min_{w\in\mathcal{W}}\phi(w) denotes its optimal value.
  * •
∈​\psi^{*}(w)\in\arg\max_{\psi\in\mathcal{A}}F(w,\psi) denotes a worst-case adversary for decision , and ∈​w^{*}\in\arg\min_{w\in\mathcal{W}}\phi(w) denotes an optimal robust decision.
  * •
:=​(,)s_{k}:=S_{\varepsilon}\left(\widehat{P}_{G_{\psi_{k}},x},\widehat{P}_{G_{\hat{\phi}},x}\right) denotes the Sinkhorn divergence at the -th inner iterate.
  * •
{\gamma_{M}}:=\varepsilon\log M and B:=B:=\max\\{\rho,4R^{2}\\}.
  * •
When analyzing the outer update, ∈\hat{g}_{k}\in\partial_{w}F(w^{(t)},\psi_{k}) denotes the outer subgradient associated with the -th inner iterate, and  
| :=\hat{g}^{(t)}:=\frac{1}{K}\sum_{k=1}^{K}\hat{g}_{k}  |  
| --- |  
denotes the averaged outer subgradient used in Algorithm .


Additional assumptions required only for the joint convergence theorem are stated explicitly in the proof of Theorem .
###  A.1 Proof of Lemma 
######  (Uniform Sinkhorn upper bound; restatement of Lemma ).
Under Assumption (A3), any two nominal or adversarial output laws satisfy 0⩽⩽0\leqslant S_{\varepsilon}(P,Q)\leqslant 4R^{2}.
###### Proof.
The independent coupling P\otimes Q is feasible in () and has zero KL penalty. Since both laws are supported in the radius- ball,  
| ⩽⩽.\|y-y^{\prime}\|_{2}^{2}\leqslant(\|y\|_{2}+\|y^{\prime}\|_{2})^{2}\leqslant 4R^{2}.  |  
| --- |  
Consequently, \operatorname{OT}_{\varepsilon}(P,Q)\leqslant 4R^{2}. The two self-transport terms are nonnegative, so ⩽⩽S_{\varepsilon}(P,Q)\leqslant\operatorname{OT}_{\varepsilon}(P,Q)\leqslant 4R^{2}. Nonnegativity follows from the positivity of the debiased Sinkhorn divergence for squared-Euclidean cost [Feydy et al., 2019]. ∎
###  A.2 Proof of the Empirical Sinkhorn–Wasserstein Comparison
###### Proof.
Let \alpha=M^{-1}\sum_{i}\delta_{a_{i}} and \beta=M^{-1}\sum_{j}\delta_{b_{j}}. The KL term in () is nonnegative, hence ⩾\operatorname{OT}_{\varepsilon}(\alpha,\beta)\geqslant W_{2}^{2}(\alpha,\beta). The unregularized problem has an optimal permutation coupling. Its nonzero entries equal , so its KL divergence from the product weights is . Therefore  
| 0⩽−⩽.0\leqslant\operatorname{OT}_{\varepsilon}(\alpha,\beta)-W_{2}^{2}(\alpha,\beta)\leqslant\varepsilon\log M.  |  
| --- |  
Applying the same argument to the two self-transport terms shows that −S_{\varepsilon}(\alpha,\beta)-W_{2}^{2}(\alpha,\beta) is one number in [0,{\gamma_{M}}] minus half of each of two numbers in [0,{\gamma_{M}}]. It therefore lies in [-{\gamma_{M}},{\gamma_{M}}], proving (). ∎
###  A.3 Proof of Theorem 
###### Proof.
The radius- ball is compact, so \mathcal{P}_{R} is compact under weak convergence. On this space, S_{\varepsilon} is continuous, positive definite, and metrizes weak convergence [Feydy et al., 2019, Theorem 1]; is also continuous.
If \omega_{\varepsilon,R}(r) did not tend to zero, there would be r_{n}\downarrow 0 and P_{n},Q_{n}\in\mathcal{P}_{R} with S_{\varepsilon}(P_{n},Q_{n})\leqslant r_{n} but W_{1}(P_{n},Q_{n}) bounded away from zero. Compactness gives a subsequence converging to some . Continuity gives S_{\varepsilon}(P,Q)=0, hence , while continuity of gives W_{1}(P_{n},Q_{n})\to 0, a contradiction. Thus \omega_{\varepsilon,R}(r)\downarrow 0.
For a population-feasible , definition () gives ⩽W_{1}(Q_{\psi}^{x},P_{0}^{x})\leqslant\omega_{\varepsilon,R}(\rho).
Assumption (A1) and Kantorovich–Rubinstein duality now yield  
| |−|⩽​​⩽.\left|\mathbb{E}_{Q_{\psi}^{x}}[f(w,Y)]-\mathbb{E}_{P_{0}^{x}}[f(w,Y)]\right|\leqslant L_{f}W_{1}(Q_{\psi}^{x},P_{0}^{x})\leqslant L_{f}\omega_{\varepsilon,R}(\rho).  |  
| --- |  
∎
###### Proof of Corollary .
For \psi\in\mathcal{A}, Assumption (A1), Kantorovich–Rubinstein duality, W_{1}\leqslant W_{2}, and () give  
| ||⩽​​(,)⩽⩽.|F(w,\psi)-F_{0}(w)|\leqslant L_{f}W_{1}(\widehat{P}_{G_{\psi},x},\widehat{P}_{G_{\hat{\phi}},x})\leqslant L_{f}\sqrt{s(\psi)+{\gamma_{M}}}\leqslant L_{f}\sqrt{\rho+{\gamma_{M}}}.  |  
| --- |  
∎
###  A.4 Proof of Theorem 
######  (Inner convergence; restated).
Under (A1)–(A3) and (), run the inner loop for dual steps with \eta_{\mu}=\mu^{(1)}/(B\sqrt{K}). Then  
| −​⩽,F\bigl(w,\psi^{*}(w)\bigr)-\frac{1}{K}\sum_{k=1}^{K}F(w,\psi_{k})\;\leqslant\;\frac{{B}\,\mu^{(1)}}{\sqrt{K}},  |  
| --- |  
where ∈​\psi^{*}(w)\in\arg\max_{\psi\in\mathcal{A}}F(w,\psi) is the inner optimum and \mu^{(1)}>0 is the initial dual variable.
###### Proof.
The inner loop is projected primal–dual ascent on the Lagrangian =−\mathcal{L}(w,\psi,\mu)=F(w,\psi)-\mu\,(s(\psi)-\rho): at each step , maximizes \mathcal{L}(w,\cdot,\mu_{k}) and the dual variable is updated by projected descent, =\mu_{k+1}=[\mu_{k}-\eta_{\mu}b_{k}]_{+}, with b_{k}:=\rho-s_{k}.
We use the standard duality-gap analysis for saddle-point subgradient problems [Zinkevich, 2003, Nedić and Ozdaglar, 2009].
Dual trajectory. Nonexpansiveness of projection gives, for any reference \mu\geqslant 0,  
| ​⩽+​.\frac{1}{K}\sum_{k=1}^{K}(\mu_{k}-\mu)\,b_{k}\;\leqslant\;\frac{(\mu^{(1)}-\mu)^{2}}{2K\eta_{\mu}}+\frac{\eta_{\mu}}{2K}\sum_{k=1}^{K}|b_{k}|^{2}.  |  
| --- |  
By Lemma , 0\leqslant s_{k}\leqslant 4R^{2}, so |b_{k}|\leqslant B. Taking and \eta_{\mu}=\mu^{(1)}/(B\sqrt{K}) yields  
| ⩽.\frac{1}{K}\sum_{k=1}^{K}\mu_{k}\,b_{k}\;\leqslant\;\frac{B\,\mu^{(1)}}{\sqrt{K}}.  |  
| --- |  
Duality gap. For every \mu_{k}\geqslant 0, weak duality gives  
| :=⁡[+]⩾=,Q(\mu_{k}):=\max_{\psi}\bigl[F(w,\psi)+\mu_{k}\,(\rho-s(\psi))\bigr]\;\geqslant\;\max_{\psi\in\mathcal{A}}F(w,\psi)=F\bigl(w,\psi^{*}(w)\bigr),  |  
| --- |  
since any feasible \psi\in\mathcal{A} satisfies s(\psi)\leqslant\rho and hence \mu_{k}(\rho-s(\psi))\geqslant 0. As maximizes the Lagrangian at ,  
| =⩾.F(w,\psi_{k})+\mu_{k}b_{k}\;=\;Q(\mu_{k})\;\geqslant\;F\bigl(w,\psi^{*}(w)\bigr).  |  
| --- |  
Averaging over k=1,\dots,K and rearranging,  
| −​⩽⩽,F\bigl(w,\psi^{*}(w)\bigr)-\frac{1}{K}\sum_{k=1}^{K}F(w,\psi_{k})\;\leqslant\;\frac{1}{K}\sum_{k=1}^{K}\mu_{k}b_{k}\;\leqslant\;\frac{B\,\mu^{(1)}}{\sqrt{K}},  |  
| --- |  
where the last step is (). An approximate oracle contributes its average Lagrangian error additively, as noted after (). ∎
###  A.5 Proof of Lemma 
The argument below follows the standard long-term-constraint analysis of Mahdavi et al. [2012]. The comparison-multiplier construction is likewise standard and is used, for example, in the GAS-DRO analysis of Wen and Yang [2026]. We include the relevant details here to keep the Sinkhorn specialization self-contained.
###### Proof.
Fix the outer decision and omit it from the notation. Define  
| ,.b_{k}:=\rho-s_{k},\qquad v_{k}:=s_{k}-\rho=-b_{k}.  |  
| --- |  
By Lemma , 0\leqslant s_{k}\leqslant 4R^{2}, and hence  
| ⩽B:=.|b_{k}|\leqslant B:=\max\\{\rho,4R^{2}\\}.  |  
| --- |  
We first upper-bound the projected-dual regret term. Applying () with reference multiplier \mu=\mu_{C} gives  
| ​⩽+​.\frac{1}{K}\sum_{k=1}^{K}(\mu_{k}-\mu_{C})b_{k}\leqslant\frac{|\mu_{C}-\mu^{(1)}|^{2}}{2K\eta_{\mu}}+\frac{\eta_{\mu}}{2K}\sum_{k=1}^{K}|b_{k}|^{2}.  |  
| --- |  
Using |b_{k}|\leqslant B and \eta_{\mu}=\mu^{(1)}/(B\sqrt{K}) yields  
| ​⩽​(+).\frac{1}{K}\sum_{k=1}^{K}(\mu_{k}-\mu_{C})b_{k}\leqslant\frac{B}{\sqrt{K}}\left(\frac{\mu^{(1)}}{2}+\frac{|\mu_{C}-\mu^{(1)}|^{2}}{2\mu^{(1)}}\right).  |  
| --- |  
We now lower-bound the same term by the average constraint violation. Recall the dual function  
| :={+}.Q_{w}(\mu):=\sup_{\psi\in\Psi}\\{F(w,\psi)+\mu(\rho-s(\psi))\\}.  |  
| --- |  
By the exact inner oracle condition (),  
| =.Q_{w}(\mu_{k})=F(w,\psi_{k})+\mu_{k}b_{k}.  |  
| --- |  
Let \mu^{*}(w) be the selected minimizer of from Assumption . Since ⩾Q_{w}(\mu_{k})\geqslant Q_{w}(\mu^{*}(w)), () implies  
| =−⩾−.\mu_{k}b_{k}=Q_{w}(\mu_{k})-F(w,\psi_{k})\geqslant Q_{w}(\mu^{*}(w))-F(w,\psi_{k}).  |  
| --- |  
Moreover, evaluating the supremum defining Q_{w}(\mu^{*}(w)) at the candidate gives  
| +⩽.F(w,\psi_{k})+\mu^{*}(w)b_{k}\leqslant Q_{w}(\mu^{*}(w)).  |  
| --- |  
Since b_{k}=-v_{k}, () is equivalent to  
| ⩽+.F(w,\psi_{k})\leqslant Q_{w}(\mu^{*}(w))+\mu^{*}(w)v_{k}.  |  
| --- |  
Substituting () into () gives  
| ⩾−[+]=.\mu_{k}b_{k}\geqslant Q_{w}(\mu^{*}(w))-\bigl[Q_{w}(\mu^{*}(w))+\mu^{*}(w)v_{k}\bigr]=-\mu^{*}(w)v_{k}.  |  
| --- |  
Therefore, using b_{k}=-v_{k},  
| \displaystyle\sum_{k=1}^{K}(\mu_{k}-\mu_{C})b_{k}  | =−\displaystyle=\sum_{k=1}^{K}\mu_{k}b_{k}-\mu_{C}\sum_{k=1}^{K}b_{k}  |  
| --- | --- |  
| =+\displaystyle=\sum_{k=1}^{K}\mu_{k}b_{k}+\mu_{C}\sum_{k=1}^{K}v_{k}  |  
| ⩾+\displaystyle\geqslant-\mu^{*}(w)\sum_{k=1}^{K}v_{k}+\mu_{C}\sum_{k=1}^{K}v_{k}  |  
| =​.\displaystyle=\bigl(\mu_{C}-\mu^{*}(w)\bigr)\sum_{k=1}^{K}v_{k}.  |  
Combining () with (), and dividing by \mu_{C}-\mu^{*}(w)>0, gives  
| ⩽​(+).\frac{1}{K}\sum_{k=1}^{K}v_{k}\leqslant\frac{B}{(\mu_{C}-\mu^{*}(w))\sqrt{K}}\left(\frac{\mu^{(1)}}{2}+\frac{|\mu_{C}-\mu^{(1)}|^{2}}{2\mu^{(1)}}\right).  |  
| --- |  
By Assumption , \mu^{*}(w)\leqslant\overline{\mu}^{*}, and \mu_{C}>\overline{\mu}^{*}. Hence  
| ⩽​(+)=.\frac{1}{K}\sum_{k=1}^{K}v_{k}\leqslant\frac{B}{(\mu_{C}-\overline{\mu}^{*})\sqrt{K}}\left(\frac{\mu^{(1)}}{2}+\frac{|\mu_{C}-\mu^{(1)}|^{2}}{2\mu^{(1)}}\right)=\frac{C_{K}}{\sqrt{K}}.  |  
| --- |  
Finally, since v_{k}=s_{k}-\rho,  
| =⩽.\frac{1}{K}\sum_{k=1}^{K}s_{k}=\rho+\frac{1}{K}\sum_{k=1}^{K}v_{k}\leqslant\rho+\frac{C_{K}}{\sqrt{K}}.  |  
| --- |  
This proves the claim. ∎
###  A.6 Proof of Theorem 
###### Proof.
Let ∈​w^{*}\in\arg\min_{w\in\mathcal{W}}\phi(w). Under Assumption , F(\cdot,\psi) is convex on 𝒲\mathcal{W} for every . Hence  
| =\phi(w)=\max_{\psi\in\mathcal{A}}F(w,\psi)  |  
| --- |  
is convex as a pointwise maximum of convex functions.
Define  
| :=​\Delta_{K}:=\frac{\max\\{\rho,4R^{2}\\}\mu^{(1)}}{\sqrt{K}}  |  
| --- |  
and  
| :=+.\mathcal{R}_{K}:=2L_{f}\sqrt{\rho+\gamma_{M}}+\frac{L_{f}C_{K}}{2\sqrt{(\rho+\gamma_{M})K}}.  |  
| --- |  
We first show that the averaged inner gradient =\hat{g}^{(t)}=K^{-1}\sum_{k=1}^{K}\hat{g}_{k} satisfies the approximate subgradient inequality  
| ⩽⟨,⟩++.\phi(w^{(t)})-\phi^{*}\leqslant\langle\hat{g}^{(t)},w^{(t)}-w^{*}\rangle+\Delta_{K}+\mathcal{R}_{K}.  |  
| --- |  
For each , convexity of F(\cdot,\psi_{k}) gives  
| −⩽.F(w^{(t)},\psi_{k})-F(w^{*},\psi_{k})\leqslant\langle\hat{g}_{k},w^{(t)}-w^{*}\rangle.  |  
| --- |  
Averaging over yields  
| ​[−]⩽⟨,⟩.\frac{1}{K}\sum_{k=1}^{K}\bigl[F(w^{(t)},\psi_{k})-F(w^{*},\psi_{k})\bigr]\leqslant\langle\hat{g}^{(t)},w^{(t)}-w^{*}\rangle.  |  
| --- |  
Next, we compare F(w^{*},\psi_{k}) to . Since =\phi^{*}=F(w^{*},\psi^{*}(w^{*})), Assumption (A1) and Kantorovich–Rubinstein duality give  
| ⩽​​(,).F(w^{*},\psi_{k})-\phi^{*}\leqslant L_{f}W_{1}(\widehat{P}_{G_{\psi_{k}},x},\widehat{P}_{G_{\psi^{*}(w^{*})},x}).  |  
| --- |  
By the triangle inequality for ,  
| ​(,)\displaystyle W_{1}(\widehat{P}_{G_{\psi_{k}},x},\widehat{P}_{G_{\psi^{*}(w^{*})},x})  | ⩽​(,)\displaystyle\leqslant W_{1}(\widehat{P}_{G_{\psi_{k}},x},\widehat{P}_{G_{\hat{\phi}},x})  |  
| --- | --- |  
| +​(,).\displaystyle\quad+W_{1}(\widehat{P}_{G_{\hat{\phi}},x},\widehat{P}_{G_{\psi^{*}(w^{*})},x}).  |  
Using W_{1}\leqslant W_{2} and the empirical Sinkhorn–Wasserstein comparison (), we have  
| ​(,)⩽,W_{1}(\widehat{P}_{G_{\psi_{k}},x},\widehat{P}_{G_{\hat{\phi}},x})\leqslant\sqrt{s_{k}+\gamma_{M}},  |  
| --- |  
while \psi^{*}(w^{*})\in\mathcal{A} implies  
| ​(,)⩽.W_{1}(\widehat{P}_{G_{\hat{\phi}},x},\widehat{P}_{G_{\psi^{*}(w^{*})},x})\leqslant\sqrt{\rho+\gamma_{M}}.  |  
| --- |  
Therefore,  
| ⩽.F(w^{*},\psi_{k})-\phi^{*}\leqslant L_{f}\left(\sqrt{s_{k}+\gamma_{M}}+\sqrt{\rho+\gamma_{M}}\right).  |  
| --- |  
Averaging the preceding pointwise bound over k=1,\ldots,K gives  
| ​−\displaystyle\frac{1}{K}\sum_{k=1}^{K}F(w^{*},\psi_{k})-\phi^{*}  | =​\displaystyle=\frac{1}{K}\sum_{k=1}^{K}\bigl[F(w^{*},\psi_{k})-\phi^{*}\bigr]  |  
| --- | --- |  
| ⩽​​+.\displaystyle\leqslant L_{f}\frac{1}{K}\sum_{k=1}^{K}\sqrt{s_{k}+\gamma_{M}}+L_{f}\sqrt{\rho+\gamma_{M}}.  |  
Since u\mapsto\sqrt{u} is concave, Jensen’s inequality gives  
| ⩽=.\frac{1}{K}\sum_{k=1}^{K}\sqrt{s_{k}+\gamma_{M}}\leqslant\sqrt{\frac{1}{K}\sum_{k=1}^{K}(s_{k}+\gamma_{M})}=\sqrt{\frac{1}{K}\sum_{k=1}^{K}s_{k}+\gamma_{M}}.  |  
| --- |  
Substituting this into () yields  
| ​−⩽​+.\frac{1}{K}\sum_{k=1}^{K}F(w^{*},\psi_{k})-\phi^{*}\leqslant L_{f}\sqrt{\frac{1}{K}\sum_{k=1}^{K}s_{k}+\gamma_{M}}+L_{f}\sqrt{\rho+\gamma_{M}}.  |  
| --- |  
By Lemma ,  
| ⩽.\frac{1}{K}\sum_{k=1}^{K}s_{k}\leqslant\rho+\frac{C_{K}}{\sqrt{K}}.  |  
| --- |  
Substituting this bound into () gives  
| ​−⩽+.\frac{1}{K}\sum_{k=1}^{K}F(w^{*},\psi_{k})-\phi^{*}\leqslant L_{f}\sqrt{\rho+\gamma_{M}+\frac{C_{K}}{\sqrt{K}}}+L_{f}\sqrt{\rho+\gamma_{M}}.  |  
| --- |  
Finally, using  
| ⩽,\sqrt{a+b}\leqslant\sqrt{a}+\frac{b}{2\sqrt{a}}\qquad(a>0,\ b\geqslant 0),  |  
| --- |  
with a=\rho+\gamma_{M} and b=C_{K}/\sqrt{K}, we have  
| ⩽+.\sqrt{\rho+\gamma_{M}+\frac{C_{K}}{\sqrt{K}}}\leqslant\sqrt{\rho+\gamma_{M}}+\frac{C_{K}}{2\sqrt{(\rho+\gamma_{M})K}}.  |  
| --- |  
Substituting this into () gives  
| ​−⩽+=.\frac{1}{K}\sum_{k=1}^{K}F(w^{*},\psi_{k})-\phi^{*}\leqslant 2L_{f}\sqrt{\rho+\gamma_{M}}+\frac{L_{f}C_{K}}{2\sqrt{(\rho+\gamma_{M})K}}=\mathcal{R}_{K}.  |  
| --- |  
By Theorem ,  
| =F​(,)⩽​+.\phi(w^{(t)})=F(w^{(t)},\psi^{*}(w^{(t)}))\leqslant\frac{1}{K}\sum_{k=1}^{K}F(w^{(t)},\psi_{k})+\Delta_{K}.  |  
| --- |  
Combining (), (), and () gives  
| \displaystyle\phi(w^{(t)})-\phi^{*}  | ⩽​−+\displaystyle\leqslant\frac{1}{K}\sum_{k=1}^{K}F(w^{(t)},\psi_{k})-\phi^{*}+\Delta_{K}  |  
| --- | --- |  
| =​[−]+(​−)+\displaystyle=\frac{1}{K}\sum_{k=1}^{K}\bigl[F(w^{(t)},\psi_{k})-F(w^{*},\psi_{k})\bigr]+\left(\frac{1}{K}\sum_{k=1}^{K}F(w^{*},\psi_{k})-\phi^{*}\right)+\Delta_{K}  |  
| ⩽​[−]++\displaystyle\leqslant\frac{1}{K}\sum_{k=1}^{K}\bigl[F(w^{(t)},\psi_{k})-F(w^{*},\psi_{k})\bigr]+\Delta_{K}+\mathcal{R}_{K}  |  
| ⩽⟨,⟩++.\displaystyle\leqslant\langle\hat{g}^{(t)},w^{(t)}-w^{*}\rangle+\Delta_{K}+\mathcal{R}_{K}.  |  
which proves ().
Now use the projected outer update  
| =​().w^{(t+1)}=\Pi_{\mathcal{W}}\bigl(w^{(t)}-\eta_{w}\hat{g}^{(t)}\bigr).  |  
| --- |  
By nonexpansiveness of projection and, using Assumption , ⩽⩽\|\hat{g}^{(t)}\|\leqslant K^{-1}\sum_{k}\|\hat{g}_{k}\|\leqslant G_{w},  
| \displaystyle\|w^{(t+1)}-w^{*}\|^{2}  | ⩽‖−−‖2\displaystyle\leqslant\|w^{(t)}-\eta_{w}\hat{g}^{(t)}-w^{*}\|^{2}  |  
| --- | --- |  
| =−2​​⟨,⟩+\displaystyle=\|w^{(t)}-w^{*}\|^{2}-2\eta_{w}\langle\hat{g}^{(t)},w^{(t)}-w^{*}\rangle+\eta_{w}^{2}\|\hat{g}^{(t)}\|^{2}  |  
| ⩽−2​​⟨,⟩+.\displaystyle\leqslant\|w^{(t)}-w^{*}\|^{2}-2\eta_{w}\langle\hat{g}^{(t)},w^{(t)}-w^{*}\rangle+\eta_{w}^{2}G_{w}^{2}.  |  
Rearranging and using (),  
| ⩽−+++.\phi(w^{(t)})-\phi^{*}\leqslant\frac{\|w^{(t)}-w^{*}\|^{2}-\|w^{(t+1)}-w^{*}\|^{2}}{2\eta_{w}}+\frac{\eta_{w}G_{w}^{2}}{2}+\Delta_{K}+\mathcal{R}_{K}.  |  
| --- |  
Summing () over t=1,\ldots,T and using \|w^{(1)}-w^{*}\|\leqslant D_{\mathcal{W}} gives  
| ​⩽+++.\frac{1}{T}\sum_{t=1}^{T}[\phi(w^{(t)})-\phi^{*}]\leqslant\frac{D_{\mathcal{W}}^{2}}{2\eta_{w}T}+\frac{\eta_{w}G_{w}^{2}}{2}+\Delta_{K}+\mathcal{R}_{K}.  |  
| --- |  
By convexity of ,  
| ⩽​.\phi(\bar{w}^{(T)})\leqslant\frac{1}{T}\sum_{t=1}^{T}\phi(w^{(t)}).  |  
| --- |  
Therefore,  
| ⩽+++.\phi(\bar{w}^{(T)})-\phi^{*}\leqslant\frac{D_{\mathcal{W}}^{2}}{2\eta_{w}T}+\frac{\eta_{w}G_{w}^{2}}{2}+\Delta_{K}+\mathcal{R}_{K}.  |  
| --- |  
Finally, substituting  
| \eta_{w}=\frac{D_{\mathcal{W}}}{G_{w}\sqrt{T}}  |  
| --- |  
gives  
| +=.\frac{D_{\mathcal{W}}^{2}}{2\eta_{w}T}+\frac{\eta_{w}G_{w}^{2}}{2}=\frac{D_{\mathcal{W}}G_{w}}{\sqrt{T}}.  |  
| --- |  
Substituting the definitions of \Delta_{K} and \mathcal{R}_{K} yields  
| \displaystyle\phi(\bar{w}^{(T)})-\phi^{*}\leqslant  | +​\displaystyle\frac{D_{\mathcal{W}}G_{w}}{\sqrt{T}}+\frac{\max\\{\rho,4R^{2}\\}\mu^{(1)}}{\sqrt{K}}  |  
| --- | --- |  
| ++,\displaystyle+\frac{L_{f}C_{K}}{2\sqrt{(\rho+\gamma_{M})K}}+2L_{f}\sqrt{\rho+\gamma_{M}},  |  
which is the desired bound. ∎
##  Appendix B Experimental Details
We evaluate GDRO on two downstream decision problems. The first is contextual newsvendor, where the decision is convex and the optimal order for a fixed scenario distribution has a weighted-quantile form. We study this task on both a synthetic benchmark, used to validate the rare-tail mechanism under a known data-generating process, and the real M5 retail demand dataset. The second downstream problem is robot navigation among pedestrians, where the decision is nonconvex and the nominal model is the official implicit SocialGAN trajectory generator. Across all experiments, the nominal generator defines P_{0}^{x}, the adversarial generator defines Q_{\psi}^{x}, and each method chooses a decision w\in\mathcal{W} before the realized outcome is revealed.
###  B.1 Baselines and Solvers
All methods use the same fitted nominal generator within each benchmark. They differ only in how they form the scenario distribution used by the downstream decision solver.
#### Nominal.
The nominal baseline optimizes the decision using Monte Carlo samples from P_{0}^{x}. This is the standard sample-average decision induced by the fitted generator.
#### KL.
The KL baseline follows the empirical -divergence DRO formulation of Namkoong and Duchi [2016]. At each context, it keeps the nominal sample cloud fixed and adversarially reweights the samples within a KL ball. For a fixed decision, the KL-constrained worst-case weights have the exponential-tilt form [Hu and Hong, 2013]; we choose the tilt temperature to match the prescribed radius. The downstream decision is then updated under the weighted samples: by weighted critical quantiles for newsvendor and by weighted first-order optimization for SocialGAN. Thus this baseline can emphasize high-loss nominal samples but cannot create outcomes outside the nominal sample cloud.
#### W2.
The W2 baseline adapts the adversarial sample-perturbation idea of Sinha et al. [2018] to the downstream decision stage as a finite-sample Wasserstein-2 robustness baseline. Given nominal scenarios from P_{0}^{x}, we introduce adversarial support points and move them directly in 𝒴\mathcal{Y} to increase the downstream loss, while controlling their average squared displacement from the nominal cloud, i.e., the sample-wise empirical W_{2}^{2} transport cost. Unlike the penalized robust-training objective in Sinha et al. [2018], we use a primal–dual update for an explicit transport-radius constraint, so that the baseline is comparable to the radius-constrained GDRO formulation. The downstream decision is then updated against the perturbed scenario cloud. This gives a uniform finite-sample W2 baseline for both the multi-product newsvendor task and the nonconvex SocialGAN planning task. Unlike GDRO, however, the adversarial scenarios are free support points in 𝒴\mathcal{Y} rather than samples produced by the chosen generator family.
#### GAS-DRO.
For the newsvendor experiments, we include a conditional version of GAS-DRO [Wen and Yang, 2026]. The adversarial model uses the same conditional decoder architecture as the nominal generator and is optimized at the active context. Its ambiguity set is controlled by the GAS-DRO reconstruction certificate, computed over conditional training pairs. We denote by the value of this reconstruction certificate for the fitted nominal generator on the training set, and set GAS-DRO radii as multiples of in the experiments below. We include this baseline only when an explicit decoder is available; we do not apply it to SocialGAN, whose released nominal model is an implicit trajectory sampler.
#### GDRO.
We use the empirical context-local Sinkhorn formulation from Section . The nominal generator is frozen, the adversarial generator is initialized from the nominal architecture, and the inner player updates adversarial generator parameters subject to the Sinkhorn certificate at the active context. The decision update uses the average outer subgradient over the active inner adversaries. All Sinkhorn divergences are computed with GeomLoss[Feydy et al., 2019] using and blur across experiments. Task-specific radii, sample sizes, and optimization budgets are listed in the configuration tables below.
#### Radius and optimization budget.
For the synthetic newsvendor experiment, we use fixed radii for KL, W2, and GDRO because the simulator is used as a controlled mechanism study. For the real-data experiments, the robustness level is adapted to the active context. In M5, we compute a historical average-cost risk score from the observed demand history and use its training-set and quantiles as low- and high-risk anchors. In SocialGAN, we use the nominal collision probability of the nominal robot plan as the risk score. The KL, W2, and GDRO radii are increased for high-risk contexts and decreased for low-risk contexts by a monotone validation-calibrated rule. The inner optimization budget is adapted in the same direction: high-risk contexts receive more adversarial updates, while low-risk contexts use a smaller budget. These adaptations use only the observed context and nominal generated scenarios, never realized test outcomes.
###  B.2 Synthetic Contextual Newsvendor
#### Motivation.
The synthetic benchmark is designed to test a specific failure mode of nominal generative decision-making: a conditional generator may fit the bulk of the demand distribution while underrepresenting rare, high-cost demand tails. The data-generating process therefore contains frequent base contexts and rare contexts in which a tail component may activate. This lets us evaluate decisions against the true conditional law while still requiring every method to make decisions from the same learned nominal generator.
#### Data-generating process.
We generate product demands from contexts x\in\mathbb{R}^{5}, with  
| x\sim\mathcal{N}(0,I).  |  
| --- |  
A context is rare if  
| =,\mathrm{rare}(x)=\mathbf{1}\\{a^{\top}x>\tau\\},  |  
| --- |  
where is a fixed unit vector and is the training quantile of a^{\top}x.
Demand is generated through a latent factor h\in\mathbb{R}^{2}. In the base component,  
| .h\mid x\sim\mathcal{N}(Ax,\Sigma_{h}).  |  
| --- |  
In rare contexts, a tail component is activated with probability =0.10\pi_{\mathrm{tail}}=0.10:  
| ∼𝒩​(,),.h\mid x,\mathrm{tail}\sim\mathcal{N}(Ax+\Delta_{h},\Sigma_{\mathrm{tail}}),\qquad\Delta_{h}=(2.0,0).  |  
| --- |  
Frequent contexts always use the base component. For product , the latent score is  
| =++++​+,,s_{j}(x,h)=b_{j}+r_{j}^{\top}x+\beta_{j}h_{1}+\gamma_{j}h_{2}+a_{j}^{\sin}\sin(v_{j}^{\top}h)+\varepsilon_{j},\qquad\varepsilon_{j}\sim\mathcal{N}(0,\sigma_{\varepsilon}^{2}),  |  
| --- |  
and demand is  
| =+​softplus​.Y_{j}=\mu_{0}+\mu_{1}\,\mathrm{softplus}(s_{j}(x,h)).  |  
| --- |  
We use \sigma_{\varepsilon}=0.15, \mu_{0}=10, and \mu_{1}=5. Product parameters share group-level structure plus product-specific perturbations, inducing correlated nonlinear demands across products.
#### Nominal generator.
The nominal model is a conditional VAE trained on samples from the data-generating process. The context is provided to the encoder and decoder. Demand is standardized for VAE training, but generated samples are transformed back to demand units before the downstream decision and evaluation. The full synthetic newsvendor configuration is summarized in Table .
#### Downstream decision.
The decision is the order vector w\in\mathbb{R}_{+}^{20}. The loss is the multi-product newsvendor cost  
| =+.f(w,Y)=\sum_{j=1}^{20}c_{u,j}(Y_{j}-w_{j})_{+}+c_{o,j}(w_{j}-Y_{j})_{+}.  |  
| --- |  
For any weighted empirical scenario cloud, the optimal decision is the per-product weighted critical quantile with critical ratio /c_{u,j}/(c_{u,j}+c_{o,j}). The oracle is computed using simulator samples from the true conditional law at the same context and is used only for evaluation.
Synthetic contextual newsvendor configuration.  
| Context dimension  |  
| --- |  
| DGP latent dimension  |  
| Rare-context threshold  |  quantile of a^{\top}x  |  
| Tail probability in rare contexts  |  
| Tail shift  | (2.0,0)  |  
| Observation noise  |  
| Demand scale (\mu_{0},\mu_{1})  |  
| Train / validation / test contexts  | 2000/500/2002000/500/200  |  
| Underage costs   | Uniform on [15,25]  |  
| Overage costs   | Uniform on   |  
| Nominal generator  | Conditional VAE  |  
| VAE latent dimension  |  
| VAE hidden width  |  
| VAE epochs  |  
| VAE learning rate  |  
| VAE KL weight  |  
| Nominal/KL samples per context  |  
| GDRO/W2/GAS-DRO samples per context  |  
| KL radius  |  
| GDRO radius  |  
| W2 radius  |  
| GAS-DRO radius  | 0.2J_{0}  |  
###  B.3 M5 Retail Newsvendor
#### Dataset and product selection.
The M5 experiment uses real retail demand from the M5 forecasting benchmark [Makridakis et al., 2022]. Our goal in this experiment is not to compete on the full M5 forecasting task, but to obtain a stable real-data nominal generator for testing the downstream newsvendor decision mechanism. We therefore construct a contextual multi-product newsvendor task from historical sales, and select products from the chosen M5 subset whose nonzero demand ratio is at least . This keeps the task multivariate while avoiding products dominated by zeros, which would make conditional scenario generation unstable and obscure the effect of the robust decision layer.
#### Downstream decision.
The downstream decision is the same multi-product newsvendor decision as in Appendix . Let =Y_{t}=(Y_{t,1},\ldots,Y_{t,p})^{\top} denote the realized demand vector for products on day , and let =∈w_{t}=(w_{t,1},\ldots,w_{t,p})^{\top}\in\mathbb{R}_{+}^{p} denote the order decision. The held-out realized loss is  
| =​+​.f(w_{t},Y_{t})=\sum_{j=1}^{20}c_{u,j}(Y_{t,j}-w_{t,j})_{+}+c_{o,j}(w_{t,j}-Y_{t,j})_{+}.  |  
| --- |  
For any weighted empirical scenario cloud, the decision is computed by the per-product weighted critical quantile.
#### Nominal generator.
The nominal model is a conditional VAE–LSTM demand generator. For each day , the input context is a historical demand window. A single-layer LSTM encodes this history into a temporal representation \widehat{H}_{t}. During training, the VAE encoder conditions on (\widehat{H}_{t},Y_{t}) and learns an approximate posterior over the latent variable. At generation time, the future demand is not observed; latent variables are sampled from the learned conditional prior given \widehat{H}_{t}, and the decoder produces next-day demand scenarios. The nominal CVAE–LSTM architecture is illustrated in Figure .
Nominal CVAE–LSTM generator for M5 demand scenarios. The LSTM encodes the historical demand window into \widehat{H}_{t}. During training, the encoder uses (\widehat{H}_{t},Y_{t}); during generation, latent variables are sampled from the conditional prior given \widehat{H}_{t} and decoded into next-day demand scenarios. 
#### Adaptive robustness.
Unlike the synthetic benchmark, M5 does not provide a known simulator mechanism for identifying rare-tail contexts. We therefore adapt the robustness level using a risk score computed from the same newsvendor objective as the downstream task. For each context , corresponding to a historical demand window, we compute as the average realized newsvendor cost over that window under the same underage and overage costs used for evaluation. Let r_{0.10} and r_{0.90} be the training-set and quantiles of this score, and define  
| =[−].\alpha(x)=\left[\frac{r(x)-r_{0.10}}{r_{0.90}-r_{0.10}}\right]_{[0,1]}.  |  
| --- |  
The KL, W2, and GDRO radii are interpolated between their low- and high-risk values using \alpha(x). For methods with adversarial inner optimization, the inner-loop budget is increased using the same risk score. All thresholds, radius endpoints, and optimization budgets are chosen on validation contexts. The full M5 configuration is summarized in Table .
M5 retail newsvendor configuration.  
|  Historical window length  |  
| --- |  
|  Input-context shape  | 10\times 20  |  
|  Forecast horizon  |  
|  Train / validation / test contexts  | 1500/100/3001500/100/300  |  
|  Nominal generator  | Conditional VAE–LSTM  |  
|  LSTM hidden-state dimension  |  
|  VAE latent dimension  |  
|  VAE hidden dimension  |  
|  Maximum VAE epochs  |  
|  Early-stopping patience  |  
|  VAE batch size  |  
|  VAE learning rate  | 5\times 10^{-4}  |  
|  VAE weight decay  |  
|  VAE KL weight  |  
|  Prior-mean loss weight  |  
|  Nominal/KL samples per context  |  
|  GDRO/W2/GAS–DRO samples per context  |  
|  Underage costs   |  
|  Overage costs   |  
| [0.14,1.99][0.14,1.99]  |  
| [1.0,58.0][1.0,58.0]  |  
| [38.0,75.0][38.0,75.0]  |  
|  GAS–DRO radius  | 0.80J_{0}  |  
###  B.4 SocialGAN Robot Navigation
#### Nominal model and data.
We use the official pretrained SocialGAN pedestrian trajectory model and the ETH/UCY benchmark protocol from Gupta et al. [2018]. The model observes frames of pedestrian history and generates future frames. We use the released SocialGAN predictor and its test split, without retraining the trajectory generator.
#### Downstream decision.
The robot navigation task is added by us on top of the SocialGAN prediction setting. At a test context , the robot observes the same past pedestrian trajectories as SocialGAN. It then chooses a -step velocity plan  
| ,,w=(u_{1},\ldots,u_{12}),\qquad u_{t}\in\mathbb{R}^{2},  |  
| --- |  
before the true pedestrian futures are revealed. The robot follows single-integrator dynamics from a sampled start point to a sampled goal, with each velocity projected onto a maximum-speed ball. Optimization uses generated pedestrian futures from the nominal or robust model; evaluation uses the true held-out pedestrian futures.
#### Planning objective and evaluation.
For a pedestrian-future scenario Y=Y=\\{y_{j,t}\\}_{j=1,t=1}^{N,T}, the robot decision is a -step velocity plan  
| ,.w=(u_{1},\ldots,u_{T}),\qquad u_{t}\in\mathbb{R}^{2},\qquad T=12.  |  
| --- |  
Starting from , the induced robot path is  
| =,.r_{t}(w)=s+\sum_{\ell=1}^{t}u_{\ell},\qquad\|u_{t}\|_{2}\leqslant v_{\max}.  |  
| --- |  
The speed constraint is enforced by projecting each velocity vector onto the Euclidean ball of radius v_{\max}. Let be the sampled goal and let \bar{r}_{t} be the straight-line reference path from to . The smooth loss optimized by all methods has the form  
| \displaystyle f(w,Y)=  | ​​+​⏟progress and terminal arrival\displaystyle\underbrace{\lambda_{p}{1\over T}\sum_{t=1}^{T}\|r_{t}(w)-g\|_{2}^{2}+\lambda_{T}\|r_{T}(w)-g\|_{2}^{2}}_{\text{progress and terminal arrival}}  |  
| --- | --- |  
| +​​⏟weak reference-path tracking\displaystyle+\underbrace{\lambda_{\rm tr}{1\over T}\sum_{t=1}^{T}\|r_{t}(w)-\bar{r}_{t}\|_{2}^{2}}_{\text{weak reference-path tracking}}  |  
| +​​+​​⏟control effort and smoothness\displaystyle+\underbrace{\lambda_{u}{1\over T}\sum_{t=1}^{T}\|u_{t}\|_{2}^{2}+\lambda_{s}{1\over T-1}\sum_{t=2}^{T}\|u_{t}-u_{t-1}\|_{2}^{2}}_{\text{control effort and smoothness}}  |  
| +softplus(−)2⏟differentiable collision barrier.\displaystyle+\underbrace{\lambda_{c}{1\over T}\sum_{t=1}^{T}\operatorname{softplus}\left({r_{\rm safe}-\widetilde{d}_{t}(w,Y)\over\tau_{b}}\right)^{2}}_{\text{differentiable collision barrier}}.  |  
Here  
| =−​log​exp⁡(−)\widetilde{d}_{t}(w,Y)=-\tau_{d}\log\sum_{j=1}^{N}\exp\left(-{\|r_{t}(w)-y_{j,t}\|_{2}\over\tau_{d}}\right)  |  
| --- |  
is a soft-min approximation of the nearest-pedestrian distance at time . The first line encourages the robot to make progress and arrive at the goal by the end of the horizon. The second line weakly discourages unnecessary detours. The third line penalizes large and rapidly changing velocities. The last line is a smooth safety barrier: it becomes large when the robot comes within the safety radius r_{\rm safe} of a sampled pedestrian future. Nominal, W2, and GDRO optimize the average of over their corresponding scenario clouds, while KL optimizes a weighted average under adversarial sample weights.
For final evaluation, we use the true held-out pedestrian future and a hard, non-differentiable score that prioritizes safety and arrival:  
| Eval​=\displaystyle\mathrm{Eval}(w,Y^{\rm true})=  | ​𝟏​+​𝟏​\displaystyle\;C_{\rm col}\mathbf{1}\\{d_{\min}<r_{\rm col}\\}+C_{\rm near}\mathbf{1}\\{d_{\min}<r_{\rm near}\\}  |  
| --- | --- |  
| +​𝟏​+++.\displaystyle+C_{\rm fail}\mathbf{1}\\{t_{\rm arr}=-1\\}+c_{\rm time}\widetilde{t}_{\rm arr}+c_{\rm len}L_{\rm path}+c_{\rm dev}D_{\rm ref}.  |  
Here d_{\min} is the minimum robot–pedestrian distance before arrival, t_{\rm arr} is the first frame at which ⩽\|r_{t}(w)-g\|_{2}\leqslant r_{\rm arr}, \widetilde{t}_{\rm arr}=t_{\rm arr} if the robot arrives and otherwise, L_{\rm path} is path length until arrival, and D_{\rm ref} is average deviation from the straight-line reference. Once the robot reaches the goal, later pedestrian motion is not counted as a collision. This hard score is used only for reporting; optimization uses the smooth loss above.
#### Fixed task set.
We uniformly select contexts from the SocialGAN test split. For each selected context, we generate start–goal queries, giving fixed robot tasks. Queries are selected using only nominal SocialGAN samples: the straight-line robot path must have nominal collision probability in [0.60,0.90][0.60,0.90] under a screening radius , and the start and goal locations must be initially clear of pedestrians. The evaluation collision radius is . Thus the benchmark focuses on nontrivial planning instances without using true future trajectories during task construction.
#### Adaptive radius and budget.
For each query, we first solve the nominal robot plan and estimate its nominal collision probability \widehat{p} using generated futures and the evaluation collision radius. The GDRO and W2 radii are chosen by the clipped linear rule  
| =+​[],\rho(\widehat{p})=\rho_{\min}+(\rho_{\max}-\rho_{\min})\left[\frac{\widehat{p}-p_{\min}}{p_{\max}-p_{\min}}\right]_{[0,1]},  |  
| --- |  
with \rho_{\min}=0.5, \rho_{\max}=3.0, p_{\min}=0.05, and p_{\max}=0.50. The KL radius is adapted by the same rule from to . The GDRO optimization budget is also adapted using \widehat{p}: low-risk queries use the smaller budget in Table , while high-risk queries use the larger budget. All adaptive quantities use only the observed context and nominal generated futures, never the realized test future.
SocialGAN robot navigation configuration.  
| Nominal model  | Official SocialGAN [Gupta et al., 2018]  |  
| --- | --- |  
| Dataset protocol  | ETH/UCY SocialGAN test split  |  
| Observed / predicted frames  |  
| Selected test contexts  |  uniformly selected contexts  |  
| Queries per context  |  
| Total robot tasks  |  
| Robot decision horizon   |  
| Robot decision   |  two-dimensional velocity controls  |  
| Robot dynamics  | r_{t}=s+\sum_{\ell=1}^{t}u_{\ell}  |  
| Robot speed limit v_{\max}  |  reference pedestrian speed  |  
| Velocity constraint  | Projection to \|u_{t}\|_{2}\leqslant v_{\max}  |  
| Straight-line screening probability  | [0.60,0.90][0.60,0.90]  |  
| Screening collision radius  |  
| Evaluation collision radius r_{\rm col}  |  
| Near-miss radius r_{\rm near}  |  
| Arrival radius r_{\rm arr}  |  
| Nominal SocialGAN samples per context  |  
| Nominal plan steps  |  
| GDRO/W2 robust samples per context  |  fixed noise samples  |  
| GDRO/W2 radius range   | [0.5,3.0]  |  
| KL radius range  | [0.1,0.7]  |  
| Risk anchors (p_{\min},p_{\max})  | (0.05,0.50)(0.05,0.50)  |  
| Low-risk GDRO budget  |  outer, dual cycles, adversary steps  |  
| High-risk GDRO budget  |  outer, dual cycles, adversary steps  |  
| Controls updates per outer step  |  
| Sinkhorn blur ε\varepsilon  |  
| Loss scale in adversarial update  |  
| Progress weight \lambda_{p}  |  
| Terminal arrival weight \lambda_{T}  |  
| Reference tracking weight \lambda_{\rm tr}  |  
| Control effort weight \lambda_{u}  |  
| Control smoothness weight \lambda_{s}  |  
| Collision barrier weight \lambda_{c}  |  
| Safety radius in smooth loss r_{\rm safe}  |  
| Barrier temperature   |  
| Soft-min temperature   |  
| Decision learning rate  |  
| Adversarial generator learning rate  |  
| Initial dual value / GDRO dual learning rate  | 5.0/10.05.0/10.0  |  
| Gradient clipping  |  
| W2 support-point learning rate  |  
| W2 dual learning rate  |  
| W2 outer / support / control steps  | 180/15/5  |  
| Evaluation collision penalty C_{\rm col}  |  
| Evaluation near-miss penalty C_{\rm near}  |  
| Evaluation failure penalty C_{\rm fail}  |  
| Evaluation time / path / deviation weights (,,)(c_{\rm time},c_{\rm len},c_{\rm dev})  | 1.0/1.0/0.21.0/1.0/0.2  |
