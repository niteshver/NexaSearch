Skip to main content
Press Enter to search · Advanced search
# Computer Science > Artificial Intelligence
**arXiv:2607.25292** (cs) 
[Submitted on 28 Jul 2026]
#  Title:Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe
View a PDF of the paper titled Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe, by Chaemin Jang and 2 other authors
View PDF HTML (experimental)
> Abstract:Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. The same persona on the same question returns the same answer on more than half of items in a public-opinion benchmark. The collapse is sharp: the model's internal probabilities concentrate on a single option, and the failure is substantially amplified by instruction tuning: across three model families with materially different post-training pipelines, every instruction-tuned model fails on every task we test, while base models fail far less often. Strikingly, the same model that cannot sample from a distribution can describe it accurately in a single call. We call this gap the KNOWS/DOES split, and trace it to a degenerate sampling primitive visible in the logits and induced by alignment training. Exploiting this split, asking the model to describe the response distribution in one call more than halves the error against human survey data compared to persona aggregation. For applications that require per-persona outputs, we propose Prompt-Perturbed Argyle (PPA), which reduces the same error by 21% at no added cost.   
| Subjects:  |  Artificial Intelligence (cs.AI)  |  
| --- | --- |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite (pending registration)  |  
## Submission history
From: Chaemin Jang [view email] **[v1]** Tue, 28 Jul 2026 04:58:46 UTC (2,453 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe, by Chaemin Jang and 2 other authors


### Current browse context:
cs.AI
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
