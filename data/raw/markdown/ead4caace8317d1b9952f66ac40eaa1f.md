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
 ![](https://www.gravatar.com/avatar/879152f9b6bfe097d157e6d68fb95332?d=retro&size=100) ⟨28⟩
DCAgent2⟨28⟩
/
swebench_verified_random_100_folders_exp_psu_swesmith_316_glm_4_7_traces_jupite35e6763a⟨29⟩
like 0
Follow
![⟨30⟩] DCAgent2 24
Modalities:  Text ⟨31⟩
Formats:  parquet ⟨32⟩
optimized-parquet
Size:  1K - 10K ⟨33⟩
Libraries:  Datasets ⟨34⟩ Dask ⟨35⟩ Polars ⟨36⟩ + 1
 Dataset card ⟨29⟩ Data Studio ⟨37⟩ Files Files and versions xet ⟨38⟩ Community ⟨39⟩
Dataset Viewer
 Auto-converted to Parquet⟨40⟩ API Embed  Duplicate⟨41⟩ Data Studio
Subset (1)
default · 4.81k rows
default (4.81k rows)
Split (1)
train · 4.81k rows
train (4.81k rows)
SQL
Console  
|  conversations list  |  agent string  |  model string  |  model_provider string  |  date string  |  task string  |  episode string  |  run_id string  |  trial_name string  |  result string  |  verifier_output string  |  trace_source string  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T10:27:22.019883Z  |  matplotlib__matplotlib-25960  |  episode-33  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  matplotlib__matplotlib-25960__K9aLJHm  |  AgentTimeoutError  |  + cd /testbed + set +x + python -m pip install -e . Obtaining file:///testbed Installing build dependencies: started Installing build dependencies: finished with status 'done' Checking if build backend supports build_editable: started Checking if build backend supports build_editable: finished with status 'done...  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T10:08:10.178108Z  |  django__django-14999  |  episode-178  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  django__django-14999__kEd8Tg6  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T10:11:39.755206Z  |  scikit-learn__scikit-learn-13135  |  episode-100  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  scikit-learn__scikit-learn-13135__cGzBeMm  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ git checkout a061ada48efccf0845acae17009553e01764452b sklearn/preprocess(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T15:04:44.539663Z  |  matplotlib__matplotlib-24870  |  episode-104  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  matplotlib__matplotlib-24870__hhvBtXG  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T12:09:01.907864Z  |  scikit-learn__scikit-learn-25931  |  episode-149  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  scikit-learn__scikit-learn-25931__To5nNur  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ git checkout e3d1f9ac39e4bf0f31430e779acc50fb05fe1b64 sklearn/ensemble/t(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T07:06:32.632314Z  |  django__django-15987  |  episode-507  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  django__django-15987__gSxLLov  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T10:30:21.978344Z  |  sympy__sympy-16450  |  episode-4  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  sympy__sympy-16450__F9rkq6y  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Preparing metad(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T05:10:20.495445Z  |  django__django-11490  |  episode-354  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  django__django-11490__UywdQdi  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T12:08:54.624382Z  |  django__django-14017  |  episode-50  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  django__django-14017__EKQAe3h  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-316_glm_4-7_traces_jupiter__Qwen3-8B  |  hosted_vllm  |  2026-07-03T03:29:55.423726Z  |  django__django-14238  |  episode-305  |  3967c4b0-4a37-423f-b19f-f99cdc8e87e0  |  django__django-14238__gM39VXX  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 49⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    53
Number of rows: 4,814 Total file size: 147 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
View Conversation
