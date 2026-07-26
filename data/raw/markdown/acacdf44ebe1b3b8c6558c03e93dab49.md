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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6a4a6b50f08e524d047b0383/HUMhK2QTn78ryZOdbm0hN.webp) ⟨28⟩
PhysInOneP13⟨28⟩
/
PhysInOneP13⟨29⟩
like 1
Tasks:  Text-to-Video ⟨30⟩ Image-to-Video ⟨31⟩ Video-to-Video ⟨32⟩ + 4
Modalities:  Video ⟨33⟩ 3D ⟨34⟩
Languages:  English ⟨35⟩
Size:  10K<n<100K ⟨36⟩
ArXiv:
arxiv: 2604.09415
Tags:  video ⟨37⟩ 3d ⟨38⟩ synthetic-data ⟨39⟩ physical-reasoning ⟨40⟩ visual-physics ⟨41⟩ world-model ⟨42⟩ + 14
License:
cc-by-nc-sa-4.0
 Dataset card ⟨29⟩ Files Files and versions xet ⟨43⟩ Community ⟨44⟩
Dataset Viewer
The dataset viewer is not available because its heuristics could not detect any supported data files⟨45⟩. You can try uploading⟨46⟩ some data files, or configuring⟨47⟩ the data files location manually.
# PhysInOne: Visual Physics Learning and Reasoning in One Suite
vLAR Group | The Hong Kong Polytechnic University | Syai Singapore | Meta 
**CVPR 2026**
 ![](https://img.shields.io/badge/Project-Page-purple) ⟨48⟩  ![](https://img.shields.io/badge/Paper-ArXiv-red) ⟨49⟩  ![](https://img.shields.io/badge/Code-GitHub-black) ⟨50⟩  ![](https://img.shields.io/badge/Dataset-HuggingFace-yellow) ⟨51⟩
**📦 Shard Repository: PhysInOneP13 (13/15)**  
This repository is one shard of **PhysInOne: Visual Physics Learning and Reasoning in One Suite**. It stores only a subset of the released data files. For the full dataset description, download scripts, annotation details, data split information, physical phenomenon definitions, and latest release progress, please refer to the **main dataset repository**⟨51⟩.
## About PhysInOne
**PhysInOne** contains **153,810 dynamic 3D scenes** and **2 million annotated videos** , covering **71 basic physical phenomena** across four domains of everyday physics: **mechanics** , **optics** , **fluid dynamics** , and **magnetism**.
Each scene may contain multi-object and multi-physics interactions in complex 3D environments. The dataset provides rich annotations including RGB videos, depth maps, object masks, 3D trajectories, camera poses, object meshes, material properties, and textual descriptions.
## Shard Repositories
Due to the large scale of PhysInOne, the rendered data and annotations are split across multiple Hugging Face repositories. Below is the list:
> **Current shard:** **PhysInOneP13**. The **← You are here** marker indicates the repository you are currently viewing.
  * PhysInOneP01: <https://huggingface.co/datasets/PhysInOneP01/PhysInOneP01>
  * PhysInOneP02: <https://huggingface.co/datasets/PhysInOneP02/PhysInOneP02>
  * PhysInOneP03: <https://huggingface.co/datasets/PhysInOneP03/PhysInOneP03>
  * PhysInOneP04: <https://huggingface.co/datasets/PhysInOneP04/PhysInOneP04>
  * PhysInOneP05: <https://huggingface.co/datasets/PhysInOneP05/PhysInOneP05>
  * PhysInOneP06: <https://huggingface.co/datasets/PhysInOneP06/PhysInOneP06>
  * PhysInOneP07: <https://huggingface.co/datasets/PhysInOneP07/PhysInOneP07>
  * PhysInOneP08: <https://huggingface.co/datasets/PhysInOneP08/PhysInOneP08>
  * PhysInOneP09: <https://huggingface.co/datasets/PhysInOneP09/PhysInOneP09>
  * PhysInOneP10: <https://huggingface.co/datasets/PhysInOneP10/PhysInOneP10>
  * PhysInOneP11: <https://huggingface.co/datasets/PhysInOneP11/PhysInOneP11>
  * PhysInOneP12: <https://huggingface.co/datasets/PhysInOneP12/PhysInOneP12>
  * **PhysInOneP13** : <https://huggingface.co/datasets/PhysInOneP13/PhysInOneP13> **← You are here**
  * PhysInOneP14: <https://huggingface.co/datasets/PhysInOneP14/PhysInOneP14>
  * PhysInOneP15: <https://huggingface.co/datasets/PhysInOneP15/PhysInOneP15>


## How to Download
We recommend downloading PhysInOne through the official scripts provided in the main repository. The scripts support filtering by split, activity complexity, physical phenomenon, and number of cases.
Please see the **How to Download**⟨52⟩ section in the main repository for details.
This shard can also be accessed directly through Hugging Face, but direct manual download is recommended only for inspecting a small number of files.
## License
All 3D assets and materials included in PhysInOne have been sourced from publicly available platforms and verified to carry licenses compatible with non-commercial use. These include:
  * SketchFab: assets under various licenses, verified that AI-related usage is allowed.
  * Fab: assets under CC BY or Unreal Engine Standard License, explicitly permitting AI-related usage.
  * BlenderKit: distributed under Royalty-Free (RF) license.
  * ShareTextures: textures under CC0 license.


In total, assets comply with licenses including CC BY-NC, CC BY-SA, CC BY-NC-SA, CC0, CC BY, and RF, ensuring all files can be legally used for building a non-commercial dataset. Users must adhere to the original licenses for any redistribution or derivative work.
## Contact
For questions about the dataset, please refer to the main repository or contact the PhysInOne team.
Copy to bucket new 

Downloads last month
    15,000
Total file size: 6.62 TB
##  Paper for PhysInOneP13/PhysInOneP13
#### PhysInOne: Visual Physics Learning and Reasoning in One Suite Paper • 2604.09415 • Published Apr 10 • 1 ⟨53⟩
System theme
Company
TOS⟨54⟩ Privacy⟨55⟩ About⟨56⟩ Careers⟨57⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
