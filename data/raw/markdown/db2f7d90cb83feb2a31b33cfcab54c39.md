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
D05-1-annotated⟨29⟩
like 0
Follow
![⟨30⟩] AI4Manufacturing 13
Tasks:  Visual Question Answering ⟨31⟩ Image Classification ⟨32⟩
Modalities:  Image ⟨33⟩ Text ⟨34⟩
Formats:  parquet ⟨35⟩
Languages:  English ⟨36⟩
Size:  10K - 100K ⟨37⟩
Tags:  manufacturing ⟨38⟩ industrial-anomaly-detection ⟨39⟩ defect-detection ⟨40⟩ chain-of-thought ⟨41⟩ vision-language ⟨42⟩ mmad ⟨43⟩
Libraries:  Datasets ⟨44⟩ Dask ⟨45⟩ Polars ⟨46⟩ + 1
License:
cc-by-nc-sa-4.0
 Dataset card ⟨29⟩ Data Studio ⟨47⟩ Files Files and versions xet ⟨48⟩ Community ⟨49⟩
##  You need to agree to share your contact information to access this dataset
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
This dataset is derived from MMAD and is licensed CC-BY-NC-SA-4.0 (non-commercial). Access requires approval.
Log in⟨50⟩ or Sign Up⟨51⟩ to review the conditions and access this dataset content.
  * What's in it⟨52⟩
  * Roles⟨53⟩
  * How it was built (improve-never-drop)⟨54⟩
  * Counts⟨55⟩
  * 2026-07-18 fix package⟨56⟩
  * Intended use & caveats⟨57⟩
  * Source & license⟨58⟩


#   ⟨59⟩ D05 Track-1 Annotated — gold-conditioned visual reasoning with chain-of-thought 
> **Want the full corpus in one download?** This track is also released merged with `D05-2a-annotated`⟨60⟩ as `AI4Manufacturing/D05-annotated`⟨61⟩ (34,414 records; filter tracks via `metadata.cot.source`).
A reasoning-augmented version of `AI4Manufacturing/D05`⟨62⟩ (MMAD, multimodal industrial anomaly-detection MCQ). This release covers **Track 1** : the MMAD question types whose gold answers are **reliable** (source-derived), so instead of re-solving we **rationalize** the given gold — a teacher model writes the expert visual reasoning that justifies it.
Track 1 spans **Anomaly Detection, Defect Localization, Defect Description, Object Classification / Analysis / Structure / Details, and Defect Classification on the label-reliable source (DS-MVTec)**. The label-poor Defect-Classification questions (VisA / GoodsAD / MVTec-LOCO) are handled separately in `AI4Manufacturing/D05-2a-annotated`⟨60⟩; the under-determined "Defect Analysis" type is excluded.
##   ⟨52⟩ What's in it   
| field  | description  |  
| --- | --- |  
| `query`  | the original MMAD multiple-choice question (directive updated to "Answer with the option content." — see fix package below)  |  
| `image`  | the test image (HF `Image`, unchanged)  |  
| `annot`  | the MMAD answer — `{answer, answer_text, question_type}`. This is the **original MMAD gold, unchanged, for all but 19 disclosed records** whose gold was overturned by an adjudication pass (see fix package below); 4 of those 19 use `answer: null`  |  
| `reasoning`  | teacher **chain-of-thought** , grounded only in the test image, ending `FINAL ANSWER: …`  |  
|  `cate` / `task`  | unchanged from the base dataset  |  
| `metadata`  | original MMAD metadata + a `cot` provenance block (below)  |  
`metadata.cot`:

```
{
  "annotator_model": "gpt-5-mini",
  "method": "rationalized" | "rationalized_regenerated",
  "screen": {"model": "claude-sonnet-5", "faithfulness": 1-5, "hallucination": bool, "reason": "..."},
  "regen": null | {"model": "gpt-5.5" | "claude-sonnet-5", "faith": 1-5, "orig_faith": 1-2},
  "source": "D05_track1_rationalized"
}

```

##   ⟨53⟩ Roles 
**Roles:** `reasoning` is the SFT imitation target — its `FINAL ANSWER` segment is the model-facing answer format; `annot` is the machine-parseable gold used for verification and reward parsing, **not** an output-format target.
##   ⟨54⟩ How it was built (improve-never-drop) 
  1. **Gold-conditioned generation (teacher = gpt-5-mini, batched).** Given the test image plus a defect-free reference image (and, for defect subtypes, a segmentation mask) as **teacher-side grounding that is never leaked into`reasoning`** , the teacher wrote the expert reasoning justifying the reliable gold answer, as if derived from the test image alone.
  2. **Faithfulness screen (judge = Claude Sonnet 5, batched).** Every CoT was scored 1–5 for faithfulness (is the reasoning grounded, or does it over-read / invent visual detail?).
  3. **Regenerate the over-reads — never drop.** CoTs scored **faith ≤ 2** were **regenerated** by a stronger model (gpt-5.5 / Claude Sonnet 5) with the screen's critique fed back as a fix, then **re-gated** ; the regeneration replaced the original **only when it was a genuine improvement** (re-gate faith strictly higher and ≥ 3). Records that didn't improve keep the original CoT. **No record is ever dropped** — every screen verdict is preserved in `metadata.cot`.
  4. **Leakage audit.** Reasoning that referred to the reference image / mask was caught and regenerated with a leakage-hardened prompt so every CoT reads as derived from the test image alone.


##   ⟨55⟩ Counts 
  * **31,405 records** (test split) — the full reliable-gold Track-1 set, **nothing dropped**.
  * Reasoning improved by regeneration: **4,707 records** (2,990 via Claude Sonnet 5, 1,717 via gpt-5.5); the rest carry the original gpt-5-mini CoT.
  * After screening + regeneration, **87% of CoTs are faithfulness ≥ 3** (27,584 records). The remaining ~3,821 (12%) carry a screen-flagged minor over-read that regeneration did not lift to ≥3; these are **leak-free** and their screen verdict is recorded in `metadata.cot` for transparency.
  * Every CoT is leak-audited (0 references to the reference image / mask / grounding) and ends with `FINAL ANSWER`.


##   ⟨56⟩ 2026-07-18 fix package 
The data files were revised in place:
  * **Query directive.** The MCQ instruction now reads **"Answer with the option content."** — previously it asked for the option letter, contradicting the answer format actually used by `reasoning` / `FINAL ANSWER`.
  * **MMAD-gold adjudication: 19 records'`annot` corrected.** An adjudication pass (unconditioned **claude-opus-4-8 re-solve** + independent **claude-sonnet-4-6 gate**) was run on suspect records; the gate **overturned the original MMAD gold on all 19** , and the corrections were **operator-verified visually on all distinct case types**. Each of the 19 carries `metadata.cot.original_mmad_gold` plus the full adjudication verdict. **10 of the 19 are a systematic mirrored-gold defect in VisA`pcb4`** (micro-USB position golds on the wrong side) — an upstream MMAD/VisA issue.
  * **Null convention.** **4 of the 19** corrections use the null convention (`answer: null` — no offered option is true). D05-1 therefore now contains **31,401 letter-answer records + 4 null-answer records**. The earlier statement that `annot` is always the unchanged MMAD gold now holds for all but these 19 disclosed records.


Counts verified by the corpus contradiction re-scan (0 contradictions, 2026-07-18).
##   ⟨57⟩ Intended use & caveats 
  * For **non-commercial research** on manufacturing-domain vision-language reasoning (CC-BY-NC-SA-4.0, inherited from MMAD).
  * The `reasoning` is **teacher-generated and model-gated** , not human-verified. The answer is the original MMAD gold for all but the 19 adjudicated records disclosed in the fix package above (each of those retains `metadata.cot.original_mmad_gold`). A small fraction of records retain a screen-flagged minor over-read that regeneration did not improve; the screen verdict is in `metadata.cot.screen` so these are transparent.
  * Only the reliable-gold Track-1 question types are included; the label-poor Defect-Classification subset is released separately as `D05-2a-annotated`.


##   ⟨58⟩ Source & license 
Derived from MMAD (via `AI4Manufacturing/D05`), which aggregates MVTec-AD, MVTec-LOCO, VisA, and PKU-GoodsAD. Licensed **CC-BY-NC-SA-4.0**. Please cite MMAD and the underlying source datasets.
Copy to bucket new 

Downloads last month
    46
Total file size: 12.1 GB
System theme
Company
TOS⟨63⟩ Privacy⟨64⟩ About⟨65⟩ Careers⟨66⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
