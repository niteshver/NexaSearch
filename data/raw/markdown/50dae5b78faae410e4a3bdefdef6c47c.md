Skip to main content
Press Enter to search · Advanced search
# Computer Science > Computer Vision and Pattern Recognition
**arXiv:2406.02021** (cs) 
[Submitted on 4 Jun 2024 (v1), last revised 28 Jul 2026 (this version, v3)]
#  Title:FFNet: MetaMixer-based Efficient Convolutional Mixer Design
View a PDF of the paper titled FFNet: MetaMixer-based Efficient Convolutional Mixer Design, by Seokju Yun and 2 other authors
View PDF HTML (experimental)
> Abstract:Transformer, composed of self-attention and Feed-Forward Network, has revolutionized the landscape of network design across various vision tasks. While self-attention is extensively explored as a key factor in performance, FFN has received little attention. FFN is a versatile operator seamlessly integrated into nearly all AI models to effectively harness rich representations. Recent works also show that FFN functions like key-value memories. Thus, akin to the query-key-value mechanism within self-attention, FFN can be viewed as a memory network, where the input serves as query and the two projection weights operate as keys and values, respectively. Based on these observations, we hypothesize that the importance lies in query-key-value framework itself for competitive performance. To verify this, we propose converting self-attention into a more FFN-like efficient token mixer with only convolutions while retaining query-key-value framework, namely FFNification. Specifically, FFNification replaces query-key-value interactions with large kernel convolutions and adopts GELU activation function instead of softmax. The derived token mixer, FFNified attention, serves as key-value memories for detecting locally distributed spatial patterns, and operates in the opposite dimension to the ConvNeXt block within each corresponding sub-operation of the query-key-value framework. Building upon the above two modules, we present a family of Fast-Forward Networks (FFNet). Despite being composed of only simple operators, FFNet outperforms sophisticated and highly specialized methods in each domain, with notable efficiency gains. These results validate our hypothesis, leading us to propose MetaMixer, a general mixer architecture that does not specify sub-operations within the query-key-value framework.   
| Comments:  | Code:   |  
| --- | --- |  
| Subjects:  |  Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Seokju Yun [view email] Tue, 4 Jun 2024 07:00:14 UTC (7,428 KB) Mon, 10 Mar 2025 05:09:16 UTC (17,711 KB) **[v3]** Tue, 28 Jul 2026 06:09:43 UTC (15,750 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled FFNet: MetaMixer-based Efficient Convolutional Mixer Design, by Seokju Yun and 2 other authors


### Current browse context:
cs.CV
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
