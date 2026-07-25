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
terminal_bench_2_a3_rl_laion_exp_rpt_codenet_python_v2_20260703_104824⟨29⟩
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
default · 1.57k rows
default (1.57k rows)
Split (1)
train · 1.57k rows
train (1.57k rows)
SQL
Console  
|  conversations listlengths 2 1.13k  |  agent stringclasses 1 value  |  model stringclasses 1 value  |  model_provider stringclasses 1 value  |  date stringclasses 244 values  |  task stringclasses 86 values  |  episode stringclasses 81 values  |  run_id stringclasses 1 value  |  trial_name stringclasses 244 values  |  result stringclasses 4 values  |  verifier_output stringclasses 242 values  |  trace_source stringclasses 147 values  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [ { "role": "user", "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON w...  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T17:23:34.082949Z  |  adaptive-rejection-sampler  |  episode-2  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  adaptive-rejection-sampler__q4gzNJF  |  AgentTimeoutError  |  Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease Reading package lists... Reading package lists... Building dependency tr...  |  main  |  
|  [ { "role": "user", "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON w...  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T17:24:49.454671Z  |  bn-fit-modify  |  episode-18  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  bn-fit-modify__N3DYiCe  |  0.0  |  Get:1 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB] Get:2 http://archive.ubuntu.com/ubuntu noble InRelease [256 kB] Get:3 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [1020 kB] Get:4 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [1417 kB] Get:5 ...  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T15:53:21.811304Z  |  bn-fit-modify  |  episode-38  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  bn-fit-modify__f7Rupna  |  0.0  |  "Get:1 http://archive.ubuntu.com/ubuntu noble InRelease [256 kB]\nGet:2 http://security.ubuntu.com/u(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T19:34:33.683484Z  |  bn-fit-modify  |  episode-39  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  bn-fit-modify__xchNAML  |  0.0  |  "Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease\nHit:2 http://archive.ubuntu.com/u(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T17:29:13.160467Z  |  break-filter-js-from-html  |  episode-17  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  break-filter-js-from-html__659E4bN  |  AgentTimeoutError  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T15:53:21.831029Z  |  break-filter-js-from-html  |  episode-10  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  break-filter-js-from-html__MJsMZzg  |  AgentTimeoutError  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T19:37:44.519067Z  |  break-filter-js-from-html  |  episode-7  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  break-filter-js-from-html__Rh9mWiJ  |  0.0  |  "Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]\nGet:2 http://deb.debian.org/debian (...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T17:29:57.398124Z  |  build-cython-ext  |  episode-86  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  build-cython-ext__Aewd4pB  |  AgentTimeoutError  |  "Collecting pytest==8.4.1\n Downloading pytest-8.4.1-py3-none-any.whl.metadata (7.7 kB)\nCollecting(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T15:53:21.851460Z  |  build-cython-ext  |  episode-10  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  build-cython-ext__PqSLPJY  |  0.0  |  "Collecting pytest==8.4.1\n Downloading pytest-8.4.1-py3-none-any.whl.metadata (7.7 kB)\nCollecting(...TRUNCATED)  |  main  |  
|  [{"role":"user","content":"You are an AI assistant tasked with solving command-line tasks in a Linux(...TRUNCATED)  |  terminus-2  |  hosted_vllm/laion/a3-rl-laion_exp_rpt_codenet-python-v2  |  hosted_vllm  |  2026-07-03T19:39:59.976043Z  |  build-cython-ext  |  episode-8  |  a46d87a9-7218-429e-9abf-fc378aaccfe0  |  build-cython-ext__wnfmLcf  |  AgentTimeoutError  |  "Collecting pytest==8.4.1\n Downloading pytest-8.4.1-py3-none-any.whl.metadata (7.7 kB)\nCollecting(...TRUNCATED)  |  main  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * ...⟨46⟩
  * 16⟨47⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    56
Number of rows: 1,570 Total file size: 96.5 MB
System theme
Company
TOS⟨48⟩ Privacy⟨49⟩ About⟨50⟩ Careers⟨51⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
View Conversation
View Conversation
