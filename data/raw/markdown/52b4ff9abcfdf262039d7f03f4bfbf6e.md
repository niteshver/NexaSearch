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
terminal_bench_2_g1_diverse_tezos_top4_3160_8b_v2_20260702_050354⟨29⟩
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
default · 263 rows
default (263 rows)
Split (1)
train · 263 rows
train (263 rows)
SQL
Console  
|  conversations listlengths 2 72  |  agent stringclasses 1 value  |  model stringclasses 1 value  |  model_provider stringclasses 1 value  |  date stringlengths 27 27  |  task stringlengths 7 32  |  episode stringclasses 18 values  |  run_id stringclasses 1 value  |  trial_name stringlengths 16 41  |  result stringclasses 2 values  |  verifier_output stringlengths 2.34k 147k  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T14:33:29.828831Z  |  extract-elf  |  episode-2  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  extract-elf__XNgkRLJ  |  AgentTimeoutError  |  Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease Hit:2 http://security.ubuntu.com/ubuntu noble-security InRelease Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease Reading package lists... Reading package lists... Building dependency tr...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T15:58:51.091371Z  |  kv-store-grpc  |  episode-2  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  kv-store-grpc__joCNSXv  |  AgentTimeoutError  |  Collecting pytest==8.4.2 Downloading pytest-8.4.2-py3-none-any.whl.metadata (7.7 kB) Collecting requests==2.32.5 Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB) Collecting psutil==7.0.0 Downloading psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T16:16:02.090131Z  |  build-pov-ray  |  episode-26  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  build-pov-ray__xvcy9Xy  |  AgentTimeoutError  |  Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease Get:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB] Get:3 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB] Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease Get:5 http://archive.ubuntu.com/ubuntu noble-updates/u...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T10:41:35.142227Z  |  sparql-university  |  episode-0  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  sparql-university__co4XZne  |  AgentTimeoutError  |  Hit:1 http://security.ubuntu.com/ubuntu noble-security InRelease Hit:2 http://archive.ubuntu.com/ubuntu noble InRelease Hit:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease Hit:4 http://archive.ubuntu.com/ubuntu noble-backports InRelease Reading package lists... Reading package lists... Building dependency tr...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T17:27:30.690151Z  |  vulnerable-secret  |  episode-4  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  vulnerable-secret__T59EwwH  |  AgentTimeoutError  |  Hit:1 http://deb.debian.org/debian bookworm InRelease Hit:2 http://deb.debian.org/debian bookworm-updates InRelease Hit:3 http://deb.debian.org/debian-security bookworm-security InRelease Reading package lists... Reading package lists... Building dependency tree... Reading state information... The following additional ...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T15:06:12.249733Z  |  make-mips-interpreter  |  episode-4  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  make-mips-interpreter__rpg4hB2  |  AgentTimeoutError  |  Hit:1 http://deb.debian.org/debian bookworm InRelease Hit:2 http://deb.debian.org/debian bookworm-updates InRelease Hit:3 http://deb.debian.org/debian-security bookworm-security InRelease Reading package lists... Reading package lists... Building dependency tree... Reading state information... curl is already the newes...  |  
|  [ { "content": "You are an AI assistant tasked with solving command-line tasks in a Linux environment. You will be given a task description and the output from previously executed commands. Your goal is to solve the task by providing batches of shell commands.\n\nFormat your response as JSON with the following st...  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T10:10:49.723509Z  |  fix-code-vulnerability  |  episode-2  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  fix-code-vulnerability__3jgyMps  |  AgentTimeoutError  |  Collecting pytest==8.4.1 Downloading pytest-8.4.1-py3-none-any.whl.metadata (7.7 kB) Collecting pytest-json-ctrf==0.3.5 Downloading pytest_json_ctrf-0.3.5-py3-none-any.whl.metadata (3.3 kB) Requirement already satisfied: iniconfig>=1 in /usr/local/lib/python3.11/site-packages (from pytest==8.4.1) (2.3.0) Requiremen...  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T12:12:38.238066Z  |  model-extraction-relu-logits  |  episode-1  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  model-extraction-relu-logits__JfBk5D5  |  AgentTimeoutError  |  "Hit:1 http://deb.debian.org/debian bookworm InRelease\nHit:2 http://deb.debian.org/debian bookworm-(...TRUNCATED)  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T10:41:11.399634Z  |  reshard-c4-data  |  episode-6  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  reshard-c4-data__XXXErVr  |  AgentTimeoutError  |  "Downloading pygments (1.2MiB)\nDownloading numpy (15.9MiB)\nDownloading pandas (10.4MiB)\nDownloadi(...TRUNCATED)  |  
|  [{"content":"You are an AI assistant tasked with solving command-line tasks in a Linux environment. (...TRUNCATED)  |  terminus-2  |  hosted_vllm/DCAgent3/g1_diverse_tezos_top4_3160_8b_v2  |  hosted_vllm  |  2026-07-02T14:13:56.091780Z  |  log-summary-date-ranges  |  episode-0  |  4c6ef0dc-40df-4a70-9bf5-90eb3196a1bc  |  log-summary-date-ranges__S7yDUBS  |  AgentTimeoutError  |  "Hit:1 http://deb.debian.org/debian bookworm InRelease\nGet:2 http://deb.debian.org/debian bookworm-(...TRUNCATED)  |  
End of preview. Expand in Data Studio⟨42⟩
* * *
  *  Previous⟨29⟩
  * 1⟨43⟩
  * 2⟨44⟩
  * 3⟨45⟩
  * Next ⟨44⟩


README.md exists but content is empty. 
Copy to bucket new
Use this dataset 

Downloads last month
    45
Number of rows: 263 Total file size: 2.18 MB
System theme
Company
TOS⟨46⟩ Privacy⟨47⟩ About⟨48⟩ Careers⟨49⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
View Conversation
View Conversation
View Conversation
View Conversation
View Conversation
View Conversation
View Conversation
