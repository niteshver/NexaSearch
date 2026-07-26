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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6722a3d5150ed6c830d8f0cd/T1GaFbEQ3XehN4V04IMuq.png) ⟨28⟩
FluidInference⟨28⟩
/
ami-corpus-mirror⟨29⟩
like 0
Follow
![⟨30⟩] Fluid Inference Community 116
Modalities:  Audio ⟨31⟩ Text ⟨32⟩
Formats:  soundfolder ⟨33⟩
Size:  1K - 10K ⟨34⟩
Tags:  audio ⟨35⟩ speaker-diarization ⟨36⟩ benchmark ⟨37⟩
Libraries:  Datasets ⟨38⟩
Croissant
License:
cc-by-4.0
 Dataset card ⟨29⟩ Data Studio ⟨39⟩ Files Files and versions xet ⟨40⟩ Community 1 ⟨41⟩
Dataset Viewer
 Auto-converted to Parquet⟨42⟩ API Embed  Duplicate⟨43⟩ Data Studio
Subset (1)
default · 5.17k rows
default (5.17k rows)
Split (1)
train · 5.17k rows
train (5.17k rows)
Search is not available for this dataset
SQL
Console
The dataset viewer is not available for this split.
Server error while post-processing the rows. This occured on row 16. Please report the issue.

```
Error code:   RowsPostProcessingError

```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨44⟩, and open a discussion⟨45⟩ for direct support.
  * Contents⟨46⟩
  * License & attribution⟨47⟩
  * Usage in FluidAudio⟨48⟩


#   ⟨49⟩ AMI Corpus Mirror 
Mirror of the subset of the AMI Meeting Corpus⟨50⟩ used by FluidAudio⟨51⟩ diarization benchmarks. Hosted here so CI and local benchmark runs do not depend on the availability of the upstream `groups.inf.ed.ac.uk` server (see FluidAudio#752⟨52⟩).
##   ⟨46⟩ Contents 
  * `annotations/ami_public_manual_1.6.2.zip` — AMI public manual annotations v1.6.2 (repackaged from the official archive; identical content, including `segments/`, `words/`, `corpusResources/meetings.xml`)
  * `sdm/{meeting}.Mix-Headset.wav` — audio for the official 16-meeting AMI-SDM evaluation split (EN2002, ES2004, IS1009, TS3003 × a–d), as fetched from the upstream AMI corpus mirror


##   ⟨47⟩ License & attribution 
The AMI Meeting Corpus is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0)⟨53⟩ license by the AMI Consortium / University of Edinburgh. This repository redistributes it unchanged, with attribution, under the same license. See `annotations` `LICENCE.txt` inside the zip.
If you use this data, cite:
> Jean Carletta et al., "The AMI Meeting Corpus: A Pre-announcement", MLMI 2005.
##   ⟨48⟩ Usage in FluidAudio 
`swift run fluidaudiocli diarization-benchmark --auto-download` fetches from this mirror first and falls back to the upstream Edinburgh server.
Copy to bucket new
Use this dataset 

Downloads last month
    334
Number of rows: 5,174 Total file size: 1.07 GB
System theme
Company
TOS⟨54⟩ Privacy⟨55⟩ About⟨56⟩ Careers⟨57⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
