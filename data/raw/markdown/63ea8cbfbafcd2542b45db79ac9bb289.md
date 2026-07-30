Skip to main content
Press Enter to search · Advanced search
# Computer Science > Artificial Intelligence
**arXiv:2607.23929** (cs) 
[Submitted on 27 Jul 2026 (v1), last revised 28 Jul 2026 (this version, v2)]
#  Title:MemTX: Transactional Belief Commit for Stateful Agent Memory
Authors:Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Mingkai Zheng, Taotao Cai
View a PDF of the paper titled MemTX: Transactional Belief Commit for Stateful Agent Memory, by Xiaoyang Li and 7 other authors
View PDF HTML (experimental)
> Abstract:LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each record carries evidence, permissions, provenance, and validity. Writes are staged inside snapshot-isolated transactions and admitted by a validate-and-commit pipeline, irreversible tool calls are gated on in-flight belief state, and retracting a belief triggers typed cascading repair of its derived records and tool side effects. Two invariants, action-safety gating and cascade-repair completeness, are machine-checked by property-based testing and bounded exhaustive enumeration of 5.5 million protocol states, with zero violations. Across five backbones from three model families, MemTX leads all eight baselines with paired-McNemar significance on four backbones and statistically ties the best baseline on the fifth and strongest, while remaining the only method with zero downstream harm on every backbone. Backbone capability does not substitute for commit discipline.   
| Comments:  | Preprint  |  
| --- | --- |  
| Subjects:  |  Artificial Intelligence (cs.AI)  |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite  |  
## Submission history
From: Xiaoyang Li [view email] Mon, 27 Jul 2026 01:57:39 UTC (297 KB) **[v2]** Tue, 28 Jul 2026 12:51:37 UTC (297 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled MemTX: Transactional Belief Commit for Stateful Agent Memory, by Xiaoyang Li and 7 other authors


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
