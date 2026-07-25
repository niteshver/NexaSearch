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
Duplicated from yaolily/Timechat-OmniCaptioner-42K⟨28⟩
![⟨29⟩]
 ![](https://huggingface.co/avatars/74850e8c8fd4efda1f0cf246ca4b8662.svg) ⟨30⟩
AdamAlKhalifa⟨30⟩
/
Timechat-OmniCaptioner-42K⟨31⟩
like 0
Tasks:  Video-Text-to-Text ⟨32⟩
Modalities:  Video ⟨33⟩
Languages:  English ⟨34⟩
Size:  10K - 100K ⟨35⟩
ArXiv:
arxiv: 2602.08711
Tags:  video-captioning ⟨36⟩ dense-video-captioning ⟨37⟩ audio-visual ⟨38⟩
Libraries:  Datasets ⟨39⟩
Croissant
 Dataset card ⟨31⟩ Data Studio ⟨40⟩ Files Files and versions xet ⟨41⟩ Community 1 ⟨42⟩
Dataset Viewer
 Auto-converted to Parquet⟨43⟩ API Embed  Duplicate⟨44⟩ Data Studio
Subset (1)
default · 42.1k rows
default (42.1k rows)
Split (1)
train · 42.1k rows
train (42.1k rows)
Search is not available for this dataset
SQL
Console
The dataset viewer is not available for this split.
Server error while post-processing the rows. Please report the issue.

```
Error code:   RowsPostProcessingError

```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨45⟩, and open a discussion⟨46⟩ for direct support.
  * 🌟 Overview⟨47⟩
  * 💻 Quick Start⟨48⟩
    * Installation⟨49⟩
    * Usage⟨50⟩
  * 📖 Citation⟨51⟩


#   ⟨52⟩ TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions 
![Paper](https://img.shields.io/badge/arXiv-2602.08711-b31b1b)⟨53⟩ ![Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)⟨54⟩ ![Dataset](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green)⟨55⟩ ![Benchmark](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Benchmark-yellow)⟨56⟩ ![GitHub](https://img.shields.io/badge/GitHub-Code-black)⟨57⟩
* * *
##   ⟨47⟩ 🌟 Overview 
**TimeChat-Captioner** is a multimodal model designed to generate detailed, time-aware, and structurally coherent captions for multi-scene videos. It effectively coordinates visual and audio information to provide comprehensive video descriptions.
  * **🌐 Project Page:** timechat-captioner.github.io⟨58⟩
  * **🏠 Model:** TimeChat-Captioner (7B)⟨54⟩
  * **📚 Train Dataset:** TimeChatCap-42K⟨28⟩
  * **🏆 Benchmark:** OmniDCBench⟨56⟩

![image⟨59⟩]
* * *
##   ⟨48⟩ 💻 Quick Start 
Below, we provide simple examples to show how to use TimeChat-Captioner-GRPO-7B with 🤗 Transformers.
###   ⟨49⟩ Installation 

```
conda create -n timechatcap python=3.12
conda activate timechatcap
pip install torch torchvision
pip install transformers==4.57.1
pip install accelerate
pip install flash-attn --no-build-isolation
# It's highly recommended to use `[decord]` feature for faster video loading.
pip install qwen-omni-utils[decord] -U

```

###   ⟨50⟩ Usage 
> **Note:** To annotate high-quality timestamps and captions, limit video input to around 1 minute. Please segment longer videos into around 60-second clips before processing.

```
import torch
from transformers import Qwen2_5OmniForConditionalGeneration, Qwen2_5OmniProcessor
from qwen_omni_utils import process_mm_info

# 1. Configuration
MODEL_ID = "yaolily/TimeChat-Captioner-GRPO-7B"
VIDEO_PATH = "example_video.mp4"  # <--- Replace with your video path

MAX_PIXELS = 297920
VIDEO_MAX_PIXELS = 297920


print(f"🚀 Processing video: {VIDEO_PATH}")

# 2. Load Model & Processor
print("⏳ Loading model...")
model = Qwen2_5OmniForConditionalGeneration.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
    device_map="cuda",
    attn_implementation="flash_attention_2"
)
processor = Qwen2_5OmniProcessor.from_pretrained(MODEL_ID)
model.disable_talker()

# 3. Construct Conversation
# The prompt encourages detailed, time-aware audio-visual description.
conversation = [
    {
        "role": "user",
        "content": [
            {
                "type": "text", 
                "text": "Thoroughly describe everything in the video, capturing every detail. Include as much information from the audio as possible, and ensure that the descriptions of both audio and video are well-coordinated."
            },
            {
                "type": "video", 
                "video": VIDEO_PATH, 
                "max_pixels": MAX_PIXELS, 
                "max_frames": 160, 
                "fps": 2.0,
                "video_max_pixels": VIDEO_MAX_PIXELS
            }
        ],
    },
]

# 4. Process Inputs
print("⚙️  Processing inputs...")
text = processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)

audios, images, videos = process_mm_info(conversation, use_audio_in_video=True)

inputs = processor(
    text=text, 
    audio=audios, 
    images=images, 
    videos=videos, 
    return_tensors="pt", 
    padding=True, 
    use_audio_in_video=True
)
inputs = inputs.to(model.device).to(model.dtype)

# 5. Generate Description
print("✨ Generating description...")
with torch.inference_mode():
    text_ids = model.generate(
        **inputs, 
        use_audio_in_video=True, 
        return_audio=False,
        thinker_max_new_tokens=9216,
        talker_max_tokens=9216
    )

response = processor.decode(text_ids[0][inputs.input_ids[0].size(0):], skip_special_tokens=True)

print("
" + "="*50)
print("🎬 VIDEO DESCRIPTION:")
print("="*50)
print(response)
print("="*50)

```

* * *
##   ⟨51⟩ 📖 Citation 

```
@misc{yao2026timechatcaptioner,
      title={TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions}, 
      author={Linli Yao and Yuancheng Wei and Yaojie Zhang and Lei Li and Xinlong Chen and Feifan Song and Ziyue Wang and Kun Ouyang and Yuanxin Liu and Lingpeng Kong and Qi Liu and Pengfei Wan and Kun Gai and Yuanxing Zhang and Xu Sun},
      year={2026},
      eprint={2602.08711},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2602.08711}
}

```

Copy to bucket new
Use this dataset 

Downloads last month
    309
Number of rows: 42,057 Total file size: 682 GB
##  Paper for AdamAlKhalifa/Timechat-OmniCaptioner-42K
#### TimeChat-Captioner: Scripting Multi-Scene Videos with Time-Aware and Structural Audio-Visual Captions Paper • 2602.08711 • Published Feb 9 • 29 ⟨60⟩
System theme
Company
TOS⟨61⟩ Privacy⟨62⟩ About⟨63⟩ Careers⟨64⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
