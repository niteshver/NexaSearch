Skip to main content
Press Enter to search · Advanced search
# Computer Science > Sound
**arXiv:2607.17761** (cs) 
[Submitted on 20 Jul 2026 (v1), last revised 28 Jul 2026 (this version, v2)]
#  Title:Time-Frequency Consistency Learning for Robust Speech Deepfake Detection
Authors:Jun Xue, Zhuolin Yi, Yanzhen Ren, Yihuan Huang, Jiayu Xiong, Yi Chai, Guanxiang Feng, Jiajun Liu, Tong Zhang
View a PDF of the paper titled Time-Frequency Consistency Learning for Robust Speech Deepfake Detection, by Jun Xue and 8 other authors
View PDF HTML (experimental)
> Abstract:Recently, speech deepfake detection (SDD) has achieved significant progress. However, its robustness evaluation remains largely confined to controlled additive noise scenarios, lacking systematic investigation of the complex distortions introduced by acoustic front-end (AFE) processing pipelines in real-world deployments. In this work, we simulate a unified AFE pipeline comprising acoustic echo cancellation, noise suppression, automatic gain control, and voice activity detection (VAD), and conduct a comprehensive evaluation of current state-of-the-art models. The results show that the nonlinear and time-frequency coupled distortions introduced by AFE significantly degrade detection performance. To address this issue, we propose a Time-Frequency Consistency Learning (TFCL) framework, which aims to learn invariant spoofing representations that remain stable before and after AFE processing. We observe that AFE not only introduces temporal misalignment (e.g., segment-level shifts caused by VAD), but also weakens or distorts critical frequency-domain cues. To this end, TFCL employs an attention-driven soft alignment mechanism to capture cross-temporal dependencies, along with frequency-domain structural consistency constraints to enforce feature invariance. As a result, the model is able to maintain stable representations under both temporal perturbations and spectral distortions. Extensive experimental results demonstrate that the proposed method effectively mitigates the performance degradation caused by AFE processing, significantly improving the robustness of SDD in real-world scenarios. The code is available at   
| Comments:  | Accepted by ACM MM 2026  |  
| --- | --- |  
| Subjects:  |  Sound (cs.SD); Artificial Intelligence (cs.AI)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Jun Xue [view email] Mon, 20 Jul 2026 09:51:03 UTC (7,470 KB) **[v2]** Tue, 28 Jul 2026 04:55:06 UTC (7,471 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Time-Frequency Consistency Learning for Robust Speech Deepfake Detection, by Jun Xue and 8 other authors


### Current browse context:
cs.SD
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
