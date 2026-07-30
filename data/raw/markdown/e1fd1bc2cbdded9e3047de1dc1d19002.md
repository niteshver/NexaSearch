Skip to main content
Press Enter to search · Advanced search
# Computer Science > Machine Learning
**arXiv:1812.05979** (cs) 
[Submitted on 14 Dec 2018]
#  Title:Scaling shared model governance via model splitting
Authors:Miljan Martic, Jan Leike, Andrew Trask, Matteo Hessel, Shane Legg, Pushmeet Kohli
View a PDF of the paper titled Scaling shared model governance via model splitting, by Miljan Martic and Jan Leike and Andrew Trask and Matteo Hessel and Shane Legg and Pushmeet Kohli
View PDF
> Abstract:Currently the only techniques for sharing governance of a deep learning model are homomorphic encryption and secure multiparty computation. Unfortunately, neither of these techniques is applicable to the training of large neural networks due to their large computational and communication overheads. As a scalable technique for shared model governance, we propose splitting deep learning model between multiple parties. This paper empirically investigates the security guarantee of this technique, which is introduced as the problem of model completion: Given the entire training data set or an environment simulator, and a subset of the parameters of a trained deep learning model, how much training is required to recover the model's original performance? We define a metric for evaluating the hardness of the model completion problem and study it empirically in both supervised learning on ImageNet and reinforcement learning on Atari and DeepMind~Lab. Our experiments show that (1) the model completion problem is harder in reinforcement learning than in supervised learning because of the unavailability of the trained agent's trajectories, and (2) its hardness depends not primarily on the number of parameters of the missing part, but more so on their type and location. Our results suggest that model splitting might be a feasible technique for shared model governance in some settings where training is very expensive.   
| Comments:  | 9 pages  |  
| --- | --- |  
| Subjects:  |  Machine Learning (cs.LG); Cryptography and Security (cs.CR); Neural and Evolutionary Computing (cs.NE)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Jan Leike [view email] **[v1]** Fri, 14 Dec 2018 15:29:21 UTC (145 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Scaling shared model governance via model splitting, by Miljan Martic and Jan Leike and Andrew Trask and Matteo Hessel and Shane Legg and Pushmeet Kohli


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
