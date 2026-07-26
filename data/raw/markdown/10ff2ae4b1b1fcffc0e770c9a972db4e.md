A Cluster-Based Representation for 
Multi-System MT Evaluation 
Nicolas Stroppa and Karolina Owczarzak 
National Centre for Language Technology 
School of Computing, Dublin City University • Evaluating Machine Translation (MT) 
– automatic metrics – human judgement – “My MT is better than yours”: unreliability of sys tem rankings 
• The need for statistical significance 
– bootstrap – approximate randomization 
• Cluster representation 
– “My MT might not be better than yours, but it’s de finitely better than his”: 
groupings and confidence levels 
• Automatic metrics vs. human judgement on the clust er level: cluster 
comparison Overview Automatic metrics in MT evaluation 
• Fast and cheap way to evaluate Machine Translation  quality 
• Used for system development or cross-system compar ison 
• Most popular: BLEU, NIST, GTM, METEOR • Criticism of string-level comparison and inadequat e correlations with human 
judgement 
• Small differences in automatic scores between syst ems due to chance: data type, 
missing punctuation, unknown word, weather, butterf ly flapping its wings in Ecuador 
• Hard rankings of systems based on raw evaluation r esults not advisable 
• Statistical significance testing necessary • Slow and expensive way to evaluate Machine Transla tion quality 
• Used in shared tasks (ACL SMT workshop 2007) • Standard scale: Adequacy 1-5, Fluency 1-5 • Standard frame of reference for developing automat ic metrics 
• Human evaluation not so consistent either: 
– inter-annotator K~0.23 
– intra-annotator K~0.5 (Callison-Burch et al. 2007) 
• Small differences in human scores between systems due to chance: personal writing 
style preferences, imperfect knowledge or understan ding, tiredness, distraction, the 
fact that it’s Tuesday – humans are unreliable and i nconsistent! (I, for one, welcome our 
new AI overlords) 
• Hard rankings of systems based on human evaluation  results not advisable 
• Statistical significance testing necessary Humans in MT Evaluation Statistical Significance Testing 
• Null hypothesis: two MT systems are of the same qu ality 
• Difference between their scores only significant i f statistical 
evidence against null hypothesis 
• Significance testing for MT evaluation: non-parame tric methods 
– bootstrap ( Efron and Tibshirani 1993, Koehn 2004) 
– approximate randomization (Noreen 1989, Riezler an d Maxwell 2005)
Bootstrap: 
Sentence 1 Sentence 2 Sentence 3 
…
Sentence nSentence 57 Sentence 82 Sentence 57 Sentence 3 
…
Sentence nscore no. of samples confidence interval Approximate randomization 
• More appropriate to MT eval (Riezler and Maxwell 2 005; Collins 
et al. 2005) 
MT 1sentence 1 
MT 1sentence 2 
MT 1sentence 3 
…
MT 1sent nMT 1
MT 2sentence 1 
MT 2sentence 2 
MT 2sentence 3 
…
MT 2sent nMT 2
MT 1sentence 1 
MT 2sentence 2 
MT 1sentence 3 
…
MT 2sent nMT’ 1
MT 2sentence 1 
MT 1sentence 2 
MT 2sentence 3 
…
MT 1sent n
MT 1>  MT 2 MT 1>  MT’ 1
MT 2<  MT’ 2
MT 1 – MT 2   >  MT’ 1 – MT’ 2 IF IF IF IF THEN THEN THEN THEN MT’ 2
p = ( ∑k
i=1 vi) + 1 
k + 1Cluster-based representation 
• Approximate randomization likely to show some MT s ystems cannot be 
distinguished (at a certain confidence level) 
• Clusters contain MT systems that are pairwise indi stinguishable 
• Clusters can overlap: A!> B, B !> C, A > C
RS-ASR   p=0.05 RS-CRR   p=0.05 
1
2
3
4
5
61
2
3
4
5
61
2
3
4
5
61
2
3
4
5
6Fluency Fluency Fluency Fluency Fluency Fluency Fluency Fluency Adequacy Adequacy Adequacy Adequacy Adequacy Adequacy Adequacy Adequacy Comparing clusters 
• Adaptation of the Rand statistics (Haldiki et al. 2001) 
• Compare relationships of pairs of MT systems across cluster rankings 
score(rel1,rel2)  = score(rel1,rel2)  = score(rel1,rel2)  = score(rel1,rel2)  = 11 11 if (rel1 = rel2) if (rel1 = rel2) if (rel1 = rel2) if (rel1 = rel2) 
-- --11 11 if ( if ( if ( if (rel rel rel rel1 = ‘<<’ and 1 = ‘<<’ and 1 = ‘<<’ and 1 = ‘<<’ and rel rel rel rel2 = ‘>>’) 2 = ‘>>’) 2 = ‘>>’) 2 = ‘>>’) 
-- --11 11 if ( if ( if ( if (rel rel rel rel1 = ‘>>’ and 1 = ‘>>’ and 1 = ‘>>’ and 1 = ‘>>’ and rel rel rel rel2 = ‘<<’) 2 = ‘<<’) 2 = ‘<<’) 2 = ‘<<’) 
00 00 otherwise otherwise otherwise otherwise 
RS-ASR   p=0.05 RS-CRR   p=0.05 
1
2
3
4
5
61
2
3
4
5
61
2
3
4
5
61
2
3
4
5
6Flue Flue Flue Flue 
ncy ncy ncy ncy Flue Flue Flue Flue 
ncy ncy ncy ncy Adequ Adequ Adequ Adequ 
acy acy acy acy Adequ Adequ Adequ Adequ 
acy acy acy acy score(ranking1,ranking2)  = score(ranking1,ranking2)  = score(ranking1,ranking2)  = score(ranking1,ranking2)  = 2 * ∑n-1
i=1 ∑nj=i+1 score (C(i, j), D(i, j))
n* (n–1)Experiment – clusters and comparisons 
• Data: IWSLT 2006 Chinese-English translations 
– 500 segments – six MT systems – three conditions: spontaneous speech (SS-ASR), rea d speech with automatic speech 
recognition (RS-ASR), read speech with correct reco gnition (RS-CRR) 
– human evaluation (adequacy and fluency) for all tr anslations 
– evaluated with BLEU, NIST, GTM, METEOR 
• Approximate randomization on all scorings 
– varying confidence levels (p=0.001, p=0.002, p=0.0 05, p=0.01, p=0.02, p=0.05) 
– analysis of resulting clusters 
• Comparison of clusters based on human and automati c scores 
• Comparison of clusters based on different automati c scores 
• Relationship between confidence level and human – a utomatic correlation Clusters and confidence levels 
SS-ASR   p=0.001 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy SS-ASR   p=0.002 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy SS-ASR   p=0.005 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy 
SS-ASR   p=0.01 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy SS-ASR   p=0.02 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy SS-ASR   p=0.05 
1
2
3
4
5
61
2
3
4
5
6Fluency Adequacy Comparison of human and automatic clusters 
0.7 0.31 GTM GTM GTM GTM 0.71 0.71 0.71 0.71 0.39 METEOR METEOR METEOR METEOR 0.64 0.34 NIST NIST NIST NIST 0.7 0.58 0.58 0.58 0.58 BLEU BLEU BLEU BLEU 
Mixed Track Mixed Track Mixed Track Mixed Track 0.33 0.33 GTM GTM GTM GTM 0.26 0.53 METEOR METEOR METEOR METEOR 0.27 0.4 NIST NIST NIST NIST 0.47 0.73 BLEU BLEU BLEU BLEU 
RS RS RS RS-- --CRR CRR CRR CRR 0.2 0.2 GTM GTM GTM GTM 0.13 0.33 METEOR METEOR METEOR METEOR 0.27 0.4 NIST NIST NIST NIST 0.33 0.47 BLEU BLEU BLEU BLEU 
RS RS RS RS-- --ASR ASR ASR ASR 0.6 -0.13 GTM GTM GTM GTM 0.53 0 METEOR METEOR METEOR METEOR 0.6 0 NIST NIST NIST NIST 0.4 0.47 BLEU BLEU BLEU BLEU 
SS SS SS SS-- --ASR ASR ASR ASR Adequacy Adequacy Adequacy Adequacy Fluency Fluency Fluency Fluency 
0.86 0.79 0.7 GTM GTM GTM GTM - 0.79 0.77 METEOR METEOR METEOR METEOR - - 0.64 NIST NIST NIST NIST METEOR METEOR METEOR METEOR NIST NIST NIST NIST BLEU BLEU BLEU BLEU Comparing automatic metrics Comparing automatic metrics Comparing automatic metrics Comparing automatic metrics 
(Mixed Track) (Mixed Track) (Mixed Track) (Mixed Track) p = 0.05 
p = 0.05 Correlations and confidence levels 
00.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
0.001 0.002 0.005 0.01 0.02 0.05 
significance levelcorrelation score 
BLEU 
METEOR 
NIST 
GTM 
00.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
0.001 0.002 0.005 0.01 0.02 0.05 
significance levelcorrelation score 
BLEU 
METEOR 
NIST 
GTM Correlation (human scores of 
fluency fluency fluency fluency, automatic metrics) vs. significance level 
Correlation (human scores of 
adequacy adequacy adequacy adequacy, automatic metrics) vs. significance level Discussion and conclusions 
• Small differences in (human or automatic) scores m ay be accidental 
• Statistical significance testing necessary for Tru th and Justice (and A 
Hard-Boiled Egg) 
• Produce clusters of MT systems at given significan ce level 
• Trade-off: as level of required confidence increas es, it‘s more difficult to 
distinguish between MT systems 
• Cluster comparison – another method for comparison of system-level 
human and automatic scores 
• Evaluating automatic metrics necessary at both sys tem and segment level 
– metrics with high system-level correlations good f or multiple MT system 
comparisons (shared tasks etc.) 
– metrics with high segment-level correlations good for MT development 
• Automatic metrics cannot reflect well fluency and adequacy at the same 
time References 
Satanjeev Banerjee and Alon Lavie. 2005. METEOR: An  automatic metric for mt evaluation with 
improved correlation with human judgments. In Proceedings of the ACL Workshop on Intrisic and 
Extrinsic Evaluation Measures for MT and/or Summarization , pages 65–72, Ann Arbor, MI. 
Chris Callison-Burch, Cameron Fordyce, Philipp Koeh n, Christof Monz, Josh Schroeder. 2007. (Meta-) 
Evaluation of Machine Translation. In Proceedings of the ACL 2007 Workshop on Statistical 
Machine Translation , pages 136-158, Prague, Czech Republic. 
Michael Collins, Philipp Koehn, and Ivona Kucerova.  2005. Clause restructuring for statistical machine 
translation. In Proceedings of ACL 2005 , pages 531–540, Ann Arbor, MI. 
George Doddington. 2002. Automatic evaluation of ma chine translation quality using n-gram 
cooccurrence statistics. In Proceedings of HLT 2002 , pages 128–132, San Diego, CA. 
Bradley Efron and Robert J. Tibshirani. 1993. An Introduction to the Bootstrap . Chapman & Hall. 
Philipp Koehn. 2004. Statistical significance tests  for machine translation evaluation. In Proceedings of 
EMNLP 2004 , pages 388–395, Barcelona, Spain. 
I. Dan Melamed, Ryan Green, and Joseph P. Turian. 2 004. Precision and recall of machine translation. 
In Proceedings of HLT-NAACL 2003 , volume 2, pages 61–63, Edmonton, Canada. 
Eric W. Noreen. 1989. Computer-Intensive Methods for Testing Hypotheses: An Introduction . Wiley-
Interscience, New York, NY. 
Kishore Papineni, Salim Roukos, Todd Ward, and Wei- Jing Zhu. 2002. BLEU: a method for automatic 
evaluation of machine translation. In Proceedings of ACL 2002 , pages 311–318, Philadelphia, PA. 
Stefan Riezler and John Maxwell. 2005. On some pitf alls in automatic evaluation and significance 
testing for MT. In Proceedings of the the ACL Workshop on Intrisic and Extrinsic Evaluation 
Measures for MT and/or Summarization , pages 57–64, Ann Arbor, MI. 