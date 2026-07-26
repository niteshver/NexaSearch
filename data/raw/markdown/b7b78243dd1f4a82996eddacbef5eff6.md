METIS-II:
 a hybrid MT syst em
Peter D irix
Vincent V andeghinste
Ineke S chuurm an
Centre for Computational Linguistics
Katholieke Universiteit Leuven
TMI 2007,  SkövdeOverview
Techniques  and is sues in MT
The METIS- II project
Intermediate ev aluation and ongoing 
workOverview of techniques 
in MT
Since 50s : word-by-word systems
Later : rule-based systems  (RBMT)
Since 80s : statistical MT ( SMT)  
90s: example- based MT ( EBMT)Issues
SMT/EBMT need huge par allel c orpora 
with aligned tex t (often not av ailable)
SMT/EBMT s parsity of data
RBMT infinity  of rules/vocabular y → 
manual w ork, near ly impos sible
RBMT adv anced analy tic resources 
neededResolve issu es
Use only large m onolingual corpora (w idely 
available)
Use basic analytic resources and an 
electronic translation dictionary
Enable construction of new  language pairs 
more easily
Combine E BMT/SMT and R BMT techniques 
to resolve disjoint issues
Construct hybrid MT systemThe METIS-II Project
European pr oject consisting of 
KULeuv en, ILSP Athens , IAI 
Saar brücken, and FU PF Bar celona
Language pair s Dutch, Greek, German 
and Spanis h to Englis h
Ongoing w ork (2004- 2007)
Build fur ther on an as sessment pr oject 
(2002- 2003)Three language models
Source-language m odel (S LM): analyses the 
structure in S L – tokenizers, lem matizers, 
PoS taggers, chunkers, …
Translation m odel (T M): models m apping 
betw een languages: dictionary, tag m apping 
rules, …
Target-language m odel (T LM): uses T L 
corpus to pick m ost likely translation Source-language model 
(Dutch)
Tokenizer
Tagger
Lemmatiz er
Chunk erSLM: Tokenizer
Rule-based tok enizer for Dutch
99.4% pr ecision and r ecallSLM: PoS tagger
External tool: TnT ( Brants 2000)
About 96- 97% ac curacy for Dutch
Trained on C GN (Corpus of Spok en 
Dutch)
Uses CGN/DCoi tag s etSLM: Lemmatizer
In-hous e, rule-based
Uses tags  and C GN lexicon as  input
Deals with separable v erbs
Futur e plans : use memor y-based D Coi 
tagger /lemmatiz erSLM: Ch unker
In-house robust chunker/shallow  parser: 
ShaRPa 2.1
Steps can be defined as context-free 
gram mars (non recursive) or perl subroutines
Detects N Ps, PPs and verb groups (F  = 95% )
Marks subclauses and relative clauses (F  = 
70%)
Future plans: add subject detectionTranslation model 
(Dutch to English)
Bilingual dic tionar y 
Tag-mapping r ules
Expander  (extra rules/statistics to deal 
with language- specific phenomena, e.g. 
reorganis ing w ord/chunk  order, 
adding/deleting w ords,…)TM: Dic tionary
Compiled from  free internet resources and 
EuroW ordN et
About 38,000 entries and 115,000 
translations
XML form at
Contains relevant P oS and chunking 
inform ation
Contains com plex and discontinuous entriesTM: Tag-mapping rules
Mapping betw een D utch (CGN/DCoi) 
and Englis h (BNC) tag s ets
Uses mapping tableTM: Expander
Generates extra translation c andidates
Deals with tens e mapping
Treats verb groups
Inserts do when n ecessary
Translates  like to + infinitiv e
Translates  om te + infinitiv eTarget-language model 
(English)
TL corpus preprocessing: sam e process as 
SL (tokenizing, lem matizing, tagging, 
chunking,… ) + draw  statistics/put in D B
TM has generated a list of possibilities
Corpus look-up ranks possibilities according 
to TL corpus statistics
Selects m ost likely translation or n-best
Token generator for m orphological generationTLM: Co rpus
Corpus preprocessing: BN C (British 
National C orpus)
BNC is already  tokenized and tagged
Lemmatiz ed us ing IAI lemmatiz er
Chunk ed us ing ShaR Pa 2.1 ( NPs, PPs , 
VGs, subclauses, …)
Put into SQ L databas eTLM: Co rpus statistics
Drawn statistics from c orpus
Co-occurrence of lemmas , chunk s 
(heads ), …
Put into databas eTLM: Co rpus look-up 
(ranker)
Dictionar y look -up, tag- mapping r ules, 
expander  => result = bag of bags
Lexical selection +  word/chunk  order is 
drawn from TL c orpus
Makes a ranking of c andidate 
translationsExample (1)
We want to tr anslate: ‘D e grote z warte 
hond blaft naar  de pos tbode’.Example (2)
MATCHING WORDSCORPUS INFO FREQ
the/big/black/dogthe/big/,/black/lead/dog 1
the/large/black/dogthe/large/black/dog 1
the/big/dogthe/big/dog 20
the/big/yellow/dog 4
the/big/dog/party 1
the/big/dog/'s/snarl 1
…
the/black/dogthe/black/,/tan/and/white/dog 1
the/black/dog 20
Churchill/and/the/black/dog 1
…
the/great/dogthe/great/dog 3
…
…
the/dog more than 1000 matchesExample (3)
SOLUTION SCOREfreqmcumul(m)NEW WEIGHT
the large black dog 1.0001420.707
the big black dog 0.6671420.472
the big gloomy dog 0.75053260.329
the grown up gloomy dog 0.500182760.243
the major gloomy dog 0.500182760.243
the great black dog 0.75023260.208
the tall black dog 0.75013260.147
the grown up black dog 0.75013260.147
the major black dog 0.75013260.147
the large gloomy dog 0.75013260.147
the black great dog 0.42913260.119
…Example (4)
BAG (HEADS)RESULT SCOREfreqm
dog / bark / to / .dog to bark . 0.26724
dog bark to . 0.22214
to bard dog . 0.19014
dog / bark / at / .dog bark at . 0.50014
dog at bark . 0.30814
at dog bark . 0.22214
dog / bark / towards / .towards dog bark . 0.26714
dog towards bark .0.06314
dog bark towards .0.28614
dog / bark / toward / .toward dog bark .0.50033
toward bark dog .0.14313
dog toward bark .0.37513
dog bark toward .0.60013
bark toward dog .0.30013
…Example (5)
SENTENCE RESULT
the large black dog barks/bark at the postman . 0.00101608892330194 
at the postman the large black dog barks/bark . 0.00101608892330194
the big black dog barks/bark at the postman . 0.00051978210288697
at the postman the big black dog barks/bark . 0.00051978210288697
the big gloomy dog barks/bark at the postman . 0.00037152767431080
at the postman the big gloomy dog barks/bark . 0.00037152767431080
the tall black dog barks/bark at the postman . 0.00028540695707770
at the postman the tall black dog barks/bark . 0.00028540695707770
the great black dog barks/bark at the postman . 0.00028243656500730
at the postman the great black dog barks/bark . 0.00028243656500730
the major gloomy dog barks/bark at the postman . 0.00022256538776012
at the postman the major gloomy dog barks/bark . 0.00022256538776012
the large black dog barks/bark to the postman . 0.00021386773758162
…Translation process
Wrapper  for whole pr ocess
Analy se SL s entenc e(s)
Build TM
Pick translations  with highes t rank(s) 
and do tok en gener ation
Offer translations  to translator for post-
editing ( not implemented y et)Evaluation
Evaluated w ith BLEU , NIST and 
Levenshtein dis tance algor ithm
BLEU
average0.3024
best0.3486Ongoing work & id eas
Reimplementing the s ystem ( code 
clean- up)
Elabor ate rules (e.g. c ontinuous  
tenses), lexica, …
Take SL c hunk  order into ac count
Improve SL and TL tools ets
Provide tools  for post-editing
PACO-MTRelated wo rk
Contex t-based Mac hine Tr anslation 
(CBMT, C arbonell 2006)
Generation- heav y Hybrid Mac hine 
Translation ( GHMT, H abas h, 2003)Questions
?