![Hugging Face's logo](https://huggingface.co/front/assets/huggingface_logo-noborder.svg) Hugging Face⟨1⟩
  *  Models ⟨2⟩
  *  Datasets ⟨3⟩
  *  Spaces ⟨4⟩
  *  Buckets new⟨5⟩
  *  Docs ⟨6⟩
  *  Enterprise ⟨7⟩
  * Pricing⟨8⟩
  *     * Website
      *  Tasks⟨9⟩
      *  HuggingChat⟨10⟩
      *  Collections⟨11⟩
      *  Languages⟨12⟩
      *  Organizations⟨13⟩
    * Community
      *  Blog⟨14⟩
      *  Posts⟨15⟩
      *  Daily Papers⟨16⟩
      *  Hardware⟨17⟩
      *  Learn⟨18⟩
      *  Discord⟨19⟩
      *  Forum⟨20⟩
      *  GitHub⟨21⟩
    * Solutions
      *  Team & Enterprise⟨7⟩
      *  Hugging Face PRO⟨22⟩
      *  Enterprise Support⟨23⟩
      *  Inference Providers⟨24⟩
      *  Inference Endpoints⟨25⟩
      *  Storage Buckets⟨5⟩
  * * * *
  * Log In⟨26⟩
  * Sign Up⟨27⟩


#   Datasets:⟨3⟩
* * *
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/no-auth/jFKssdAmmfvEqpmuPo8Oe.png) ⟨28⟩
Akram98⟨28⟩
/
AM-RAGBench⟨29⟩
like 0
Tasks:  Question Answering ⟨30⟩
Modalities:  Text ⟨31⟩
Formats:  json ⟨32⟩
Languages:  Arabic ⟨33⟩ Malay ⟨34⟩
Size:  1K - 10K ⟨35⟩
Libraries:  Datasets ⟨36⟩ Dask ⟨37⟩ Polars ⟨38⟩ + 1
License:
cc-by-4.0
 Dataset card ⟨29⟩ Data Studio ⟨39⟩ Files Files and versions xet ⟨40⟩ Community 1 ⟨41⟩
Dataset Viewer
 Auto-converted to Parquet⟨42⟩ API Embed  Duplicate⟨43⟩ Data Studio
Subset (1)
default · 1.14k rows
default (1.14k rows)
Split (1)
train · 1.14k rows
train (1.14k rows)
SQL
Console  
|  id stringlengths 14 17  |  language stringclasses 2 values  |  domain stringclasses 2 values  |  question stringlengths 12 175  |  gold_passage_id stringlengths 14 17  |  gold_passage_text stringlengths 13 957  |  gold_answer stringlengths 1 372  |  source_citation stringlengths 61 83  |  annotator_id stringclasses 1 value  |  verification_pass stringclasses 1 value  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  quran-1:2-ar-q0  |  ar  |  quran  |  إلى من يُوجه الثناء في هذا النص؟  |  quran-1:2-ar-q0  |  الحمد لله رب العالمين  |  الله  |  Quran 1:2 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:5-ar-q0  |  ar  |  quran  |  ما هما الفعلان المذكوران في النص؟  |  quran-1:5-ar-q0  |  إياك نعبد وإياك نستعين  |  نعبد ونستعين  |  Quran 1:5 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:7-ar-q0  |  ar  |  quran  |  إلى أي مجموعة يوجه النص صراطهم؟  |  quran-1:7-ar-q0  |  صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين  |  إلى الذين أنعمت عليهم  |  Quran 1:7 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:7-ar-q1  |  ar  |  quran  |  من هم الذين لا يسلكون هذا الصراط؟  |  quran-1:7-ar-q1  |  صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين  |  المغضوب عليهم والذين ضلوا  |  Quran 1:7 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:10-ar-q0  |  ar  |  quran  |  ماذا فعل الله في قلوبهم؟  |  quran-2:10-ar-q0  |  في قلوبهم مرض فزادهم الله مرضا ۖ ولهم عذاب أليم بما كانوا يكذبون  |  زادهم الله مرضاً  |  Quran 2:10 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:16-ar-q1  |  ar  |  quran  |  ما النتيجة التي ذكرت في النص عن تجارتهم؟  |  quran-2:16-ar-q1  |  أولئك الذين اشتروا الضلالة بالهدى فما ربحت تجارتهم وما كانوا مهتدين  |  لم يربحوا تجارتهم وما كانوا مهتدين  |  Quran 2:16 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:17-ar-q1  |  ar  |  quran  |  ماذا فعل الله بنورهم بعد أن أضاءت ما حوله؟  |  quran-2:17-ar-q1  |  مثلهم كمثل الذي استوقد نارا فلما أضاءت ما حوله ذهب الله بنورهم وتركهم في ظلمات لا يبصرون  |  ذهب بنورهم وتركهم في ظلمات لا يبصرون  |  Quran 2:17 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:18-ar-q0  |  ar  |  quran  |  من هو الشخص الذي يُشار إليه في النص؟  |  quran-2:18-ar-q0  |  صم بكم عمي فهم لا يرجعون  |  المنافقين  |  Quran 2:18 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:2-ar-q0  |  ar  |  quran  |  ما موقف النص من وجود ريب في الكتاب؟  |  quran-2:2-ar-q0  |  ذلك الكتاب لا ريب ۛ فيه ۛ هدى للمتقين  |  لا ريب فيه  |  Quran 2:2 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:20-ar-q0  |  ar  |  quran  |  ماذا يفعلون عندما يضيء لهم البرق؟  |  quran-2:20-ar-q0  |  يكاد البرق يخطف أبصارهم ۖ كلما أضاء لهم مشوا فيه وإذا أظلم عليهم قاموا ۚ ولو شاء الله لذهب بسمعهم وأبصارهم ۚ إن الله على كل شيء قدير  |  يمشون فيه  |  Quran 2:20 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:20-ar-q1  |  ar  |  quran  |  كيف يُوصف الله في النص؟  |  quran-2:20-ar-q1  |  يكاد البرق يخطف أبصارهم ۖ كلما أضاء لهم مشوا فيه وإذا أظلم عليهم قاموا ۚ ولو شاء الله لذهب بسمعهم وأبصارهم ۚ إن الله على كل شيء قدير  |  أنه على كل شيء قدير  |  Quran 2:20 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:21-ar-q0  |  ar  |  quran  |  إلى من توجّه الخطاب في هذا النص؟  |  quran-2:21-ar-q0  |  يا أيها الناس اعبدوا ربكم الذي خلقكم والذين من قبلكم لعلكم تتقون  |  إلى الناس  |  Quran 2:21 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:23-ar-q0  |  ar  |  quran  |  ماذا يُطلب من الأشخاص إذا كانوا في ريب مما نزل على عبدنا؟  |  quran-2:23-ar-q0  |  وإن كنتم في ريب مما نزلنا على عبدنا فأتوا بسورة من مثله وادعوا شهداءكم من دون الله إن كنتم صادقين  |  أن يأتوا بسورة من مثله وادعوا شهداءكم من دون الله  |  Quran 2:23 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:23-ar-q1  |  ar  |  quran  |  ما هو الشرط المذكور في نهاية النص؟  |  quran-2:23-ar-q1  |  وإن كنتم في ريب مما نزلنا على عبدنا فأتوا بسورة من مثله وادعوا شهداءكم من دون الله إن كنتم صادقين  |  أن يكونوا صادقين  |  Quran 2:23 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:24-ar-q1  |  ar  |  quran  |  لمن أعدت النار التي ذُكر في النص؟  |  quran-2:24-ar-q1  |  فإن لم تفعلوا ولن تفعلوا فاتقوا النار التي وقودها الناس والحجارة ۖ أعدت للكافرين  |  الكافرين  |  Quran 2:24 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:28-ar-q0  |  ar  |  quran  |  ما كانت حالهم قبل أن يُحيهم الله؟  |  quran-2:28-ar-q0  |  كيف تكفرون بالله وكنتم أمواتا فأحياكم ۖ ثم يميتكم ثم يحييكم ثم إليه ترجعون  |  كانوا أمواتا  |  Quran 2:28 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:33-ar-q0  |  ar  |  quran  |  من هو الشخص الذي وجه له الله الأمر بأن يُخبرهم بأسمائهم؟  |  quran-2:33-ar-q0  |  قال يا آدم أنبئهم بأسمائهم ۖ فلما أنبأهم بأسمائهم قال ألم أقل لكم إني أعلم غيب السماوات والأرض وأعلم ما تبدون وما كنتم تكتمون  |  آدم.  |  Quran 2:33 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:33-ar-q1  |  ar  |  quran  |  ما هو ما قاله هو أنه يعلمه؟  |  quran-2:33-ar-q1  |  قال يا آدم أنبئهم بأسمائهم ۖ فلما أنبأهم بأسمائهم قال ألم أقل لكم إني أعلم غيب السماوات والأرض وأعلم ما تبدون وما كنتم تكتمون  |  غيب السماوات والأرض وأعلم ما تبدون وما كنتم تكتمون.  |  Quran 2:33 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:35-ar-q0  |  ar  |  quran  |  إلى من وجه الله هذه الأوامر في النص؟  |  quran-2:35-ar-q0  |  وقلنا يا آدم اسكن أنت وزوجك الجنة وكلا منها رغدا حيث شئتما ولا تقربا هذه الشجرة فتكونا من الظالمين  |  إلى آدم وزوجته  |  Quran 2:35 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:35-ar-q1  |  ar  |  quran  |  ما العاقبة التي تنذر بها النص لمن قد يقرب هذه الشجرة؟  |  quran-2:35-ar-q1  |  وقلنا يا آدم اسكن أنت وزوجك الجنة وكلا منها رغدا حيث شئتما ولا تقربا هذه الشجرة فتكونا من الظالمين  |  أن يكونا من الظالمين  |  Quran 2:35 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:41-ar-q0  |  ar  |  quran  |  Q1: ماذا يُطلب من المؤمنين؟  |  quran-2:41-ar-q0  |  وآمنوا بما أنزلت مصدقا لما معكم ولا تكونوا أول كافر به ۖ ولا تشتروا بآياتي ثمنا قليلا وإياي فاتقون  |  A1: أن يؤمنوا بما أنزلت مصدقا لما معكم.  |  Quran 2:41 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:42-ar-q1  |  ar  |  quran  |  متى يجب على الإنسان عدم كتمان الحق؟  |  quran-2:42-ar-q1  |  ولا تلبسوا الحق بالباطل وتكتموا الحق وأنتم تعلمون  |  عندما تعلمون  |  Quran 2:42 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:44-ar-q1  |  ar  |  quran  |  ما السبب الذي يُسأل به في النص "أفلا تعقلون"؟  |  quran-2:44-ar-q1  |  أتأمرون الناس بالبر وتنسون أنفسكم وأنتم تتلون الكتاب ۚ أفلا تعقلون  |  يأمرون الناس بالبر وتنسون أنفسكم ويتلون الكتاب  |  Quran 2:44 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:57-ar-q0  |  ar  |  quran  |  ماذا أنزل الله عليكم لتأكلوا من طيبات؟  |  quran-2:57-ar-q0  |  وظللنا عليكم الغمام وأنزلنا عليكم المن والسلوى ۖ كلوا من طيبات ما رزقناكم ۖ وما ظلمونا ولكن كانوا أنفسهم يظلمون  |  المن والسلوى.  |  Quran 2:57 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:57-ar-q1  |  ar  |  quran  |  من كان يظلمون أنفسهم في هذا الأمر؟  |  quran-2:57-ar-q1  |  وظللنا عليكم الغمام وأنزلنا عليكم المن والسلوى ۖ كلوا من طيبات ما رزقناكم ۖ وما ظلمونا ولكن كانوا أنفسهم يظلمون  |  بنو إسرائيل  |  Quran 2:57 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:62-ar-q0  |  ar  |  quran  |  ما هي الشروط المذكورة في النص للحصول على الأجر عند الرب وخلاص من الخوف والحزن؟  |  quran-2:62-ar-q0  |  إن الذين آمنوا والذين هادوا والنصارى والصابئين من آمن بالله واليوم الآخر وعمل صالحا فلهم أجرهم عند ربهم ولا خوف عليهم ولا هم يحزنون  |  الإيمان بالله واليوم الآخر والعمل صالحاً  |  Quran 2:62 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:64-ar-q0  |  ar  |  quran  |  ما كان سيحدث للناس لو لم يكن فضل الله ورحمته؟  |  quran-2:64-ar-q0  |  ثم توليتم من بعد ذلك ۖ فلولا فضل الله عليكم ورحمته لكنتم من الخاسرين  |  كانوا من الخاسرين  |  Quran 2:64 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:66-ar-q0  |  ar  |  quran  |  من هم المستهدفون بهذه الموعظة؟  |  quran-2:66-ar-q0  |  فجعلناها نكالا لما بين يديها وما خلفها وموعظة للمتقين  |  المؤمنون الصادقون  |  Quran 2:66 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:68-ar-q0  |  ar  |  quran  |  ماذا طلبوا من ربه ليبيّن لهم؟  |  quran-2:68-ar-q0  |  قالوا ادع لنا ربك يبين لنا ما هي ۚ قال إنه يقول إنها بقرة لا فارض ولا بكر عوان بين ذلك ۖ فافعلوا ما تؤمرون  |  صفات وحقيقة البقرة  |  Quran 2:68 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:7-ar-q0  |  ar  |  quran  |  ماذا فعل الله على قلوبهم وعلى سمعهم وعلى أبصارهم؟  |  quran-2:7-ar-q0  |  ختم الله على قلوبهم وعلى سمعهم ۖ وعلى أبصارهم غشاوة ۖ ولهم عذاب عظيم  |  ختم الله على قلوبهم وعلى سمعهم وعلى أبصارهم غشاوة  |  Quran 2:7 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:72-ar-q1  |  ar  |  quran  |  ما هو وصف الله فيما يتعلق بما كنتم تكتمون؟  |  quran-2:72-ar-q1  |  وإذ قتلتم نفسا فادارأتم فيها ۖ والله مخرج ما كنتم تكتمون  |  هو مخرج ما كنتم تكتمون  |  Quran 2:72 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:75-ar-q1  |  ar  |  quran  |  ماذا يُعرف بالفريق المذكور في نهاية الجملة؟  |  quran-2:75-ar-q1  |  أفتطمعون أن يؤمنوا لكم وقد كان فريق منهم يسمعون كلام الله ثم يحرفونه من بعد ما عقلوه وهم يعلمون  |  أنهم يعلمون  |  Quran 2:75 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:78-ar-q0  |  ar  |  quran  |  من هم الذين لا يعلمون الكتاب في هذا النص؟  |  quran-2:78-ar-q0  |  ومنهم أميون لا يعلمون الكتاب إلا أماني وإن هم إلا يظنون  |  الأميون  |  Quran 2:78 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:78-ar-q1  |  ar  |  quran  |  كيف يصف النص فهمهم للكتاب؟  |  quran-2:78-ar-q1  |  ومنهم أميون لا يعلمون الكتاب إلا أماني وإن هم إلا يظنون  |  أنهم لا يعلمونه إلا أماني وإن هم إلا يظنون  |  Quran 2:78 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:79-ar-q0  |  ar  |  quran  |  من هم الذين يُذْكَر في النص؟  |  quran-2:79-ar-q0  |  فويل للذين يكتبون الكتاب بأيديهم ثم يقولون هذا من عند الله ليشتروا به ثمنا قليلا ۖ فويل لهم مما كتبت أيديهم وويل لهم مما يكسبون  |  هم الذين يكتبون الكتاب بأيديهم ثم يقولون هذا من عند الله ليشتروا به ثمنا قليلا  |  Quran 2:79 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:8-ar-q0  |  ar  |  quran  |  ماذا يقول هؤلاء الأشخاص عن أنفسهم؟  |  quran-2:8-ar-q0  |  ومن الناس من يقول آمنا بالله وباليوم الآخر وما هم بمؤمنين  |  أنهم آمنا بالله وباليوم الآخر  |  Quran 2:8 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:81-ar-q0  |  ar  |  quran  |  من هم أولئك أصحاب النار المذكورون في النص؟  |  quran-2:81-ar-q0  |  بلى من كسب سيئة وأحاطت به خطيئته فأولئك أصحاب النار ۖ هم فيها خالدون  |  هم من كسب سيئة وأحاطت به خطيئته  |  Quran 2:81 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:82-ar-q0  |  ar  |  quran  |  من هم أصحاب الجنة المذكورون في هذا النص؟  |  quran-2:82-ar-q0  |  والذين آمنوا وعملوا الصالحات أولئك أصحاب الجنة ۖ هم فيها خالدون  |  أولئك الذين آمنوا وعملوا الصالحات  |  Quran 2:82 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:82-ar-q1  |  ar  |  quran  |  ماذا وصف النص لهم في الجنة؟  |  quran-2:82-ar-q1  |  والذين آمنوا وعملوا الصالحات أولئك أصحاب الجنة ۖ هم فيها خالدون  |  أنهم خالدون  |  Quran 2:82 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:92-ar-q1  |  ar  |  quran  |  ماذا فعل "أنتم" بعد موسى؟  |  quran-2:92-ar-q1  |  ولقد جاءكم موسى بالبينات ثم اتخذتم العجل من بعده وأنتم ظالمون  |  اتخذوا العجل اله من غير رب العالمين  |  Quran 2:92 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:1-ar-q0  |  ar  |  quran  |  ما هو الاسم المذكور في النص؟  |  quran-1:1-ar-q0  |  بسم الله الرحمن الرحيم  |  الله  |  Quran 1:1 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:1-ar-q1  |  ar  |  quran  |  ما هي الكلمات التي تلي الاسم في النص؟  |  quran-1:1-ar-q1  |  بسم الله الرحمن الرحيم  |  الرحمن الرحيم  |  Quran 1:1 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:2-ar-q1  |  ar  |  quran  |  ما هو الوصف الذي يُنسب إلى الله في هذا النص؟  |  quran-1:2-ar-q1  |  الحمد لله رب العالمين  |  رب العالمين  |  Quran 1:2 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:3-ar-q0  |  ar  |  quran  |  ما هي الكلمات الموجودة في النص؟  |  quran-1:3-ar-q0  |  الرحمن الرحيم  |  الرحمن الرحيم  |  Quran 1:3 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-1:5-ar-q1  |  ar  |  quran  |  ما هو العنصر المتكرر في بداية كل جزء من النص؟  |  quran-1:5-ar-q1  |  إياك نعبد وإياك نستعين  |  إياك  |  Quran 1:5 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:1-ar-q0  |  ar  |  quran  |  ما هي العبارة التي تبدأ النص؟  |  quran-2:1-ar-q0  |  بسم الله الرحمن الرحيم الم  |  بسم الله الرحمن الرحيم  |  Quran 2:1 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:1-ar-q1  |  ar  |  quran  |  ما هو الجزء الذي يأتي في نهاية النص؟  |  quran-2:1-ar-q1  |  بسم الله الرحمن الرحيم الم  |  الم  |  Quran 2:1 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:10-ar-q1  |  ar  |  quran  |  ما سبب عذابهم الأليم؟  |  quran-2:10-ar-q1  |  في قلوبهم مرض فزادهم الله مرضا ۖ ولهم عذاب أليم بما كانوا يكذبون  |  بما كانوا يكذبون  |  Quran 2:10 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:11-ar-q0  |  ar  |  quran  |  ماذا يقولون إذا قيل لهم لا تفسدوا في الأرض؟  |  quran-2:11-ar-q0  |  وإذا قيل لهم لا تفسدوا في الأرض قالوا إنما نحن مصلحون  |  قالوا إنما نحن مصلحون  |  Quran 2:11 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:11-ar-q1  |  ar  |  quran  |  ما هو الأمر الذي يُوجه إليهم في النص؟  |  quran-2:11-ar-q1  |  وإذا قيل لهم لا تفسدوا في الأرض قالوا إنما نحن مصلحون  |  لا تفسدوا في الأرض  |  Quran 2:11 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:13-ar-q0  |  ar  |  quran  |  ماذا قالوا عندما قيل لهم أنؤمنوا كما آمن الناس؟  |  quran-2:13-ar-q0  |  وإذا قيل لهم آمنوا كما آمن الناس قالوا أنؤمن كما آمن السفهاء ۗ ألا إنهم هم السفهاء ولكن لا يعلمون  |  قالوا أنؤمن كما آمن السفهاء  |  Quran 2:13 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:13-ar-q1  |  ar  |  quran  |  ماذا يُقال عنهم في النص؟  |  quran-2:13-ar-q1  |  وإذا قيل لهم آمنوا كما آمن الناس قالوا أنؤمن كما آمن السفهاء ۗ ألا إنهم هم السفهاء ولكن لا يعلمون  |  هم السفهاء ولكن لا يعلمون  |  Quran 2:13 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:14-ar-q0  |  ar  |  quran  |  ماذا يقولون إذا لقوا الذين آمنوا؟  |  quran-2:14-ar-q0  |  وإذا لقوا الذين آمنوا قالوا آمنا وإذا خلوا إلى شياطينهم قالوا إنا معكم إنما نحن مستهزئون  |  قالوا آمنا  |  Quran 2:14 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:14-ar-q1  |  ar  |  quran  |  متى يقولون أنهم مستهزئون؟  |  quran-2:14-ar-q1  |  وإذا لقوا الذين آمنوا قالوا آمنا وإذا خلوا إلى شياطينهم قالوا إنا معكم إنما نحن مستهزئون  |  إذا خلوا إلى شياطينهم  |  Quran 2:14 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:15-ar-q0  |  ar  |  quran  |  ما هي الأفعال التي يمارسها الله تجاههم في النص؟  |  quran-2:15-ar-q0  |  الله يستهزئ بهم ويمدهم في طغيانهم يعمهون  |  يستهزئ بهم ويمدهم في طغيانهم وكفرهم  |  Quran 2:15 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:15-ar-q1  |  ar  |  quran  |  ما هو الوصف الخاص بهم المذكور في الجملة؟  |  quran-2:15-ar-q1  |  الله يستهزئ بهم ويمدهم في طغيانهم يعمهون  |  في طغيانهم يعمهون  |  Quran 2:15 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:16-ar-q0  |  ar  |  quran  |  ماذا اشترى أولئك الذين بالهدى؟  |  quran-2:16-ar-q0  |  أولئك الذين اشتروا الضلالة بالهدى فما ربحت تجارتهم وما كانوا مهتدين  |  الضلالة  |  Quran 2:16 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:17-ar-q0  |  ar  |  quran  |  ما هو التشبيه الذي ورد في النص لوصف حالتهم؟  |  quran-2:17-ar-q0  |  مثلهم كمثل الذي استوقد نارا فلما أضاءت ما حوله ذهب الله بنورهم وتركهم في ظلمات لا يبصرون  |  كمثل الذي استوقد نارا  |  Quran 2:17 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:18-ar-q1  |  ar  |  quran  |  ماذا يفعلون (أو لا يفعلون) حسب النص؟  |  quran-2:18-ar-q1  |  صم بكم عمي فهم لا يرجعون  |  لا يرجعون  |  Quran 2:18 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:19-ar-q0  |  ar  |  quran  |  من هو الذي محيط بالكافرين؟  |  quran-2:19-ar-q0  |  أو كصيب من السماء فيه ظلمات ورعد وبرق يجعلون أصابعهم في آذانهم من الصواعق حذر الموت ۚ والله محيط بالكافرين  |  الله  |  Quran 2:19 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:19-ar-q1  |  ar  |  quran  |  ماذا يفعلون عند حدوث الصواعق؟  |  quran-2:19-ar-q1  |  أو كصيب من السماء فيه ظلمات ورعد وبرق يجعلون أصابعهم في آذانهم من الصواعق حذر الموت ۚ والله محيط بالكافرين  |  يجعلون أصابعهم في آذانهم  |  Quran 2:19 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:2-ar-q1  |  ar  |  quran  |  من المتصفون بهذا الكتاب كهدى؟  |  quran-2:2-ar-q1  |  ذلك الكتاب لا ريب ۛ فيه ۛ هدى للمتقين  |  للمتقين  |  Quran 2:2 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:21-ar-q1  |  ar  |  quran  |  ما هو الغرض المذكور من عبادة ربكم؟  |  quran-2:21-ar-q1  |  يا أيها الناس اعبدوا ربكم الذي خلقكم والذين من قبلكم لعلكم تتقون  |  لعلكم تتقون  |  Quran 2:21 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:22-ar-q0  |  ar  |  quran  |  ماذا فعل الله بالأرض والسماء؟  |  quran-2:22-ar-q0  |  الذي جعل لكم الأرض فراشا والسماء بناء وأنزل من السماء ماء فأخرج به من الثمرات رزقا لكم ۖ فلا تجعلوا لله أندادا وأنتم تعلمون  |  جعل لكم الأرض فراشا والسماء بناء  |  Quran 2:22 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:22-ar-q1  |  ar  |  quran  |  ما التحذير الذي ورد في النص؟  |  quran-2:22-ar-q1  |  الذي جعل لكم الأرض فراشا والسماء بناء وأنزل من السماء ماء فأخرج به من الثمرات رزقا لكم ۖ فلا تجعلوا لله أندادا وأنتم تعلمون  |  لا تجعلوا لله أندادا  |  Quran 2:22 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:24-ar-q0  |  ar  |  quran  |  ما هو وقود النار الذي ذُكر في النص؟  |  quran-2:24-ar-q0  |  فإن لم تفعلوا ولن تفعلوا فاتقوا النار التي وقودها الناس والحجارة ۖ أعدت للكافرين  |  الناس والحجارة  |  Quran 2:24 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:25-ar-q0  |  ar  |  quran  |  ما الذي جاء به النص للذين آمنوا وعملوا الصالحات؟  |  quran-2:25-ar-q0  |  وبشر الذين آمنوا وعملوا الصالحات أن لهم جنات تجري من تحتها الأنهار ۖ كلما رزقوا منها من ثمرة رزقا ۙ قالوا هذا الذي رزقنا من قبل ۖ وأتوا به متشابها ۖ ولهم فيها أزواج مطهرة ۖ وهم فيها خالدون  |  أن لهم جنات تجري من تحتها الأنهار  |  Quran 2:25 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:25-ar-q1  |  ar  |  quran  |  ماذا قالوا كلما رزقوا منها من ثمرة رزقا؟  |  quran-2:25-ar-q1  |  وبشر الذين آمنوا وعملوا الصالحات أن لهم جنات تجري من تحتها الأنهار ۖ كلما رزقوا منها من ثمرة رزقا ۙ قالوا هذا الذي رزقنا من قبل ۖ وأتوا به متشابها ۖ ولهم فيها أزواج مطهرة ۖ وهم فيها خالدون  |  قالوا هذا الذي رزقنا من قبل  |  Quran 2:25 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:26-ar-q0  |  ar  |  quran  |  من يعلمون أنه الحق من ربهم؟  |  quran-2:26-ar-q0  |  إن الله لا يستحيي أن يضرب مثلا ما بعوضة فما فوقها ۚ فأما الذين آمنوا فيعلمون أنه الحق من ربهم ۖ وأما الذين كفروا فيقولون ماذا أراد الله بهذا مثلا ۘ يضل به كثيرا ويهدي به كثيرا ۚ وما يضل به إلا الفاسقين  |  الذين آمنوا  |  Quran 2:26 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:26-ar-q1  |  ar  |  quran  |  ما يضل الله به إلا؟  |  quran-2:26-ar-q1  |  إن الله لا يستحيي أن يضرب مثلا ما بعوضة فما فوقها ۚ فأما الذين آمنوا فيعلمون أنه الحق من ربهم ۖ وأما الذين كفروا فيقولون ماذا أراد الله بهذا مثلا ۘ يضل به كثيرا ويهدي به كثيرا ۚ وما يضل به إلا الفاسقين  |  الفاسقين  |  Quran 2:26 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:27-ar-q0  |  ar  |  quran  |  ما هو الحكم المذكور لأولئك الذين ينقضون عهد الله ويقطعون ما أمر الله به في الأرض؟  |  quran-2:27-ar-q0  |  الذين ينقضون عهد الله من بعد ميثاقه ويقطعون ما أمر الله به أن يوصل ويفسدون في الأرض ۚ أولئك هم الخاسرون  |  أولئك هم الخاسرون  |  Quran 2:27 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:27-ar-q1  |  ar  |  quran  |  ما هو الفعل الذي يمارسونه في الأرض؟  |  quran-2:27-ar-q1  |  الذين ينقضون عهد الله من بعد ميثاقه ويقطعون ما أمر الله به أن يوصل ويفسدون في الأرض ۚ أولئك هم الخاسرون  |  يفسدون في الأرض  |  Quran 2:27 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:28-ar-q1  |  ar  |  quran  |  إلى من تُرجعون في النهاية؟  |  quran-2:28-ar-q1  |  كيف تكفرون بالله وكنتم أمواتا فأحياكم ۖ ثم يميتكم ثم يحييكم ثم إليه ترجعون  |  الى الله رب العالمين يوم القيامة  |  Quran 2:28 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:29-ar-q0  |  ar  |  quran  |  ماذا فعل هو بعد خلق ما في الأرض؟  |  quran-2:29-ar-q0  |  هو الذي خلق لكم ما في الأرض جميعا ثم استوى إلى السماء فسواهن سبع سماوات ۚ وهو بكل شيء عليم  |  استوى إلى السماء فسواهن سبع سماوات  |  Quran 2:29 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:29-ar-q1  |  ar  |  quran  |  ما الصفة التي يوصف بها هو في نهاية النص؟  |  quran-2:29-ar-q1  |  هو الذي خلق لكم ما في الأرض جميعا ثم استوى إلى السماء فسواهن سبع سماوات ۚ وهو بكل شيء عليم  |  هو بكل شيء عليم  |  Quran 2:29 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:3-ar-q0  |  ar  |  quran  |  من هم الذين ينفقون مما رزقناهم؟  |  quran-2:3-ar-q0  |  الذين يؤمنون بالغيب ويقيمون الصلاة ومما رزقناهم ينفقون  |  الذين يؤمنون بالغيب ويقيمون الصلاة  |  Quran 2:3 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:3-ar-q1  |  ar  |  quran  |  ماذا ينفقون؟  |  quran-2:3-ar-q1  |  الذين يؤمنون بالغيب ويقيمون الصلاة ومما رزقناهم ينفقون  |  مما رزقناهم  |  Quran 2:3 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:30-ar-q0  |  ar  |  quran  |  من الذي قال للملائكة إنه سيضع في الأرض خليفة؟  |  quran-2:30-ar-q0  |  وإذ قال ربك للملائكة إني جاعل في الأرض خليفة ۖ قالوا أتجعل فيها من يفسد فيها ويسفك الدماء ونحن نسبح بحمدك ونقدس لك ۖ قال إني أعلم ما لا تعلمون  |  الله رب العالمين  |  Quran 2:30 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:30-ar-q1  |  ar  |  quran  |  ما هي المخاوف التي عبّر عنها الملائكة بخصوص وضع خليفة في الأرض؟  |  quran-2:30-ar-q1  |  وإذ قال ربك للملائكة إني جاعل في الأرض خليفة ۖ قالوا أتجعل فيها من يفسد فيها ويسفك الدماء ونحن نسبح بحمدك ونقدس لك ۖ قال إني أعلم ما لا تعلمون  |  قالوا أتجعل فيها من يفسد فيها ويسفك الدماء  |  Quran 2:30 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:31-ar-q0  |  ar  |  quran  |  من هو الشخص الذي تعلم الأسماء كلها ثم عرضها على الملائكة؟  |  quran-2:31-ar-q0  |  وعلم آدم الأسماء كلها ثم عرضهم على الملائكة فقال أنبئوني بأسماء هؤلاء إن كنتم صادقين  |  ادم عليه السلام  |  Quran 2:31 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:31-ar-q1  |  ar  |  quran  |  ماذا قال آدم للملائكة؟  |  quran-2:31-ar-q1  |  وعلم آدم الأسماء كلها ثم عرضهم على الملائكة فقال أنبئوني بأسماء هؤلاء إن كنتم صادقين  |  أنبئوني بأسماء هؤلاء إن كنتم صادقين  |  Quran 2:31 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:32-ar-q0  |  ar  |  quran  |  ماذا قالوا عن معرفتهم؟  |  quran-2:32-ar-q0  |  قالوا سبحانك لا علم لنا إلا ما علمتنا ۖ إنك أنت العليم الحكيم  |  لا علم لنا إلا ما علمتنا  |  Quran 2:32 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:32-ar-q1  |  ar  |  quran  |  كيف يصفون الله في هذا القول؟  |  quran-2:32-ar-q1  |  قالوا سبحانك لا علم لنا إلا ما علمتنا ۖ إنك أنت العليم الحكيم  |  العليم الحكيم  |  Quran 2:32 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:34-ar-q0  |  ar  |  quran  |  من هو الذي أبى أن يسجد لآدم؟  |  quran-2:34-ar-q0  |  وإذ قلنا للملائكة اسجدوا لآدم فسجدوا إلا إبليس أبى واستكبر وكان من الكافرين  |  إبليس  |  Quran 2:34 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:34-ar-q1  |  ar  |  quran  |  كيف وصف الله إبليس في الآية؟  |  quran-2:34-ar-q1  |  وإذ قلنا للملائكة اسجدوا لآدم فسجدوا إلا إبليس أبى واستكبر وكان من الكافرين  |  أبى واستكبر وكان من الكافرين  |  Quran 2:34 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:37-ar-q0  |  ar  |  quran  |  ماذا تلقى آدم من ربه؟  |  quran-2:37-ar-q0  |  فتلقى آدم من ربه كلمات فتاب عليه ۚ إنه هو التواب الرحيم  |  كلمات  |  Quran 2:37 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:37-ar-q1  |  ar  |  quran  |  كيف وصف الله نفسه في نهاية النص؟  |  quran-2:37-ar-q1  |  فتلقى آدم من ربه كلمات فتاب عليه ۚ إنه هو التواب الرحيم  |  التواب الرحيم  |  Quran 2:37 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:38-ar-q0  |  ar  |  quran  |  ما هو الأمر الذي قيل لهم؟  |  quran-2:38-ar-q0  |  قلنا اهبطوا منها جميعا ۖ فإما يأتينكم مني هدى فمن تبع هداي فلا خوف عليهم ولا هم يحزنون  |  اهبطوا منها جميعا  |  Quran 2:38 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:38-ar-q1  |  ar  |  quran  |  من هم الذين لا خوف عليهم ولا هم يحزنون؟  |  quran-2:38-ar-q1  |  قلنا اهبطوا منها جميعا ۖ فإما يأتينكم مني هدى فمن تبع هداي فلا خوف عليهم ولا هم يحزنون  |  من تبع هداي  |  Quran 2:38 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:39-ar-q0  |  ar  |  quran  |  من هم أصحاب النار؟  |  quran-2:39-ar-q0  |  والذين كفروا وكذبوا بآياتنا أولئك أصحاب النار ۖ هم فيها خالدون  |  الذين كفروا وكذبوا بآياتنا  |  Quran 2:39 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:39-ar-q1  |  ar  |  quran  |  ما وصف لحال أولئك الأشخاص في النار؟  |  quran-2:39-ar-q1  |  والذين كفروا وكذبوا بآياتنا أولئك أصحاب النار ۖ هم فيها خالدون  |  هم فيها خالدون  |  Quran 2:39 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:4-ar-q0  |  ar  |  quran  |  من هم الذين يوقنون؟  |  quran-2:4-ar-q0  |  والذين يؤمنون بما أنزل إليك وما أنزل من قبلك وبالآخرة هم يوقنون  |  الذين يؤمنون بما أنزل إليك وما أنزل من قبلك وبالآخرة  |  Quran 2:4 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:4-ar-q1  |  ar  |  quran  |  ماذا يؤمنون به؟  |  quran-2:4-ar-q1  |  والذين يؤمنون بما أنزل إليك وما أنزل من قبلك وبالآخرة هم يوقنون  |  بما أنزل إليك وما أنزل من قبلك وبالآخرة  |  Quran 2:4 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:40-ar-q0  |  ar  |  quran  |  إلى من يوجه الخطاب في هذا النص؟  |  quran-2:40-ar-q0  |  يا بني إسرائيل اذكروا نعمتي التي أنعمت عليكم وأوفوا بعهدي أوف بعهدكم وإياي فارهبون  |  بني إسرائيل  |  Quran 2:40 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:40-ar-q1  |  ar  |  quran  |  ماذا يُطلب من المستمعين أن يذكرو؟  |  quran-2:40-ar-q1  |  يا بني إسرائيل اذكروا نعمتي التي أنعمت عليكم وأوفوا بعهدي أوف بعهدكم وإياي فارهبون  |  نعمتي التي أنعمت عليكم  |  Quran 2:40 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:42-ar-q0  |  ar  |  quran  |  ما هما الأمران المحرمان المذكوران في النص؟  |  quran-2:42-ar-q0  |  ولا تلبسوا الحق بالباطل وتكتموا الحق وأنتم تعلمون  |  تلبسوا الحق بالباطل وتكتموا الحق  |  Quran 2:42 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:44-ar-q0  |  ar  |  quran  |  ما الفعل الذي يُمارس تجاه أنفسهم في النص؟  |  quran-2:44-ar-q0  |  أتأمرون الناس بالبر وتنسون أنفسكم وأنتم تتلون الكتاب ۚ أفلا تعقلون  |  تنسون أنفسكم  |  Quran 2:44 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:45-ar-q0  |  ar  |  quran  |  ما هي الوسيلة التي يُوصى بالاستعانة بها في النص؟  |  quran-2:45-ar-q0  |  واستعينوا بالصبر والصلاة ۚ وإنها لكبيرة إلا على الخاشعين  |  الصبر والصلاة  |  Quran 2:45 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:45-ar-q1  |  ar  |  quran  |  من هي الفئة التي تُفهم فيها أن الصبر والصلاة ليستا كبيرة؟  |  quran-2:45-ar-q1  |  واستعينوا بالصبر والصلاة ۚ وإنها لكبيرة إلا على الخاشعين  |  الخاشعين  |  Quran 2:45 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
|  quran-2:46-ar-q0  |  ar  |  quran  |  من هم الأشخاص الذين يصفهم النص؟  |  quran-2:46-ar-q0  |  الذين يظنون أنهم ملاقو ربهم وأنهم إليه راجعون  |  المؤمنين الخاشعين.  |  Quran 2:46 (Arabic, Tanzil.net Uthmani/Simple text, CC BY 3.0)  |  akram  |  primary  |  
End of preview. Expand in Data Studio⟨44⟩
* * *
  *  Previous⟨29⟩
  * 1⟨45⟩
  * 2⟨46⟩
  * 3⟨47⟩
  * ...⟨48⟩
  * 12⟨49⟩
  * Next ⟨46⟩


  * Files⟨50⟩
  * Fields⟨51⟩
  * License⟨52⟩


#   ⟨53⟩ AM-RAGBench 
Human-verified Arabic-Malay benchmark for evaluating retrieval-augmented generation (RAG) faithfulness. 1,140 question-answer pairs spanning a specialized domain (Quran, Arabic and Basmeih Malay translation) and a general domain (Arabic and Malay Wikipedia), each with a gold passage, a gold answer, and a verification decision made during construction.
##   ⟨50⟩ Files 
  * `quran_verified.jsonl`: specialized-domain records.
  * `wiki_verified.jsonl`: general-domain records.


##   ⟨51⟩ Fields 
Each record includes: `id`, `domain`, `language`, `question`, `gold_answer`, `gold_passage_text`, `source_citation`, `verification_pass`.
##   ⟨52⟩ License 
The questions, answers, and verification labels in this dataset are released under CC BY 4.0. The underlying passage text carries its own upstream license: Quran text is from Tanzil.net (CC BY 3.0), and Wikipedia passages are CC BY-SA 4.0. Redistribution of the Wikipedia-derived `gold_passage_text` fields must comply with CC BY-SA 4.0's share-alike requirement in addition to attribution.
Copy to bucket new
Use this dataset 

Downloads last month
    56
Number of rows: 1,140 Total file size: 1.07 MB
System theme
Company
TOS⟨54⟩ Privacy⟨55⟩ About⟨56⟩ Careers⟨57⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
