arXiv is now an independent nonprofit! Learn more ×
License: CC BY 4.0 
arXiv:2607.25130v1 [cs.SE] 27 Jul 2026
# Learning from 53.6K Real-World Developer Edits of AI-Generated Code
Jenny T. Liang Mihika Bairathi Wayne Chi Ameet Talwalkar Nishant Subramani Valerie Chen Carnegie Mellon University {jtliang, mbairath, vchen2}@cs.cmu.edu
###### Abstract
Imperfections in AI-generated code require that software developers modify the generated code manually, or by re-prompting an AI programming assistant. Manual code edits provide more realistic and granular information on editing behavior than Git commits, which only contain final successful code snippets. Yet, due to a lack of high-quality, realistic code editing data, LLMs are mostly trained on publicly available Git data (e.g., commits). To address this gap, we introduce Decode (Developer Edits of Code Dataset), a dataset of 53.6K real-world in-IDE code edits of AI-generated code in Python, TypeScript, and JavaScript, sourced from 1K+ developers. First, we demonstrate the utility of Decode for data analysis, obtaining insights on when, why, and how AI-generated code is edited. We find that most edits occur within the first 15 minutes after accepting an AI completion, resulting in the removal of AI completions in 31% of edit trajectories. Second, we use Decode to benchmark the ability of LLMs to predict code edits. We find that finetuning on Decode enables open-source 3B models to perform code edit prediction tasks significantly better than frontier LLMs. We then discuss implications of this work, emphasizing the necessity of developer-centric machine learning approaches for future AI programming assistants.
Decode captures diverse code editing behavior. We show three examples of real-world developer code edit trajectories in Decode. The original AI completion is highlighted in gray, with subsequent removal edits shown in red and addition edits shown in green. The original AI completion is highlighted in gray, subsequent removal edits are shown in red, and addition edits are shown in green. For each edit, we show the time between accepting the AI completion and making the edit () and whether the edit was AI-generated (). 
##  Introduction
Extensive adoption of AI programming assistants has made them a common tool for software developers (Anthropic, 2026a; Cursor, 2026; GitHub, 2026b). However, AI-generated code is imperfect, since in practice, generated code snippets may contain bugs or not match a specific coding style (Liang et al., 2024). In such cases, developers must modify the code, often by making an _instructed edit_ by writing a natural language prompt to an LLM (_e.g.,_ “Fix the bug in my code”). Or, developers may also make a _code edit_ by directly modifying the code themselves (_e.g.,_ changing a variable name). Giving LLMs the capability to handle manual code edits is essential, particularly in the era of coding agents. Studies suggest that only 44% agent-written code is retained by developers (Baumann et al., 2026) and 60% of code generated through prompting requires manual edits (Nam et al., 2025), suggesting that manual editing of AI-generated code is a prevalent task for developers working with agents.
Modern LLMs have been primarily trained to handle instructed edits by grounding code with natural language via data sources like web pages or Git pull requests (Li et al., 2023b; Roziere et al., 2023; Dubey et al., 2024; Cao et al., 2026), but they have not been trained directly on code edits. Limited availability of high-quality code edit data has made improving LLMs for code editing particularly challenging (Gupta et al., 2023; GitHub, 2025). As a workaround, existing approaches approximate edit data using publicly available Git sources like commits and pull requests (Wei et al., 2024; GitHub, 2025; Lu et al., 2025). Yet, finetuning LLMs on such data can yield worse performance than vanilla LLMs in practice because Git data is not a faithful approximation of the code editing process, lacking important context such as intermediate edits and temporal ordering of actions . To the best of our knowledge, no public dataset of real-world developer code edits currently exists.
To address this gap, we introduce Decode (Developer Edits of Code Dataset), a dataset of 53.6K real-world in-IDE code edits of AI-generated code in Python, TypeScript, and JavaScript, sourced from 1K+ developers. This data is derived from a Visual Studio Code (VS Code) extension that enables access to a variety of LLMs by providing AI code completions from a developer’s code file context. By extracting and tracking localized edits to actual accepted AI completions, Decode diverges from prior code editing datasets by serving as a source of _realistic_ , _diverse_ , and _high-quality_ edits of AI-generated code (examples in ).
We demonstrate the utility of Decode for both understanding how developers edit AI-generated code and providing LLMs with the capability to model developer edit behavior. First, we use the dataset to analyze how developers edit AI-generated code (), deriving insights on when, why, and how AI-generated code is edited. For example, we find that most edits occur within the first 15 minutes of accepting a completion, which results in completely removing an AI completion 31% of the time.
Second, we use Decode to understand to what extent LLMs can predict developer code edits for two tasks (): classifying whether AI completions will be modified, deleted, or unmodified by developers, as well as generating the final edited code. Finetuning on Decode enables open-source 3B and 7B models to significantly surpass frontier models on both generating code edits (+0.17 Levenshtein similarity) and classifying whether developers will edit AI completions (+0.17 F1).
Together, our results demonstrate the promise of developer-centric machine learning approaches for better alignment. This necessitates the creation of new modeling and evaluation paradigms that account for developer interaction for future AI programming assistants.
##  Related Work
Code Edits. Several works have investigated benchmarking LLM abilities of instructed edits from both laboratory (Cassano et al., 2024; Muennighoff et al., 2023) and real-world (Chi et al., 2025b) settings, and found that code LLM performance differs by model size and open- and closed-source models. Meanwhile, approaches for modeling code edits are fill-in-the-middle code LLMs (Fried et al., 2023; Roziere et al., 2023; Guo et al., 2024) or directly modeling sequences of code changes (Zhang et al., 2022a; Gupta et al., 2023; Li et al., 2023a; Wei et al., 2024; GitHub, 2026a). To evaluate LLMs’ abilities to perform code-based edits, several works have developed datasets of developer edits using GitHub commits (Wei et al., 2024; Lu et al., 2025), competitive programming problem submissions (Chae et al., 2024; Shypula et al., 2024), student programming problem submissions (Ross et al., 2025), and synthetic data (Zhang et al., 2025; Li et al., 2024). Most related to Decode is the Overwatch (Zhang et al., 2022b), a private dataset of code edits from 12 professional developers at a large technology company. Decode differs from this work by serving as a public resource on code editing data of AI-generated code from over 1K+ developers from diverse contexts.
Decode differs from existing code editing datasets and benchmarks by being the first dataset to obtain code edits from real-world software developer contexts at scale. In comparison, existing work either focuses on the task of instructed edits or obtains code edits by simulating data or using constrained software development settings. These data sources pose limitations, as our experiments indicate that models not trained on real-world code edits struggle on edit prediction tasks (), echoing prior work .
Learning from Human Interaction Data. The advancements enabled by reinforcement learning from human feedback (RLHF) highlight the importance of training LLMs on user data for alignment (Ouyang et al., 2022). Recent work argues for the utilization of real-world user interaction data rather than preference data (Silver and Sutton, 2025), which can improve model performance across tasks such as personalization, instruction-following, reasoning, and Q&A (Chen et al., 2025; Jin et al., 2025; Liu et al., 2025; Shaikh et al., 2026). Several real-world data collection efforts of user interactions have emerged, including WildChat (Zhao et al., 2024) and LMSYS-Chat-1M (Zheng et al., 2024), two datasets with one million user in-the-wild chat conversations with LLMs as well as NAPSack (Shaikh et al., 2026), a platform for collecting screenshots to train computer-use agents. Meanwhile, other works have performed analyses of real-world user interaction data that reveal insights on how users collaborate with LLMs for writing assistance (Mysore et al., 2025), use generative search (Suri et al., 2024), and interact with chat-based LLMs (Tamkin et al., 2024). Recent work from Baumann et al. (2026) analyzed 6,000+ developer-agent collaboration sessions, producing insights on the types of agent collaboration, the amount of agent-written code is retained, and the quality of agent-generated code.
Inspired by such works, we frame code generation as a developer-centric machine learning problem by focusing on how to collect and leverage real-world developer interaction data for LLMs. Through Decode, a dataset of real-world code edits, we show that incorporating developer interaction data improves LLMs and yields insights on developer usage of LLMs.  
 |  
|  |  
|  OCEDataFT   |   |  
|  CanItEdit  (Cassano et al.2024)  |   |  Programming  exercises  |  
|  EditEval   |   |  
|  Coffee   |   |  
|  Pencil Code   |  
 |  
Table 1: Decode is the only dataset that represents real-world coding problems written by actual developers. We compare Decode to other code editing datasets and report the edit setting, coding domain, data source, number of problems, and the programming languages (Python , JavaScript , TypeScript , CoffeeScript , HTML/CSS ) that are included in each dataset.
##  Decode: Developer Edits of Code Dataset
Example code edit extraction from Decode. The data extraction pipeline begins with identifying an original AI completion (gray code snippet). It tracks what changes made to the AI completion, including additions (green) and removals (red), even when the developer changes the surrounding code. 
###  3.1 Dataset Construction
Decode contains 53.6K real-world in-IDE developer code edits of AI-generated code in Python, TypeScript, and JavaScript. Decode is constructed using data collected from a VS Code extension used by thousands of developers to access a variety of frontier models for code completion. In addition to saving AI code completions, the extension saves the current working code file each time a developer pauses activity in the IDE for one second, yielding a rich source of code edit data. This distinguishes Decode from datasets derived from GitHub commits (e.g., (Wei et al., 2024; Lu et al., 2025)), which primarily capture relatively polished checkpoints and may omit the intermediate states through which developers iteratively arrive at an implementation Liang et al. (2023). We compare Decode to other publicly available code editing datasets and benchmarks in Table .
Using the trajectory in as a running example, we formulate the code editing problem for Decode as follows. Given an initial version of an accepted AI code completion within a code file (gray highlighted code in ), a developer will edit the code snippet at time , producing a new _snapshot_ of the code snippet (middle panel in ). Over time, this produces a _trajectory_ of edits made by developer on the original completion: =[,,,…,]Y^{d}=[y_{0}^{d},y_{1}^{d},y_{2}^{d},...,y_{t}^{d}] (left, middle, and right panels in ).
To extract code edits for Decode, we develop a pipeline that follows a four-step process. All data in Decode are collected from developers who have explicitly opted to sharing their code data via the VS Code extension. Before releasing the dataset, we remove personally identifiable information (PII) from the entire dataset. More specifically, we reuse the PII redaction pipeline used by Starcoder and the Stack (Li et al., 2023b; Lozhkov et al., 2024). We additionally apply OpenAI Privacy Filter , a general-purpose PII redaction model. The study was reviewed by our university’s Institutional Review Board (IRB).
We describe the pipeline below. For full details on the data construction pipeline, refer to :
#### Step 1: Obtaining Code Files.
The pipeline first begins with a pool of 4,110 developers who accepted AI code completions on the VS Code extension. We collect their code files and identify those likely containing edits of via a rough file header match based on line overlap between ’s code file and all other code files associated with . We remove redundant data by discarding snapshots within 10 seconds of the previous one.
#### Step 2: Code Edit Extraction.
After identifying candidate code files that may contain snapshots of , we extract the code snippet relevant to the edit from each file. A key challenge is isolating the lines of code directly relevant to an edit, since the data quality of the code edits is more important than the data quantity for model training . Our approach for accurately extracting code edits relies on git diff --histogram to identify differences in the source code (Nugroho et al., 2020). For each file containing an edit snapshot , we generate a “diff” between and to locate and map the lines of code that were edited, relative to the original snapshot . The git diff filtering step reduces the dataset from 6.5M lines of code overall to 772.2K lines of code directly relevant to code edits of AI completions. An example of the extraction is shown in .
#### Step 3: Data Cleaning & Validation
After obtaining the initial trajectories, we clean each trajectory by removing malformed data and validating each is relevant to using a CodeBERTScore (Zhou et al., 2023) threshold of 0.68, which was selected based on preliminary analysis. This cleaning step reduces the dataset from 78K before-after pairs from 4K developers to 56K before-after pairs from 1K developers. Given the importance of data quality for the code editing task , we performed a validation of the pipeline by hand-annotating a sample of 125 before-and-after pairs that were the first and last snapshots from a sample of edit trajectories.
#### Step 4: PII Redaction.
After obtaining the dataset, we take careful steps to reduce the likelihood that Decode contains any personally identifiable information (PII). We reuse the PII redaction pipeline used by Starcoder and the Stack (Li et al., 2023b; Lozhkov et al., 2024), which relies on an LLM trained on PII contained in code files. We additionally apply OpenAI Privacy Filter , a general-purpose PII redaction model.
###  3.2 Dataset Statistics
Decode contains trajectories from developers corresponding to 53,614 before-after code pairs from 20 different LLMs. We discuss the dataset in more detail:
#### Development Context.
The before-after code pairs are written in Python (40,390), JavaScript (), and TypeScript (). The edit trajectories also span a diverse set of software development task contexts, such as data analysis and visualization (), web development (), machine learning (), web scraping (), user interfaces (), file processing (), backend development (), game development (), and testing ().
#### Edit Trajectories.
Decode’s edit trajectories last for a median duration of 49.7 minutes. The minimum edit duration is one second, while the maximum duration is 283.5 days. In addition, the number of snapshots per trajectory ranges from one to 424 snapshots, with a median of 4 snapshots. Finally, each trajectory contains a substantial amount of code edits between the initial AI completion and final state (median of 329 Levenshtein edits).
#### AI Completions.
Most AI completions were substantial in size, with a median length of 97 characters or 9 lines of code. In addition, the code context surrounding the AI completion had a median of 2,949 characters. The AI completions were invoked by developers via both natural language comments () and code ().
##  How Do Developers Edit AI-Generated Code?
###  4.1 Metrics
We use Decode to study how developers edit AI-generated code with the following metrics. For more details, see .
#### Amount of AI-Generated Code Remaining.
This metric represents the proportion of an AI completion that is remaining at the end of an edit trajectory. We use the number of Levenshtein removal and replacement operations to identify the original code that was removed or replaced by the developer.
#### Amount of Developer-Added Code.
This metric represents the proportion of the code at the end of the edit sequence that was newly added by the developer and was not a part of the original AI completion. We use the Levenshtein addition operations to identify which code was newly added by the developer.
#### Total Amount of Code Edits.
This metric represents the total amount of edits made by all developers at a specific time step. It is computed by aggregating Levenshtein distances made within the same time period.
###  4.2 Observations of Developer Edit Behavior
#### Developers edit AI-generated code for a variety of reasons.
We identify four types of code edits by qualitatively analyzing a sample of edit trajectories and using LLM-as-a-judge to classify edit snapshots (see ). We identify four types of code edits:
  * •
Customizing code: Code edits to fine-tune the AI completion to better align with the developer’s intent without significantly changing the code’s functionality, which accounts for 10% of edit snapshots. Examples include changing parameter, variable, and literal values (_e.g.,_ changing the text passed to print()) and renaming variables.
  * •
Improving code quality: Code edits to improve the quality of the AI-generated code, such as fixing syntax errors, improving code readability, or adding comments. This type of edit constitutes 14% of edit snapshots.
  * •
Changing code functionality: Code edits to change the AI-generated code’s behavior, such as adding new methods, changing logic, or modifying API calls. This type of edit accounts for 56% of edit snapshots.
  * •
Removing: Code edits with the intent of removing the AI completion from the codebase and starting from the original state (_e.g.,_ commenting out the completion), representing 9% of edit snapshots.


Developer editing behavior after accepting AI-generated code. _Left:_ The number of changes made to AI completions drops after the first 15 minutes (vertical gray dotted line). _Middle:_ Developers often completely remove the completion or leave it fully intact. _Right:_ Developers rarely add new code to AI-generated code. 
#### AI completions are often abandoned within 15 minutes when completions are not aligned to the developer’s intent.
A majority (72%) of code edits occur within one day of accepting the suggestion. In fact, 50% of the code edits in Decode occurr within the first 50 minutes after acceptance. Most edits occur very shortly after acceptance, as we observe a steep drop in the total amount of edits 15 minutes after acceptance (see ).
In this time frame, most code editing includes modifying functionality (76% of trajectories), followed by improving code quality (40%) and customizing code (25%). Interestingly, a large portion of AI completions are abandoned: 31% of trajectories contain edits with the intent of removing the completion. Examining the first two steps of edit trajectories (see ) provides insight into why: developers are more likely to remove an AI completion after first attempting to customize the code (23%) compared to improving code quality (14%) and changing functionality (12%). This suggests that AI completions that subtly do not align with a developer’s intent or programming context are difficult for developers to adapt. 23% of edit trajectories immediately remove the AI completion, which is often followed by changing the code functionality (40%), indicating that developers often write their own implementations as a replacement.
#### Developers rely heavily on AI-generated code.
Developers make significant use of AI-generated code, since a median of 63% of the original AI completion remains. Yet, the amount of code remaining is bi-modally distributed (see ), indicating that for a majority of the time, AI-generated code is either accepted with few modifications or almost completely removed. Developers also tend to add very little new code to AI-generated completions, as 20% of the final code was added by a developer rather than AI (see ). Further, 36% of the final code contained small amounts (< 5%) of developer-added code (see ), indicating heavy reliance on AI-generated code.
Editing behavior after accepting an AI completion. We show the first (black arrow) and second (gray arrow) edits after accepting an AI code completion. For presentation clarity, we present second edits that are frequent ( 10%). 
#### Developers follow a common process to edit AI-generated code.
Different types of edits occur at varying times after acceptance with statistical significance based on a Kruskal-Wallis test (H=394.5, p<0.001) (McKight and Najab, 2010). Edits related to removing the completion occur first (\mu=23.6 minutes). This is then followed by edits related to code quality (\mu=28.3 minutes), customizing the code (\mu=49.3 minutes), and modifying functionality (\mu=59.2 minutes). This indicates that after accepting an AI-generated completion, developers first decide whether they want to keep the code. After deciding to do so, they then follow the process of fixing any errors in the code, adapting the code to their needs, and finally modifying the code’s functionality to add new features.
#### Editing behavior is generally consistent across models.
We do not observe substantial variance in editing behavior between models. Using Kruskal-Wallis tests (McKight and Najab, 2010) with a Benjamini-Hochberg correction, we observe statistical significant differences between all models for the amount of AI-generated code remaining (H=31.5, p=0.04) and amount of developer-written code added (H=57.3, p<0.001). However, the effect size is small based on the eta-squared value (\eta=0.002 and \eta=0.007 respectively) (Fiel Peres, 2026). While the types of edits also differ with statistical significance based on a Chi-squiared test (\chi^{2}=320.7, p<0.001), the effect size is also small by Cramér’s V (\phi=0.05) .
##  Improving Code LLMs with Decode
###  5.1 Experimental Setup
#### Tasks.
We now demonstrate the utility of Decode to improve LLMs’ abilities to learn developer edit behavior on two tasks related to predicting an AI completion’s final state:
  * •
Classification— _How much code remains after editing?_ Predict whether the AI completion will be deleted, unmodified, or modified, based the amount of AI-generated code remaining (see ). Because the amount of code remaining is bi-modal (), we use the distribution peaks to stratify edit trajectories into three categories: deleted ([0,0.1]), unmodified ([0.9,1]), and modified ((0.1,0.9)).
  * •
Generation— _What code remains after editing?_ Given an AI completion , predict , the final code state after developer edits.


#### Baselines.
To evaluate LLMs’ existing abilities to reason about real-world code edits, we experiment with few-shot in-context learning. We prompt the following models: Qwen2.5-Coder-3B (Hui et al., 2024), Qwen2.5-Coder-7B, Llama3.2-3B (Dubey et al., 2024), Llama-3.3-70B (Dubey et al., 2024), Qwen3-Coder-Next (Cao et al., 2026), GPT-5.2 (Singh et al., 2025), Claude-Sonnet-4.6 (Anthropic, 2026b), DeepSeek-v3.2 (DeepSeek-AI, 2024), and Devstral-2512 (Mistral-AI, 2025).
We prompt each model with two to three before-after pairs from Decode; supply the code prefix, AI completion, and code suffix; and instruct the LLM to generate the completion’s final state after editing. To understand whether LLMs can reason about code edits, we experiment with providing models with the first k\in[0,4] edit snapshots in the trajectory.
#### Fine-Tuning.
To study LLMs’ abilities to learn from code edits, we fine-tune three models on Decode: Qwen2.5-Coder-3B (Hui et al., 2024), Qwen2.5-Coder-7B, and Llama3.2-3B (Dubey et al., 2024). The models are trained using LoRA (Hu et al., 2022). To assess how training additional edit data affects performance, we train model variants using the first k\in[0,4] edits. For the classification task, we rebalance the dataset by upsampling for equal representation for each label during training. Full experimental details are in .  
| _Classification_  |  
| --- |  
 |  
 |  
|   |  
 |  
 |  
|   |  
|  Llama3.3-70B-Instruct  |  
|   |  
 |  
|   |  
 |  
 |  
 |  
Table 2: LLMs fine-tuned on Decode predict code edits better. We report classification (F1, accuracy) and generation (BLEU, ROUGE-L, Levenshtein similarity, line overlap) results, comparing few-shot LLMs with models fine-tuned on Decode (+Decode). 
#### Decoding Strategy.
Code generation benefits from sampling (Li et al., 2022; Shypula et al., 2024); thus, we follow Shypula et al. (2024) and use beam search with a beam width of 3 and temperature of 0.7. We set the maximum new tokens for all models to be the 95th percentile of the training set’s final edit lengths.
#### Evaluation.
We create train, development, and test sets corresponding to 80%, 10%, and 10% of the trajectories respectively (randomly split). For the classification task, we report the F1 and accuracy on the balanced dataset. For the generation task, we report standard generation metrics (_i.e.,_ BLEU score and ROUGE-L) on the test set. To measure code editing performance, we use normalized Levenshtein similarity and the percent of line overlap following prior work in code editing (Wei et al., 2024; Lu et al., 2025). Metrics related to the functionality of the code For additional results, refer to .
###  5.2 Results
#### Predicting developer code edits is a challenging task for LLMs, even for frontier models.
Small LLMs struggle to predict code edits in a few-shot setting, with a maximum F1 score of 0.23 from Llama3.2-3B and a maximum Levenshtein similarity of 0.30 from Qwen2.5-Coder-7B (see ). Frontier models also struggle to reason about developer edits without fine-tuning. The best model, Claude-Sonnet-4.6, has an F1 score of 0.37 for the classification task, marginally improving over a random classifier on the balanced dataset (0.33). For the generation task, the best model is Devstral-2512, with a Levenshtein similarity of 0.41.
#### Fine-tuning on developer edit trajectories improves LLMs’ ability to predict code edits compared to the base models.
For all fine-tuned models, training on Decode achieved average F1 and Levenshtein similarity scores of 0.44 and 0.42 respectively, improving over base models by 0.23 in F1 and 0.18 in Levenshtein similarity. Even 3B parameter models performed significantly better than frontier models for both tasks (see ), indicating that exposure to real-world edits enables even small LLMs to model developer intents better.
LLMs’ ability to predict code edits increases the more edits they are exposed to. We display the results of varying the number of additional edits provided to a model during fine-tuning for the classification (left) and generation (right) tasks. 
#### LLMs’ ability to predict code edits improves as more code edits are provided during training.
As LLMs are exposed to more code edits, performance for all models increase (see ), as training on four edits achieves average F1 and Levenshtein similarity scores of 0.50 and 0.52. Fine-tuned models’ F1 scores increase by an average of 0.06, with a maximum of 0.08 for Qwen2.5-Coder-3B. Levenshtein similarity increases by an average of 0.10, with a maximum increase of 0.11 for Qwen2.5-Coder-3B. This suggests that providing LLMs with code edits can improve their ability to predict developer intent.
#### Fine-tuning on Decode does not degrade code generation ability.
The best fine-tuned models have similar or better performance on HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021) compared to their base versions (see ). Qwen2.5-Coder-3B fine-tuned on Decode improves pass@1 by 0.02 and 0.01 on HumanEval and MBPP respectively, while other models such as Llama3.2-3B and Qwen2.5-Coder-7B do not improve on the benchmarks.  
 |  
|  |  
|   |  
 |  
|   |  
 |  
 |  
 |  
Table 3: LLMs fine-tuned on Decode do not degrade in code generation ability. We show the pass@1 of LLMs fine-tuned on Decode on code generation benchmarks, HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021). 
This indicates that training on code edits does not degrade, and can sometimes improve, code generation performance.
##  Discussion & Conclusion
We introduce Decode, a dataset of 53.6K edits of AI-generated code. By analyzing it and evaluating LLMs’ ability to model code edits, we show how it reveals developer editing patterns and improves LLMs’ ability to predict edits. We conclude with key takeaways.
#### Generate code that is not only correct, but aligned with developer intent.
Developers edit AI-generated code quickly, add relatively little new code themselves, and abandon completions if because the completion cannot be easily adapted to their intended use. This suggests a key barrier for AI programming assistants is determining how well a completion aligns with developer intent and context, corroborating prior work (Liang et al., 2024). Yet, standard benchmarks for code generation emphasize code correctness over developer alignment, such as pass@k on HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), SWE-Bench (Jimenez et al., 2023), and BigCodeBench (Zhuo et al., 2025).
#### Detect generations that are low in editability.
AI-generated code is either kept fully intact or completely discarded, suggesting that an important consideration is AI-generated code’s editability (_i.e.,_ how easily the code can be adapted, even when it is not immediately usable). Yet, approaches to quantify code editability are limited, with the closest approximations being metrics like CodeBERTScore (Zhou et al., 2023) and CodeBLEU (Ren et al., 2020) for code similarity. Future work could investigate modeling approaches to detect whether a suggestion is likely to be retained or discarded to regenerate low-quality completions.
#### Train on recent developer edit history.
Fine-tuning on early developer edits improves LLMs’ ability to predict future code edits. Moreover, different types of code edits exhibit temporal patterns, as early-stage edits involve removals or customizing code, while later edits involve functionality changes. Thus, LLMs should capture the sequential and temporal nature of developer edits , yet this is often overlooked in prior work.
#### Towards developer-centric machine learning.
Our results highlight the promise of developer-centric approaches, as training on developer edits improves LLMs. Yet, current training and evaluation paradigms do not capture alignment with developer needs, necessitating a new suite of methods for incorporating developer interaction. Avenues for future work include personalization, modeling techniques on developer edits (_e.g.,_ reinforcement learning from developer interactions), and designing developer-centric evaluations and metrics that reflect real-world workflows (_e.g.,_ code retention, AI completion abandonment rates).
#### Limitations
Decode captures edits from a fixed set of LLMs within a specific time window and only includes edits to accepted AI-generated code. This excludes rejected completions, human-written code, and code obtained from outside the VS Code extension. In addition, the task of generating code edits is subjective since developers vary in how they write code, and there are multiple valid ways to edit a completion. Thus, Decode may not capture the full diversity of code edits, which can affect performance on the edit generation task and limit the ability of fine-tuned LLMs to generalize across different editing styles.
## Acknowledgments
We thank Brad A. Myers, Chris Donahue, Sean Welleck, Daniel Fried, and Nikitha Rao for their advice on the project. We also thank Peter Muller, Chenyang Yang, and Manisha Mukherjee for their feedback on the manuscript. Last but not least, we give a special thanks to Mei , an outstanding canine ML researcher, for providing support and motivation throughout the study. Jenny T. Liang is supported by the National Science Foundation under grants DGE1745016 and DGE2140739.
## References
  * Anthropic [2026a] Anthropic.  Claude code by anthropic | ai coding agent, terminal, ide. 
  * Anthropic [2026b] Anthropic.  Claude sonnet 4.6 system card.  _Anthropic Technical Report_ , 2026b.  URL 
  * Austin et al. [2021] J. Austin, A. Odena, M. Nye, M. Bosma, H. Michalewski, D. Dohan, E. Jiang, C. Cai, M. Terry, Q. Le, and C. Sutton.  Program synthesis with large language models.  _arXiv preprint arXiv:2108.07732_ , 2021. 
  * Baumann et al. [2026] J. Baumann, V. Padmakumar, X. Li, J. Yang, D. Yang, and S. Koyejo.  Swe-chat: Coding agent interactions from real users in the wild.  _arXiv preprint arXiv:2604.20779_ , 2026. 
  * Cao et al. [2026] R. Cao, M. Chen, J. Chen, Z. Cui, Y. Feng, B. Hui, Y. Jing, K. Li, M. Li, J. Lin, Z. Ma, K. Shum, X. Wang, J. Wei, J. Yang, J. Zhang, L. Zhang, Z. Zhang, W. Zhao, and F. Zhou.  Qwen3-coder-next technical report.  _arXiv preprint arXiv:2603.00729_ , 2026. 
  * Cassano et al. [2024] F. Cassano, L. Li, A. Sethi, N. Shinn, A. Brennan-Jones, J. Ginesin, E. Berman, G. Chakhnashvili, A. Lozhkov, C. J. Anderson, and A. Guha.  Can it edit? evaluating the ability of large language models to follow code editing instructions.  In _First Conference on Language Modeling (COLM)_ , 2024.  URL 
  * Chae et al. [2024] H. Chae, T. Kwon, S. Moon, Y. Song, D. Kang, K. T.-i. Ong, B.-w. Kwak, S. Bae, S.-w. Hwang, and J. Yeo.  Coffee-gym: An environment for evaluating and improving natural language feedback on erroneous code.  In _Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 22503–22524, 2024. 
  * Chen et al. [2021] M. Chen, J. Tworek, H. Jun, Q. Yuan, H. P. d. O. Pinto, J. Kaplan, H. Edwards, Y. Burda, N. Joseph, G. Brockman, et al.  Evaluating large language models trained on code.  _arXiv preprint arXiv:2107.03374_ , 2021. 
  * Chen et al. [2025] Z. Chen, M. O. Gul, Y. Chen, G. Geng, A. Wu, and Y. Artzi.  Retrospective learning from interactions.  In _Annual Meeting of the Association for Computational Linguistics (ACL)_ , pages 24580–24606, 2025. 
  * Chi et al. [2025a] W. Chi, V. Chen, A. N. Angelopoulos, W.-L. Chiang, A. Mittal, N. Jain, T. Zhang, I. Stoica, C. Donahue, and A. Talwalkar.  Copilot arena: A platform for code LLM evaluation in the wild.  In _Forty-second International Conference on Machine Learning_ , 2025a.  URL 
  * Chi et al. [2025b] W. Chi, V. Chen, R. Shar, A. Mittal, J. T. Liang, W.-L. Chiang, A. N. Angelopoulos, I. Stoica, G. Neubig, A. Talwakar, and C. Donahue.  Editbench: Evaluating LLM abilities to perform real-world instructed code edits.  In _Submitted to The Fourteenth International Conference on Learning Representations_ , 2025b.  URL  under review. 
  * Cohen [2013] J. Cohen.  _Statistical power analysis for the behavioral sciences_.  routledge, 2013. 
  * Cursor [2026] Cursor.  Cursor: The best way to code with ai. 
  * DeepSeek-AI [2024] DeepSeek-AI.  Deepseek-v3 technical report.  _arXiv preprint arXiv:2412.19437_ , 2024. 
  * Dubey et al. [2024] A. Dubey, A. Jauhri, A. Pandey, A. Kadian, A. Al-Dahle, et al.  The llama 3 herd of models.  _arXiv preprint arXiv:2407.21783_ , 2024. 
  * Fiel Peres [2026] F. Fiel Peres.  Effect sizes for nonparametric tests.  _Biochemia medica_ , 36(1):5–16, 2026. 
  * Fried et al. [2023] D. Fried, A. Aghajanyan, J. Lin, S. Wang, E. Wallace, F. Shi, R. Zhong, S. Yih, L. Zettlemoyer, and M. Lewis.  Incoder: A generative model for code infilling and synthesis.  In _International Conference on Learning Representations (ICLR)_ , 2023.  URL 
  * GitHub [2025] GitHub.  Evolving github copilot’s next edit suggestions through custom model training. 
  * GitHub [2026a] GitHub.  Copilot next edit suggestions. 
  * GitHub [2026b] GitHub.  Github copilot - your ai pair programmer. 
  * Graves [2012] A. Graves.  Sequence transduction with recurrent neural networks.  In _International Conference on Machine learning (ICML)_ , page 9, 2012. 
  * Guo et al. [2024] D. Guo, Q. Zhu, D. Yang, Z. Xie, K. Dong, W. Zhang, G. Chen, X. Bi, Y. Wu, Y. Li, et al.  Deepseek-coder: When the large language model meets programming–the rise of code intelligence.  _arXiv preprint arXiv:2401.14196_ , 2024. 
  * Gupta et al. [2023] P. Gupta, A. Khare, Y. Bajpai, S. Chakraborty, S. Gulwani, A. Kanade, A. Radhakrishna, G. Soares, and A. Tiwari.  Grace: Language models meet code edits.  In _ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE)_ , pages 1483–1495, 2023. 
  * Hu et al. [2022] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al.  Lora: Low-rank adaptation of large language models.  _Intenational Conference on Learning Representations (ICLR)_ , 1(2):3, 2022. 
  * Hui et al. [2024] B. Hui, J. Yang, Z. Cui, J. Yang, D. Liu, L. Zhang, T. Liu, J. Zhang, B. Yu, K. Lu, et al.  Qwen2.5-coder technical report.  _arXiv preprint arXiv:2409.12186_ , 2024. 
  * Jimenez et al. [2023] C. E. Jimenez, J. Yang, A. Wettig, S. Yao, K. Pei, O. Press, and K. Narasimhan.  Swe-bench: Can language models resolve real-world github issues?  In _International Conference on Learning Representations (ICLR)_ , 2023. 
  * Jin et al. [2025] C. Jin, J. Xu, B. Liu, L. Tao, O. Golovneva, T. Shu, W. Zhao, X. Li, and J. Weston.  The era of real-world human interaction: RL from user conversations.  _arXiv preprint arXiv:2509.25137_ , 2025. 
  * Kingma and Ba [2015] D. P. Kingma and J. Ba.  Adam: A method for stochastic optimization.  In _International Conference on Learning Representations (ICLR)_ , 2015. 
  * Li et al. [2023a] J. Li, G. Li, Z. Li, Z. Jin, X. Hu, K. Zhang, and Z. Fu.  Codeeditor: Learning to edit source code with pre-trained models.  _ACM Transactions on Software Engineering and Methodology (TOSEM)_ , 32(6):1–22, 2023a. 
  * Li et al. [2024] K. Li, Q. Hu, J. X. Zhao, H. Chen, Y. Xie, T. Liu, M. Shieh, and J. He.  Instructcoder: Instruction tuning large language models for code editing.  In _Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 4: Student Research Workshop)_ , pages 473–493, 2024.  URL 
  * Li et al. [2023b] R. Li, L. B. allal, Y. Zi, N. Muennighoff, D. Kocetkov, C. Mou, M. Marone, C. Akiki, J. LI, J. Chim, Q. Liu, E. Zheltonozhskii, T. Y. Zhuo, T. Wang, O. Dehaene, J. Lamy-Poirier, J. Monteiro, N. Gontier, M.-H. Yee, L. K. Umapathi, J. Zhu, B. Lipkin, M. Oblokulov, Z. Wang, R. Murthy, J. T. Stillerman, S. S. Patel, D. Abulkhanov, M. Zocca, M. Dey, Z. Zhang, U. Bhattacharyya, W. Yu, S. Luccioni, P. Villegas, F. Zhdanov, T. Lee, N. Timor, J. Ding, C. S. Schlesinger, H. Schoelkopf, J. Ebert, T. Dao, M. Mishra, A. Gu, C. J. Anderson, B. Dolan-Gavitt, D. Contractor, S. Reddy, D. Fried, D. Bahdanau, Y. Jernite, C. M. Ferrandis, S. Hughes, T. Wolf, A. Guha, L. V. Werra, and H. de Vries.  Starcoder: May the source be with you!  _Transactions on Machine Learning Research (TMLR)_ , 2023b.  ISSN 2835-8856.  URL 
  * Li et al. [2022] Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al.  Competition-level code generation with alphacode.  _Science_ , 378(6624):1092–1097, 2022. 
  * Liang et al. [2023] J. T. Liang, M. Arab, M. Ko, A. J. Ko, and T. D. LaToza.  A qualitative study on the implementation design decisions of developers.  In _IEEE/ACM International Conference on Software Engineering (ICSE)_ , pages 435–447. IEEE, 2023. 
  * Liang et al. [2024] J. T. Liang, C. Yang, and B. A. Myers.  A large-scale survey on the usability of AI programming assistants: Successes and challenges.  In _IEEE/ACM International Conference on Software Engineering (ICSE)_ , pages 1–13, 2024. 
  * Liu et al. [2025] Y. Liu, M. J. Zhang, and E. Choi.  User feedback in human-llm dialogues: A lens to understand users but noisy as a learning signal.  In _Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 2666–2681, 2025. 
  * Lozhkov et al. [2024] A. Lozhkov, R. Li, L. B. Allal, F. Cassano, J. Lamy-Poirier, N. Tazi, A. Tang, D. Pykhtar, J. Liu, Y. Wei, et al.  Starcoder 2 and the stack v2: The next generation.  _arXiv preprint arXiv:2402.19173_ , 2024. 
  * Lu et al. [2025] R. Lu, Y. Huo, M. Zhang, Y. Li, and M. R. Lyu.  Next edit prediction: Learning to predict code edits from context and interaction history.  _arXiv preprint arXiv:2508.10074_ , 2025. 
  * McKight and Najab [2010] P. E. McKight and J. Najab.  Kruskal-wallis test.  _The Corsini Encyclopedia of Psychology_ , pages 1–1, 2010. 
  * Mistral-AI [2025] Mistral-AI.  Devstral 2: Frontier models for agentic software engineering.  _Mistral AI Technical Report_ , 2025.  URL 
  * Muennighoff et al. [2023] N. Muennighoff, Q. Liu, A. Zebaze, Q. Zheng, B. Hui, T. Y. Zhuo, S. Singh, X. Tang, L. V. Werra, and S. Longpre.  Octopack: Instruction tuning code large language models.  In _NeurIPS Workshop on Instruction Tuning and Instruction Following_ , 2023.  URL 
  * Mysore et al. [2025] S. Mysore, D. Das, H. Cao, and B. Sarrafzadeh.  Prototypical human-ai collaboration behaviors from llm-assisted writing in the wild.  In _Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 16830–16857, 2025. 
  * Nam et al. [2025] D. Nam, A. Omran, A. Murillo, S. Thakur, A. Araujo, M. Blistein, A. Frömmgen, V. Hellendoorn, and S. Chandra.  Prompting LLMs for code editing: Struggles and remedies.  _arXiv preprint arXiv:2504.20196_ , 2025. 
  * Nugroho et al. [2020] Y. S. Nugroho, H. Hata, and K. Matsumoto.  How different are different diff algorithms in git? use–histogram for code changes.  _Empirical Software Engineering_ , 25(1):790–823, 2020. 
  * OpenAI [2026] OpenAI.  Introducing openai privacy filter. 
  * Ouyang et al. [2022] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al.  Training language models to follow instructions with human feedback.  _Advances in Neural Information Processing Systems (NeurIPS)_ , 35:27730–27744, 2022.  URL 
  * Ren et al. [2020] S. Ren, D. Guo, S. Lu, L. Zhou, S. Liu, D. Tang, N. Sundaresan, M. Zhou, A. Blanco, and S. Ma.  Codebleu: a method for automatic evaluation of code synthesis.  _arXiv preprint arXiv:2009.10297_ , 2020. 
  * Ross et al. [2025] A. Ross, M. Srivastava, J. Blanchard, and J. Andreas.  Modeling student learning with 3.8 million program traces.  _arXiv preprint arXiv:2510.05056_ , 2025. 
  * Roziere et al. [2023] B. Roziere, J. Gehring, F. Gloeckle, S. Sootla, I. Gat, X. E. Tan, Y. Adi, J. Liu, R. Sauvestre, T. Remez, et al.  Code llama: Open foundation models for code.  _arXiv preprint arXiv:2308.12950_ , 2023. 
  * Shaikh et al. [2026] O. Shaikh, V. Teutschbein, K. Gandhi, Y. Chi, N. Haber, T. Robinson, N. Ram, B. Reeves, S. Yang, M. S. Bernstein, et al.  Learning next action preditors from human-computer interaction.  _arXiv preprint arXiv:2603.05923_ , 2026. 
  * Shypula et al. [2024] A. G. Shypula, A. Madaan, Y. Zeng, U. Alon, J. R. Gardner, Y. Yang, M. Hashemi, G. Neubig, P. Ranganathan, O. Bastani, and A. Yazdanbakhsh.  Learning performance-improving code edits.  In _International Conference on Learning Representations (ICLR)_ , 2024.  URL 
  * Silver and Sutton [2025] D. Silver and R. S. Sutton.  Welcome to the era of experience.  _Google AI_ , 1:11, 2025.  URL 
  * Singh et al. [2025] A. Singh, A. Fry, A. Perelman, A. Tart, A. Ganesh, A. El-Kishky, A. McLaughlin, A. Low, A. Ostrow, A. Ananthram, et al.  Openai gpt-5 system card.  _arXiv preprint arXiv:2601.03267_ , 2025. 
  * Suri et al. [2024] S. Suri, S. Counts, L. Wang, C. Chen, M. Wan, T. Safavi, J. Neville, C. Shah, R. W. White, R. Andersen, et al.  The use of generative search engines for knowledge work and complex tasks.  _arXiv preprint arXiv:2404.04268_ , 2024. 
  * Tamkin et al. [2024] A. Tamkin, M. McCain, K. Handa, E. Durmus, L. Lovitt, A. Rathi, S. Huang, A. Mountfield, J. Hong, S. Ritchie, et al.  Clio: Privacy-preserving insights into real-world ai use.  _arXiv preprint arXiv:2412.13678_ , 2024. 
  * Wei et al. [2024] J. Wei, G. Durrett, and I. Dillig.  Coeditor: Leveraging repo-level diffs for code auto-editing.  In _International Conference on Learning Representations (ICLR)_ , 2024.  URL 
  * Zhang et al. [2022a] J. Zhang, S. Panthaplackel, P. Nie, J. J. Li, and M. Gligoric.  Coditt5: Pretraining for source code and natural language editing.  In _IEEE/ACM International Conference on Automated Software Engineering (ASE)_ , pages 1–12, 2022a. 
  * Zhang et al. [2022b] Y. Zhang, Y. Bajpai, P. Gupta, A. Ketkar, M. Allamanis, T. Barik, S. Gulwani, A. Radhakrishna, M. Raza, G. Soares, et al.  Overwatch: Learning patterns in code edit sequences.  _Proceedings of the ACM on Programming Languages_ , 6(OOPSLA2):395–423, 2022b. 
  * Zhang et al. [2025] Z. Zhang, M. Liu, Z. Chen, L. Liang, Y. Chen, G. Ou, Y. Wang, D. Li, X. Peng, and Z. Zheng.  Generating high-quality datasets for code editing via open-source language models.  _arXiv preprint arXiv:2509.25203_ , 2025. 
  * Zhao et al. [2024] W. Zhao, X. Ren, J. Hessel, C. Cardie, Y. Choi, and Y. Deng.  Wildchat: 1M chatgpt interaction logs in the wild.  _International Conference on Learning Representations (ICLR)_ , 2024. 
  * Zheng et al. [2024] L. Zheng, W.-L. Chiang, Y. Sheng, T. Li, S. Zhuang, Z. Wu, Y. Zhuang, Z. Li, Z. Lin, E. P. Xing, et al.  LMSYS-chat-1m: A large-scale real-world LLM conversation dataset.  _International Conference on Learning Representations (ICLR)_ , 2024. 
  * Zhou et al. [2023] S. Zhou, U. Alon, S. Agarwal, and G. Neubig.  CodeBERTScore: Evaluating code generation with pretrained models of code.  In _Conference on Empirical Methods in Natural Language Processing (EMNLP)_ , pages 13921–13937, 2023. 
  * Zhuo et al. [2025] T. Y. Zhuo, M. C. Vu, J. Chim, H. Hu, W. Yu, R. Widyasari, I. N. B. Yusuf, H. Zhan, J. He, I. Paul, et al.  Bigcodebench: Benchmarking code generation with diverse function calls and complex instructions.  In _International Conference on Learning Representations (ICLR)_ , 2025. 


## Appendix
##  Appendix A Decode: Developer Edits of Code Dataset
###  A.1 Dataset Construction
Below, we enumerate additional details of the data construction process of Decode.
Languages selected. The VS Code extension consisted of completions in several languages, but we selected all Python, Javascript, and Typescript completions as they were the three most popular languages, comprised well over half of the available completions, and were supported well by CodeBERT with only slight pre-processing.
Models included. The VS Code extension, and subsequently Decode, includes code completions from the following models: gpt-4o-mini-2024-07-18, llama-3.1-70b-instruct, llama-3.1-405b-instruct, codestral-2405, deepseek-coder-fim, gemini-1.5-flash-002, gemini-1.5-pro-002, claude-3-5-sonnet-20240620, gpt-4o-2024-08-06, gpt-4o-2024-11-20, qwen-2.5-coder-32b-instruct, claude-3-5-sonnet-20241022, gemini-2.0-flash-exp, codestral-2501, deepseek-coder-v3-fim, anonymous-titan, gemini-2.0-flash-001, gemini-2.0-pro-exp-02-05, anonymous-q, and claude-3-7-sonnet-20250219.
Matching file headers. In order to identify code files that may contain edited code snippets for an initial completion, we identify the initial ’substantive’ lines in each file of the developer, and compute the similarity between the originally modified file and other files. After validation by hand-annotation, we set a similarity cutoff for 0.5 for Python files, and 0.4 for Javascript and Typescript files.
Removing edits at the ends. Identifying the final state of an edit that was made on the very first or very last line of a file is a challenging task as it is difficult to determine programatically where the edit ends in its final state, and other unrelated edits begin. To preserve the quality of Decode, we chose to remove the of edits that fell into this category.
CodeBERT threshold. We perform a final filtering round of edits by validating that each edit snippet identified is relevant to the original outcome by using a CodeBERT score threshold of 0.68. We also allow for a score of 0 to capture entire removals of edits. Preliminary experiments showed that this threshold was achieved by 67.68% of all initially identified extracted code snippets. We then hand-annotated and validated cases on the edge to see if our threshold worked as expected. We also noted that with the cutoff applied, the number of edits extracted reduced, but the number of trajectories remainder similar, indicating an implicit cutoff in trajectories for when snapshots stray too far away from the initial outcome to extract a meaningful edit.
###  A.2 Dataset Quality Validation
Given the importance of data quality for the code editing task , we performed a validation of the dataset construction pipeline. We gathered a sample of 125 before-after edit pairs that were the first and last snapshots from a sample of edit trajectories. These trajectories were sampled to represent important cases: AI completions with large code prefixes or suffixes, in-line completions, multi-line completions, and long trajectories. We also randomly sampled before-after edit pairs. These samples were divided evenly across the three languages in the dataset. We chose to annotate the first and last snapshots from each trajectory to best capture performance drops with drifts over a trajectory.
Each trajectory’s code edits was manually annotated by an author and compared to the pipeline’s. We found that the approach detected the presence of 94.7% of code edits, with an 88.1% overlap with code-based edits manually extracted by humans.
##  Appendix B How Do Developers Edit AI-Generated Code?
###  B.1 Metrics
Amount of AI-Generated Code Remaining. This metric represents the proportion of an AI completion that is remaining at the end of an edit trajectory. We use the number of Levenshtein removal and replacement operations to identify the original code that was removed or replaced by the developer:  
| code_remaining​=1−removal_ops​+replacement_ops​\displaystyle\texttt{code\\_remaining}(Y^{d})=1-\frac{\texttt{removal\\_ops}(y_{0}^{d},y_{t}^{d})+\texttt{replacement\\_ops}(y_{0}^{d},y_{t}^{d})}{\texttt{len}(y_{0}^{d})}  |  
| --- |  
Amount of Developer-Added Code. This metric represents the proportion of the code at the end of the edit sequence that was newly added by the developer and was not a part of the original AI completion. We use the Levenshtein addition operations to identify which code was newly added by the developer:  
| code_added​=addition_ops​\texttt{code\\_added}(Y^{d})=\frac{\texttt{addition\\_ops}(y_{0}^{d},y_{t}^{d})}{\texttt{len}(y_{t}^{d})}  |  
| --- |  
Total Amount of Code Edits. This metric represents the total amount of edits made by all developers at a specific time step. It is computed by aggregating Levenshtein distances made within the same time period:  
| edit_volume​=levenshtein​\texttt{edit\\_volume}(t)=\sum_{d}\texttt{levenshtein}(y_{t-1}^{d},y_{t}^{d})  |  
| --- |  
Code Edit Position. This metric represents where within a code snippet an edit occurs. We use the index of a Levenshtein operation to identify the edit’s location:  
| edit_position​=op_index​\texttt{edit\\_position}(y_{t}^{d})=\frac{\texttt{op\\_index}(y_{t-1}^{d},y_{t}^{d})}{\texttt{len}(y_{t-1}^{d})}  |  
| --- |  
The distribution of where code edits occur in AI completions.
###  B.2 Additional Analyses
#### Where are code edits made to AI-generated code?
The locations in which code edits are performed are approximately uniformly distributed, with increases in frequency at the beginning and end of AI code completions. This suggests that a significant portion of the code edits are related to integrating the completion into existing code or extending the completion’s functionality. Where edits are made in the code also do not vary over time. We did not observe a strong relationship between code edit positions and time (r=-0.12, p0.0001p<0.0001) based on Pearson’s .
###  B.3 Types of Code Edits
To identify types of code edits, the authors manually annotated every single code edit in 30 trajectories (_i.e.,_ 85 total snapshots) to get the initial types of edits. Through discussion between authors, the types and definitions of edits were refined. For examples of code edits in Decode, refer to .
To scale the analysis, we used LLM-as-a-judge to classify edit types (see ). We labeled each edit snapshot using gpt-5-mini with a 94% agreement rate with human raters, based on a sample of 120 before-after pairs.  
|  Accepted Completion  |  
| --- |  
|  Changing Code Functionality  |   |  
|  Improving Code Quality  |  returnquick_sort(left)+ returnquick_sort(left)+  |  
|   |  json.dump(output_list,f,  |  
|  ax.set_title(’Occurrences’)  |  
Table 4: Examples of each edit type. We show the original accepted completion and the edit to the completion. For brevity, we shorten the completion and edits.
##  Appendix C Improving Code LLMs with Decode
###  C.1 Experimental Setup
#### Dataset Processing.
All 5,831 trajectories were utilized for the classification task. For more robust training and better measurement of metrics, we upsampled the majority class (i.e., modified) to ensure a more balanced dataset. Trajectories where the final code snippet was empty were removed from consideration for the generation task. This resulted in a slightly smaller dataset of 4,710 trajectories. We used this modeling approach because it is a harder task to train models to not generate any new code at all. In addition, models trained on the classification task could be used identify such cases rather than try to generate an empty code snippet. For both tasks, the train, development, and tests sets were created corresponding to 80%, 10%, and 10% of developers respectively (randomly split).
#### Training and Inference Hyper-Parameters.
We assessed the effectiveness of both parameter-efficient fine-tuning (LoRA) and full supervised fine-tuning (SFT) using Decode by fine-tuning Qwen2.5-Coder at 3B and 7B parameters, and Llama3.2 at 3B parameters. Both tasks were learned with a causal language modeling head. The models were trained for 15 epochs on NVIDIA A100-80GB and L40S GPUs using the AdamW optimizer , a batch size of 32, BF16 precision, and maximum context lengths of 2048 for the classification task and 4096 for the generation task.
An initial learning rate sweep covering [,,,,,][1e-4,5e-4,1e-5,2e-5,5e-5,1e-6] identified different learning rates as optimal based on the base model family as well as the task at hand. Consequently, we selected those learning rates for all subsequent experiments. Furthermore, experimenting with warm-up ratios of 0.03 and 0.05 as well as gradient accumulation steps of 8 and 16 led to different optimal configurations which we continued with for all subsequent experiments. We kept a fixed LoRA dropout of 0.05, but experimented with different values of Alpha and Rank, and found different optimal configurations based on the task.
For the fine-tuning experiments on the classification taks, the models had the following hyperparameters:
  * •
Fine-tuned Qwen2.5-Coder-3B: Lora alpha of 16, LoRA rank of 8, learning rate of , warmup of 0.03, and gradient accumulation of 16
  * •
Fine-tuned Qwen2.5-Coder-7B: Lora alpha of 32, LoRA rank of 8, learning rate of , warmup of 0.05, and gradient accumulation of 16.
  * •
Fine-tuned Llama-3.2-3B: Lora alpha of 32, LoRA rank of 8, learning rate of , warmup of 0.03, and gradient accumulation of 8.


For the fine-tuning experiments for the generation task, the models had the following hyperparameters:
  * •
Fine-tuned Qwen2.5-Coder-3B: LoRA alpha of 64, LoRA rank of 32, learning rate of 5e^{-}4, warmup of 0.03, and gradient accumulation of 16.
  * •
Fine-tuned Qwen2.5-Coder-7B: LoRA alpha of 64, LoRA rank of 32, learning rate of 5e^{-}4, warmup of 0.03, and gradient accumulation of 16.
  * •
Fine-tuned Llama-3.2-3B: LoRA alpha of 64, LoRA rank of 32, learning rate of 5e^{-}4, warmup of 0.03, and gradient accumulation of 8.


Decoding Strategy. Code generation is known to benefit from sampling [Li et al.2022, Shypula et al.2024], so inference in the generation task specifically was performed with beam sampling with 3 beams, a temperature of 0.7, default top_k and top_p values, and early stopping.
#### Model Access.
For the large base models, we used the OpenAI API to query the GPT models, the Anthropic API for the Claude models, and OpenRouter for access to all other models. For every model provider, the default settings were used.
#### Evaluation Metrics.
For the classification task, standard metrics including precision, recall, accuracy, and F1 score were reported on the balanced dataset. For the generation task, text-similarity metrics including ROUGE-1, ROUGE-2, ROUGE-L, BLEU (Hugging Face Version 0.4.0), percentage of character/line overlap, and normalized Levenshtein similarity were reported. The F1 score and Levenshtein similarity were used to determine the best checkpoint for evaluation.
Statistical Significance Testing. Model differences were determined to be statistically significant or not using the a permutation test on various model pairs. For the classification task, the difference in F1 score between the two models on the same subset of data was computed, and then a two-sided permutation test with 10,000 resamples was run. For the generation task, the normalized Levenshtein similarity was computed for each example in the same dataset split, and then a two-sided permutation test with 10,000 resamples was run. Within each base model family, comparisons were made between the following pairs of models:
  * •
Fine-tuned model trained on initial completion only vs. base model (few-shot)
  * •
Fine-tuned model trained on the first k edits vs. base model (few-shot) given the first k edits
  * •
Fine-tuned model trained on initial completion only vs. frontier model (few-shot)
  * •
Fine-tuned model trained on the first k edits vs. frontier model (few-shot) given the first k edits.


###  C.2 Additional Results
Figure 7:  We display the results of varying the number of additional edits provided to a model during fine-tuning for the classification (left) and generation (right) tasks. 
Predicting developer code edits is a challenging task for LLMs, even for frontier models. A more complete version of  with multiple evaluation metrics can be seen in .
LLMs’ ability to predict code edits improves as more code edits are provided during training. A more complete tabular version of  can be seen in .
Some edits are harder to reason about than others. Based on majority vote, we grouped trajectories by edit type (Customizing code, Improving code quality, Changing functionality, Removing code - and a mixed category when there is no clear majority) and analyzed performance of both base models and fine-tuned models per category. Results can be observed in .  
 |  
|  |  
| Closed-source SOTA Models  |  
 |  
 |  
|   |  
 |  
 |  
 |  
 |  
 |  
|   |  
 |  
|  Llama3.3-70B-Instruct  |  
 |  
| Open-source Base Models (No Fine-Tuning)  |  
|   |  
 |  
|   |  
 |  
 |  
 |  
|  Open-source Base Models (+ Decode)  |  
|   |  
|   |  
 |  
Table 5: Baseline comparison across the classification task.  
| Generation Task  |  
| --- |  
 |  
| Closed-source SOTA Models  |  
 |  
 |  
| Claude Sonnet 4.6  |  
 |  
| DeepSeek-v3.2  |  
 |  
| Devstral-2512  |  
 |  
| Qwen3-Coder-Next  |  
 |  
| Llama3.3-70B-Instruct  |  
 |  
| Open-source Base Models (No Fine-Tuning)  |  
| Qwen2.5-Coder-3B  |  
 |  
| Qwen2.5-Coder-7B  |  
 |  
| Llama-3.2-3B  |  
 |  
|  Open-source Base Models (+ Decode)  |  
| Qwen2.5-Coder-3B  | Fine-tuned  |  
| Qwen2.5-Coder-7B  | Fine-tuned  |  
| Llama-3.2-3B  | Fine-tuned  |  
Table 6: Baseline comparison across the generation task. We report BLEU, ROUGE-1 (R-1), ROUGE-2 (R-2), ROUGE-L (R-L), Levenshtein similarity, character overlap (Char), and line overlap (Line).  
 |  
|  |  
| Qwen2.5-3B (Fine-tuned)  |  
 |  
 |  
 |  
| Qwen2.5-7B (Fine-tuned)  |  
 |  
 |  
 |  
| Llama-3.2-3B (Fine-tuned)  |  
 |  
 |  
 |  
| DeepSeek-v3.2 (Few-shot)  |  
 |  
 |  
 |  
| Claude Sonnet 4.6 (Few-shot)  |  
 |  
 |  
 |  
Table 7: Classification results for multiple-edit settings across hyperparameter configurations and numbers of additional edits. We report precision, recall, F1, and accuracy.  
 |  
|  |  
| Qwen2.5-3B (Fine-tuned)  |  
 |  
 |  
 |  
 |  
| Qwen2.5-7B (Fine-tuned)  |  
 |  
 |  
 |  
 |  
| Llama-3.2-3B (Fine-tuned)  |  
 |  
 |  
 |  
 |  
| Devstral-2512 (Few-shot)  |  
 |  
 |  
 |  
 |  
| Claude Sonnet 4.6 (Few=shot)  |  
 |  
 |  
 |  
 |  
Table 8: Generation results for multiple-edit settings across training, inference, and numbers of additional edits. We report BLEU, ROUGE-1 (R-1), ROUGE-2 (R-2), ROUGE-L (R-L), Levenshtein similarity, character overlap (Char), and line overlap (Line).  
 |  
|  |  
 |  
| Qwen-3B (base)  |  
| Qwen-3B (fine-tuned)  |  
| Qwen-7B (base)  |  
| Qwen-7B (fine-tuned)  |  
| Llama-3.2-3B (base)  |  
| Llama-3.2-3B (fine-tuned)  |  
Table 9: Pass@ results across code generation benchmarks.  
| Customizing  |  
| --- |  
| Devstral-2512 (Few-shot)  |  
| Claude-Sonnet-4.6 (Few-shot)  |  
| GPT-5.2 (Few-shot)  |  
| DeepSeek-v3.2 (Few-shot)  |  
| Qwen3-Coder-Next (Few-shot)  |  
| Llama3.3-70B-Instruct (Few-shot)  |  
| Qwen2.5-3B (base)  |  
| Qwen2.5-3B (Fine-tuned)  |  
| Qwen2.5-7B (base)  |  
| Qwen2.5-7B (Fine-tuned)  |  
| Llama-3.2-3B (base)  |  
| Llama-3.2-3B (Fine-tuned)  |  
Table 10: Generation performance (Levenshtein similarity) stratified by edit type.
##  Appendix D Prompts
Here we report the prompts utilized for various tasks during the dataset analysis, labeling, and model training stages.
###  D.1 Prompt to identify code context.
We replicated the multi-step prompting process employed by Copilot Arena  to cluster code contexts and categorize code trajectories. Below are the three prompts used directly from Copilot Arena with model GPT-4o-mini. Refer to , and  for the prompts.
You are a helpful assistant that describes code files in a single, concise sentence. Focus on the main purpose and functionality of the code. Keep descriptions clear, technical, and under 100 characters. Do not mention file names or extensions in your description. General Prompt Describe this code in one sentence Figure 8: The first prompt used to identify the code context, which summarizes the code file. You are a code organization expert. Analyze the provided code descriptions and: 1. Identify 5-10 main functional clusters or themes 2. Assign each description to the most appropriate cluster 3. Provide a brief name and description for each cluster 4. Format the response as valid JSON with the following structure: 
```
{
      "clusters": [
        {
          "name": "cluster_name",
          "description": "brief cluster description",
          "descriptions": ["description", "description2"]
        }
      ]
    }

```
Figure 9: The second prompt used to identify the code context, which generates clusters of code files. Please categorize the following code into one of these categories: • User Interaction and Input Handling: Code that manages user inputs, prompts, and basic interaction with the system • Frontend Development and UI Design: Code snippets focused on designing user interfaces and creating interactive components • Backend Development and APIs: Server-side logic, data management, and API integration for applications • Algorithm Design and Problem Solving: Code implementing algorithms to solve computational problems or optimize tasks • Data Processing and File Operations: Code that reads, writes, or processes data from files and other data sources • Game Development and Simulations: Code focused on creating games, simulations, and managing game dynamics • Artificial Intelligence and Machine Learning: Code related to AI and machine learning for training, inference, and application Only respond with the exact category name that best fits. No other text. Here’s the code: Figure 10: The third prompt used to identify the code context, which classifies each code file into categories.
###  D.2 Prompt to label edit type.
In order to categorize edits into one of four categories (changing code functionality, improving code quality, customizing code, deleting code), we used GPT 5 mini for labeling with the following prompt. Refer to , and  for the prompts.
You are a code-edit classifier. You must determine how each line in current_snippet changed relative to earlier versions of the code. You will receive: • outcome_snippet: the oldest known version of the snippet • prev_full_snippet: the version immediately before the current edit. it may or may not simply be the outcome_snippet itself • current_full_snippet: the complete snippet at the current moment • current_snippet: ONLY the lines that changed in this edit (a subset of current_full_snippet) • after_full_snippet: the next version after the current edit. it may or may not simply be the current_full_snippet itself Timeline of code from oldest to newest: outcome_snippet, prev_full_snippet, current_full_snippet, after_full_snippet For each line in current_snippet, assign exactly one label using the taxonomy below. Prioritize using prev_full_snippet to understand the change. Use all surrounding snippets only to understand how the line changed. Prioritize using prev_full_snippet to understand how the line changed - only when you cannot do this use the other snippets as well. 1. customizing-personalizing: The line keeps the same behavior but changes literal values or symbol names that customizes the code to fit the remaining file well, stylistically or otherwise. Examples: renaming variables, changing constant values/literal values, swapping variable names, replacing variables with literals, changing variable values. Changing the value of a comment string is improving-code-quality instead. 2. improving-code-quality: The line improves readability, formatting, comments, or syntax without changing semantic meaning. Examples: Includes fixing syntax such as closing code structures, adjusting tabbing, cleaning up the code (such as removing unnecessary comments, adding new empty lines), deleting partial code, and adding comments. If the entire line was removed, use start-over-commenting-out instead. Figure 11: The prompt used to edit label types (part 1). The remainder of the prompt is located in and . 1. modifying-functionality: The line introduces new code that changes program behavior. Examples: Includes adding methods, changing code logic (such as adding new method calls, changing control flow), and changing API calls (such as changing the API, API methods used, parameters passed in). Do not use if only names/values were changed but the logic remains the same, that is customizing-personalizing instead. 2. start-over-commenting-out: The line corresponds to complete deletion of an earlier line OR the line in current_snippet is an empty string representing removed code. This includes lines that were fully commented out. Partial deletions that still leave a meaningful line are improving-code-quality instead. If a line is empty but not due to code deletion, rather the empty line is a new addition, then this is improving-code-quality instead. If the entire snippet of code in current_snippet is an empty string or not provided, label the empty string under this category. If a new empty line is added but has a matching empty line in prev_full_snippet, then this is unchanged instead. 3. unchanged: The line is EXACTLY the same between prev_full_snippet and current_full_snippet. Even one character difference means it is NOT unchanged. If a line seems ambiguous, apply this priority order: modifying-functionality customizing-personalizing improving-code-quality start-over-commenting-out unchanged Return a JSON array, where each object includes:
```
{
    "line": "<the line from current_snippet>",
    "label": "<one label from the taxonomy>"
}

```
Use strict JSON (no comments, no trailing commas, no code fences). Here are some examples to guide you. I have provided additional rationale per label, but you don’t need to include that in your output. outcome_snippet: {outcome_snippet_1} current_full_snippet: {current_full_snippet_1} current_snippet: {current_snippet_1} prev_full_snippet: {prev_full_snippet_1} after_full_snippet: {after_full_snippet_1} output: {output_1} Figure 12: The prompt used to edit label types (part 2). The remainder of the prompt is located in and . outcome_snippet: {outcome_snippet_2} current_full_snippet: {current_full_snippet_2} current_snippet: {current_snippet_2} prev_full_snippet: {prev_full_snippet_2} after_full_snippet: {after_full_snippet_2} output: {output_2} outcome_snippet: {outcome_snippet_3} current_full_snippet: {current_full_snippet_3} current_snippet: {current_snippet_3} prev_full_snippet: {prev_full_snippet_3} after_full_snippet: {after_full_snippet_3} output: {output_3} outcome_snippet: {outcome_snippet_4} current_full_snippet: {current_full_snippet_4} current_snippet: {current_snippet_4} prev_full_snippet: {prev_full_snippet_4} after_full_snippet: {after_full_snippet_4} output: {output_4} outcome_snippet: {outcome_snippet_5} current_full_snippet: {current_full_snippet_5} current_snippet: {current_snippet_5} prev_full_snippet: {prev_full_snippet_5} after_full_snippet: {after_full_snippet_5} output: {output_5} Figure 13: The prompt used to edit label types (part 3). The remainder of the prompt is located in and .
###  D.3 Prompt for generation task.
For the prompt provided during fine-tuning and inference for the generation task, refer to .
You are a code-edit prediction model. COMPLETION (snippet of code inserted by the user), PREFIX (code before the COMPLETION), and SUFFIX (code after the COMPLETION). Predict what the COMPLETION will look like after the user makes their final edits later. • Output ONLY the final edited COMPLETION (no prefix/suffix, no explanations, no markdown fences) • Preserve semantics; make the minimal necessary edits • Keep the same language and style as the surrounding code • If the completion would be completely deleted in the final version, output exactly: <EDIT DELETED> PREFIX: {prefix_1} COMPLETION: {completion_1} SUFFIX: {suffix_1} FINAL EDITED VERSION OF COMPLETION SNIPPET: {target_0} PREFIX: {prefix_2} COMPLETION: {completion_2} SUFFIX: {suffix_2} FINAL EDITED VERSION OF COMPLETION SNIPPET: {target_1} PREFIX: {prefix} COMPLETION: {completion} SUFFIX: {suffix} Here are some initial edits to the COMPLETION (intermediate versions, oldest to newest). Use them as additional context to predict the FINAL edited completion. If an intermediate edit is <EDIT DELETED>, it does not mean the final output is <EDIT DELETED>. EDIT 1: {edit_1} EDIT 2: {edit_2} Final Edited Version of Completion Snippet: Figure 14: The prompt provided during fine-tuning and inference for the generation task.
###  D.4 Prompt for the classification task
For the prompt provided during fine-tuning and inference for the classification task, refer to .
You are a code-edit prediction model. COMPLETION (snippet of code inserted by the user), PREFIX (code before the COMPLETION), and SUFFIX (code after the COMPLETION). Classify how the COMPLETION will look after the user makes their final edits. Output ONLY the final label (no code, no explanations). "A": deleted by user "B": partially modified by user "C": unmodified by user PREFIX: {prefix_1} COMPLETION: {completion_1} SUFFIX: {suffix_1} FINAL COMPLETION SNIPPET LABEL: {label_1}: {label_1_desc} PREFIX: {prefix_2} COMPLETION: {completion_2} SUFFIX: {suffix_2} FINAL COMPLETION SNIPPET LABEL: {label_2}: {label_2_desc} PREFIX: {prefix_3} COMPLETION: {completion_3} SUFFIX: {suffix_3} FINAL COMPLETION SNIPPET LABEL: {label_3}: {label_3_desc} PREFIX: {prefix} COMPLETION: {completion} SUFFIX: {suffix} Here are some initial edits to the COMPLETION (intermediate versions, oldest to newest). Use them as additional context to predict the final label. If an intermediate edit is <EDIT DELETED>, it does not necessarily mean the final completion is <EDIT DELETED>. EDIT 1: {edit_1} EDIT 2: {edit_2} Final Completion Snippet Label: Figure 15: The prompt provided during fine-tuning and inference for the classification task.
