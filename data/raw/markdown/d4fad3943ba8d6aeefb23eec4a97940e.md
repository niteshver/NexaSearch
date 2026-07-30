Skip to main content
arXiv is now an independent nonprofit! Learn more ×
Press Enter to search · Advanced search
# Computer Science > Robotics
**arXiv:2606.24208** (cs) 
[Submitted on 23 Jun 2026]
#  Title:Grounding Generative Policies in Physics: Optimization-Guided Diffusion for Robot Control
Authors:Sabrina Bodmer, René Zurbrügg, Tifanny Portela, Hao Ma, Alexandre Didier, Marco Hutter, Colin Jones, Melanie Zeilinger
View a PDF of the paper titled Grounding Generative Policies in Physics: Optimization-Guided Diffusion for Robot Control, by Sabrina Bodmer and 7 other authors
View PDF HTML (experimental)
> Abstract:Diffusion models sample effectively from high-dimensional, multimodal distributions, but their outputs may violate deployment constraints. For task-space robot policies, generated grasps, waypoints, or trajectories can be distributionally valid yet infeasible, violating reachability, collision-avoidance, or closed-loop executability requirements. This embodiment gap limits zero-shot deployment across robots, even when the task-space behavior itself is transferable. We propose an inference-time optimization framework that couples the behavior generation to physical feasibility by formulating diffusion guidance as a constrained optimization problem. Our key insight is to replace the sampling perturbation in the backward process with an optimized correction, allowing hard constraints or soft penalties to be imposed during sampling without the need to retrain the diffusion model, while keeping samples close to the learned prior. We evaluate the method on dexterous grasp synthesis with reachability and collision-avoidance constraints, and dynamic manipulation with controller-level trackability constraints. Across settings and robot embodiments, optimization-guided denoising matches the feasibility of projection- and gradient-guidance baselines while better preserving grasp quality, and improving controller-level executability and task success, with task success improving by up to 20pp. on dexterous grasping and 23pp. on visuomotor manipulation over the best baseline.   
| Subjects:  |  Robotics (cs.RO)  |  
| --- | --- |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Sabrina Bodmer [view email] **[v1]** Tue, 23 Jun 2026 06:49:30 UTC (20,217 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Grounding Generative Policies in Physics: Optimization-Guided Diffusion for Robot Control, by Sabrina Bodmer and 7 other authors


### Current browse context:
cs.RO
Change to browse by: 
### References & Citations
export BibTeX citation Loading...
## BibTeX formatted citation
×
Data provided by: 
### Bookmark
Bibliographic Tools
# Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
Connected Papers Toggle
Connected Papers _(_
Litmaps Toggle
scite.ai Toggle
scite Smart Citations _(_
Code, Data, Media
# Code, Data and Media Associated with this Article
alphaXiv Toggle
Links to Code Toggle
CatalyzeX Code Finder for Papers _(_
DagsHub Toggle
GotitPub Toggle
Gotit.pub _(_
Huggingface Toggle
Hugging Face _(_
ScienceCast Toggle
ScienceCast _(_
Demos
# Demos
Replicate Toggle
Replicate _(_
Spaces Toggle
Hugging Face Spaces _(_
Spaces Toggle
Related Papers
# Recommenders and Search Tools
Link to Influence Flower
Influence Flower _(_
Core recommender toggle
CORE Recommender _(_


About arXivLabs 
# arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.
Which authors of this paper are endorsers? | What is MathJax?) 
