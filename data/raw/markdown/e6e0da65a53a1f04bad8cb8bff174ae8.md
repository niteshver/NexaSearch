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
swebench_verified_random_100_folders_ablation_pymethods2test_shaped_45_8B_202602afa4779⟨29⟩
like 0
Follow
![⟨30⟩] DCAgent2 24
Modalities:  Text ⟨31⟩
Formats:  parquet ⟨32⟩
optimized-parquet
Size:  1K - 10K ⟨33⟩
Libraries:  Datasets ⟨34⟩ pandas ⟨35⟩ Polars ⟨36⟩ + 1
 Dataset card ⟨29⟩ Data Studio ⟨37⟩ Files Files and versions xet ⟨38⟩ Community ⟨39⟩
Dataset Viewer
 Auto-converted to Parquet⟨40⟩ API Embed  Duplicate⟨41⟩ Data Studio
Subset (1)
default · 2.42k rows
default (2.42k rows)
Split (1)
train · 2.42k rows
train (2.42k rows)
SQL
Console  
|  conversations list  |  agent string  |  model string  |  model_provider string  |  date string  |  task string  |  episode string  |  run_id string  |  trial_name string  |  result string  |  verifier_output string  |  trace_source string  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T01:30:25.923138Z  |  astropy__astropy-13236  |  episode-22  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-13236__7rPpLc9  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T12:30:25.973318Z  |  astropy__astropy-13236  |  episode-50  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-13236__MQGCWnD  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T08:02:09.060655Z  |  astropy__astropy-13236  |  episode-17  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-13236__YACwa7V  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T15:58:20.464389Z  |  astropy__astropy-14369  |  episode-77  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14369__4ZY6vtV  |  DaytonaAuthenticationError  |  null  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T03:03:27.135448Z  |  astropy__astropy-14369  |  episode-32  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14369__YbHUECN  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T06:47:19.030068Z  |  astropy__astropy-14369  |  episode-233  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14369__pVx5EMG  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T13:36:44.617940Z  |  astropy__astropy-14508  |  episode-37  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14508__RbCU9mD  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T00:53:53.817239Z  |  astropy__astropy-14508  |  episode-142  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14508__kWXTfLX  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T08:27:52.780117Z  |  astropy__astropy-14508  |  episode-26  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14508__p8TGBPU  |  1.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/ablation-pymethods2test-shaped-45-8B  |  hosted_vllm  |  2026-07-08T13:46:26.058511Z  |  astropy__astropy-14598  |  episode-20  |  ce4fe387-d19f-474b-a74b-30db83637d11  |  astropy__astropy-14598__5ku2RXo  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 25⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    49
Number of rows: 2,424 Total file size: 262 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
