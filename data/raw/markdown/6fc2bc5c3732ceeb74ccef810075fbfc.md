NAACL 2022
The 2022 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language
Technologies
Tutorial Abstracts
July 10-15, 2022©2022 Association for Computational Linguistics
Order copies of this and other ACL proceedings from:
Association for Computational Linguistics (ACL)
209 N. Eighth Street
Stroudsburg, PA 18360
USA
Tel: +1-570-476-8006
Fax: +1-570-476-0860
acl@aclweb.org
ISBN 978-1-955917-99-5
iIntroduction
Welcome to the Tutorials Session of NAACL 2022!
The tutorials give an opportunity to the NAACL conference attendees to be lectured by highly qualiﬁed
expert researchers on cutting-edge and new relevant upcoming topics in our research community.
As in previous years, the organization (including submission, reviewing and selection) were coordinated
jointly with other conferences in the 2022 calendar year: ACL, NAACL, COLING and EMNLP. We
formed a review committee of 34 members, which includes the NAACL tutorial chairs, the ACL tutorial
chairs, the COLING tutorial chairs, the EMNLP tutorial chairs and 23 external reviewers (see Program
Committee for the full list). We organized a reviewing process so that each proposal received at least 3
reviews. Tutorials were evaluated based on their clarity, novelty, timely character of the topic, diversity
and inclusion, instructor’s experience, likely audience interest and open access of the tutorial instructio-
nal material. We received a total of 47 tutorial submissions, of which 6 were selected for presentation
at NAACL, considering the preferences expressed by authors and the relevance for the NAACL research
community.
We solicited two types of tutorials, namely cutting-edge themes and introductory themes. The 6 tutorials
for NAACL include one introductory tutorial and ﬁve cutting-edge tutorials. The introductory tutorial is
dedicated to Human-Centered Evaluation of Explanations (T4). The cutting-edge tutorials are: (T1) Text
Generation with Text-Editing Models, (T2) Self-supervised Representation Learning for Speech Pro-
cessing, (T3) New Frontiers of Information Extraction, (T5) Multimodal Machine Learning, and (T6)
Contrastive Data and Learning for Natural Language Processing. NAACL 2022 tutorials are delivered
in a live hybrid format and also available as pre-recorded captioned videos, with additional live Q&A
sessions.
We would like to thank the tutorial authors for their quick responses and ﬂexibility while organizing the
conference in a hybrid mode. We are also grateful to the 23 external reviewers for their invaluable help in
the decision process. Finally, we thank the conference organizers for effective collaboration, the general
chair Dan Roth, the program chairs (Marine Carpuat, Marie-Catherine de Marneffe and Ivan Vladimir
Meza Ruiz), the publication chair Ryan Cotterell, and the authors of aclpub2 with special mention to
Jordan Zhang and Danilo Croce.
NAACL 2022 Tutorial Co-chairs,
Miguel Ballesteros
Yulia Tsvetkov
Cecilia O. Alm
iiOrganizing Committee
General Chair
Dan Roth, University of Pennsylvania & AWS AI Labs, USA
Program Chairs
Marine Carpuat, University of Maryland, USA
Marie-Catherine de Marneffe de Marneffe, Ohio State University, USA
Ivan Vladimir Meza Ruiz, National Autonomous University of Mexico, Mexico
Tutorial Chairs
Miguel Ballesteros, AWS AI Labs, USA
Yulia Tsvetkov, University of Washington, USA
Cecilia O. Alm, Rochester Institute of Technology, USA
iiiProgram Committee
Program Committee
Cecilia O. Alm, Rochester Institute of Technology, USA
Antonios Anastasopoulos, George Mason University, USA
Miguel Ballesteros, AWS AI Labs, USA
Daniel Beck, University of Melbourne, Australia
Luciana Benotti, National University of Córdoba, Argentina
Yevgeni Berzak, Technion, Israel Institute of Technology, Israel
Erik Cambria, Nanyang Technological University, Singapore
Hsin-Hsi Chen, National Taiwan University, Taiwan
Gaël Dias, University of Caen Normandy, France
Lucia Donatelli, Saarland University, Germany
Samhaa R. El-Beltagy, Newgiza University, Egypt
Karën Fort, Sorbonne Université / LORIA, France
Heng Ji, University of Illinois, Urbana-Champaign, USA
David Jurgens, University of Michigan, USA
Naoaki Okazaki, Tokyo Institute of Technology, Japan
Alexis Palmer, University of Colorado, Boulder, USA
Mohammad Taher Pilehvar, Tehran Institute for Advanced Studies, Iran
Barbara Plank, LMU Munich, Germany and IT University of Copenhagen, Denmark
Emily Prud’hommeaux, Boston College, USA
Xipeng Qiu, Fudan University, China
Agata Savary, Université Paris-Saclay, France
João Sedoc, New York University, USA
Yulia Tsvetkov, University of Washington, USA
Aline Villavicencio, University of Shefﬁeld, UK
Ivan Vuli ´c, University of Cambridge, UK
Yogarshi Vyas, AWS AI Labs, USA
Joachim Wagner, Dublin City University, Ireland
Taro Watanabe, Nara Institute of Science and Technology, Japan
Aaron Steven White, University of Rochester, USA
Diyi Yang, Georgia Institute of Technology, USA
Marcos Zampieri, Rochester Institute of Technology, USA
Meishan Zhang, Harbin Institute of Technology (Shenzhen), China
Yue Zhang, Westlake University, China
Arkaitz Zubiaga, Queen Mary University London, UK
ivTable of Contents
Text Generation with Text-Editing Models
Eric Malmi, Yue Dong, Jonathan Mallinson, Aleksandr Chuklin, Jakub Adamek, Daniil Mirylen-
ka, Felix Stahlberg, Sebastian Krause, Shankar Kumar and Aliaksei Severyn . . . . . . . . . . . . . . . . . . . . . . 1
Self-supervised Representation Learning for Speech Processing
Hung-yi Lee, Abdelrahman Mohamed, Shinji Watanabe, Tara Sainath, Karen Livescu, Shang-Wen
Li, Shu-wen Yang and Katrin Kirchhoff. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
New Frontiers of Information Extraction
Muhao Chen, Lifu Huang, Manling Li, Ben Zhou, Heng Ji and Dan Roth . . . . . . . . . . . . . . . . . . . 14
Human-Centered Evaluation of Explanations
Jordan Boyd-Graber, Samuel Carton, Shi Feng, Q. Vera Liao, Tania Lombrozo, Alison Smith-
Renner and Chenhao Tan. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .26
Tutorial on Multimodal Machine Learning
Louis-Philippe Morency, Paul Pu Liang and Amir Zadeh . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Contrastive Data and Learning for Natural Language Processing
Rui Zhang, Yangfeng Ji, Yue Zhang and Rebecca J. Passonneau. . . . . . . . . . . . . . . . . . . . . . . . . . . .39
v