Skip to main content
arXiv is now an independent nonprofit! Learn more ×
Press Enter to search · Advanced search
# Computer Science > Computers and Society
**arXiv:1912.05652** (cs) 
[Submitted on 5 Dec 2019 (v1), last revised 24 Mar 2021 (this version, v2)]
#  Title:Learning Human Objectives by Evaluating Hypothetical Behavior
Authors:Siddharth Reddy, Anca D. Dragan, Sergey Levine, Shane Legg, Jan Leike
View a PDF of the paper titled Learning Human Objectives by Evaluating Hypothetical Behavior, by Siddharth Reddy and 4 other authors
View PDF
> Abstract:We seek to align agent behavior with a user's objectives in a reinforcement learning setting with unknown dynamics, an unknown reward function, and unknown unsafe states. The user knows the rewards and unsafe states, but querying the user is expensive. To address this challenge, we propose an algorithm that safely and interactively learns a model of the user's reward function. We start with a generative model of initial states and a forward dynamics model trained on off-policy data. Our method uses these models to synthesize hypothetical behaviors, asks the user to label the behaviors with rewards, and trains a neural network to predict the rewards. The key idea is to actively synthesize the hypothetical behaviors from scratch by maximizing tractable proxies for the value of information, without interacting with the environment. We call this method reward query synthesis via trajectory optimization (ReQueST). We evaluate ReQueST with simulated users on a state-based 2D navigation task and the image-based Car Racing video game. The results show that ReQueST significantly outperforms prior methods in learning reward models that transfer to new environments with different initial state distributions. Moreover, ReQueST safely trains the reward model to detect unsafe states, and corrects reward hacking before deploying the agent.   
| Comments:  | Published at International Conference on Machine Learning (ICML) 2020  |  
| --- | --- |  
| Subjects:  |  Computers and Society (cs.CY); Machine Learning (cs.LG); Machine Learning (stat.ML)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Siddharth Reddy [view email] Thu, 5 Dec 2019 18:25:48 UTC (1,349 KB) **[v2]** Wed, 24 Mar 2021 22:26:35 UTC (1,349 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Learning Human Objectives by Evaluating Hypothetical Behavior, by Siddharth Reddy and 4 other authors


### Current browse context:
cs.CY
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
