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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/636865b8cca0a0a962c21f3f/n1PEv1RXr_QrhK7DIZbOg.png) ⟨28⟩
AI4Manufacturing⟨28⟩
/
D24⟨29⟩
like 0
Follow
![⟨30⟩] AI4Manufacturing 13
Modalities:  Image ⟨31⟩ Text ⟨32⟩
Formats:  parquet ⟨33⟩
Size:  1K - 10K ⟨34⟩
Tags:  smart-manufacturing ⟨35⟩ sft ⟨36⟩ industrial ⟨37⟩ vision ⟨38⟩
Libraries:  Datasets ⟨39⟩ Dask ⟨40⟩ Polars ⟨41⟩ + 1
License:
other
 Dataset card ⟨29⟩ Data Studio ⟨42⟩ Files Files and versions xet ⟨43⟩ Community 1 ⟨44⟩
##  You need to agree to share your contact information to access this dataset
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
This dataset is released for **research use**. Access is reviewed and granted **manually** by the maintainers. Please state your name, affiliation, and intended use.
Log in⟨45⟩ or Sign Up⟨46⟩ to review the conditions and access this dataset content.
  * Records⟨47⟩
  * Unified SFT schema⟨48⟩
  * Task, mask & split⟨49⟩
  * Provenance⟨50⟩
  * Overlap / de-duplication (§8)⟨51⟩


#   ⟨52⟩ D24 
BeanTech anomaly detection & localization. Category **B** , task **T-B1** , in the unified Smart-Manufacturing SFT schema.
> The repository name is an internal task code. See **Provenance** below for the underlying dataset.
##   ⟨47⟩ Records 
**2,540** records (test=741 · train=1799). Pixel masks are embedded as a `mask` image column.
##   ⟨48⟩ Unified SFT schema   
| field  | type  | meaning  |  
| --- | --- | --- |  
| `query`  | str  | the question / instruction (model input)  |  
| `image`  | Image  | the input image (bytes embedded)  |  
| `annot`  | str  | the answer — for this dataset: the plain-text image-level label `good` or `anomalous` (BTAD is binary `ok`/`ko` — no fine-grained defect types). Pixel-level localization is a separate task whose target is the `mask` column — see **Task, mask & split** below  |  
| `reasoning`  | null  | no native CoT in these datasets  |  
| `cate`  | "B"  | SFT category  |  
| `task`  | "T-xx"  | unified task id  |  
| `metadata`  | str (JSON)  | split, provenance, `image_path`, `image_sha256` (dedup key)  |  
| `mask`  | Image | null  |  _(T-B1/T-B2 only)_ the pixel ground-truth mask, bytes embedded  |  
| `masks`  | list[Image]  |  _(D21 only)_ multi-region masks  |  
##   ⟨49⟩ Task, mask & split 
This dataset supports two levels of the anomaly task:
  * **Image-level detection** — `query` asks only whether the pictured product is **good** or **anomalous** , and `annot` is the plain-text answer `good` or `anomalous`.
  * **Pixel-level localization / segmentation** — for every **anomalous** image the `mask` column carries the ground-truth defect mask: a **binary image** (pixel `1` = defect, `0` = background) at the input resolution. **Normal** images have no defect and therefore **no mask** (`null`). A model addressing the localization task is expected to output a binary mask image of the same height×width (`1` = defect pixel, `0` = background); this repo ships that mask as the localization target.


**Split.** `train` = **normal images only** (the `ok` folders; no anomalies, no masks); `test` = **normal + anomalous** (`ok` + `ko`), with a mask on each anomalous image (see the exact counts under **Records**). BTAD ships a single anomaly detection-and-localization protocol (no supervised / few-shot variants); the three products are `01` / `02` / `03`.
##   ⟨50⟩ Provenance 
Underlying dataset: **BTAD**. Upstream license: **CC-BY-SA** (this card is `license: other`; respect the upstream terms). Converted read-only from the raw source into the unified schema; conversion script: `D24/convert_d24.py`, published with `publish/push_to_hf.py`, both in `AI4Manufacturing/forge_model`⟨53⟩.
##   ⟨51⟩ Overlap / de-duplication (§8) 
None notable. Each record carries `metadata.image_sha256` so overlapping images can be kept entirely on one side of a train/eval split.
Copy to bucket new 

Downloads last month
    55
Total file size: 1.1 GB
System theme
Company
TOS⟨54⟩ Privacy⟨55⟩ About⟨56⟩ Careers⟨57⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
