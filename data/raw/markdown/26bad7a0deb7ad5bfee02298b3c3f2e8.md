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
ovos-vad-bench-speech-vs-nonspeech-en-AU⟨29⟩
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
 Dataset card ⟨29⟩ Data Studio ⟨42⟩ Files Files and versions xet ⟨43⟩ Community 1 ⟨44⟩
Dataset Viewer
 Auto-converted to Parquet⟨45⟩ API Embed  Duplicate⟨46⟩ Data Studio
Subset (1)
default · 350 rows
default (350 rows)
Split (1)
en_AU · 350 rows
en_AU (350 rows)
SQL
Console  
|  competitor_id stringclasses 7 values  |  sample_id stringclasses 50 values  |  dataset_id stringclasses 1 value  |  dataset_revision stringclasses 1 value  |  lang stringclasses 1 value  |  modality stringclasses 1 value  |  plugin_id stringclasses 3 values  |  plugin_version stringclasses 3 values  |  runner_version stringclasses 1 value  |  created_at stringlengths 32 32  |  label stringclasses 2 values  |  prediction stringclasses 2 values  |  audio_url stringclasses 25 values  |  latency_ms float64 0.06 152  |  
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
|  noise-vad-strict  |  speech/response_4.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:55.422625+00:00  |  speech  |  speech  |  null  |  0.636  |  
|  noise-vad-strict  |  speech/response_17.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:55.611623+00:00  |  speech  |  speech  |  null  |  0.195  |  
|  noise-vad-strict  |  speech/response_16.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:55.728278+00:00  |  speech  |  speech  |  null  |  0.096  |  
|  noise-vad-strict  |  speech/response_7.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:55.832554+00:00  |  speech  |  speech  |  null  |  0.081  |  
|  noise-vad-strict  |  speech/response_14.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:55.930558+00:00  |  speech  |  speech  |  null  |  0.105  |  
|  noise-vad-strict  |  speech/response_28.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.116018+00:00  |  speech  |  speech  |  null  |  0.14  |  
|  noise-vad-strict  |  speech/response_29.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.286020+00:00  |  speech  |  speech  |  null  |  0.355  |  
|  noise-vad-strict  |  speech/response_15.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.414101+00:00  |  speech  |  speech  |  null  |  0.343  |  
|  noise-vad-strict  |  speech/response_6.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.532137+00:00  |  speech  |  speech  |  null  |  0.331  |  
|  noise-vad-strict  |  speech/response_2.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.683676+00:00  |  speech  |  speech  |  null  |  0.107  |  
|  noise-vad-strict  |  speech/response_39.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.821486+00:00  |  speech  |  speech  |  null  |  0.238  |  
|  noise-vad-strict  |  speech/response_11.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:56.946466+00:00  |  speech  |  speech  |  null  |  0.096  |  
|  noise-vad-strict  |  speech/CAaa55d8308b78b23493096c8533cc793d_1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.058776+00:00  |  speech  |  speech  |  null  |  0.215  |  
|  noise-vad-strict  |  speech/response_10.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.180600+00:00  |  speech  |  speech  |  null  |  0.152  |  
|  noise-vad-strict  |  speech/response_38.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.373308+00:00  |  speech  |  speech  |  null  |  0.143  |  
|  noise-vad-strict  |  speech/response_3.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.509180+00:00  |  speech  |  speech  |  null  |  0.272  |  
|  noise-vad-strict  |  speech/response_1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.624392+00:00  |  speech  |  speech  |  null  |  0.1  |  
|  noise-vad-strict  |  speech/response_12.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.737564+00:00  |  speech  |  speech  |  null  |  0.385  |  
|  noise-vad-strict  |  speech/response_13.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:57.936167+00:00  |  speech  |  speech  |  null  |  0.186  |  
|  noise-vad-strict  |  speech/response_48.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.060533+00:00  |  speech  |  speech  |  null  |  0.089  |  
|  noise-vad-strict  |  speech/response_49.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.179368+00:00  |  speech  |  speech  |  null  |  0.113  |  
|  noise-vad-strict  |  speech/CAd5ed736dfa950bdf92966ff6ce83214f_3.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.325830+00:00  |  speech  |  speech  |  null  |  3.208  |  
|  noise-vad-strict  |  speech/response_40.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.497191+00:00  |  speech  |  speech  |  null  |  0.107  |  
|  noise-vad-strict  |  speech/response_42.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.621563+00:00  |  speech  |  speech  |  null  |  0.185  |  
|  noise-vad-strict  |  speech/response_43.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:58.742508+00:00  |  speech  |  speech  |  null  |  0.256  |  
|  noise-vad-strict  |  1-100032-A-0.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:59.179547+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-100032-A-0.wav ⟨47⟩  |  0.167  |  
|  noise-vad-strict  |  1-57163-A-38.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:21:59.654155+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-57163-A-38.wav ⟨48⟩  |  0.256  |  
|  noise-vad-strict  |  2-141682-A-36.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:00.101208+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-141682-A-36.wav ⟨49⟩  |  0.216  |  
|  noise-vad-strict  |  3-118069-A-27.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:00.459456+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-118069-A-27.wav ⟨50⟩  |  0.134  |  
|  noise-vad-strict  |  3-20861-A-8.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:00.839447+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/3-20861-A-8.wav ⟨51⟩  |  0.21  |  
|  noise-vad-strict  |  4-183487-A-1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:01.368234+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…4-183487-A-1.wav ⟨52⟩  |  0.241  |  
|  noise-vad-strict  |  5-195518-A-7.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:01.964559+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…5-195518-A-7.wav ⟨53⟩  |  0.176  |  
|  noise-vad-strict  |  100976.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:02.368415+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/100976.mp3 ⟨54⟩  |  0.118  |  
|  noise-vad-strict  |  117450.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:02.750253+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/117450.mp3 ⟨55⟩  |  0.108  |  
|  noise-vad-strict  |  14663.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:03.081550+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/14663.mp3 ⟨56⟩  |  0.131  |  
|  noise-vad-strict  |  38830.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:03.436008+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/38830.mp3 ⟨57⟩  |  0.142  |  
|  noise-vad-strict  |  56030.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:03.750502+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/56030.mp3 ⟨58⟩  |  0.178  |  
|  noise-vad-strict  |  7527.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:04.177830+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…ve/main/7527.mp3 ⟨59⟩  |  0.1  |  
|  noise-vad-strict  |  nips4b_birds_trainfile001.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:05.065062+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile001.wav ⟨60⟩  |  0.193  |  
|  noise-vad-strict  |  nips4b_birds_trainfile455.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:06.228575+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile455.wav ⟨61⟩  |  0.235  |  
|  noise-vad-strict  |  sig_210726_112120.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:06.681268+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_112120.wav ⟨62⟩  |  0.059  |  
|  noise-vad-strict  |  sig_210726_114629.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:07.138854+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_114629.wav ⟨63⟩  |  0.066  |  
|  noise-vad-strict  |  sig_210818_162101.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:07.703561+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10818_162101.wav ⟨64⟩  |  0.088  |  
|  noise-vad-strict  |  sig_210914_112218.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:07.973464+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10914_112218.wav ⟨65⟩  |  0.063  |  
|  noise-vad-strict  |  pd_3sec/006No Title-.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:08.209621+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-.mp3.wav000.wav ⟨66⟩  |  0.14  |  
|  noise-vad-strict  |  pd_3sec/STE-011_0.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:08.391212+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…0.mp3.wav000.wav ⟨67⟩  |  0.117  |  
|  noise-vad-strict  |  pd_3sec/chainsaw-9.mp3.wav067.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:08.578510+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…9.mp3.wav067.wav ⟨68⟩  |  0.108  |  
|  noise-vad-strict  |  pd_3sec/faucet_water_into_sink.mp3.wav008.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:09.033320+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…k.mp3.wav008.wav ⟨69⟩  |  0.127  |  
|  noise-vad-strict  |  pd_3sec/koe2.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:09.417889+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…2.mp3.wav000.wav ⟨70⟩  |  0.186  |  
|  noise-vad-strict  |  pd_3sec/popping_bubble_wrap.mp3.wav005.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:09.785762+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…p.mp3.wav005.wav ⟨71⟩  |  0.101  |  
|  noise-vad  |  speech/response_4.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:29.413400+00:00  |  speech  |  speech  |  null  |  0.218  |  
|  noise-vad  |  speech/response_17.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:29.525888+00:00  |  speech  |  speech  |  null  |  0.511  |  
|  noise-vad  |  speech/response_16.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:29.711143+00:00  |  speech  |  speech  |  null  |  0.128  |  
|  noise-vad  |  speech/response_7.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:29.864711+00:00  |  speech  |  speech  |  null  |  0.146  |  
|  noise-vad  |  speech/response_14.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:29.983653+00:00  |  speech  |  speech  |  null  |  0.155  |  
|  noise-vad  |  speech/response_28.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.104568+00:00  |  speech  |  speech  |  null  |  0.087  |  
|  noise-vad  |  speech/response_29.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.369969+00:00  |  speech  |  speech  |  null  |  0.45  |  
|  noise-vad  |  speech/response_15.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.513049+00:00  |  speech  |  speech  |  null  |  0.25  |  
|  noise-vad  |  speech/response_6.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.634190+00:00  |  speech  |  speech  |  null  |  0.168  |  
|  noise-vad  |  speech/response_2.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.758052+00:00  |  speech  |  speech  |  null  |  0.106  |  
|  noise-vad  |  speech/response_39.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:30.963509+00:00  |  speech  |  speech  |  null  |  0.362  |  
|  noise-vad  |  speech/response_11.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.119951+00:00  |  speech  |  speech  |  null  |  0.102  |  
|  noise-vad  |  speech/CAaa55d8308b78b23493096c8533cc793d_1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.234370+00:00  |  speech  |  speech  |  null  |  0.163  |  
|  noise-vad  |  speech/response_10.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.343147+00:00  |  speech  |  speech  |  null  |  0.111  |  
|  noise-vad  |  speech/response_38.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.509452+00:00  |  speech  |  speech  |  null  |  0.176  |  
|  noise-vad  |  speech/response_3.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.665464+00:00  |  speech  |  speech  |  null  |  0.297  |  
|  noise-vad  |  speech/response_1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:31.902571+00:00  |  speech  |  speech  |  null  |  0.145  |  
|  noise-vad  |  speech/response_12.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.065914+00:00  |  speech  |  speech  |  null  |  0.348  |  
|  noise-vad  |  speech/response_13.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.193135+00:00  |  speech  |  speech  |  null  |  0.149  |  
|  noise-vad  |  speech/response_48.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.311386+00:00  |  speech  |  speech  |  null  |  0.086  |  
|  noise-vad  |  speech/response_49.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.460481+00:00  |  speech  |  speech  |  null  |  0.14  |  
|  noise-vad  |  speech/CAd5ed736dfa950bdf92966ff6ce83214f_3.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.616013+00:00  |  speech  |  speech  |  null  |  0.235  |  
|  noise-vad  |  speech/response_40.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.787158+00:00  |  speech  |  speech  |  null  |  0.139  |  
|  noise-vad  |  speech/response_42.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:32.909481+00:00  |  speech  |  speech  |  null  |  0.204  |  
|  noise-vad  |  speech/response_43.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:33.029912+00:00  |  speech  |  speech  |  null  |  0.253  |  
|  noise-vad  |  1-100032-A-0.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:33.513096+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-100032-A-0.wav ⟨47⟩  |  0.141  |  
|  noise-vad  |  1-57163-A-38.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:33.915702+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…1-57163-A-38.wav ⟨48⟩  |  0.163  |  
|  noise-vad  |  2-141682-A-36.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:34.203982+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-141682-A-36.wav ⟨49⟩  |  0.167  |  
|  noise-vad  |  3-118069-A-27.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:34.607012+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-118069-A-27.wav ⟨50⟩  |  0.193  |  
|  noise-vad  |  3-20861-A-8.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:34.954704+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/3-20861-A-8.wav ⟨51⟩  |  0.166  |  
|  noise-vad  |  4-183487-A-1.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:35.367027+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…4-183487-A-1.wav ⟨52⟩  |  0.149  |  
|  noise-vad  |  5-195518-A-7.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:35.832756+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…5-195518-A-7.wav ⟨53⟩  |  0.135  |  
|  noise-vad  |  100976.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:36.130648+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/100976.mp3 ⟨54⟩  |  0.141  |  
|  noise-vad  |  117450.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:36.371501+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…/main/117450.mp3 ⟨55⟩  |  0.112  |  
|  noise-vad  |  14663.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:36.617414+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/14663.mp3 ⟨56⟩  |  0.113  |  
|  noise-vad  |  38830.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:36.879406+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/38830.mp3 ⟨57⟩  |  0.116  |  
|  noise-vad  |  56030.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:37.169565+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…e/main/56030.mp3 ⟨58⟩  |  0.117  |  
|  noise-vad  |  7527.mp3  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:37.349027+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…ve/main/7527.mp3 ⟨59⟩  |  0.151  |  
|  noise-vad  |  nips4b_birds_trainfile001.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:37.712727+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile001.wav ⟨60⟩  |  0.147  |  
|  noise-vad  |  nips4b_birds_trainfile455.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:38.163454+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…trainfile455.wav ⟨61⟩  |  0.17  |  
|  noise-vad  |  sig_210726_112120.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:38.760021+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_112120.wav ⟨62⟩  |  0.09  |  
|  noise-vad  |  sig_210726_114629.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:39.518618+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10726_114629.wav ⟨63⟩  |  0.078  |  
|  noise-vad  |  sig_210818_162101.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:40.247739+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10818_162101.wav ⟨64⟩  |  0.092  |  
|  noise-vad  |  sig_210914_112218.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:41.363173+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…10914_112218.wav ⟨65⟩  |  0.129  |  
|  noise-vad  |  pd_3sec/006No Title-.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:41.636504+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…-.mp3.wav000.wav ⟨66⟩  |  0.118  |  
|  noise-vad  |  pd_3sec/STE-011_0.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:41.874119+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…0.mp3.wav000.wav ⟨67⟩  |  0.124  |  
|  noise-vad  |  pd_3sec/chainsaw-9.mp3.wav067.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:42.183810+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…9.mp3.wav067.wav ⟨68⟩  |  0.112  |  
|  noise-vad  |  pd_3sec/faucet_water_into_sink.mp3.wav008.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:42.501672+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…k.mp3.wav008.wav ⟨69⟩  |  0.123  |  
|  noise-vad  |  pd_3sec/koe2.mp3.wav000.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:42.854840+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…2.mp3.wav000.wav ⟨70⟩  |  0.153  |  
|  noise-vad  |  pd_3sec/popping_bubble_wrap.mp3.wav005.wav  |  speech-vs-nonspeech-en-AU  |  40ce77cb32a384e4d50a568e1ec39ac804019d33  |  en-AU  |  vad  |  ovos-vad-plugin-noise  |  ovos-vad-plugin-noise==0.1.2  |  ovos-plugin-arena==0.1.0a1  |  2026-07-04T05:22:43.097317+00:00  |  non_speech  |  speech  |  https://huggingface.co/d…p.mp3.wav005.wav ⟨71⟩  |  0.103  |  
End of preview. Expand in Data Studio⟨72⟩
* * *
  *  Previous⟨29⟩
  * 1⟨73⟩
  * 2⟨74⟩
  * 3⟨75⟩
  * 4⟨76⟩
  * Next ⟨74⟩


#   ⟨77⟩ OVOS `vad` bench — `speech-vs-nonspeech-en-AU`
Per-clip speech / non-speech decisions predictions of the registered OVOS Plugin Arena⟨78⟩ `vad` fighters over `PolyAI/minds14`⟨79⟩.
One dedicated repo per modality; one dataset split per language; one JSONL file per fighter under `predictions/<lang>/<competitor_id>.jsonl`. Rows follow the arena §3.2 contract (pinned `dataset_revision`, `plugin_version`, `latency_ms`). Produced by the reproducible benchmark script in the arena repo; the arena's `assemble` workflow turns these rows into benchmark boards, blind battle pools and a benchmark-seeded ELO ladder.
Funded by the NGI0 Commons Fund⟨80⟩ / NLnet⟨81⟩ under grant agreement No 101135429⟨82⟩, through the European Commission's Next Generation Internet⟨83⟩ programme.
Copy to bucket new
Use this dataset 

Downloads last month
    84
Number of rows: 350 Total file size: 192 kB
System theme
Company
TOS⟨84⟩ Privacy⟨85⟩ About⟨86⟩ Careers⟨87⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
