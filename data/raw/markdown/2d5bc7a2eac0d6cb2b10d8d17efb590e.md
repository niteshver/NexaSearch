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
swebench_verified_random_100_folders_exp_psu_swesmith_1K_glm_4_7_traces_jupiter18465471⟨29⟩
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
default · 8.22k rows
default (8.22k rows)
Split (1)
train · 8.22k rows
train (8.22k rows)
SQL
Console  
|  conversations list  |  agent string  |  model string  |  model_provider string  |  date string  |  task string  |  episode string  |  run_id string  |  trial_name string  |  result string  |  verifier_output string  |  trace_source string  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T22:41:10.074955Z  |  astropy__astropy-13236  |  episode-79  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-13236__BXbCDZS  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T15:37:35.539629Z  |  astropy__astropy-13236  |  episode-176  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-13236__Bw65WJ8  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-02T06:52:19.459528Z  |  astropy__astropy-13236  |  episode-264  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-13236__o4XUHp3  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-02T06:54:36.745389Z  |  astropy__astropy-14369  |  episode-614  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14369__cLny7sb  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T22:43:16.140509Z  |  astropy__astropy-14369  |  episode-562  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14369__eyrbRCc  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T15:37:35.625373Z  |  astropy__astropy-14369  |  episode-529  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14369__kvzv2Hb  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T22:44:27.331731Z  |  astropy__astropy-14508  |  episode-452  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14508__EEWE3TB  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T15:37:35.649907Z  |  astropy__astropy-14508  |  episode-21  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14508__EoN8ZGk  |  0.0  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-02T07:00:08.006756Z  |  astropy__astropy-14508  |  episode-537  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14508__a7WYuTD  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/exp-psu-swesmith-1K_glm_4-7_traces_jupiter__0-93__Qwen3-8B  |  hosted_vllm  |  2026-07-01T22:44:42.585180Z  |  astropy__astropy-14598  |  episode-650  |  39427169-6dab-4013-ba60-43bd1b685694  |  astropy__astropy-14598__Lk7kEjZ  |  AgentTimeoutError  |  "+ cd /testbed\n+ set +x\n+ python -m pip install -e '.[test]' --verbose\nUsing pip 24.2 from /opt/m(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 83⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    48
Number of rows: 8,216 Total file size: 876 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
