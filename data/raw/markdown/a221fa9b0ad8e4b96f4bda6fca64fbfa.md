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
dev_set_v2_a3_rl_laion_exp_rpt_codenet_python_v2_20260703_153928⟨29⟩
like 0
Follow
![⟨30⟩] DCAgent2 24
Modalities:  Text ⟨31⟩
Formats:  parquet ⟨32⟩
optimized-parquet
Size:  < 1K ⟨33⟩
Libraries:  Datasets ⟨34⟩ pandas ⟨35⟩ Polars ⟨36⟩ + 1
 Dataset card ⟨29⟩ Data Studio ⟨37⟩ Files Files and versions xet ⟨38⟩ Community ⟨39⟩
Dataset Viewer
 Auto-converted to Parquet⟨40⟩ API Embed  Duplicate⟨41⟩ Data Studio
Subset (1)
default · 644 rows
default (644 rows)
Split (1)
train · 644 rows
train (644 rows)
SQL
Console  
|  conversations listlengths 2 324  |  agent stringclasses 1 value  |  model stringclasses 1 value  |  model_provider stringclasses 1 value  |  date stringlengths 27 27  |  task stringclasses 87 values  |  episode stringclasses 48 values  |  run_id stringclasses 1 value  |  trial_name stringlengths 19 41  |  result stringclasses 12 values  |  verifier_output stringlengths 66 322k ⌀  |  trace_source stringclasses 58 values  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T22:53:38.983529Z  |  grid-pathfinding  |  episode-4  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  grid-pathfinding__PB7Pb22  |  AgentTimeoutError  |  ============================= test session starts ============================== platform linux -- Python 3.11.15, pytest-8.4.1, pluggy-1.6.0 rootdir: /tests collected 1 item ../tests/test_outputs.py . [100%] ==================================== PASSES ===================...  |  main  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T22:42:32.555615Z  |  jq-data-processing  |  episode-12  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  jq-data-processing__94BpGUb  |  AgentTimeoutError  |  Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB] Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB] Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB] Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8790 kB] Get:5 http://deb.debian.org/d...  |  main  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-04T00:52:26.299783Z  |  supply-chain-fulfillment  |  episode-2  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  supply-chain-fulfillment__PJReytz  |  AgentTimeoutError  |  downloading uv 0.9.5 x86_64-unknown-linux-gnu no checksums to verify installing to /root/.local/bin uv uvx everything's installed! Downloading pygments (1.2MiB) Downloading pygments Installed 6 packages in 11ms ============================= test session starts ============================== platform linux -- Pytho...  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T23:59:28.641979Z  |  grid-pathfinding  |  episode-17  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  grid-pathfinding__qbMtvWH  |  1.0  |  "============================= test session starts ==============================\nplatform linux --(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-04T00:10:34.995167Z  |  floor-plan-geometry  |  episode-6  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  floor-plan-geometry__pwWveYv  |  0.0  |  "============================= test session starts ==============================\nplatform linux --(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T23:04:52.874135Z  |  neutron-submission  |  episode-7  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  neutron-submission__53wb6B5  |  0.0  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-04T00:48:26.309901Z  |  neural-architecture-search-final  |  episode-21  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  neural-architecture-search-final__5yCb9J8  |  AgentTimeoutError  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T22:26:33.696016Z  |  parking-lot-pathfinding  |  episode-10  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  parking-lot-pathfinding__boKeYfn  |  0.0  |  "============================= test session starts ==============================\nplatform linux --(...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T22:20:35.858241Z  |  mech-system  |  episode-0  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  mech-system__Tu49fte  |  AgentTimeoutError  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-04T00:06:14.949667Z  |  permutation-construction-100k  |  episode-13  |  cf64659f-deea-4926-8f4c-290b6fc131b9  |  permutation-construction-100k__mTZc3Vt  |  AgentTimeoutError  |  "============================= test session starts ==============================\nplatform linux --(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 7⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    58
Number of rows: 644 Total file size: 13.1 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
View Conversation
View Conversation
View Conversation
