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


##  Colton Chapin ⟨22⟩
* * *
#### 2021
pdf ⟨25⟩bib ⟨26⟩abs⟨27⟩ ⟨28⟩
**An Architecture for Accelerated Large-Scale Inference of Transformer-Based Language Models⟨29⟩**  
Amir Ganiev⟨30⟩ | Colton Chapin⟨31⟩ | Anderson de Andrade⟨32⟩ | Chen Liu⟨33⟩  
Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies: Industry Papers⟨34⟩
This work demonstrates the development process of a machine learning architecture for inference that can scale to a large volume of requests. We used a BERT model that was fine-tuned for emotion analysis, returning a probability distribution of emotions given a paragraph. The model was deployed as a gRPC service on Kubernetes. Apache Spark was used to perform inference in batches by calling the service. We encountered some performance and concurrency challenges and created solutions to achieve faster running time. Starting with 200 successful inference requests per minute, we were able to achieve as high as 18 thousand successful requests per minute with the same batch job resource allocation. As a result, we successfully stored emotion probabilities for 95 million paragraphs within 96 hours.
Search⟨35⟩
##### Co-authors
  * Amir Ganiev⟨30⟩ 1
  * Chen Cecilia Liu⟨33⟩ 1
  * Anderson de Andrade⟨32⟩ 1


##### Venues
  * NAACL⟨36⟩1


 Fix author⟨37⟩
![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)⟨38⟩ ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License⟨39⟩. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License⟨40⟩.
The ACL Anthology is managed and built by the ACL Anthology team⟨7⟩ of volunteers.
_Site last built on 22 July 2026 at 14:46 UTC withcommit 280e4ed⟨41⟩._
