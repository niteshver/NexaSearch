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
swebench_verified_random_100_folders_a3_rl_DCAgent_r2egym_patched_full_oracle_7d9d41a99⟨29⟩
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
default · 3.08k rows
default (3.08k rows)
Split (1)
train · 3.08k rows
train (3.08k rows)
SQL
Console  
|  conversations list  |  agent string  |  model string  |  model_provider string  |  date string  |  task string  |  episode string  |  run_id string  |  trial_name string  |  result string  |  verifier_output string  |  trace_source string  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T06:23:13.127211Z  |  django__django-11490  |  episode-245  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-11490__zhBedov  |  1.0  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T02:41:13.224873Z  |  matplotlib__matplotlib-26466  |  episode-31  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  matplotlib__matplotlib-26466__bw3KH8o  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T00:41:36.476317Z  |  django__django-16595  |  episode-50  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-16595__FyMdUpj  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T02:09:31.661029Z  |  django__django-14315  |  episode-37  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-14315__GXwfYNF  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T06:05:03.590368Z  |  django__django-12406  |  episode-185  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-12406__FNna6Tz  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-03T22:34:29.072681Z  |  sympy__sympy-21847  |  episode-16  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  sympy__sympy-21847__A9RoqMW  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Preparing metad(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T02:44:16.942911Z  |  django__django-13401  |  episode-45  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-13401__3UDYj3j  |  0.0  |  "+ cd /testbed\n+ set +x\n+ sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen\n+ locale-gen\nGenerating(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T01:44:32.892467Z  |  django__django-15467  |  episode-57  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  django__django-15467__PNxqKwM  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T03:19:33.192526Z  |  matplotlib__matplotlib-24870  |  episode-80  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  matplotlib__matplotlib-24870__TX5QBt7  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e .\nObtaining file:///testbed\n Installing buil(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-DCAgent_r2egym-patched-full-oracle-75-8B  |  hosted_vllm  |  2026-07-04T04:38:41.890622Z  |  sphinx-doc__sphinx-8721  |  episode-154  |  b210ac55-4000-488f-a1a0-55f53dbae5f2  |  sphinx-doc__sphinx-8721__2xVm3XU  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]'\nObtaining file:///testbed\n Prepari(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 31⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    52
Number of rows: 3,080 Total file size: 121 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
