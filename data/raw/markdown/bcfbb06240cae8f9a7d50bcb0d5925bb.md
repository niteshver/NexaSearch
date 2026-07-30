Skip to main content
Press Enter to search · Advanced search
# Computer Science > Artificial Intelligence
**arXiv:2607.25532** (cs) 
[Submitted on 28 Jul 2026]
#  Title:Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners
Authors:Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz, Sotirios Tsaftaris
View a PDF of the paper titled Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners, by Athanasios Vlontzos and 3 other authors
View PDF HTML (experimental)
> Abstract:Consider a model trained at a single hospital to predict patient recovery, where the measured feature bundles the patient's true health signal () with a systematic artefact from that hospital's equipment (). Within that hospital, the artefact correlates with outcomes through unmeasured confounders such as patient demographics; an in-context learner rationally routes predictions through , not , and fails silently when deployed at a new hospital with different equipment. We formalise this as \emph{spurious routing in composite representations}: when a feature encodes a causal signal and a spurious signal in distinct subspaces, the ICL cannot determine which drives predictions. We prove that under ridge ICL, a linear in-context learner, this routing is unavoidable regardless of context size; TabPFN, a state-of-the-art pretrained tabular ICL model, shows qualitatively consistent behaviour empirically. We derive a closed-form characterisation, , confirmed at for linear ICL and for TabPFN. Contrary to intuition, larger context sharpens commitment to the dominant in-context signal, amplifying spurious routing by up to ; in the high-spurious corner, more expressive models show greater vulnerability empirically ( CSR gap at high entanglement). We introduce two lightweight mitigations: environment-stratified context construction and S-swap augmentation, that require only weak environment labels and no knowledge of the causal partition. S-swap reduces spurious routing by for linear ICL and for TabPFN, with TabPFN's causal sensitivity increasing simultaneously: the model does not become agnostic, it reroutes through the causal signal.   
| Subjects:  |  Artificial Intelligence (cs.AI)  |  
| --- | --- |  
| Cite as:  |   |  
| (or for this version)   |  
|  Focus to learn more arXiv-issued DOI via DataCite (pending registration)  |  
## Submission history
From: Athanasios Vlontzos [view email] **[v1]** Tue, 28 Jul 2026 10:17:59 UTC (41 KB) 
Full-text links:
## Access Paper:
View a PDF of the paper titled Entangled by Design: Spurious Intra-Variable Signal Routing in Tabular In-Context Learners, by Athanasios Vlontzos and 3 other authors


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
