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
 ![](https://huggingface.co/avatars/0dc074cfd9be6321196ed97c63c7de9a.svg) ⟨28⟩
MikoMurra⟨28⟩
/
FuguFableFlow-Prompt-Guides⟨29⟩
like 0
 Dataset card ⟨29⟩ Files Files and versions xet ⟨30⟩ Community ⟨31⟩
Dataset Viewer
The dataset viewer is not available because its heuristics could not detect any supported data files⟨32⟩. You can try uploading⟨33⟩ some data files, or configuring⟨34⟩ the data files location manually.
**YAML Metadata Warning:** empty or missing yaml metadata in repo card
Check out the documentation⟨35⟩ for more information.
  * One-Time Setup⟨36⟩
  * Add A Guide⟨37⟩
  * Source Documents⟨38⟩


#   ⟨39⟩ FuguFableFlow Prompt Guides 
This folder is the low-effort authoring area for public Prompt Builder guides.
Drop Markdown guides into `guides/`, keep the tiny front matter block at the top, then run:

```
./script/publish_prompt_guides.sh MikoMurra/FuguFableFlow-Prompt-Guides

```

That script regenerates `manifest.json` and uploads this folder to a Hugging Face Dataset repo. It excludes `sources/**` by default, so the public bucket contains the compact app-readable guides instead of the full research exports.
##   ⟨36⟩ One-Time Setup 
Install and log in to the Hugging Face CLI:

```
curl -LsSf https://hf.co/cli/install.sh | bash
hf auth login

```

Create or use the public Dataset repo on Hugging Face:

```
MikoMurra/FuguFableFlow-Prompt-Guides

```

After that, publishing is just:

```
./script/publish_prompt_guides.sh MikoMurra/FuguFableFlow-Prompt-Guides

```

If the Dataset repo accidentally contains a full app checkout, run the cleanup publish once:

```
./script/publish_prompt_guides.sh --clean MikoMurra/FuguFableFlow-Prompt-Guides

```

Clean mode deletes known app-repo folders from the remote Dataset and republishes only the prompt-guide payload.
Or set it once in your shell:

```
export HF_PROMPT_GUIDES_REPO="MikoMurra/FuguFableFlow-Prompt-Guides"
./script/publish_prompt_guides.sh

```

##   ⟨37⟩ Add A Guide 
  1. Copy `templates/guide-template.md`.
  2. Put it under `guides/<modality>/<model-name>.md`.
  3. Fill in the front matter.
  4. Write the guide in normal Markdown.
  5. Run the publish script.


Example:

```
guides/video/seedance-2.md
guides/image/flux.md
guides/music/suno-v5-5.md

```

The app should consume `manifest.json` first, then fetch only the guide files it needs. No crawling. No surprise downloads. No model weights.
##   ⟨38⟩ Source Documents 
Put large Notion exports, upstream docs, and rough research captures under `sources/`. These files are for authoring and review. They are not included in the generated manifest, and the publish script does not upload them.
Copy to bucket new 

Downloads last month
    96
Total file size: 94.5 MB
System theme
Company
TOS⟨40⟩ Privacy⟨41⟩ About⟨42⟩ Careers⟨43⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
