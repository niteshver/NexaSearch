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


# 
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6a195e6122cdefac115f893c/fhc_vsBdCceLMNXDWtwJO.jpeg) ⟨28⟩
Prience91⟨28⟩
/
MLM_model_output⟨29⟩
like 0
 Fill-Mask ⟨30⟩ Transformers ⟨31⟩ Safetensors ⟨32⟩ distilbert ⟨33⟩
arxiv: 1910.09700
 Model card ⟨29⟩ Files Files and versions xet ⟨34⟩ Community ⟨35⟩
Deploy
Copy to bucket new
Use this model
### Instructions to use Prience91/MLM_model_output with libraries, inference providers, notebooks, and local apps. Follow these links to get started.
  * Libraries
  *  Transformers⟨36⟩
How to use Prience91/MLM_model_output with Transformers:

```
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("fill-mask", model="Prience91/MLM_model_output")
```

```
# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("Prience91/MLM_model_output")
model = AutoModelForMaskedLM.from_pretrained("Prience91/MLM_model_output", device_map="auto")
```

  * Notebooks
  *  Google Colab⟨37⟩
  *  Kaggle⟨38⟩


  * Model Card for Model ID⟨39⟩
    * Model Details⟨40⟩
      * Model Description⟨41⟩
      * Model Sources [optional]⟨42⟩
    * Uses⟨43⟩
      * Direct Use⟨44⟩
      * Downstream Use [optional]⟨45⟩
      * Out-of-Scope Use⟨46⟩
    * Bias, Risks, and Limitations⟨47⟩
      * Recommendations⟨48⟩
    * How to Get Started with the Model⟨49⟩
    * Training Details⟨50⟩
      * Training Data⟨51⟩
      * Training Procedure⟨52⟩
    * Evaluation⟨53⟩
      * Testing Data, Factors & Metrics⟨54⟩
      * Results⟨55⟩
    * Model Examination [optional]⟨56⟩
    * Environmental Impact⟨57⟩
    * Technical Specifications [optional]⟨58⟩
      * Model Architecture and Objective⟨59⟩
      * Compute Infrastructure⟨60⟩
    * Citation [optional]⟨61⟩
    * Glossary [optional]⟨62⟩
    * More Information [optional]⟨63⟩
    * Model Card Authors [optional]⟨64⟩
    * Model Card Contact⟨65⟩


#   ⟨39⟩ Model Card for Model ID 
##   ⟨40⟩ Model Details 
###   ⟨41⟩ Model Description 
This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.
  * **Developed by:** [More Information Needed]
  * **Funded by [optional]:** [More Information Needed]
  * **Shared by [optional]:** [More Information Needed]
  * **Model type:** [More Information Needed]
  * **Language(s) (NLP):** [More Information Needed]
  * **License:** [More Information Needed]
  * **Finetuned from model [optional]:** [More Information Needed]


###   ⟨42⟩ Model Sources [optional] 
  * **Repository:** [More Information Needed]
  * **Paper [optional]:** [More Information Needed]
  * **Demo [optional]:** [More Information Needed]


##   ⟨43⟩ Uses 
###   ⟨44⟩ Direct Use 
[More Information Needed]
###   ⟨45⟩ Downstream Use [optional] 
[More Information Needed]
###   ⟨46⟩ Out-of-Scope Use 
[More Information Needed]
##   ⟨47⟩ Bias, Risks, and Limitations 
[More Information Needed]
###   ⟨48⟩ Recommendations 
Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.
##   ⟨49⟩ How to Get Started with the Model 
Use the code below to get started with the model.
[More Information Needed]
##   ⟨50⟩ Training Details 
###   ⟨51⟩ Training Data 
[More Information Needed]
###   ⟨52⟩ Training Procedure 
####   ⟨66⟩ Preprocessing [optional] 
[More Information Needed]
####   ⟨67⟩ Training Hyperparameters 
  * **Training regime:** [More Information Needed] 


####   ⟨68⟩ Speeds, Sizes, Times [optional] 
[More Information Needed]
##   ⟨53⟩ Evaluation 
###   ⟨54⟩ Testing Data, Factors & Metrics 
####   ⟨69⟩ Testing Data 
[More Information Needed]
####   ⟨70⟩ Factors 
[More Information Needed]
####   ⟨71⟩ Metrics 
[More Information Needed]
###   ⟨55⟩ Results 
[More Information Needed]
####   ⟨72⟩ Summary 
##   ⟨56⟩ Model Examination [optional] 
[More Information Needed]
##   ⟨57⟩ Environmental Impact 
Carbon emissions can be estimated using the Machine Learning Impact calculator⟨73⟩ presented in Lacoste et al. (2019)⟨74⟩.
  * **Hardware Type:** [More Information Needed]
  * **Hours used:** [More Information Needed]
  * **Cloud Provider:** [More Information Needed]
  * **Compute Region:** [More Information Needed]
  * **Carbon Emitted:** [More Information Needed]


##   ⟨58⟩ Technical Specifications [optional] 
###   ⟨59⟩ Model Architecture and Objective 
[More Information Needed]
###   ⟨60⟩ Compute Infrastructure 
[More Information Needed]
####   ⟨75⟩ Hardware 
[More Information Needed]
####   ⟨76⟩ Software 
[More Information Needed]
##   ⟨61⟩ Citation [optional] 
**BibTeX:**
[More Information Needed]
**APA:**
[More Information Needed]
##   ⟨62⟩ Glossary [optional] 
[More Information Needed]
##   ⟨63⟩ More Information [optional] 
[More Information Needed]
##   ⟨64⟩ Model Card Authors [optional] 
[More Information Needed]
##   ⟨65⟩ Model Card Contact 
[More Information Needed] 

Downloads last month
    102
Safetensors⟨77⟩
Model size
67M params
Tensor type
F32 
·
Files info
Inference Providers NEW⟨78⟩
 Fill-Mask ⟨79⟩
This model isn't deployed by any Inference Provider. 🙋 Ask for provider support⟨80⟩
##  Paper for Prience91/MLM_model_output
#### Quantifying the Carbon Emissions of Machine Learning Paper • 1910.09700 • Published Oct 21, 2019 • 59 ⟨81⟩
System theme
Company
TOS⟨82⟩ Privacy⟨83⟩ About⟨84⟩ Careers⟨85⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
Inference providers allow you to run inference using different serverless providers.
