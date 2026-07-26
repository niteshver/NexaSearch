Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -1- TMI 2007 Michael Paul, Andrew Finch, EiichiroSumita Reducing Human Assessment of 
Machine Translation Quality 
to Binary Classifiers Reducing Human Assessment of 
Machine Translation Quality 
to Binary Classifiers 
September 8, 2007 
NICT Spoken Language Communication Group, 
ATR Spoken Language Communication Research Laborato ries 
Kyoto, Japan Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -2- TMI 2007 Assessment of 
Machine Translation Quality Assessment of 
Machine Translation Quality 
Sentence 
•translation of a single input Document 
•set of sentence translations Human •average of sentence-level 
grades •discrete evaluation grade 
•median score of multiple 
human grades 
metrics : fluency, adequacy, …
•confidence estimation 
•machine learning approach to 
predict human grades 
classifiers : SVM, DT, … metrics : BLEU, METEOR, …Machine •comparison to (multiple) 
reference translations 
•assign single numerical score Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -3- TMI 2007 Assessment of 
Machine Translation Quality Assessment of 
Machine Translation Quality 
Document Sentence Usage •evaluation of MT system 
development progress 
•MT system comparison 
(NIST, IWSLT, …)•usability of given translation 
in a real-world application (post-editing, dialog trans-
lation, …) Problems •complexity of evaluation task 
(multi-class classification) 
•granularity of evaluation 
grades •quality/coverage of 
reference translations 
•“meaning”of (numerical) 
automatic evaluation scores Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -4- TMI 2007 Outline of Talk Outline of Talk 
2. Experimental Results: 
•large-scale human-annotated evaluation corpus 
•• ••coding matrix optimization 
•• ••classification accuracy 
•• ••correlation to human assessments 1. Prediction of Sentence-Level Translation Quality : 
•• ••decompose multi-class to binary classification 
°a codingsmatrix 
•• ••learn set of binary classifiers 
°feature selection, standard machine learning techni ques 
•• ••predict multi-class label 
°compare binary classification results to codingsmatrix Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -5- TMI 2007 Prediction of Sentence-Level
Translation Quality Prediction of Sentence-Level
Translation Quality 
54321Grade = fluency 
Flawless English Good English 
Non-native English 
Disfluent English Incomprehensible Human Assessment 
Training Corpus 
Test  Set Annotated 
Evaluation Corpus 
Evaluation 
(classification accuracy) 
5, 4, 3, 2, 1 
Binary 
Classifier +1, −− −−1Machine Learning 
(SVM, DT, …)ID | Grade | F 1| F 2| …Feature Extraction 
Multi-class 
Classifier ID | F 1| F 2| …Feature Extraction 
ID | Binary-Class ID | Multi-Class Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -6- TMI 2007 Classification Task Classification Task 
Goal: predict human evaluation grade (fluency , 
adequacy , …) for a given translation 
→multi-class label
Multi-Class Classification: 
☺☺ ☺☺direct prediction of multi-class label 
/frownface/frownface /frownface/frownfaceclassification accuracy is low 
Binary-Class Classification: 
☺☺ ☺☺classification accuracy is high 
/frownface/frownface /frownface/frownfacemulti-class label cannot be derived reliably Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -7- TMI 2007 Proposed Solution Proposed Solution 
Reduction of Classification Complexity: 
•decomposemulti-class task into a set of binary 
classification problems 
•apply standard learning algorithm to train 
binary classifiers 
•combine results of binary classifiers 
using a “coding matrix ”to predict multi-class label 
→→ →→increase in classification accuracy 
→→ →→independent from learning algorithm Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -8- TMI 2007 Proposed Solution Proposed Solution 
Feature Selection for Translation Quality Predictio n: 
•multiple automatic evaluation metricscores 
°BLEU °WER °GTM 
°NIST °PER 
°METEOR °TER 
•metric-internal features 
°ngram-prec °length ratio °…
→→ →→takes into account different aspects of MT quality 
→→ →→independent from target language and MT system Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -9- TMI 2007 Binary 
Classifier 
Binary 
Classifier +1, −− −−1+1, −− −−1
:Combination 
of Binary 
Classification 
Results :Multi-Class To Binary 
Class Decomposition Prediction of Sentence-Level
Translation Quality Prediction of Sentence-Level
Translation Quality 
54321Grade = fluency 
Flawless English Good English 
Non-native English 
Disfluent English Incomprehensible Human Assessment 
Training Corpus 
Test  Set Annotated 
Evaluation Corpus 
ID | Grade | F 1| F 2| …Feature Extraction 
Machine Learning 
(SVM, DT, …)Evaluation 
(classification accuracy) ID | F 1| F 2| …Feature Extraction 
ID | Multi-Class Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -10- TMI 2007 Proposed Method Proposed Method 
1. Decomposition Phase: 
•decompose multi-class into set of binary classification tasks: 
°one-against-all (5, 4, 3, 2, 1): 
Example : 
5: +1 →all training examples tagged with grade 5
−1 →all training examples tagged with grade 4s or 3s or 2or 1)
°boundary (54_321 , 543_21 ): 
Example : 
54_321 : +1 →all training examples tagged with grade 5or 4
−1 →all training examples tagged with grade 3 or 2 or 1 
°all-pairs (5_4 , 5_3 , 5_2 , 5_1 , 4_3 , 4_2 , 4_1 , 3_2 , 3_1 , 2_1 ): 
Example : 
5_4 : +1 →all training examples tagged with grade 5
−1 →all training examples tagged with grade 4Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -11- TMI 2007 Proposed Method Proposed Method 
2. Learning Phase: 
•learn binary classifier for each decomposition task 
°feature set selection/extraction 
(exp) :  + 54 features (7 autom. eval. scores + metric-internal features) 
°classifier training 
(exp) :  + fluency /adequacy ,  DT classifier (+ SVM classifier) 
•identify optimal subset of binary classifiers 
•create coding matrix 
°column : class of pos./neg. training examples (for given binary classifier) 
°row : correct binary classification result (for a given multi-c lass label) 
3. Application Phase: 
•apply all binary classifiers to given input →classification vector v 
•match vagainst codingsmatrix rows to identify multi-class labelSpoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -12- TMI 2007 Outline of Proposed Method Outline of Proposed Method 
Source Text 
Evaluation Grade MT system 
Translated Text 
Feature Extraction 
Binary 
Classifiers 
Binary Class Vector 
Compare Annotated 
Evaluation Corpus 
Coding Matrix 
Optimization 
Optimized 
Coding Matrix Class De-
composition Machine 
Learning 
Binary 
Classifiers Coding 
Matrix Application Decomposition/Learning Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -13- TMI 2007 Coding Matrix Coding Matrix 
()
{ }0 , 1, 1,,...,1;,...,1,
−+∈===
jiljkiji
mmΜ
one-against-all all-pairs ( k=3 , l=3 ) 
−1−1 0c3 +1 −1 −1c3+1 0c2•c3
0+1 c1•c3
−1−1c3 •c1 c2
+1 −1c2 •c1 c3 c1•c2 c1 •c2 c3
c2c1
−1+1 
c2c1
−1+1 Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -14- TMI 2007 all-pairs 
−1 −1 0c3+1 0c2 •c3
0+1 c1 •c3 c1 •c2 
c2c1
−1+1 Combination of Binary 
Classifiers using a Coding Matrix Combination of Binary 
Classifiers using a Coding Matrix 
−1c2 •c3
+1 c1 •c3 c1 •c2 
v+1 input 
Hamming 
Distance 
(number of 
positions 
that differ) 
= 3 Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -15- TMI 2007 231distance 
−1+1 0c2 •c3
−1 0c3c1select 
0+1 c1 •c3 c1 •c2 
c2c1all-pairs 
−1+1 Combination of Binary 
Classifiers using a Coding Matrix Combination of Binary 
Classifiers using a Coding Matrix 
−1c2 •c3
+1 c1 •c3 c1 •c2 
v+1 input Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -16- TMI 2007 Basic Travel Expression Corpus (BTEC): 
•36K English translations of 4K Japanese/Chinese input s 
•human assessments and automatic evaluation scores Evaluation Corpus Evaluation Corpus 
0% 10% 20% 30% 40% 
5 4 3 2 1fluency adequacy 
7,590 (15 MT x 506) test 2,024 ( 4 MT x 506) develop 25,988 training fluency/ adequacy sentence count Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -17- TMI 2007 40 50 60 70 80 90 100 multicl
ass 
54
_32
1 54
3_
21 
5_4 
5_3 
5_
2 
5_
1 
4_3 
4_2 
4_
1 
3_
2 
3_
1 
2_1 
5
4
3
2
1(%)Fluency Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) classification accuracy Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -18- TMI 2007 Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) 
−1−1−1+1 +1 54_ 321 
−1−1+1 +1 +1 543 
_21 
000−1+1 5_4 
00−10+1 5_3 
0−100+1 5_2 
−1000+1 5_1 
00−1+1 04_3 
0−10+1 04_2 
−100+1 04_1 
0−1+1 003_2 
−10+1 003_1 
−1+1 0002_1 
−1−1−1+1 −14
−1−1+1 −1−13
−1−1 −1 4
−1−1 −1 3
+1 −1 −1 1−1−11
+1 −12 5
25
−1+1 Coding Matrix Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -19- TMI 2007 0510 15 20 25 30 35 40 45 
AL
L Fluency Coding Matrix Optimization 
(omission of worst-performing classifier) Coding Matrix Optimization 
(omission of worst-performing classifier) classification accuracy (%) 
omitted binary classifier Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -20- TMI 2007 40 50 60 70 80 90 100 mul
ticlass 
54_321 
543_21 
5_
4 
5_
3 
5_
2 
5_1 
4_3 
4_
2 
4_1 
3_2 
3_1 
2_1 
5
4
3
2
1(%)Fluency Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) classification accuracy Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -21- TMI 2007 Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) 
−1−1−1+1 +1 54_ 321 
−1−1+1 +1 +1 543 
_21 
000−1+1 5_4 
00−1−1+1 5_3 
0−100+1 5_2 
−1000+1 5_1 
00−1+1 04_3 
0−10+1 04_2 
−100+1 04_1 
0−1+1 003_2 
0−1+1 003_1 
−1+1 0002_1 
−1−1−1+1 −14
−1−1+1 −1−13
−1−1 −1 4
−1−1 −1 3
+1 −1 −1 1−1−11
+1 −12 5
25
−1+1 Coding Matrix Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -22- TMI 2007 0510 15 20 25 30 35 40 45 
AL
L 
4_3 Fluency Coding Matrix Optimization 
(omission of worst-performing classifier) Coding Matrix Optimization 
(omission of worst-performing classifier) classification accuracy (%) 
omitted binary classifier Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -23- TMI 2007 40 50 60 70 80 90 100 mul
ticlass 
54_321 
543_21 
5_
4 
5_
3 
5_
2 
5_1 
4_3 
4_
2 
4_1 
3_2 
3_1 
2_1 
5
4
3
2
1(%)Fluency Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) classification accuracy Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -24- TMI 2007 Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) 
−1−1−1+1 +1 54_ 321 
−1−1+1 +1 +1 543 
_21 
000−1+1 5_4 
00−1−1+1 5_3 
0−100+1 5_2 
−1000+1 5_1 
00−1+1 04_3 
0−10+1 04_2 
−100+1 04_1 
0−1+1 003_2 
0−1+1 003_1 
−1+1 0002_1 
−1−1−1+1 −14
−1−1+1 −1−13
−1−1 −1 4
−1−1 −1 3
+1 −1 −1 1−1−11
+1 −12 5
25
−1+1 Coding Matrix Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -25- TMI 2007 010 20 30 40 50 60 
ALL 
4_3 
3_2 
2_1 
4_2 
3_1 54_321 Fluency Coding Matrix Optimization 
(omission of worst-performing classifier) Coding Matrix Optimization 
(omission of worst-performing classifier) classification accuracy (%) 
omitted binary classifier Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -26- TMI 2007 010 20 30 40 50 60 
ALL 
4_3 
3_2 
2_1 
4_2 
3_1 54_321 543_21 
4_1 
5
1
5_4 
5_3 
5_2 
5_1 
2
3Fluency Coding Matrix Optimization 
(omission of worst-performing classifier) Coding Matrix Optimization 
(omission of worst-performing classifier) classification accuracy (%) 
omitted binary classifier Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -27- TMI 2007 Coding Matrix Optimization 
(classification accuracy on DEV set) Coding Matrix Optimization 
(classification accuracy on DEV set) 
−1−1−1+1 +1 54_ 321 
−1−1+1 +1 +1 543 
_21 
000−1+1 5_4 
00−1−1+1 5_3 
0−100+1 5_2 
−1000+1 5_1 
00−1+1 04_3 
0−10+1 04_2 
−100+1 04_1 
0−1+1 003_2 
0−1+1 003_1 
−1+1 0002_1 
−1−1−1+1 −14
−1−1+1 −1−13
−1−1 −1 4
−1−1 −1 3
+1 −1 −1 1−1−11
+1 −12 5
25
−1+1 Optimized Coding Matrix Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -28- TMI 2007 20 25 30 35 40 45 50 55 60 65 70 75 
multi-class coding matrix 
fluency adequacy Evaluation 
(classification accuracy on TEST set) Evaluation 
(classification accuracy on TEST set) 
49.2 / 56.0 55.2 / 62.2 +6.0 / +6.6 
(%)classification accuracy Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -29- TMI 2007 Correlation to Human 
Assessment on Sentence-LevelCorrelation to Human 
Assessment on Sentence-Level
Fluency 
00.1 0.2 0.3 0.4 0.5 0.6 0.7 coding matrix multicl
ass 
METEOR 
WER 
TER 
BLEU 
PER 
GTM 
NIST Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -30- TMI 2007 Correlation to Human 
Assessment on Sentence-LevelCorrelation to Human 
Assessment on Sentence-Level
Adequacy 
00.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 coding m
atrix 
METEO
R 
mul
ticlass 
GT
M 
WE
R 
PER 
NIST 
BLEU 
TER Spoken Language Communications 
Research Laboratories Spoken Language Communication Group 
2007 NICT/ATR -31- TMI 2007 Summary Summary 
Multiclassreduction to binary: 
•robust and reliable method to predict human assessments 
on sentence-level 
•high correlation to human judges outperforming commonly used 
automatic evaluation metrics 
•outperforms standard classification methods 
→gains: +6.0 (fluency )and +6.6 (adequacy )in classification accuracy 
Extension of proposed method: 
•apply learning method to select features used to build 
the coding matrix 
•investigate in the use of additional features that increase 
binary classification accuracy and thus boost overa ll multi-class 
prediction accuracy 