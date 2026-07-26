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
 ![](https://huggingface.co/avatars/b9a6d8e11ec7a62ca2b819e0b6c37222.svg) ⟨28⟩
gokaygokay⟨28⟩
/
ocr-region-1024-v1⟨29⟩
like 0
Tasks:  Image-to-Text ⟨30⟩ Object Detection ⟨31⟩
Languages:  English ⟨32⟩
ArXiv:
arxiv: 2003.06571
Tags:  ocr ⟨33⟩ grounding ⟨34⟩ bounding-boxes ⟨35⟩ document-understanding ⟨36⟩
License:
other
 Dataset card ⟨29⟩ Files Files and versions xet ⟨37⟩ Community ⟨38⟩
Dataset Viewer
The dataset could not be loaded because the splits use different data file formats, which is not supported. Read more about the splits configuration⟨39⟩. Click for more details.
Couldn't infer the same data file format for all splits. Got {NamedSplit('train'): ('webdataset', {}), NamedSplit('validation'): ('json', {})}

```
Error code:   FileFormatMismatchBetweenSplitsError

```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨40⟩, and open a discussion⟨41⟩ for direct support.
  * Overview⟨42⟩
    * Data Format⟨43⟩
  * Dataset Layout⟨44⟩
  * Sources and Licensing⟨45⟩
  * Data Cleaning and Filtering⟨46⟩
    * Global (applies to every record after resize to 1024px)⟨47⟩
    * Per-Source⟨48⟩
  * Intended Use⟨49⟩
    * Not Suitable For⟨50⟩
  * Statistics⟨51⟩
  * Access and Citation⟨52⟩
  * Known Limitations⟨53⟩
  * Dataset Versioning⟨54⟩


#   ⟨55⟩ OCR-Region 1024 v1 
##   ⟨42⟩ Overview 
OCR-Region 1024 v1 is a line-level OCR-with-region training dataset for vision language models. Each sample combines:
  * **Image** : JPEG at 1024px longest side (quality 92)
  * **OCR Annotations** : Line-level text with bounding boxes, plus optional word-level boxes
  * **Provenance Metadata** : Source origin, original dimensions, and scale factor


The dataset is stored as webdataset⟨56⟩ tar shards, enabling efficient streaming at scale. Each record contains axis-aligned bounding boxes as integer pixel coordinates in the 1024px resized space, with optional polygon vertices for skewed text.
###   ⟨43⟩ Data Format 

```
{
  "__key__": "idl/shard0007/doc123_p4",
  "image": "<jpeg bytes, longest side = 1024, quality 92>",
  "meta": {
    "source": "idl-wds",
    "orig_size": [width, height],
    "scale": 0.53
  },
  "lines": [
    {
      "text": "TOTAL AMOUNT DUE",
      "bbox": [x0, y0, x1, y1],
      "conf": 0.991,
      "poly": [[x0, y0], [x1, y0], [x1, y1], [x0, y1]]
    }
  ],
  "words": [
    {
      "text": "TOTAL",
      "bbox": [x0, y0, x1, y1],
      "line_idx": 0
    }
  ]
}

```

**Coordinate Convention** : All bbox coordinates are integer pixels in the 1024px resized image space. Format is `[x0, y0, x1, y1]` with `x0 < x1` and `y0 < y1`. Polygons are optional and preserve original skew information from source annotations.
##   ⟨44⟩ Dataset Layout 

```
dataset/
├── train/
│   ├── idl/<n>/
│   │   ├── shard0000.tar
│   │   ├── shard0001.tar
│   │   └── manifest.jsonl
│   ├── doclaynet/
│   │   ├── *.tar
│   │   └── manifest.jsonl
│   ├── hiertext/
│   │   ├── *.tar
│   │   └── manifest.jsonl
│   └── textocr/
│       ├── *.tar
│       └── manifest.jsonl
└── val/
    ├── idl/
    │   ├── *.tar
    │   └── manifest.jsonl
    ├── doclaynet/
    │   ├── *.tar
    │   └── manifest.jsonl
    ├── hiertext/
    │   ├── *.tar
    │   └── manifest.jsonl
    └── textocr/
        ├── *.tar
        └── manifest.jsonl

```

Each directory contains one `manifest.jsonl` file with per-shard metadata: record counts, drop statistics, and processing timestamps.
##   ⟨45⟩ Sources and Licensing   
| Source  | License  | Volume  | Annotations  | Notes  |  
| --- | --- | --- | --- | --- |  
| **pixparse/idl-wds**  | Custom IDL-Train  | ~450K pages  | Line text + bbox + confidence score  | Industry Documents Library via AWS. Textract-extracted coordinates. Confidence threshold >= 90%. **ATTRIBUTION** : This dataset repo is private; custom license requires explicit licensing agreement. See original IDL documentation⟨57⟩.  |  
| **HierText (Official)**  | CC BY-SA 4.0  | 8,281 train images  | Word/line/paragraph polygons  | Gold-standard semantic hierarchy. Images sourced from Open Images via CVDF. **ATTRIBUTION REQUIRED** : Per CC BY-SA 4.0, derivative works must credit original. Images retain Open Images attribution. Share-alike clause applies.  |  
| **ds4sd/DocLayNet-v1.1**  | CDLA-Permissive-1.0  | ~50K train pages  | Cell text + bbox; lines reconstructed  | PDF-derived layout cells. Line-level annotations reconstructed via y-overlap clustering. Permissive commercial use.  |  
| **TextOCR (Official)**  | CC BY 4.0  | 21,778 train images  | Word quadrilaterals only  | Meta-sponsored OCR dataset on scene images. Word-level polygons converted to axis-aligned boxes. **Attribution** : Credit Meta (Facebook). No share-alike restriction.  |  
##   ⟨46⟩ Data Cleaning and Filtering 
All records undergo aggressive quality gates applied during conversion:
###   ⟨47⟩ Global (applies to every record after resize to 1024px) 
  1. **Bbox Validation** : Every bounding box is clamped to image bounds and validated: `x1 > x0 + 2` and `y1 > y0 + 2` (minimum 3-pixel extent). Records exceeding 10% invalid boxes are discarded entirely.
  2. **Text Filtering** : Empty or whitespace-only text entries are dropped.
  3. **Minimum Content** : Records must contain ≥5 lines (for line-level sources) or ≥5 words (for word-level sources) to be kept.
  4. **Deduplication** : Exact page duplicates within a source are identified via SHA1 of sorted line texts and dropped.
  5. **Provenance Tracking** : Every record carries source, shard ID, and original key for later excision if needed.


###   ⟨48⟩ Per-Source 
  * **idl-wds** : Textract confidence >= 90%. Pages where > 30% of lines fall below threshold are dropped (bad scans).
  * **DocLayNet** : Pseudo-tokens and zero-height boxes discarded. Reconstructed lines with > 40% mutual token overlap are dropped.
  * **HierText** : Illegible words (`legible == false`) dropped. Vertical text (`vertical == true`) skipped. Placeholder `.` transcriptions removed. Handwritten flag preserved in metadata.
  * **TextOCR** : Illegible (`.`) word annotations dropped.


**Build Date** : 2026-07-04  
**Acceptance Criterion** : Drop rate < 25% per source; zero invalid boxes in pilot verification.
##   ⟨49⟩ Intended Use 
OCR-Region 1024 v1 is designed for:
  * **Grounding Supervision** : Training vision-language models to bind text predictions to spatial regions (line-level bounding box regression).
  * **Region-to-Text Tasks** : "Read the text in region [bbox]" or "locate line X in the image."
  * **Document Understanding** : Fine-grained layout comprehension on real documents and scene images.


###   ⟨50⟩ Not Suitable For 
  * This dataset is **not a hallucination cure**. It provides spatial alignment supervision but does not guarantee factual correctness of OCR transcriptions (particularly for rare scripts or degraded images).
  * General text-only OCR training (use TextOCR⟨58⟩ or Scene Text Recognition Benchmarks⟨59⟩ instead).


##   ⟨51⟩ Statistics   
| Split  | idl-wds  | DocLayNet  | HierText  | TextOCR  | Total  |  
| --- | --- | --- | --- | --- | --- |  
| Train  | ~450K  | ~50K  | 8,281  | 21,778  | ~530K  |  
| Val  | 2K  | ~5K  | 1,724  | 3,124  | ~11.8K  |  
Training sampling weights: idl-wds 0.55 / doclaynet 0.25 / hiertext 0.12 / textocr 0.08 (HierText upweighted for hierarchy quality).
##   ⟨52⟩ Access and Citation 
This dataset is **private**. Access requires permission from the repository owner.
If you use OCR-Region 1024 v1 in research, please:
  1. Cite the IDL documentation⟨57⟩ for pixparse/idl-wds samples
  2. Cite HierText⟨60⟩ for HierText samples with proper CC BY-SA 4.0 attribution
  3. Cite DocLayNet⟨61⟩ for document layout samples
  4. Cite TextOCR⟨62⟩ for scene text samples with Meta attribution


##   ⟨53⟩ Known Limitations 
  * **Coordinate Convention** : Bboxes are axis-aligned (AABB), even for skewed text. Raw polygon vertices are preserved in `poly` fields where available.
  * **Language** : Primarily English (IDL US documents, Open Images, TextOCR). Some multilingual content from HierText.
  * **Quality Variance** : Textract confidence scores (idl-wds) range 0.90–1.0; other sources lack per-box confidence.
  * **Scene vs. Document Split** : Mixed; no explicit scene/document split in train. Validation splits isolate sources for source-specific evaluation.


##   ⟨54⟩ Dataset Versioning 
**Version** : 1.0  
**Built** : 2026-07-04  
**Freeze Hash** : [revision tagged by training config]
* * *
_Generated for vision-language model training with attribution to all upstream sources._
Copy to bucket new 

Downloads last month
    1,016
Total file size: 133 GB
##  Paper for gokaygokay/ocr-region-1024-v1
#### A novel and efficient algorithm to solve subset sum problem Paper • 2003.06571 • Published May 3, 2020 ⟨63⟩
System theme
Company
TOS⟨64⟩ Privacy⟨65⟩ About⟨66⟩ Careers⟨67⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
