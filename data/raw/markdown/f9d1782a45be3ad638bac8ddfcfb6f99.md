![ACL Logo](https://aclanthology.org/images/acl-logo.svg) ACL Anthology ⟨1⟩
  * About⟨2⟩
    * Announcements⟨3⟩
    * Communication channels⟨4⟩
    * Related work⟨5⟩
    * Copyright⟨6⟩
    * * * *
    * Credits⟨7⟩
    * Volunteer⟨8⟩
    * Development⟨9⟩
    * Feedback⟨10⟩
  * Using⟨2⟩
    * Citing papers⟨11⟩
    * Links in the Anthology⟨12⟩
    * Data access⟨13⟩
    * * * *
    * All FAQs⟨14⟩
    * * * *
    * ###### Details
    * Anthology identifiers⟨15⟩
    * Names⟨16⟩
    * ORCID iDs⟨17⟩
    * DOIs⟨18⟩
    * Verified authors⟨19⟩
  * Contributions⟨2⟩
    * Submissions⟨20⟩
    * Corrections⟨21⟩
    * Author pages⟨22⟩
    * Attachments⟨23⟩
  * GitHub⟨24⟩


##  Kapil Krishnakumar ⟨22⟩
* * *
#### 2026
pdf ⟨25⟩bib ⟨26⟩abs⟨27⟩
**V ideoMind: Thinking in Steps for Long Video Understanding⟨28⟩**  
Shubhang Bhatnagar⟨29⟩ | Renxiong Wang⟨30⟩ | Kapil Krishnakumar⟨31⟩ | Adel Ahmadyan⟨32⟩ | Zhaojiang Lin⟨33⟩ | Lambert Mathias⟨34⟩ | Xin Luna Dong⟨35⟩ | Babak Damavandi⟨36⟩ | Narendra Ahuja⟨37⟩ | Seungwhan Moon⟨38⟩  
Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track)⟨39⟩
Multimodal Large Language Models (MLLMs) struggle with Long Video Understanding (LVU) due to their limited context window and the distributed nature of salient information across many redundant frames. To address this, we present VideoMind, a novel training free framework for LVU designed to mimic a human reasoning process. The framework is orchestrated by an MLLM that breaks down a user’s query into a series of simpler, actionable sub-queries. For each sub query, the MLLM reconfigures itself by invoking specialized ‘modes’ that are instantiations of the same MLLM, but with appropriately tailored context for the given sub query to extract targeted evidence. After gathering this evidence, the model resumes its role as the orchestrator which evaluates the results and decides if an answer is complete or if it must refine its strategy by engaging further modes with new context. Our specialized operational modes include: 1) a Multi-Scale Temporal Search mode to identify and summarize relevant video sub-snippets at varying time scales, and 2) a Single-Frame Visual Detail mode for precise spatial localization of objects. This dynamic allocation of computation yields state-of-the-art results on the Video-MME, LongVideo, and MLVU benchmarks, achieving 77.6% performance on Video MME using Qwen 2.5 72B (4.8% enhancement) while also yielding a 5% improvement on Llama 4 Scout.
Search⟨40⟩
##### Co-authors
  * Adel Ahmadyan⟨32⟩ 1
  * Narendra Ahuja⟨37⟩ 1
  * Shubhang Bhatnagar⟨29⟩ 1
  * Babak Damavandi⟨36⟩ 1
  * Xin Luna Dong⟨35⟩ 1
show all...
  * Zhaojiang Lin⟨33⟩ 1
  * Lambert Mathias⟨34⟩ 1
  * Seungwhan Moon⟨38⟩ 1
  * Renxiong Wang⟨30⟩ 1


##### Venues
  * EACL⟨41⟩1


 Fix author⟨42⟩
![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)⟨43⟩ ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License⟨44⟩. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License⟨45⟩.
The ACL Anthology is managed and built by the ACL Anthology team⟨7⟩ of volunteers.
_Site last built on 22 July 2026 at 14:46 UTC withcommit 280e4ed⟨46⟩._
