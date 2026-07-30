Skip to main content
Press Enter to search · Advanced search
# Computer Science > Machine Learning
**arXiv:2607.23388** (cs) 
This paper has been withdrawn by Xin Wang
[Submitted on 25 Jul 2026 (v1), last revised 28 Jul 2026 (this version, v2)]
#  Title:Directional Influence Function: Estimating Training Data Influence in Constrained Learning
Authors:Xin Wang, R. Tyrrell Rockafellar, Xuegang (Jeff)Ban
View a PDF of the paper titled Directional Influence Function: Estimating Training Data Influence in Constrained Learning, by Xin Wang and 2 other authors
No PDF available, click to view other formats
> Abstract:As constrained learning becomes increasingly common, models are trained under explicit feasibility requirements to enforce fairness, safety, robustness, regulariza- tion, and physics or logic constraints. Understanding how training samples in- fluence the model solution (e.g., learned parameters) is crucial for interpretability and robustness. The classical influence function (IF) estimates sample contribu- tions via local sensitivity analysis, measuring how the solution changes when a specific training sample is perturbed or removed. However, IF becomes unreli- able in constrained settings: data perturbations can reshape both the objective and the feasible region, leading to estimates that violate feasibility. In response, we propose the Directional Influence Function (DIF), a novel estimator that explicitly incorporates these constraints into influence estimation. DIF formulates the opti- mality conditions of constrained learning as a variational inequality (VI) and ana- lyzes how perturbing training data affects this VI. We validate DIF on constrained linear regression and demonstrate that it recovers leave-one-out retraining results, whereas IF and penalty-based IF exhibit significant bias. We further apply DIF to fairness-constrained CNNs, where DIF accurately predicts test loss changes under data removal and aligns closely with actual retraining. Our results establish DIF as an efficient and reliable tool for data attribution in constrained learning.   
| Comments:  | _Need revision_  |  
| --- | --- |  
| Subjects:  |  Machine Learning (cs.LG); Artificial Intelligence (cs.AI)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Xin Wang [view email] Sat, 25 Jul 2026 22:50:09 UTC (170 KB) **[v2]** Tue, 28 Jul 2026 03:42:07 UTC (1 KB) _(withdrawn)_
Full-text links:
## Access Paper:
View a PDF of the paper titled Directional Influence Function: Estimating Training Data Influence in Constrained Learning, by Xin Wang and 2 other authors
  * Withdrawn


No license for this version due to withdrawn
### Current browse context:
cs.LG
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
IArxiv recommender toggle
IArxiv Recommender


About arXivLabs 
# arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? **Learn more about arXivLabs**.
Which authors of this paper are endorsers? | What is MathJax?) 
