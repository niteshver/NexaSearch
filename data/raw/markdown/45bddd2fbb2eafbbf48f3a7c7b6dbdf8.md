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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6417f46bfff753e7c158e23f/-p5xGWDWjWT7jZ_LqeA-u.png) ⟨28⟩
OpenVoiceOS⟨28⟩
/
ovos-vad-bench-speech-vs-nonspeech-ar-SA⟨29⟩
like 0
Follow
![⟨30⟩] OpenVoiceOS 34
Modalities:  Text ⟨31⟩
Formats:  json ⟨32⟩
Size:  < 1K ⟨33⟩
Tags:  openvoiceos ⟨34⟩ benchmark ⟨35⟩ predictions ⟨36⟩ voice-activity-detection ⟨37⟩ vad ⟨38⟩
Libraries:  Datasets ⟨39⟩ Dask ⟨40⟩ Polars ⟨41⟩ + 1
License:
apache-2.0
 Dataset card ⟨29⟩ Data Studio ⟨42⟩ Files Files and versions xet ⟨43⟩ Community ⟨44⟩
Dataset Viewer
 Auto-converted to Parquet⟨45⟩ API Embed  Duplicate⟨46⟩ Data Studio
Subset (1)
default · 350 rows
default (350 rows)
Split (1)
ar_SA · 350 rows
ar_SA (350 rows)
SQL
Console  
|  competitor_id stringclasses 7 values  |  sample_id stringclasses 50 values  |  dataset_id stringclasses 1 value  |  dataset_revision stringclasses 1 value  |  lang stringclasses 1 value  |  modality stringclasses 1 value  |  plugin_id stringclasses 3 values  |  plugin_version stringclasses 3 values  |  runner_version stringclasses 1 value  |  created_at stringlengths 32 32  |  label stringclasses 2 values  |  prediction stringclasses 2 values  |  audio_url stringclasses 25 values  |  latency_ms float64 0.05 76.8  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  noise-vad-strict  |  speech/52a84b06a97e6a87ac7f592f0054e393.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:36.794651+00:00  |  speech  |  speech  |  null  |  0.133  |  
|  noise-vad-strict  |  speech/23d0559fb6c7382b77af9d33e04e187f.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:36.885615+00:00  |  speech  |  speech  |  null  |  0.121  |  
|  noise-vad-strict  |  speech/de453494ff51f7134f009ce17feeeace.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:36.971629+00:00  |  speech  |  speech  |  null  |  0.053  |  
|  noise-vad-strict  |  speech/36fb4ca607e29c0efa60498b5e9338fa.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.069092+00:00  |  speech  |  speech  |  null  |  0.105  |  
|  noise-vad-strict  |  speech/ab595f04376fceb90d98d5009ebf66f3.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.162998+00:00  |  speech  |  speech  |  null  |  0.087  |  
|  noise-vad-strict  |  speech/d1ca74f2061c97d4a52fbbe3efa219e5.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.253508+00:00  |  speech  |  speech  |  null  |  0.068  |  
|  noise-vad-strict  |  speech/e84fe1e2bc8049cf53748105be8b6124.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.342613+00:00  |  speech  |  speech  |  null  |  0.085  |  
|  noise-vad-strict  |  speech/3c2a264ab7219c7e8278b83b5c1f06fc.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.430904+00:00  |  speech  |  speech  |  null  |  0.086  |  
|  noise-vad-strict  |  speech/ffaffa6ba0f62a6288e3530b20247bbe.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.523313+00:00  |  speech  |  speech  |  null  |  0.087  |  
|  noise-vad-strict  |  speech/d80492f7a73e66404c089215747999da.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.615526+00:00  |  speech  |  speech  |  null  |  0.114  |  
|  noise-vad-strict  |  speech/f19d819fc28aadd568baa03e6896dfc9.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.706022+00:00  |  speech  |  speech  |  null  |  0.088  |  
|  noise-vad-strict  |  speech/765525aae092d729531f3e56ac1c162e.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.814431+00:00  |  speech  |  speech  |  null  |  0.107  |  
|  noise-vad-strict  |  speech/929e2cdef68518b0622d5e35d2820ca4.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:37.920639+00:00  |  speech  |  speech  |  null  |  0.085  |  
|  noise-vad-strict  |  speech/0e7353fe38c9e01015de5ea6e88c3342.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.017623+00:00  |  speech  |  speech  |  null  |  0.087  |  
|  noise-vad-strict  |  speech/22224fe95c5803a78a85332c16815b46.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.119098+00:00  |  speech  |  speech  |  null  |  0.129  |  
|  noise-vad-strict  |  speech/a0698e752f4f7ed0d3c355115c8138bb.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.211974+00:00  |  speech  |  speech  |  null  |  0.101  |  
|  noise-vad-strict  |  speech/fbde3839603706527ceeaeacbbe4f3b7.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.301688+00:00  |  speech  |  speech  |  null  |  0.062  |  
|  noise-vad-strict  |  speech/06ff08ed539a07974593e2ba778abbe1.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.392874+00:00  |  speech  |  speech  |  null  |  0.117  |  
|  noise-vad-strict  |  speech/fa61222c757ed6e8f4599055ecea2420.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.486070+00:00  |  speech  |  speech  |  null  |  0.08  |  
|  noise-vad-strict  |  speech/cec3685c2306570f38266326189bba7a.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.579614+00:00  |  speech  |  speech  |  null  |  0.139  |  
|  noise-vad-strict  |  speech/0cfd495eb8bd434e7e4286f8c49d7719.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.672279+00:00  |  speech  |  speech  |  null  |  0.152  |  
|  noise-vad-strict  |  speech/917c3a6e9891f3dfd86f26db91bc8927.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.774206+00:00  |  speech  |  speech  |  null  |  0.066  |  
|  noise-vad-strict  |  speech/ca1004a5ff02195e5e0c63b2367b1dce.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.867420+00:00  |  speech  |  speech  |  null  |  0.063  |  
|  noise-vad-strict  |  speech/ba83c4c3fd4f07fd6ab535b81f7e7957.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:38.962596+00:00  |  speech  |  speech  |  null  |  0.064  |  
|  noise-vad-strict  |  speech/73b978459b74612ff24a488e1bf7c293.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:39.060708+00:00  |  speech  |  speech  |  null  |  0.132  |  
|  noise-vad-strict  |  1-100032-A-0.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:50.613909+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-100032-A-0.wav ⟨47⟩  |  0.236  |  
|  noise-vad-strict  |  1-57163-A-38.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:50.934877+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-57163-A-38.wav ⟨48⟩  |  0.123  |  
|  noise-vad-strict  |  2-141682-A-36.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:51.213063+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-141682-A-36.wav ⟨49⟩  |  0.123  |  
|  noise-vad-strict  |  3-118069-A-27.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:51.532250+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-118069-A-27.wav ⟨50⟩  |  0.11  |  
|  noise-vad-strict  |  3-20861-A-8.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:51.807893+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/3-20861-A-8.wav ⟨51⟩  |  0.115  |  
|  noise-vad-strict  |  4-183487-A-1.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:52.328384+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…4-183487-A-1.wav ⟨52⟩  |  0.102  |  
|  noise-vad-strict  |  5-195518-A-7.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:52.656132+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…5-195518-A-7.wav ⟨53⟩  |  0.116  |  
|  noise-vad-strict  |  100976.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:52.813228+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/100976.mp3 ⟨54⟩  |  0.096  |  
|  noise-vad-strict  |  117450.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:52.966859+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/117450.mp3 ⟨55⟩  |  0.086  |  
|  noise-vad-strict  |  14663.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:53.143403+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/14663.mp3 ⟨56⟩  |  0.097  |  
|  noise-vad-strict  |  38830.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:53.338553+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/38830.mp3 ⟨57⟩  |  0.112  |  
|  noise-vad-strict  |  56030.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:53.533392+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/56030.mp3 ⟨58⟩  |  0.109  |  
|  noise-vad-strict  |  7527.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:53.743274+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…ve/main/7527.mp3 ⟨59⟩  |  0.093  |  
|  noise-vad-strict  |  nips4b_birds_trainfile001.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:54.051243+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile001.wav ⟨60⟩  |  0.114  |  
|  noise-vad-strict  |  nips4b_birds_trainfile455.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:54.373230+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile455.wav ⟨61⟩  |  0.106  |  
|  noise-vad-strict  |  sig_210726_112120.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:54.674631+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_112120.wav ⟨62⟩  |  0.054  |  
|  noise-vad-strict  |  sig_210726_114629.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:55.026015+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_114629.wav ⟨63⟩  |  0.068  |  
|  noise-vad-strict  |  sig_210818_162101.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:55.293255+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10818_162101.wav ⟨64⟩  |  0.052  |  
|  noise-vad-strict  |  sig_210914_112218.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:55.607859+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10914_112218.wav ⟨65⟩  |  0.063  |  
|  noise-vad-strict  |  pd_3sec/006No Title-.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:55.859545+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-.mp3.wav000.wav ⟨66⟩  |  0.089  |  
|  noise-vad-strict  |  pd_3sec/STE-011_0.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:56.067516+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…0.mp3.wav000.wav ⟨67⟩  |  0.105  |  
|  noise-vad-strict  |  pd_3sec/chainsaw-9.mp3.wav067.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:56.310466+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…9.mp3.wav067.wav ⟨68⟩  |  0.091  |  
|  noise-vad-strict  |  pd_3sec/faucet_water_into_sink.mp3.wav008.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:56.603310+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…k.mp3.wav008.wav ⟨69⟩  |  0.09  |  
|  noise-vad-strict  |  pd_3sec/koe2.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:56.810539+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…2.mp3.wav000.wav ⟨70⟩  |  0.125  |  
|  noise-vad-strict  |  pd_3sec/popping_bubble_wrap.mp3.wav005.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:40:56.991719+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…p.mp3.wav005.wav ⟨71⟩  |  0.141  |  
|  noise-vad  |  speech/52a84b06a97e6a87ac7f592f0054e393.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.125334+00:00  |  speech  |  speech  |  null  |  0.105  |  
|  noise-vad  |  speech/23d0559fb6c7382b77af9d33e04e187f.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.219643+00:00  |  speech  |  speech  |  null  |  0.116  |  
|  noise-vad  |  speech/de453494ff51f7134f009ce17feeeace.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.307853+00:00  |  speech  |  speech  |  null  |  0.056  |  
|  noise-vad  |  speech/36fb4ca607e29c0efa60498b5e9338fa.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.414892+00:00  |  speech  |  speech  |  null  |  0.116  |  
|  noise-vad  |  speech/ab595f04376fceb90d98d5009ebf66f3.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.509297+00:00  |  speech  |  speech  |  null  |  0.093  |  
|  noise-vad  |  speech/d1ca74f2061c97d4a52fbbe3efa219e5.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.605559+00:00  |  speech  |  speech  |  null  |  0.089  |  
|  noise-vad  |  speech/e84fe1e2bc8049cf53748105be8b6124.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.697568+00:00  |  speech  |  speech  |  null  |  0.089  |  
|  noise-vad  |  speech/3c2a264ab7219c7e8278b83b5c1f06fc.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.786655+00:00  |  speech  |  speech  |  null  |  0.082  |  
|  noise-vad  |  speech/ffaffa6ba0f62a6288e3530b20247bbe.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.880767+00:00  |  speech  |  speech  |  null  |  0.098  |  
|  noise-vad  |  speech/d80492f7a73e66404c089215747999da.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:10.976438+00:00  |  speech  |  speech  |  null  |  0.107  |  
|  noise-vad  |  speech/f19d819fc28aadd568baa03e6896dfc9.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.070836+00:00  |  speech  |  speech  |  null  |  0.086  |  
|  noise-vad  |  speech/765525aae092d729531f3e56ac1c162e.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.166939+00:00  |  speech  |  speech  |  null  |  0.085  |  
|  noise-vad  |  speech/929e2cdef68518b0622d5e35d2820ca4.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.256187+00:00  |  speech  |  speech  |  null  |  0.076  |  
|  noise-vad  |  speech/0e7353fe38c9e01015de5ea6e88c3342.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.353639+00:00  |  speech  |  speech  |  null  |  0.09  |  
|  noise-vad  |  speech/22224fe95c5803a78a85332c16815b46.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.453207+00:00  |  speech  |  speech  |  null  |  0.094  |  
|  noise-vad  |  speech/a0698e752f4f7ed0d3c355115c8138bb.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.554697+00:00  |  speech  |  speech  |  null  |  0.084  |  
|  noise-vad  |  speech/fbde3839603706527ceeaeacbbe4f3b7.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.646890+00:00  |  speech  |  speech  |  null  |  0.062  |  
|  noise-vad  |  speech/06ff08ed539a07974593e2ba778abbe1.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.739556+00:00  |  speech  |  speech  |  null  |  0.101  |  
|  noise-vad  |  speech/fa61222c757ed6e8f4599055ecea2420.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.831603+00:00  |  speech  |  speech  |  null  |  0.086  |  
|  noise-vad  |  speech/cec3685c2306570f38266326189bba7a.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:11.921966+00:00  |  speech  |  speech  |  null  |  0.118  |  
|  noise-vad  |  speech/0cfd495eb8bd434e7e4286f8c49d7719.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.014267+00:00  |  speech  |  speech  |  null  |  0.146  |  
|  noise-vad  |  speech/917c3a6e9891f3dfd86f26db91bc8927.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.108818+00:00  |  speech  |  speech  |  null  |  0.066  |  
|  noise-vad  |  speech/ca1004a5ff02195e5e0c63b2367b1dce.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.200567+00:00  |  speech  |  speech  |  null  |  0.099  |  
|  noise-vad  |  speech/ba83c4c3fd4f07fd6ab535b81f7e7957.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.295105+00:00  |  speech  |  speech  |  null  |  0.068  |  
|  noise-vad  |  speech/73b978459b74612ff24a488e1bf7c293.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.390503+00:00  |  speech  |  speech  |  null  |  0.094  |  
|  noise-vad  |  1-100032-A-0.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:12.874743+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-100032-A-0.wav ⟨47⟩  |  0.097  |  
|  noise-vad  |  1-57163-A-38.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:13.394102+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-57163-A-38.wav ⟨48⟩  |  0.137  |  
|  noise-vad  |  2-141682-A-36.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:13.894144+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-141682-A-36.wav ⟨49⟩  |  0.107  |  
|  noise-vad  |  3-118069-A-27.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:14.424233+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-118069-A-27.wav ⟨50⟩  |  0.119  |  
|  noise-vad  |  3-20861-A-8.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:15.010089+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/3-20861-A-8.wav ⟨51⟩  |  0.11  |  
|  noise-vad  |  4-183487-A-1.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:15.646000+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…4-183487-A-1.wav ⟨52⟩  |  0.124  |  
|  noise-vad  |  5-195518-A-7.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:16.424214+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…5-195518-A-7.wav ⟨53⟩  |  0.108  |  
|  noise-vad  |  100976.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:16.976170+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/100976.mp3 ⟨54⟩  |  0.105  |  
|  noise-vad  |  117450.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:17.422676+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/117450.mp3 ⟨55⟩  |  0.098  |  
|  noise-vad  |  14663.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:17.892481+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/14663.mp3 ⟨56⟩  |  0.102  |  
|  noise-vad  |  38830.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:18.330894+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/38830.mp3 ⟨57⟩  |  0.092  |  
|  noise-vad  |  56030.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:18.823516+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/56030.mp3 ⟨58⟩  |  0.088  |  
|  noise-vad  |  7527.mp3  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:19.281399+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…ve/main/7527.mp3 ⟨59⟩  |  0.092  |  
|  noise-vad  |  nips4b_birds_trainfile001.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:19.916838+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile001.wav ⟨60⟩  |  0.115  |  
|  noise-vad  |  nips4b_birds_trainfile455.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:20.537679+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile455.wav ⟨61⟩  |  0.116  |  
|  noise-vad  |  sig_210726_112120.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:21.202257+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_112120.wav ⟨62⟩  |  0.057  |  
|  noise-vad  |  sig_210726_114629.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:21.822034+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_114629.wav ⟨63⟩  |  0.062  |  
|  noise-vad  |  sig_210818_162101.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:22.383807+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10818_162101.wav ⟨64⟩  |  0.076  |  
|  noise-vad  |  sig_210914_112218.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:22.964167+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10914_112218.wav ⟨65⟩  |  0.056  |  
|  noise-vad  |  pd_3sec/006No Title-.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:23.473189+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-.mp3.wav000.wav ⟨66⟩  |  0.078  |  
|  noise-vad  |  pd_3sec/STE-011_0.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:23.956684+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…0.mp3.wav000.wav ⟨67⟩  |  0.087  |  
|  noise-vad  |  pd_3sec/chainsaw-9.mp3.wav067.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:24.414521+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…9.mp3.wav067.wav ⟨68⟩  |  0.092  |  
|  noise-vad  |  pd_3sec/faucet_water_into_sink.mp3.wav008.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:24.873779+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…k.mp3.wav008.wav ⟨69⟩  |  0.085  |  
|  noise-vad  |  pd_3sec/koe2.mp3.wav000.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:25.451383+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…2.mp3.wav000.wav ⟨70⟩  |  0.086  |  
|  noise-vad  |  pd_3sec/popping_bubble_wrap.mp3.wav005.wav  |  speech-vs-nonspeech-ar-SA  |  2e6d34fb35e3ac7021980fb018e7894b151a5c8e  |  ar-SA  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T03:41:26.174443+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…p.mp3.wav005.wav ⟨71⟩  |  0.124  |  
End of preview. Expand in Data Studio⟨72⟩
* * *
  *  Previous⟨29⟩
  * 1⟨73⟩
  * 2⟨74⟩
  * 3⟨75⟩
  * 4⟨76⟩
  * Next ⟨74⟩


#   ⟨77⟩ OVOS `vad` bench — `speech-vs-nonspeech-ar-SA`
Per-clip speech / non-speech decisions predictions of the registered OVOS Plugin Arena⟨78⟩ `vad` fighters over `FBK-MT/Speech-MASSIVE-test`⟨79⟩.
One dedicated repo per modality; one dataset split per language; one JSONL file per fighter under `predictions/<lang>/<competitor_id>.jsonl`. Rows follow the arena §3.2 contract (pinned `dataset_revision`, `plugin_version`, `latency_ms`). Produced by the reproducible benchmark script in the arena repo; the arena's `assemble` workflow turns these rows into benchmark boards, blind battle pools and a benchmark-seeded ELO ladder.
Funded by the NGI0 Commons Fund⟨80⟩ / NLnet⟨81⟩ under grant agreement No 101135429⟨82⟩, through the European Commission's Next Generation Internet⟨83⟩ programme.
Copy to bucket new
Use this dataset 

Downloads last month
    80
Number of rows: 350 Total file size: 195 kB
System theme
Company
TOS⟨84⟩ Privacy⟨85⟩ About⟨86⟩ Careers⟨87⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
