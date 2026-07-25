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
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/6a4c9d2e4a3d561dc83676f6/aVBzRkcixaQQHaq-UKZcH.png) ⟨28⟩
Datoric⟨28⟩
/
robot-teleoperation-2000-episodes⟨29⟩
like 0
Follow
![⟨30⟩] Datoric 1
Tasks:  Robotics ⟨31⟩ Reinforcement Learning ⟨32⟩
Modalities:  Tabular ⟨33⟩ Text ⟨34⟩
Formats:  parquet ⟨35⟩
Size:  100K - 1M ⟨36⟩
Tags:  teleoperation ⟨37⟩ imitation-learning ⟨38⟩ visuomotor-policies ⟨39⟩ manipulation ⟨40⟩ robot-episodes ⟨41⟩ physical-ai ⟨42⟩ + 2
Libraries:  Datasets ⟨43⟩ pandas ⟨44⟩ Polars ⟨45⟩ + 1
License:
datoric-commercial
 Dataset card ⟨29⟩ Data Studio ⟨46⟩ Files Files and versions xet ⟨47⟩ Community ⟨48⟩
##  Request sample access
This repository is publicly accessible, but you have to accept the conditions to access its files and content.
This repository contains the dataset specification, annotation schema, and sample metadata files. The production dataset (2,000 robot manipulation episodes with multi-camera video, robot states, and action trajectories) is rights-cleared and delivered directly under a commercial license. Approved requesters get the full episode schema and data dictionary in this repository, and can request a review package with real episodes and QA summaries. Requests are reviewed within 1 business day.
Log in⟨49⟩ or Sign Up⟨50⟩ to review the conditions and access this dataset content.
  * Overview⟨51⟩
  * At a glance⟨52⟩
  * Task coverage⟨53⟩
  * Technical specifications⟨54⟩
  * Episode schema⟨55⟩
  * How to evaluate this dataset⟨56⟩
  * Licensing⟨57⟩
  * About Datoric⟨58⟩


#   ⟨59⟩ Robot Teleoperation Dataset 
**2,000 robot manipulation episodes with multi-camera video, robot joint states, gripper states, action trajectories, object labels, task phases, and success/failure outcomes for imitation learning and Physical AI.**
> This repository contains the full technical specification, annotation schema, and sample metadata files (Parquet). The production dataset is delivered directly to buyers. Request access⟨56⟩ to see the full schema and get real episode samples.
##   ⟨51⟩ Overview 
The Robot Teleoperation Dataset is a focused collection of 2,000 robot manipulation episodes for robot learning, imitation learning, visuomotor policy training, embodied AI, and Physical AI. Each episode captures a robot performing a physical task while recording perception data, robot state, and action trajectories, making the dataset directly useful for training and evaluating models that map visual observations and robot states into physical actions.
##   ⟨52⟩ At a glance   
|   |   |  
| --- | --- |  
| Episodes  | 2,000  |  
| Estimated activity  | ~100 to 250 hours depending on episode length  |  
| Perception  | Multi-camera video + wrist-camera video  |  
| Robot state  | Joint positions, end-effector pose, gripper open/close state  |  
| Actions  | Action commands and trajectories with timestamps  |  
| Outcomes  | Success/failure labels, retry/recovery events  |  
| Higher-fidelity subsets  | Depth, force, tactile, or other sensor streams where available  |  
##   ⟨53⟩ Task coverage 
Pick-and-place, bin loading and unloading, drawer opening and closing, object sorting, wiping, folding, shelf stocking, simple assembly, tool use, and household manipulation.
##   ⟨54⟩ Technical specifications 
  * **Per-episode data:** multi-camera video, wrist-camera video, robot joint position logs, end-effector pose, gripper open/close state, action commands, timestamps, object labels, task phase labels, success/failure outcomes, trajectory metadata
  * **Annotation coverage:** task type, object labels, task phase, success/failure, retry/recovery events, trajectory metadata
  * **Buyer evaluation metrics:** episode success rate, action frequency, robot state frequency, camera frame rate, calibration quality, failure labels, trajectory completeness
  * **QA metrics:** synchronized timestamps, missing-frame detection, action-log completeness, failed episode labeling, human review
  * **Delivery format:** MP4 video, robot state logs, action trajectory files, CSV metadata, JSON annotations


Failed episodes are labeled rather than discarded; failure and recovery data is often as valuable as clean successes for policy robustness.
##   ⟨55⟩ Episode schema 
The gated file `annotation_schema.json` in this repository contains the full episode schema with an illustrative example record, including state/action stream descriptors at their native frequencies and outcome labels.
The `samples/` folder holds sample metadata in Parquet format: `index_sample.parquet` (item-level) and `trajectory_sample.parquet` (event-level), both conforming to this schema. Values are generated to illustrate structure and field distributions; production records ship in buyer review packages.
##   ⟨56⟩ How to evaluate this dataset 
  1. **Request access** using the form above. Requests are reviewed within 1 business day.
  2. On approval you get the gated files in this repository: full episode schema, sample metadata Parquet files, data dictionary, and access instructions.
  3. **Request a review package** and we deliver real episodes (video, state logs, action trajectories), QA summaries, and licensing documentation within 2 business days.


All samples are delivered with structured CSV metadata and JSON annotation files where available. Buyer review packages include representative media files, metadata samples, annotation schema, QA summaries, and data dictionary documentation.
##   ⟨57⟩ Licensing 
The production dataset is licensed for commercial AI training directly by Datoric with full chain-of-custody documentation. Subset, exclusive, and custom-collection options (specific tasks, platforms, or embodiments) are available.
##   ⟨58⟩ About Datoric 
Datoric supplies rights-cleared, spec-exact training data for frontier AI labs and enterprise model teams: robot episodes, human manipulation data, egocentric and industrial video, expressive multilingual voice, computer-use traces, and gameplay trajectories. We also run managed collection pipelines for custom specifications.
**Contact:** nikhil@arzule.com
Copy to bucket new 

Downloads last month
    13
Total file size: 9.89 MB
System theme
Company
TOS⟨60⟩ Privacy⟨61⟩ About⟨62⟩ Careers⟨63⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
