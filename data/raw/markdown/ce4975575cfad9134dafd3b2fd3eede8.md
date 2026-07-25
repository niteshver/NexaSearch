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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/643e9018e1b2a57ff0d50e65/T-dgJGgGGdlYyS18DGuce.jpeg) ⟨28⟩
Frinkleko⟨28⟩
/
kuaishou-llmrec-sft-baseline-0.91⟨29⟩
like 3
Tasks:  Text Generation ⟨30⟩
Languages:  Chinese ⟨31⟩
Size:  10K<n<100K ⟨32⟩
Tags:  recommendation ⟨33⟩ kuaishou ⟨34⟩ onereason ⟨35⟩ sft ⟨36⟩ llm-rec ⟨37⟩
License:
apache-2.0
 Dataset card ⟨29⟩ Files Files and versions xet ⟨38⟩ Community ⟨39⟩
Dataset Viewer
API Embed  Duplicate⟨40⟩ Data Studio
Subset (1)
default
default
Split (1)
train
train
The dataset viewer is not available for this split.
Cannot extract the features (columns) for the split 'train' of the config 'default' of the dataset.

```
Error code:   FeaturesError
Exception:    ValueError
Message:      Trailing data
Traceback:    Traceback (most recent call last):
                File "/src/services/worker/src/worker/job_runners/split/first_rows.py", line 243, in compute_first_rows_from_streaming_response
                  iterable_dataset = iterable_dataset._resolve_features()
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 4379, in _resolve_features
                  features = _infer_features_from_batch(self.with_format(None)._head())
                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2661, in _head
                  return next(iter(self.iter(batch_size=n)))
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2839, in iter
                  for key, pa_table in ex_iterable.iter_arrow():
                                       ~~~~~~~~~~~~~~~~~~~~~~^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2377, in _iter_arrow
                  yield from self.ex_iterable._iter_arrow()
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 536, in _iter_arrow
                  for key, pa_table in iterator:
                                       ^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 419, in _iter_arrow
                  for key, pa_table in self.generate_tables_fn(**gen_kwags):
                                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/packaged_modules/json/json.py", line 251, in _generate_tables
                  batch = "\n".join(ujson_dumps(x) for x in ujson_loads(full_data)).encode()
                                                            ~~~~~~~~~~~^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/utils/json.py", line 20, in ujson_loads
                  return pd.io.json.ujson_loads(*args, **kwargs)
                         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
              ValueError: Trailing data
```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨41⟩, and open a discussion⟨42⟩ for direct support.
  * Dataset⟨43⟩
  * Data recipe (from `comp_sft`)⟨44⟩
  * LoRA hyperparameters⟨45⟩
  * Eval scores⟨46⟩
  * How to reproduce⟨47⟩
  * License⟨48⟩


#   ⟨49⟩ Kuaishou LLM-Rec Challenge (SIGIR 2026) — OneReason-0.8B SFT Baseline (0.9107) 
Minimal SFT dataset + LoRA hyperparameters that reach **0.9107 leaderboard score** on the Kuaishou LLM-Rec Challenge, fine-tuning `OpenOneRec/OneReason-0.8B-pretrain-competition`.
##   ⟨43⟩ Dataset 
`train.jsonl` — **32,705 rows** , competition-platform format:

```
[{"system": "...", "prompt": "...", "response": "..."}]

```

Each line is a JSON array containing one dict. Bucket composition:  
| Bucket  | Rows  | Description  |  
| --- | --- | --- |  
| comp_recommend  | 18,651  | User history → next-SID prediction across 4 domains (video/prod/ad/live)  |  
| comp_item  | 9,684  | Bidirectional item encode/decode (SID ↔ caption)  |  
| comp_user_interest  | 2,792  | Free-form user profile analysis (JSON array or reasoning)  |  
| common_sense  | 1,578  | CEval multi-choice questions  |  
| **TOTAL**  | **32,705**  | shuffled with seed=42  |  
##   ⟨44⟩ Data recipe (from `comp_sft`) 
  1. Load all rows from the competition's `comp_sft` split
  2. **Exact-row dedup** (drops rows with identical prompt+response hash)
  3. **Special-char filter** (drops rows with control chars, U+FFFD, etc.)
  4. **Length filter** : prompt 20-100K chars, response 5-100K chars
  5. **`dedupe_identical_think_per_prompt`**on the`recommend` bucket:
     * Group rows by prompt
     * If multiple rows share an identical `<think>` block, keep 1 filled-think and convert the rest to `/no_think` variants (empty `<think></think>` + direct SID output)
     * Result: 6,378 filled-think rows + 12,273 no-think direct-SID rows
  6. `item`, `user_interest`, `common_sense` buckets: think traces preserved as-is
  7. Load `common_sense` from `ceval` + `eval_log` sources
  8. Shuffle all buckets together (seed=42)


Reproducing the dedup step (pseudocode):

```
from collections import defaultdict
import re

THINK_RE = re.compile(r'<think>(.*?)</think>', re.DOTALL)

def think_of(response: str) -> str:
    m = THINK_RE.search(response)
    return m.group(1).strip() if m else ''

def dedupe_identical_think_per_prompt(rows):
    by_prompt = defaultdict(list)
    for r in rows:
        by_prompt[(r.system, r.user)].append(r)
    out = []
    for group in by_prompt.values():
        thinks = {think_of(r.assistant) for r in group}
        if len(thinks) == 1 and next(iter(thinks)):
            out.append(group[0])
            for r in group[1:]:
                out.append(convert_to_no_think(r))
        else:
            out.extend(group)
    return out

```

##   ⟨45⟩ LoRA hyperparameters 

```
method: LoRA
lora_rank: 32
lora_alpha: 32
lora_dropout: 0.05

learning_rate: 2.0e-4
weight_decay: 0.001
warmup_ratio: 0.03
lr_scheduler: cosine

per_device_batch_size: 1
gradient_accumulation_steps: 4
sequence_length: 32768
packing: true

bf16: true
enable_thinking: false

num_train_epochs: 1
save_every_steps: 256

```

Same values in `hyperparameters.json` for programmatic use.
##   ⟨46⟩ Eval scores   
| Task  | Score  |  
| --- | --- |  
| **Overall**  | **0.9107**  |  
| `challenge_itemic_pattern_grounding`  | 0.2146  |  
| `challenge_evolution_action_select`  | 0.0678  |  
| `challenge_evolution_topic_gen`  | 0.0390  |  
| `challenge_recommendation_video`  | 0.0672  |  
| `challenge_recommendation_product`  | 0.1190  |  
| `challenge_recommendation_ad`  | 0.1498  |  
| `challenge_recommendation_live`  | 0.1098  |  
| `challenge_common_sense`  | 0.1435  |  
##   ⟨47⟩ How to reproduce 
  1. Download `train.jsonl`
  2. Upload to the Kuaishou LLM-Rec competition platform SFT UI
  3. Set base model: `OpenOneRec/OneReason-0.8B-pretrain-competition`
  4. Apply hyperparameters above
  5. Train 1 epoch
  6. Submit for eval


##   ⟨48⟩ License 
Apache 2.0.
Copy to bucket new 

Downloads last month
    554
Total file size: 243 MB
System theme
Company
TOS⟨50⟩ Privacy⟨51⟩ About⟨52⟩ Careers⟨53⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
