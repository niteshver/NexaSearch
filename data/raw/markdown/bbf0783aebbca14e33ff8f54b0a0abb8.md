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
eval-fsr-a3-nemotron-gym-calendar-swe-r319-traces⟨29⟩
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
default · 2.1k rows
default (2.1k rows)
Split (1)
train · 2.1k rows
train (2.1k rows)
SQL
Console  
|  conversations list  |  agent string  |  model string  |  model_provider string  |  date string  |  task string  |  episode string  |  run_id string  |  trial_name string  |  result string  |  verifier_output string  |  trace_source string  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T19:34:27.673588Z  |  scikit-learn__scikit-learn-15100  |  episode-29  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  scikit-learn__scikit-learn-15100__7K5ynzn  |  1.0  |  + cd /testbed + set +x + git checkout af8a6e592a1a15d92d77011856d5aa0ec4db4c6c sklearn/feature_extraction/tests/test_text.py Updated 1 path from 401f293ad + for path in sklearn/feature_extraction/tests/test_text.py + '[' -e sklearn/feature_extraction/tests/test_text.py ']' + git ls-files --error-unmatch -- sklearn/feat...  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T12:03:31.843836Z  |  django__django-13516  |  episode-29  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  django__django-13516__yY5dRye  |  1.0  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T22:19:18.029003Z  |  django__django-14999  |  episode-37  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  django__django-14999__XTjGVhQ  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T10:10:29.727827Z  |  django__django-15278  |  episode-45  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  django__django-15278__5T4tbVa  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T11:51:13.748568Z  |  sympy__sympy-21379  |  episode-72  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  sympy__sympy-21379__Ynethqk  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Preparing metad(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T22:37:48.917623Z  |  django__django-12050  |  episode-53  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  django__django-12050__8yfKsKA  |  1.0  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T20:13:14.992777Z  |  django__django-12406  |  episode-94  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  django__django-12406__cp9t5sq  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T21:53:55.115755Z  |  pydata__xarray-4687  |  episode-48  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  pydata__xarray-4687__zzzRtgR  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T20:11:29.385182Z  |  pydata__xarray-6938  |  episode-28  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  pydata__xarray-6938__wS9P9fx  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/7137252316510037  |  hosted_vllm  |  2026-07-08T22:37:22.057439Z  |  sympy__sympy-16450  |  episode-25  |  bfd34645-f9e3-4941-8d8f-bac523f33e20  |  sympy__sympy-16450__4miLn6Y  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Preparing metad(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 21⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    39
Number of rows: 2,100 Total file size: 287 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
View Conversation
