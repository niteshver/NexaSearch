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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/630a5ef0e81e1dea2cedcec0/1nJpWm5L2XxDK7svPF9Hl.png) ⟨28⟩
Meddies⟨28⟩
/
meddies-asr-benchmark⟨29⟩
like 2
Follow
![⟨30⟩] Meddies 16
Tasks:  Automatic Speech Recognition ⟨31⟩
Modalities:  Audio ⟨32⟩ Text ⟨33⟩
Formats:  parquet ⟨34⟩
Languages:  Vietnamese ⟨35⟩ English ⟨36⟩
Size:  < 1K ⟨37⟩
Libraries:  Datasets ⟨38⟩ pandas ⟨39⟩ Polars ⟨40⟩ + 1
 Dataset card ⟨29⟩ Data Studio ⟨41⟩ Files Files and versions xet ⟨42⟩ Community 1 ⟨43⟩
##  You need to agree to share your contact information to access this dataset
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
Log in⟨44⟩ or Sign Up⟨45⟩ to review the conditions and access this dataset content.
  * Configs⟨46⟩
  * Subset Status⟨47⟩
  * Row Schema⟨48⟩
  * Build Notes⟨49⟩


#   ⟨50⟩ Meddies ASR Benchmark 
Vietnamese and English ASR benchmark slices for Meddies evaluation, packaged as Parquet with embedded audio in a `datasets.Audio` column.
This repo currently exposes four subsets:
  * `vi_general`: deterministic Vietnamese general-domain slice from `google/fleurs` test
  * `en_general`: deterministic English general-domain slice from `google/fleurs` test
  * `vi_medical`: Vietnamese medical audio set from `Dr Cao Huu Thinh Official`, with references pending later curation
  * `en_medical`: English medical evaluation set packaged from `Omi-Health/medical-STT-eval`


##   ⟨46⟩ Configs   
| config  | rows  | hours  | source  |  
| --- | --- | --- | --- |  
| `vi_general`  | 200  | 0.6944  |  `google/fleurs` (`vi_vn`, deterministic test slice)  |  
| `en_general`  | 200  | 0.5403  |  `google/fleurs` (`en_us`, deterministic test slice)  |  
| `vi_medical`  | 24  | 4.8148  |  `DrCaoHuuThinhOfficial` YouTube playlist download  |  
| `en_medical`  | 57  | 8.6126  | `Omi-Health/medical-STT-eval`  |  
##   ⟨47⟩ Subset Status 
  * `vi_general` and `en_general` are directly scorable.
  * `en_medical` is directly scorable.
  * `vi_medical` is intentionally not yet directly scorable:
    * `text` and `reference_text` are blank
    * `reference_status` is `missing_reference`
    * transcript hint paths and YouTube provenance are preserved for later labeling


##   ⟨48⟩ Row Schema   
| column  | meaning  |  
| --- | --- |  
| `audio`  | embedded benchmark audio  |  
| `text`  | primary transcript field  |  
| `reference_text`  | explicit scoring reference; identical to `text` when available  |  
| `example_id`  | stable benchmark row id  |  
|  `language`, `domain`, `split`  | benchmark routing metadata  |  
|  `source_dataset`, `source_config`  | provenance back to the original source  |  
|  `speaker_id`, `segment_id`  | optional grouping identifiers  |  
| `medical_terms`  | reserved field for later medical-term scoring  |  
| `reference_status`  |  `available` or `missing_reference`  |  
|  `transcript_hint_path`, `transcript_hint_source`  | later curation hooks for transcript recovery  |  
|  `title`, `youtube_video_id`, `youtube_url`  | source metadata when relevant  |  
|  `raw_audio_path`, `raw_transcript_path`, `original_id`  | raw provenance fields  |  
|  `gender`, `duration_s`  | source metadata useful for analysis  |  
##   ⟨49⟩ Build Notes 
  * General subsets were built from deterministic `google/fleurs` test slices using seed `20260703`.
  * Vietnamese medical audio was normalized from source `webm` into `16 kHz` mono WAV during packaging.
  * English medical rows preserve the cleaned Omi references and embed the corresponding WAV audio.


Build metadata for this staged snapshot lives in `metadata/build_summary.json`.
Copy to bucket new 

Downloads last month
    232
Total file size: 1.7 GB
##  Collection including Meddies/meddies-asr-benchmark
#### Meddies ASR Collection Resources of Meddies ASR  • 9 items • Updated about 8 hours ago • 1 ⟨51⟩
System theme
Company
TOS⟨52⟩ Privacy⟨53⟩ About⟨54⟩ Careers⟨55⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
