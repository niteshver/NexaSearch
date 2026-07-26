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


##  Tapio Salakoski ⟨22⟩
* * *
#### 2019
pdf ⟨25⟩bib ⟨26⟩abs⟨27⟩
**Is Multilingual BERT Fluent in Language Generation?⟨28⟩**  
Samuel Rönnqvist⟨29⟩ | Jenna Kanerva⟨30⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the First NLPL Workshop on Deep Learning for Natural Language Processing⟨33⟩
The multilingual BERT model is trained on 104 languages and meant to serve as a universal language model and tool for encoding sentences. We explore how well the model performs on several languages across several tasks: a diagnostic classification probing the embeddings for a particular syntactic property, a cloze task testing the language modelling ability to fill in gaps in a sentence, and a natural language generation task testing for the ability to produce coherent text fitting a given context. We find that the currently available multilingual BERT model is clearly inferior to the monolingual counterparts, and cannot in many cases serve as a substitute for a well-trained monolingual model. We find that the English and German models perform well at generation, whereas the multilingual model is lacking, in particular, for Nordic languages. The code of the experiments in the paper is available at: <https://github.com/TurkuNLP/bert-eval>
pdf ⟨34⟩bib ⟨35⟩abs⟨36⟩
**Template-free Data-to-Text Generation of Finnish Sports News⟨37⟩**  
Jenna Kanerva⟨30⟩ | Samuel Rönnqvist⟨29⟩ | Riina Kekki⟨38⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 22nd Nordic Conference on Computational Linguistics⟨39⟩
News articles such as sports game reports are often thought to closely follow the underlying game statistics, but in practice they contain a notable amount of background knowledge, interpretation, insight into the game, and quotes that are not present in the official statistics. This poses a challenge for automated data-to-text news generation with real-world news corpora as training data. We report on the development of a corpus of Finnish ice hockey news, edited to be suitable for training of end-to-end news generation methods, as well as demonstrate generation of text, which was judged by journalists to be relatively close to a viable product. The new dataset and system source code are available for research purposes.
pdf ⟨40⟩bib ⟨41⟩abs⟨42⟩
**An Unsupervised Query Rewriting Approach Using N-gram Co-occurrence Statistics to Find Similar Phrases in Large Text Corpora⟨43⟩**  
Hans Moen⟨44⟩ | Laura-Maria Peltonen⟨45⟩ | Henry Suhonen⟨46⟩ | Hanna-Maria Matinolli⟨47⟩ | Riitta Mieronkoski⟨48⟩ | Kirsi Telen⟨49⟩ | Kirsi Terho⟨50⟩ | Tapio Salakoski⟨31⟩ | Sanna Salanterä⟨51⟩  
Proceedings of the 22nd Nordic Conference on Computational Linguistics⟨39⟩
We present our work towards developing a system that should find, in a large text corpus, contiguous phrases expressing similar meaning as a query phrase of arbitrary length. Depending on the use case, this task can be seen as a form of (phrase-level) query rewriting. The suggested approach works in a generative manner, is unsupervised and uses a combination of a semantic word n-gram model, a statistical language model and a document search engine. A central component is a distributional semantic model containing word n-grams vectors (or embeddings) which models semantic similarities between n-grams of different order. As data we use a large corpus of PubMed abstracts. The presented experiment is based on manual evaluation of extracted phrases for arbitrary queries provided by a group of evaluators. The results indicate that the proposed approach is promising and that the use of distributional semantic models trained with uni-, bi- and trigrams seems to work better than a more traditional unigram model.
#### 2018
pdf ⟨52⟩bib ⟨53⟩abs⟨54⟩
**Evaluation of a Prototype System that Automatically Assigns Subject Headings to Nursing Narratives Using Recurrent Neural Network⟨55⟩**  
Hans Moen⟨44⟩ | Kai Hakala⟨56⟩ | Laura-Maria Peltonen⟨45⟩ | Henry Suhonen⟨46⟩ | Petri Loukasmäki⟨57⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩ | Sanna Salanterä⟨51⟩  
Proceedings of the Ninth International Workshop on Health Text Mining and Information Analysis⟨58⟩
We present our initial evaluation of a prototype system designed to assist nurses in assigning subject headings to nursing narratives – written in the context of documenting patient care in hospitals. Currently nurses may need to memorize several hundred subject headings from standardized nursing terminologies when structuring and assigning the right section/subject headings to their text. Our aim is to allow nurses to write in a narrative manner without having to plan and structure the text with respect to sections and subject headings, instead the system should assist with the assignment of subject headings and restructuring afterwards. We hypothesize that this could reduce the time and effort needed for nursing documentation in hospitals. A central component of the system is a text classification model based on a long short-term memory (LSTM) recurrent neural network architecture, trained on a large data set of nursing notes. A simple Web-based interface has been implemented for user interaction. To evaluate the system, three nurses write a set of artificial nursing shift notes in a fully unstructured narrative manner, without planning for or consider the use of sections and subject headings. These are then fed to the system which assigns subject headings to each sentence and then groups them into paragraphs. Manual evaluation is conducted by a group of nurses. The results show that about 70% of the sentences are assigned to correct subject headings. The nurses believe that such a system can be of great help in making nursing documentation in hospitals easier and less time consuming. Finally, various measures and approaches for improving the system are discussed.
pdf ⟨59⟩bib ⟨60⟩abs⟨61⟩
**Biomedical Event Extraction Using Convolutional Neural Networks and Dependency Parsing⟨62⟩**  
Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the BioNLP 2018 workshop⟨64⟩
Event and relation extraction are central tasks in biomedical text mining. Where relation extraction concerns the detection of semantic connections between pairs of entities, event extraction expands this concept with the addition of trigger words, multiple arguments and nested events, in order to more accurately model the diversity of natural language. In this work we develop a convolutional neural network that can be used for both event and relation extraction. We use a linear representation of the input text, where information is encoded with various vector space embeddings. Most notably, we encode the parse graph into this linear space using dependency path embeddings. We integrate our neural network into the open source Turku Event Extraction System (TEES) framework. Using this system, our machine learning model can be easily applied to a large set of corpora from e.g. the BioNLP, DDI Extraction and BioCreative shared tasks. We evaluate our system on 12 different event, relation and NER corpora, showing good generalizability to many tasks and achieving improved performance on several corpora.
pdf ⟨65⟩bib ⟨66⟩abs⟨67⟩
**T urku Neural Parser Pipeline: An End-to-End System for the CoNLL 2018 Shared Task⟨68⟩**  
Jenna Kanerva⟨30⟩ | Filip Ginter⟨32⟩ | Niko Miekka⟨69⟩ | Akseli Leino⟨70⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the CoNLL 2018 Shared Task: Multilingual Parsing from Raw Text to Universal Dependencies⟨71⟩
In this paper we describe the TurkuNLP entry at the CoNLL 2018 Shared Task on Multilingual Parsing from Raw Text to Universal Dependencies. Compared to the last year, this year the shared task includes two new main metrics to measure the morphological tagging and lemmatization accuracies in addition to syntactic trees. Basing our motivation into these new metrics, we developed an end-to-end parsing pipeline especially focusing on developing a novel and state-of-the-art component for lemmatization. Our system reached the highest aggregate ranking on three main metrics out of 26 teams by achieving 1st place on metric involving lemmatization, and 2nd on both morphological tagging and parsing.
#### 2017
pdf ⟨72⟩bib ⟨73⟩abs⟨74⟩
**Detecting mentions of pain and acute confusion in Finnish clinical text⟨75⟩**  
Hans Moen⟨44⟩ | Kai Hakala⟨56⟩ | Farrokh Mehryary⟨76⟩ | Laura-Maria Peltonen⟨45⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩ | Sanna Salanterä⟨51⟩  
Proceedings of the 16th BioNLP Workshop⟨77⟩
We study and compare two different approaches to the task of automatic assignment of predefined classes to clinical free-text narratives. In the first approach this is treated as a traditional mention-level named-entity recognition task, while the second approach treats it as a sentence-level multi-label classification task. Performance comparison across these two approaches is conducted in the form of sentence-level evaluation and state-of-the-art methods for both approaches are evaluated. The experiments are done on two data sets consisting of Finnish clinical text, manually annotated with respect to the topics pain and acute confusion. Our results suggest that the mention-level named-entity recognition approach outperforms sentence-level classification overall, but the latter approach still manages to achieve the best prediction scores on several annotation classes.
pdf ⟨78⟩bib ⟨79⟩abs⟨80⟩
**End-to-End System for Bacteria Habitat Extraction⟨81⟩**  
Farrokh Mehryary⟨76⟩ | Kai Hakala⟨56⟩ | Suwisa Kaewphan⟨82⟩ | Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 16th BioNLP Workshop⟨77⟩
We introduce an end-to-end system capable of named-entity detection, normalization and relation extraction for extracting information about bacteria and their habitats from biomedical literature. Our system is based on deep learning, CRF classifiers and vector space models. We train and evaluate the system on the BioNLP 2016 Shared Task Bacteria Biotope data. The official evaluation shows that the joint performance of our entity detection and relation extraction models outperforms the winning team of the Shared Task by 19pp on F1-score, establishing a new top score for the task. We also achieve state-of-the-art results in the normalization task. Our system is open source and freely available at <https://github.com/TurkuNLP/BHE>.
pdf ⟨83⟩bib ⟨84⟩
**Applying BLAST to Text Reuse Detection in Finnish Newspapers and Journals, 1771-1910⟨85⟩**  
Aleksi Vesanto⟨86⟩ | Asko Nivala⟨87⟩ | Heli Rantala⟨88⟩ | Tapio Salakoski⟨31⟩ | Hannu Salmi⟨89⟩ | Filip Ginter⟨32⟩  
Proceedings of the NoDaLiDa 2017 Workshop on Processing Historical Language⟨90⟩
pdf ⟨91⟩bib ⟨92⟩
**A System for Identifying and Exploring Text Repetition in Large Historical Document Corpora⟨93⟩**  
Aleksi Vesanto⟨86⟩ | Filip Ginter⟨32⟩ | Hannu Salmi⟨89⟩ | Asko Nivala⟨87⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 21st Nordic Conference on Computational Linguistics⟨94⟩
pdf ⟨95⟩bib ⟨96⟩
**Creating register sub-corpora for the Finnish Internet Parsebank⟨97⟩**  
Veronika Laippala⟨98⟩ | Juhani Luotolahti⟨99⟩ | Aki-Juhani Kyröläinen⟨100⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 21st Nordic Conference on Computational Linguistics⟨94⟩
#### 2016
pdf ⟨101⟩bib ⟨102⟩
**Deep Learning with Minimal Training Data: TurkuNLP Entry in the BioNLP Shared Task 2016⟨103⟩**  
Farrokh Mehryary⟨76⟩ | Jari Björne⟨63⟩ | Sampo Pyysalo⟨104⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 4th BioNLP Shared Task Workshop⟨105⟩
pdf ⟨106⟩bib ⟨107⟩
**Syntactic analyses and named entity recognition for PubMed and PubMed Central — up-to-the-minute⟨108⟩**  
Kai Hakala⟨56⟩ | Suwisa Kaewphan⟨82⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 15th Workshop on Biomedical Natural Language Processing⟨109⟩
pdf ⟨110⟩bib ⟨111⟩
**UTU at SemEval-2016 Task 10: Binary Classification for Expression Detection (BCED)⟨112⟩**  
Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 10th International Workshop on Semantic Evaluation (SemEval-2016)⟨113⟩
#### 2015
pdf ⟨114⟩bib ⟨115⟩
**Towards the Classification of the Finnish Internet Parsebank: Detecting Translations and Informality⟨116⟩**  
Veronika Laippala⟨98⟩ | Jenna Kanerva⟨30⟩ | Anna Missilä⟨117⟩ | Sampo Pyysalo⟨104⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 20th Nordic Conference of Computational Linguistics (NODALIDA 2015)⟨118⟩
#### 2014
pdf ⟨119⟩bib ⟨120⟩
**Care Episode Retrieval⟨121⟩**  
Hans Moen⟨44⟩ | Erwin Marsi⟨122⟩ | Filip Ginter⟨32⟩ | Laura-Maria Murtola⟨123⟩ | Tapio Salakoski⟨31⟩ | Sanna Salanterä⟨51⟩  
Proceedings of the 5th International Workshop on Health Text Mining and Information Analysis (Louhi)⟨124⟩
#### 2013
pdf ⟨125⟩bib ⟨126⟩
**Building a Large Automatically Parsed Corpus of Finnish⟨127⟩**  
Filip Ginter⟨32⟩ | Jenna Nyblom⟨30⟩ | Veronika Laippala⟨98⟩ | Samuel Kohonen⟨128⟩ | Katri Haverinen⟨129⟩ | Simo Vihjanen⟨130⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 19th Nordic Conference of Computational Linguistics (NODALIDA 2013)⟨131⟩
pdf ⟨132⟩bib ⟨133⟩
**Towards a Dependency-Based PropBank of General Finnish⟨134⟩**  
Katri Haverinen⟨129⟩ | Veronika Laippala⟨98⟩ | Samuel Kohonen⟨128⟩ | Anna Missilä⟨117⟩ | Jenna Nyblom⟨30⟩ | Stina Ojala⟨135⟩ | Timo Viljanen⟨136⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the 19th Nordic Conference of Computational Linguistics (NODALIDA 2013)⟨131⟩
pdf ⟨137⟩bib ⟨138⟩
**Predicting Conjunct Propagation and Other Extended Stanford Dependencies⟨139⟩**  
Jenna Nyblom⟨30⟩ | Samuel Kohonen⟨128⟩ | Katri Haverinen⟨129⟩ | Tapio Salakoski⟨31⟩ | Filip Ginter⟨32⟩  
Proceedings of the Second International Conference on Dependency Linguistics (DepLing 2013)⟨140⟩
pdf ⟨141⟩bib ⟨142⟩
**EVEX in ST’13: Application of a large-scale text mining resource to event extraction and network construction⟨143⟩**  
Kai Hakala⟨56⟩ | Sofie Van Landeghem⟨144⟩ | Tapio Salakoski⟨31⟩ | Yves Van de Peer⟨145⟩ | Filip Ginter⟨32⟩  
Proceedings of the BioNLP Shared Task 2013 Workshop⟨146⟩
pdf ⟨147⟩bib ⟨148⟩
**TEES 2.1: Automated Annotation Scheme Learning in the BioNLP 2013 Shared Task⟨149⟩**  
Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the BioNLP Shared Task 2013 Workshop⟨146⟩
pdf ⟨150⟩bib ⟨151⟩
**UT urku: Drug Named Entity Recognition and Drug-Drug Interaction Extraction Using SVM Classification and Domain Knowledge⟨152⟩**  
Jari Björne⟨63⟩ | Suwisa Kaewphan⟨82⟩ | Tapio Salakoski⟨31⟩  
Second Joint Conference on Lexical and Computational Semantics (*SEM), Volume 2: Proceedings of the Seventh International Workshop on Semantic Evaluation (SemEval 2013)⟨153⟩
#### 2012
pdf ⟨154⟩bib ⟨155⟩
**P ubMed-Scale Event Extraction for Post-Translational Modifications, Epigenetics and Protein Structural Relations⟨156⟩**  
Jari Björne⟨63⟩ | Sofie Van Landeghem⟨144⟩ | Sampo Pyysalo⟨104⟩ | Tomoko Ohta⟨157⟩ | Filip Ginter⟨32⟩ | Yves Van de Peer⟨145⟩ | Sophia Ananiadou⟨158⟩ | Tapio Salakoski⟨31⟩  
BioNLP: Proceedings of the 2012 Workshop on Biomedical Natural Language Processing⟨159⟩
#### 2011
pdf ⟨160⟩bib ⟨161⟩
**Generalizing Biomedical Event Extraction⟨162⟩**  
Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩  
Proceedings of BioNLP Shared Task 2011 Workshop⟨163⟩
pdf ⟨164⟩bib ⟨165⟩
**EVEX : A PubMed-Scale Resource for Homology-Based Generalization of Text Mining Predictions⟨166⟩**  
Sofie Van Landeghem⟨144⟩ | Filip Ginter⟨32⟩ | Yves Van de Peer⟨145⟩ | Tapio Salakoski⟨31⟩  
Proceedings of BioNLP 2011 Workshop⟨167⟩
#### 2010
pdf ⟨168⟩bib ⟨169⟩
**Reconstruction of Semantic Relationships from Their Projections in Biomolecular Domain⟨170⟩**  
Juho Heimonen⟨171⟩ | Jari Björne⟨63⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 2010 Workshop on Biomedical Natural Language Processing⟨172⟩
pdf ⟨173⟩bib ⟨174⟩
**Scaling up Biomedical Event Extraction to the Entire PubMed⟨175⟩**  
Jari Björne⟨63⟩ | Filip Ginter⟨32⟩ | Sampo Pyysalo⟨104⟩ | Jun’ichi Tsujii⟨176⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 2010 Workshop on Biomedical Natural Language Processing⟨172⟩
pdf ⟨177⟩bib ⟨178⟩
**Dependency-Based PropBanking of Clinical Finnish⟨179⟩**  
Katri Haverinen⟨129⟩ | Filip Ginter⟨32⟩ | Timo Viljanen⟨136⟩ | Veronika Laippala⟨98⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the Fourth Linguistic Annotation Workshop⟨180⟩
#### 2009
pdf ⟨181⟩bib ⟨182⟩
**Parsing Clinical Finnish: Experiments with Rule-Based and Statistical Dependency Parsers⟨183⟩**  
Katri Haverinen⟨129⟩ | Filip Ginter⟨32⟩ | Veronika Laippala⟨98⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 17th Nordic Conference of Computational Linguistics (NODALIDA 2009)⟨184⟩
pdf ⟨185⟩bib ⟨186⟩
**Learning to Extract Biological Event and Relation Graphs⟨187⟩**  
Jari Björne⟨63⟩ | Filip Ginter⟨32⟩ | Juho Heimonen⟨171⟩ | Sampo Pyysalo⟨104⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 17th Nordic Conference of Computational Linguistics (NODALIDA 2009)⟨184⟩
pdf ⟨188⟩bib ⟨189⟩
**Extracting Complex Biological Events with Rich Graph-Based Feature Sets⟨190⟩**  
Jari Björne⟨63⟩ | Juho Heimonen⟨171⟩ | Filip Ginter⟨32⟩ | Antti Airola⟨191⟩ | Tapio Pahikkala⟨192⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the BioNLP 2009 Workshop Companion Volume for Shared Task⟨193⟩
#### 2008
pdf ⟨194⟩bib ⟨195⟩
**A Graph Kernel for Protein-Protein Interaction Extraction⟨196⟩**  
Antti Airola⟨191⟩ | Sampo Pyysalo⟨104⟩ | Jari Björne⟨63⟩ | Tapio Pahikkala⟨192⟩ | Filip Ginter⟨32⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the Workshop on Current Trends in Biomedical Natural Language Processing⟨197⟩
#### 2007
pdf ⟨198⟩bib ⟨199⟩
**Role of Different Spectral Attributes in Vowel Categorization: the Case of Udmurt⟨200⟩**  
Janne Savela⟨201⟩ | Stina Ojala⟨135⟩ | Olli Aaltonen⟨202⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 16th Nordic Conference of Computational Linguistics (NODALIDA 2007)⟨203⟩
pdf ⟨204⟩bib ⟨205⟩
**Utterance-Initial Duration of Finnish Non-Plosive Consonants⟨206⟩**  
Tuomo Saarni⟨207⟩ | Jussi Hakokari⟨208⟩ | Olli Aaltonen⟨202⟩ | Jouni Isoaho⟨209⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the 16th Nordic Conference of Computational Linguistics (NODALIDA 2007)⟨203⟩
pdf ⟨210⟩bib ⟨211⟩
**On the unification of syntactic annotations under the Stanford dependency scheme: A case study on BioInfer and GENIA⟨212⟩**  
Sampo Pyysalo⟨104⟩ | Filip Ginter⟨32⟩ | Veronika Laippala⟨98⟩ | Katri Haverinen⟨129⟩ | Juho Heimonen⟨171⟩ | Tapio Salakoski⟨31⟩  
Biological, translational, and clinical language processing⟨213⟩
#### 2006
pdf ⟨214⟩bib ⟨215⟩
**A Probabilistic Search for the Best Solution Among Partially Completed Candidates⟨216⟩**  
Filip Ginter⟨32⟩ | Aleksandr Mylläri⟨217⟩ | Tapio Salakoski⟨31⟩  
Proceedings of the Workshop on Computationally Hard Problems and Joint Inference in Speech and Language Processing⟨218⟩
#### 2004
pdf ⟨219⟩bib ⟨220⟩
**Analysis of Link Grammar on Biomedical Dependency Corpus Targeted at Protein-Protein Interactions⟨221⟩**  
Sampo Pyysalo⟨104⟩ | Filip Ginter⟨32⟩ | Tapio Pahikkala⟨192⟩ | Jorma Boberg⟨222⟩ | Jouni Järvinen⟨223⟩ | Tapio Salakoski⟨31⟩ | Jeppe Koivula⟨224⟩  
Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications (NLPBA/BioNLP)⟨225⟩
Search⟨226⟩
##### Co-authors
  * Filip Ginter⟨32⟩ 28
  * Jari Björne⟨63⟩ 13
  * Sampo Pyysalo⟨104⟩ 8
  * Jenna Kanerva⟨30⟩ 7
  * Veronika Laippala⟨98⟩ 7
show all...
  * Katri Haverinen⟨129⟩ 6
  * Kai Hakala⟨56⟩ 5
  * Juho Heimonen⟨171⟩ 4
  * Hans Moen⟨44⟩ 4
  * Sanna Salanterä⟨51⟩ 4
  * Suwisa Kaewphan⟨82⟩ 3
  * Samuel Kohonen⟨128⟩ 3
  * Farrokh Mehryary⟨76⟩ 3
  * Tapio Pahikkala⟨192⟩ 3
  * Laura-Maria Peltonen⟨45⟩ 3
  * Sofie Van Landeghem⟨144⟩ 3
  * Yves Van de Peer⟨145⟩ 3
  * Olli Aaltonen⟨202⟩ 2
  * Antti Airola⟨191⟩ 2
  * Anna Missilä⟨117⟩ 2
  * Asko Nivala⟨87⟩ 2
  * Stina Ojala⟨135⟩ 2
  * Samuel Rönnqvist⟨29⟩ 2
  * Hannu Salmi⟨89⟩ 2
  * Henry Suhonen⟨46⟩ 2
  * Aleksi Vesanto⟨86⟩ 2
  * Timo Viljanen⟨136⟩ 2
  * Sophia Ananiadou⟨158⟩ 1
  * Jorma Boberg⟨222⟩ 1
  * Jussi Hakokari⟨208⟩ 1
  * Jouni Isoaho⟨209⟩ 1
  * Jouni Järvinen⟨223⟩ 1
  * Riina Kekki⟨38⟩ 1
  * Jeppe Koivula⟨224⟩ 1
  * Aki-Juhani Kyröläinen⟨100⟩ 1
  * Akseli Leino⟨70⟩ 1
  * Petri Loukasmäki⟨57⟩ 1
  * Juhani Luotolahti⟨99⟩ 1
  * Erwin Marsi⟨122⟩ 1
  * Hanna-Maria Matinolli⟨47⟩ 1
  * Niko Miekka⟨69⟩ 1
  * Riitta Mieronkoski⟨48⟩ 1
  * Laura-Maria Murtola⟨123⟩ 1
  * Aleksandr Mylläri⟨217⟩ 1
  * Tomoko Ohta⟨157⟩ 1
  * Heli Rantala⟨88⟩ 1
  * Tuomo Saarni⟨207⟩ 1
  * Janne Savela⟨201⟩ 1
  * Kirsi Telen⟨49⟩ 1
  * Kirsi Terho⟨50⟩ 1
  * Jun’ichi Tsujii⟨176⟩ 1
  * Simo Vihjanen⟨130⟩ 1


##### Venues
  * BioNLP⟨227⟩15
  * NoDaLiDa⟨228⟩13
  * Louhi⟨229⟩2
  * SemEval⟨230⟩2
  * WS⟨231⟩2
show all...
  * CoNLL⟨232⟩1
  * DepLing⟨233⟩1
  * LAW⟨234⟩1


 Fix author⟨235⟩
![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)⟨236⟩ ACL materials are Copyright © 1963–2026 ACL; other materials are copyrighted by their respective copyright holders. Materials prior to 2016 here are licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0 International License⟨237⟩. Permission is granted to make copies for the purposes of teaching and research. Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License⟨238⟩.
The ACL Anthology is managed and built by the ACL Anthology team⟨7⟩ of volunteers.
_Site last built on 22 July 2026 at 14:46 UTC withcommit 280e4ed⟨239⟩._
