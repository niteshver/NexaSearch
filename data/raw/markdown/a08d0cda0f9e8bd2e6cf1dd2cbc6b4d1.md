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
Duplicated from Trupal7/Sisfall_Dataset⟨28⟩
![⟨29⟩]
 ![](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/4WkRWSnkcn1Z1rNQ_ei0j.png) ⟨30⟩
Algo-rythmic⟨30⟩
/
Sisfall_Dataset⟨31⟩
like 0
 Dataset card ⟨31⟩ Files Files and versions xet ⟨32⟩ Community ⟨33⟩
Dataset Viewer
API Embed  Duplicate⟨34⟩ Data Studio
Subset (1)
default
default
Split (1)
train
train
The dataset viewer is not available for this split.
Cannot extract the features (columns) for the split 'train' of the config 'default' of the dataset.

```
Error code:   FeaturesError
Exception:    UnicodeDecodeError
Message:      'utf-8' codec can't decode byte 0xb5 in position 12: invalid start byte
Traceback:    Traceback (most recent call last):
                File "/src/services/worker/src/worker/job_runners/split/first_rows.py", line 243, in compute_first_rows_from_streaming_response
                  iterable_dataset = iterable_dataset._resolve_features()
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 4379, in _resolve_features
                  features = _infer_features_from_batch(self.with_format(None)._head())
                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2661, in _head
                  return next(iter(self.iter(batch_size=n)))
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2839, in iter
                  for key, pa_table in ex_iterable.iter_arrow():
                                       ~~~~~~~~~~~~~~~~~~~~~~^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 2377, in _iter_arrow
                  yield from self.ex_iterable._iter_arrow()
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 536, in _iter_arrow
                  for key, pa_table in iterator:
                                       ^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 419, in _iter_arrow
                  for key, pa_table in self.generate_tables_fn(**gen_kwags):
                                       ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/packaged_modules/text/text.py", line 98, in _generate_tables
                  batch = f.read(self.config.chunksize)
                File "/usr/local/lib/python3.14/site-packages/datasets/utils/file_utils.py", line 844, in read_with_retries
                  out = read(*args, **kwargs)
                File "<frozen codecs>", line 325, in decode
              UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 12: invalid start byte
```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨35⟩, and open a discussion⟨36⟩ for direct support.
**YAML Metadata Warning:** empty or missing yaml metadata in repo card
Check out the documentation⟨37⟩ for more information.
  * Context & Purpose⟨38⟩
  * Data Provenance & Citation⟨39⟩
  * Ethical & Safety Notice (SOTIF)⟨40⟩
  * license: cc-by-4.0⟨41⟩


#   ⟨42⟩ SisFall: A Fall and Movement Dataset (Hugging Face Mirror) 
##   ⟨38⟩ Context & Purpose 
This repository serves as a reliable, programmatically accessible mirror of the SisFall dataset for the global Human Activity Recognition (HAR) and Machine Learning community. It allows researchers and engineers to easily hydrate their environments via the Hugging Face API, ensuring complete code reproducibility in open-science workflows without the need for manual zip file transfers or relying on unstable institutional servers.
##   ⟨39⟩ Data Provenance & Citation 
The original data is the **SisFall: A Fall and Movement Dataset**. It is legally re-hosted here under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license to facilitate open-source machine learning pipelines. All credit for the rigorous data collection, hardware engineering, and initial validation belongs strictly to the original authors.
  * **Original Paper:** Sucerquia, A., López, J. D., & Vargas-Bonilla, J. F. (2017). _SisFall: A Fall and Movement Dataset_. Sensors, 17(1), 198. 
  * **DOI:** <https://doi.org/10.3390/s17010198>


##   ⟨40⟩ Ethical & Safety Notice (SOTIF) 
**Ethical Deployment Warning:** While SisFall is an excellent foundational dataset for baseline Human Activity Recognition (HAR), researchers should be acutely aware of critical demographic imbalances before using this data to train models for safety-critical, edge-native wearable devices. 
Specifically, the elderly cohort (subjects SE01-SE15) contains severe class imbalances regarding hard impacts and falls. Evaluating or training models without rigorously addressing this covariate shift may lead to dangerously uncalibrated confidence scores and Out-of-Distribution (OOD) failures when deployed on frail populations. Researchers are highly encouraged to evaluate models trained on this data through a strict Safety of the Intended Functionality (SOTIF / ISO 21448) framework.
* * *
##   ⟨41⟩ license: cc-by-4.0 
Copy to bucket new 

Downloads last month
    56
Total file size: 232 MB
System theme
Company
TOS⟨43⟩ Privacy⟨44⟩ About⟨45⟩ Careers⟨46⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
