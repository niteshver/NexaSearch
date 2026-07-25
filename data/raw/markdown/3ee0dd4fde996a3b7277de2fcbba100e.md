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
 ![](https://huggingface.co/avatars/cf8955cdad31c5b4f839586e63cbdc2d.svg) ⟨28⟩
Godlydonuts⟨28⟩
/
shohin⟨29⟩
like 0
Tasks:  Text Generation ⟨30⟩
Languages:  English ⟨31⟩
Tags:  reasoning ⟨32⟩ math ⟨33⟩ code ⟨34⟩ shohin ⟨35⟩
License:
cc-by-4.0
 Dataset card ⟨29⟩ Data Studio ⟨36⟩ Files Files and versions xet ⟨37⟩ Community ⟨38⟩
Dataset Preview
API Embed  Duplicate⟨39⟩ Data Studio
Subset (1)
default
default
Split (2)
train
train test
The full dataset viewer is not available (click to read why). Only showing a preview of the rows.
The dataset generation failed

```
Error code:   DatasetGenerationError
Exception:    CastError
Message:      Couldn't cast
family: string
split: string
difficulty: struct<num_terms: list<item: int64>, num_digits: list<item: int64>, decimal_places: list<item: int64 (... 2 chars omitted)
  child 0, num_terms: list<item: int64>
      child 0, item: int64
  child 1, num_digits: list<item: int64>
      child 0, item: int64
  child 2, decimal_places: list<item: int64>
      child 0, item: int64
question: string
answer: string
document: string
trace: string
to
{'family': Value('string'), 'question': Value('string'), 'trace': Value('string'), 'answer': Value('string'), 'document': Value('string')}
because column names don't match
Traceback:    Traceback (most recent call last):
                File "/usr/local/lib/python3.14/site-packages/datasets/builder.py", line 1816, in _prepare_split_single
                  for key, table in generator:
                                    ^^^^^^^^^
                File "/src/services/worker/src/worker/job_runners/config/parquet_and_info.py", line 613, in wrapped
                  for item in generator(*args, **kwargs):
                              ~~~~~~~~~^^^^^^^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/packaged_modules/json/json.py", line 343, in _generate_tables
                  self._cast_table(pa_table, json_field_paths=json_field_paths),
                  ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/packaged_modules/json/json.py", line 132, in _cast_table
                  pa_table = table_cast(pa_table, self.info.features.arrow_schema)
                File "/usr/local/lib/python3.14/site-packages/datasets/table.py", line 2369, in table_cast
                  return cast_table_to_schema(table, schema)
                File "/usr/local/lib/python3.14/site-packages/datasets/table.py", line 2297, in cast_table_to_schema
                  raise CastError(
                  ...<3 lines>...
                  )
              datasets.table.CastError: Couldn't cast
              family: string
              split: string
              difficulty: struct<num_terms: list<item: int64>, num_digits: list<item: int64>, decimal_places: list<item: int64 (... 2 chars omitted)
                child 0, num_terms: list<item: int64>
                    child 0, item: int64
                child 1, num_digits: list<item: int64>
                    child 0, item: int64
                child 2, decimal_places: list<item: int64>
                    child 0, item: int64
              question: string
              answer: string
              document: string
              trace: string
              to
              {'family': Value('string'), 'question': Value('string'), 'trace': Value('string'), 'answer': Value('string'), 'document': Value('string')}
              because column names don't match
              
              The above exception was the direct cause of the following exception:
              
              Traceback (most recent call last):
                File "/src/services/worker/src/worker/job_runners/config/parquet_and_info.py", line 1369, in compute_config_parquet_and_info_response
                  parquet_operations, partial, estimated_dataset_info = stream_convert_to_parquet(
                                                                        ~~~~~~~~~~~~~~~~~~~~~~~~~^
                      builder, max_dataset_size_bytes=max_dataset_size_bytes
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  )
                  ^
                File "/src/services/worker/src/worker/job_runners/config/parquet_and_info.py", line 948, in stream_convert_to_parquet
                  builder._prepare_split(split_generator=splits_generators[split], file_format="parquet")
                  ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                File "/usr/local/lib/python3.14/site-packages/datasets/builder.py", line 1683, in _prepare_split
                  for job_id, done, content in self._prepare_split_single(
                                               ~~~~~~~~~~~~~~~~~~~~~~~~~~^
                      gen_kwargs=gen_kwargs, job_id=job_id, **_prepare_split_args
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  ):
                  ^
                File "/usr/local/lib/python3.14/site-packages/datasets/builder.py", line 1869, in _prepare_split_single
                  raise DatasetGenerationError("An error occurred while generating the dataset") from e
              datasets.exceptions.DatasetGenerationError: An error occurred while generating the dataset
```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨40⟩, and open a discussion⟨41⟩ for direct support.  
|  family string  |  question string  |  trace string  |  answer string  |  document string  |  
| --- | --- | --- | --- | --- |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8453 - 3863 - 7439 =  |  8453 - 3863 = 4590 ; 4590 - 7439 = -2849  |  -2849  |  State the final answer to the following arithmetic problem: 8453 - 3863 - 7439 = <think>8453 - 3863 = 4590 ; 4590 - 7439 = -2849</think> <answer>-2849</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 79 + 55 + 69 - 16 - 94 + 74 =  |  79 + 55 = 134 ; 134 + 69 = 203 ; 203 - 16 = 187 ; 187 - 94 = 93 ; 93 + 74 = 167  |  167  |  State the final answer to the following arithmetic problem: 79 + 55 + 69 - 16 - 94 + 74 = <think>79 + 55 = 134 ; 134 + 69 = 203 ; 203 - 16 = 187 ; 187 - 94 = 93 ; 93 + 74 = 167</think> <answer>167</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 273 + 667 - 829 =  |  273 + 667 = 940 ; 940 - 829 = 111  |  111  |  State the final answer to the following arithmetic problem: 273 + 667 - 829 = <think>273 + 667 = 940 ; 940 - 829 = 111</think> <answer>111</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 98 - 19 - 87 - 25 + 93 =  |  98 - 19 = 79 ; 79 - 87 = -8 ; -8 - 25 = -33 ; -33 + 93 = 60  |  60  |  State the final answer to the following arithmetic problem: 98 - 19 - 87 - 25 + 93 = <think>98 - 19 = 79 ; 79 - 87 = -8 ; -8 - 25 = -33 ; -33 + 93 = 60</think> <answer>60</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 39 - 60 =  |  39 - 60 = -21  |  -21  |  State the final answer to the following arithmetic problem: 39 - 60 = <think>39 - 60 = -21</think> <answer>-21</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 694 - 909 - 211 + 102 - 419 + 636 =  |  694 - 909 = -215 ; -215 - 211 = -426 ; -426 + 102 = -324 ; -324 - 419 = -743 ; -743 + 636 = -107  |  -107  |  State the final answer to the following arithmetic problem: 694 - 909 - 211 + 102 - 419 + 636 = <think>694 - 909 = -215 ; -215 - 211 = -426 ; -426 + 102 = -324 ; -324 - 419 = -743 ; -743 + 636 = -107</think> <answer>-107</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8 + 8 + 7 - 0 - 4 =  |  8 + 8 = 16 ; 16 + 7 = 23 ; 23 - 0 = 23 ; 23 - 4 = 19  |  19  |  State the final answer to the following arithmetic problem: 8 + 8 + 7 - 0 - 4 = <think>8 + 8 = 16 ; 16 + 7 = 23 ; 23 - 0 = 23 ; 23 - 4 = 19</think> <answer>19</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8905 - 6062 + 3257 =  |  8905 - 6062 = 2843 ; 2843 + 3257 = 6100  |  6100  |  State the final answer to the following arithmetic problem: 8905 - 6062 + 3257 = <think>8905 - 6062 = 2843 ; 2843 + 3257 = 6100</think> <answer>6100</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 6 + 4 + 6 =  |  6 + 4 = 10 ; 10 + 6 = 16  |  16  |  State the final answer to the following arithmetic problem: 6 + 4 + 6 = <think>6 + 4 = 10 ; 10 + 6 = 16</think> <answer>16</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 68 + 67 + 80 - 17 =  |  68 + 67 = 135 ; 135 + 80 = 215 ; 215 - 17 = 198  |  198  |  State the final answer to the following arithmetic problem: 68 + 67 + 80 - 17 = <think>68 + 67 = 135 ; 135 + 80 = 215 ; 215 - 17 = 198</think> <answer>198</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 62 + 71 - 45 - 91 + 79 =  |  62 + 71 = 133 ; 133 - 45 = 88 ; 88 - 91 = -3 ; -3 + 79 = 76  |  76  |  State the final answer to the following arithmetic problem: 62 + 71 - 45 - 91 + 79 = <think>62 + 71 = 133 ; 133 - 45 = 88 ; 88 - 91 = -3 ; -3 + 79 = 76</think> <answer>76</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 605 - 298 + 507 =  |  605 - 298 = 307 ; 307 + 507 = 814  |  814  |  State the final answer to the following arithmetic problem: 605 - 298 + 507 = <think>605 - 298 = 307 ; 307 + 507 = 814</think> <answer>814</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 816 + 576 - 531 + 869 - 779 =  |  816 + 576 = 1392 ; 1392 - 531 = 861 ; 861 + 869 = 1730 ; 1730 - 779 = 951  |  951  |  State the final answer to the following arithmetic problem: 816 + 576 - 531 + 869 - 779 = <think>816 + 576 = 1392 ; 1392 - 531 = 861 ; 861 + 869 = 1730 ; 1730 - 779 = 951</think> <answer>951</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 118 - 589 =  |  118 - 589 = -471  |  -471  |  State the final answer to the following arithmetic problem: 118 - 589 = <think>118 - 589 = -471</think> <answer>-471</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 5 + 3 + 9 =  |  5 + 3 = 8 ; 8 + 9 = 17  |  17  |  State the final answer to the following arithmetic problem: 5 + 3 + 9 = <think>5 + 3 = 8 ; 8 + 9 = 17</think> <answer>17</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 24 - 78 - 24 - 52 =  |  24 - 78 = -54 ; -54 - 24 = -78 ; -78 - 52 = -130  |  -130  |  State the final answer to the following arithmetic problem: 24 - 78 - 24 - 52 = <think>24 - 78 = -54 ; -54 - 24 = -78 ; -78 - 52 = -130</think> <answer>-130</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 108 - 870 - 761 + 223 - 855 - 235 =  |  108 - 870 = -762 ; -762 - 761 = -1523 ; -1523 + 223 = -1300 ; -1300 - 855 = -2155 ; -2155 - 235 = -2390  |  -2390  |  State the final answer to the following arithmetic problem: 108 - 870 - 761 + 223 - 855 - 235 = <think>108 - 870 = -762 ; -762 - 761 = -1523 ; -1523 + 223 = -1300 ; -1300 - 855 = -2155 ; -2155 - 235 = -2390</think> <answer>-2390</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 31 + 36 - 61 =  |  31 + 36 = 67 ; 67 - 61 = 6  |  6  |  State the final answer to the following arithmetic problem: 31 + 36 - 61 = <think>31 + 36 = 67 ; 67 - 61 = 6</think> <answer>6</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 201 - 819 + 470 =  |  201 - 819 = -618 ; -618 + 470 = -148  |  -148  |  State the final answer to the following arithmetic problem: 201 - 819 + 470 = <think>201 - 819 = -618 ; -618 + 470 = -148</think> <answer>-148</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 78 + 95 + 80 - 65 =  |  78 + 95 = 173 ; 173 + 80 = 253 ; 253 - 65 = 188  |  188  |  State the final answer to the following arithmetic problem: 78 + 95 + 80 - 65 = <think>78 + 95 = 173 ; 173 + 80 = 253 ; 253 - 65 = 188</think> <answer>188</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 34 - 91 + 85 + 95 - 69 - 21 =  |  34 - 91 = -57 ; -57 + 85 = 28 ; 28 + 95 = 123 ; 123 - 69 = 54 ; 54 - 21 = 33  |  33  |  State the final answer to the following arithmetic problem: 34 - 91 + 85 + 95 - 69 - 21 = <think>34 - 91 = -57 ; -57 + 85 = 28 ; 28 + 95 = 123 ; 123 - 69 = 54 ; 54 - 21 = 33</think> <answer>33</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 84 + 60 =  |  84 + 60 = 144  |  144  |  State the final answer to the following arithmetic problem: 84 + 60 = <think>84 + 60 = 144</think> <answer>144</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 86 + 48 + 19 - 56 - 38 + 68 =  |  86 + 48 = 134 ; 134 + 19 = 153 ; 153 - 56 = 97 ; 97 - 38 = 59 ; 59 + 68 = 127  |  127  |  State the final answer to the following arithmetic problem: 86 + 48 + 19 - 56 - 38 + 68 = <think>86 + 48 = 134 ; 134 + 19 = 153 ; 153 - 56 = 97 ; 97 - 38 = 59 ; 59 + 68 = 127</think> <answer>127</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 189 - 887 =  |  189 - 887 = -698  |  -698  |  State the final answer to the following arithmetic problem: 189 - 887 = <think>189 - 887 = -698</think> <answer>-698</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 2 - 0 + 6 - 4 =  |  2 - 0 = 2 ; 2 + 6 = 8 ; 8 - 4 = 4  |  4  |  State the final answer to the following arithmetic problem: 2 - 0 + 6 - 4 = <think>2 - 0 = 2 ; 2 + 6 = 8 ; 8 - 4 = 4</think> <answer>4</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 86 + 48 - 82 =  |  86 + 48 = 134 ; 134 - 82 = 52  |  52  |  State the final answer to the following arithmetic problem: 86 + 48 - 82 = <think>86 + 48 = 134 ; 134 - 82 = 52</think> <answer>52</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9 - 9 + 7 + 3 + 2 - 7 =  |  9 - 9 = 0 ; 0 + 7 = 7 ; 7 + 3 = 10 ; 10 + 2 = 12 ; 12 - 7 = 5  |  5  |  State the final answer to the following arithmetic problem: 9 - 9 + 7 + 3 + 2 - 7 = <think>9 - 9 = 0 ; 0 + 7 = 7 ; 7 + 3 = 10 ; 10 + 2 = 12 ; 12 - 7 = 5</think> <answer>5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 - 0 =  |  0 - 0 = 0  |  0  |  State the final answer to the following arithmetic problem: 0 - 0 = <think>0 - 0 = 0</think> <answer>0</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9380 - 6963 + 3196 =  |  9380 - 6963 = 2417 ; 2417 + 3196 = 5613  |  5613  |  State the final answer to the following arithmetic problem: 9380 - 6963 + 3196 = <think>9380 - 6963 = 2417 ; 2417 + 3196 = 5613</think> <answer>5613</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 147 + 811 + 508 + 746 + 330 - 437 =  |  147 + 811 = 958 ; 958 + 508 = 1466 ; 1466 + 746 = 2212 ; 2212 + 330 = 2542 ; 2542 - 437 = 2105  |  2105  |  State the final answer to the following arithmetic problem: 147 + 811 + 508 + 746 + 330 - 437 = <think>147 + 811 = 958 ; 958 + 508 = 1466 ; 1466 + 746 = 2212 ; 2212 + 330 = 2542 ; 2542 - 437 = 2105</think> <answer>2105</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 5478 - 8211 + 8518 - 1359 + 6871 + 4932 =  |  5478 - 8211 = -2733 ; -2733 + 8518 = 5785 ; 5785 - 1359 = 4426 ; 4426 + 6871 = 11297 ; 11297 + 4932 = 16229  |  16229  |  State the final answer to the following arithmetic problem: 5478 - 8211 + 8518 - 1359 + 6871 + 4932 = <think>5478 - 8211 = -2733 ; -2733 + 8518 = 5785 ; 5785 - 1359 = 4426 ; 4426 + 6871 = 11297 ; 11297 + 4932 = 16229</think> <answer>16229</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 888 - 620 + 189 - 502 =  |  888 - 620 = 268 ; 268 + 189 = 457 ; 457 - 502 = -45  |  -45  |  State the final answer to the following arithmetic problem: 888 - 620 + 189 - 502 = <think>888 - 620 = 268 ; 268 + 189 = 457 ; 457 - 502 = -45</think> <answer>-45</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 62 + 17 + 31 + 15 - 49 =  |  62 + 17 = 79 ; 79 + 31 = 110 ; 110 + 15 = 125 ; 125 - 49 = 76  |  76  |  State the final answer to the following arithmetic problem: 62 + 17 + 31 + 15 - 49 = <think>62 + 17 = 79 ; 79 + 31 = 110 ; 110 + 15 = 125 ; 125 - 49 = 76</think> <answer>76</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 593 - 430 + 887 + 730 - 927 =  |  593 - 430 = 163 ; 163 + 887 = 1050 ; 1050 + 730 = 1780 ; 1780 - 927 = 853  |  853  |  State the final answer to the following arithmetic problem: 593 - 430 + 887 + 730 - 927 = <think>593 - 430 = 163 ; 163 + 887 = 1050 ; 1050 + 730 = 1780 ; 1780 - 927 = 853</think> <answer>853</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 81 - 91 + 26 - 13 + 93 =  |  81 - 91 = -10 ; -10 + 26 = 16 ; 16 - 13 = 3 ; 3 + 93 = 96  |  96  |  State the final answer to the following arithmetic problem: 81 - 91 + 26 - 13 + 93 = <think>81 - 91 = -10 ; -10 + 26 = 16 ; 16 - 13 = 3 ; 3 + 93 = 96</think> <answer>96</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 599 + 400 - 940 - 822 =  |  599 + 400 = 999 ; 999 - 940 = 59 ; 59 - 822 = -763  |  -763  |  State the final answer to the following arithmetic problem: 599 + 400 - 940 - 822 = <think>599 + 400 = 999 ; 999 - 940 = 59 ; 59 - 822 = -763</think> <answer>-763</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9652 + 1994 + 8096 - 9112 + 4303 + 7925 =  |  9652 + 1994 = 11646 ; 11646 + 8096 = 19742 ; 19742 - 9112 = 10630 ; 10630 + 4303 = 14933 ; 14933 + 7925 = 22858  |  22858  |  State the final answer to the following arithmetic problem: 9652 + 1994 + 8096 - 9112 + 4303 + 7925 = <think>9652 + 1994 = 11646 ; 11646 + 8096 = 19742 ; 19742 - 9112 = 10630 ; 10630 + 4303 = 14933 ; 14933 + 7925 = 22858</think> <answer>22858</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 62 + 51 =  |  62 + 51 = 113  |  113  |  State the final answer to the following arithmetic problem: 62 + 51 = <think>62 + 51 = 113</think> <answer>113</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8374 - 5939 + 4411 =  |  8374 - 5939 = 2435 ; 2435 + 4411 = 6846  |  6846  |  State the final answer to the following arithmetic problem: 8374 - 5939 + 4411 = <think>8374 - 5939 = 2435 ; 2435 + 4411 = 6846</think> <answer>6846</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 866 + 660 =  |  866 + 660 = 1526  |  1526  |  State the final answer to the following arithmetic problem: 866 + 660 = <think>866 + 660 = 1526</think> <answer>1526</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 4 + 0 =  |  4 + 0 = 4  |  4  |  State the final answer to the following arithmetic problem: 4 + 0 = <think>4 + 0 = 4</think> <answer>4</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9 - 7 + 2 - 9 - 7 + 0 =  |  9 - 7 = 2 ; 2 + 2 = 4 ; 4 - 9 = -5 ; -5 - 7 = -12 ; -12 + 0 = -12  |  -12  |  State the final answer to the following arithmetic problem: 9 - 7 + 2 - 9 - 7 + 0 = <think>9 - 7 = 2 ; 2 + 2 = 4 ; 4 - 9 = -5 ; -5 - 7 = -12 ; -12 + 0 = -12</think> <answer>-12</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3709 + 8963 + 5678 - 6657 + 6863 + 5290 =  |  3709 + 8963 = 12672 ; 12672 + 5678 = 18350 ; 18350 - 6657 = 11693 ; 11693 + 6863 = 18556 ; 18556 + 5290 = 23846  |  23846  |  State the final answer to the following arithmetic problem: 3709 + 8963 + 5678 - 6657 + 6863 + 5290 = <think>3709 + 8963 = 12672 ; 12672 + 5678 = 18350 ; 18350 - 6657 = 11693 ; 11693 + 6863 = 18556 ; 18556 + 5290 = 23846</think> <answer>23846</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 + 3 + 2 =  |  0 + 3 = 3 ; 3 + 2 = 5  |  5  |  State the final answer to the following arithmetic problem: 0 + 3 + 2 = <think>0 + 3 = 3 ; 3 + 2 = 5</think> <answer>5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 7 - 1 - 2 + 6 - 1 =  |  7 - 1 = 6 ; 6 - 2 = 4 ; 4 + 6 = 10 ; 10 - 1 = 9  |  9  |  State the final answer to the following arithmetic problem: 7 - 1 - 2 + 6 - 1 = <think>7 - 1 = 6 ; 6 - 2 = 4 ; 4 + 6 = 10 ; 10 - 1 = 9</think> <answer>9</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 7 - 0 + 5 - 7 + 9 =  |  7 - 0 = 7 ; 7 + 5 = 12 ; 12 - 7 = 5 ; 5 + 9 = 14  |  14  |  State the final answer to the following arithmetic problem: 7 - 0 + 5 - 7 + 9 = <think>7 - 0 = 7 ; 7 + 5 = 12 ; 12 - 7 = 5 ; 5 + 9 = 14</think> <answer>14</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 89 + 52 - 18 =  |  89 + 52 = 141 ; 141 - 18 = 123  |  123  |  State the final answer to the following arithmetic problem: 89 + 52 - 18 = <think>89 + 52 = 141 ; 141 - 18 = 123</think> <answer>123</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 60 - 66 - 88 - 67 + 33 - 90 =  |  60 - 66 = -6 ; -6 - 88 = -94 ; -94 - 67 = -161 ; -161 + 33 = -128 ; -128 - 90 = -218  |  -218  |  State the final answer to the following arithmetic problem: 60 - 66 - 88 - 67 + 33 - 90 = <think>60 - 66 = -6 ; -6 - 88 = -94 ; -94 - 67 = -161 ; -161 + 33 = -128 ; -128 - 90 = -218</think> <answer>-218</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 6 + 5 - 4 + 4 - 1 =  |  6 + 5 = 11 ; 11 - 4 = 7 ; 7 + 4 = 11 ; 11 - 1 = 10  |  10  |  State the final answer to the following arithmetic problem: 6 + 5 - 4 + 4 - 1 = <think>6 + 5 = 11 ; 11 - 4 = 7 ; 7 + 4 = 11 ; 11 - 1 = 10</think> <answer>10</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 4 + 6 =  |  4 + 6 = 10  |  10  |  State the final answer to the following arithmetic problem: 4 + 6 = <think>4 + 6 = 10</think> <answer>10</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 4078 + 4726 + 5978 - 8836 =  |  4078 + 4726 = 8804 ; 8804 + 5978 = 14782 ; 14782 - 8836 = 5946  |  5946  |  State the final answer to the following arithmetic problem: 4078 + 4726 + 5978 - 8836 = <think>4078 + 4726 = 8804 ; 8804 + 5978 = 14782 ; 14782 - 8836 = 5946</think> <answer>5946</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 55 - 46 - 57 + 83 - 24 =  |  55 - 46 = 9 ; 9 - 57 = -48 ; -48 + 83 = 35 ; 35 - 24 = 11  |  11  |  State the final answer to the following arithmetic problem: 55 - 46 - 57 + 83 - 24 = <think>55 - 46 = 9 ; 9 - 57 = -48 ; -48 + 83 = 35 ; 35 - 24 = 11</think> <answer>11</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 58 + 35 + 21 + 89 - 12 =  |  58 + 35 = 93 ; 93 + 21 = 114 ; 114 + 89 = 203 ; 203 - 12 = 191  |  191  |  State the final answer to the following arithmetic problem: 58 + 35 + 21 + 89 - 12 = <think>58 + 35 = 93 ; 93 + 21 = 114 ; 114 + 89 = 203 ; 203 - 12 = 191</think> <answer>191</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 - 4 - 6 + 9 - 9 =  |  0 - 4 = -4 ; -4 - 6 = -10 ; -10 + 9 = -1 ; -1 - 9 = -10  |  -10  |  State the final answer to the following arithmetic problem: 0 - 4 - 6 + 9 - 9 = <think>0 - 4 = -4 ; -4 - 6 = -10 ; -10 + 9 = -1 ; -1 - 9 = -10</think> <answer>-10</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8969 + 4404 - 8269 =  |  8969 + 4404 = 13373 ; 13373 - 8269 = 5104  |  5104  |  State the final answer to the following arithmetic problem: 8969 + 4404 - 8269 = <think>8969 + 4404 = 13373 ; 13373 - 8269 = 5104</think> <answer>5104</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 802 - 893 + 526 + 652 + 647 + 524 =  |  802 - 893 = -91 ; -91 + 526 = 435 ; 435 + 652 = 1087 ; 1087 + 647 = 1734 ; 1734 + 524 = 2258  |  2258  |  State the final answer to the following arithmetic problem: 802 - 893 + 526 + 652 + 647 + 524 = <think>802 - 893 = -91 ; -91 + 526 = 435 ; 435 + 652 = 1087 ; 1087 + 647 = 1734 ; 1734 + 524 = 2258</think> <answer>2258</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 5054 + 6859 - 3489 - 4654 - 3580 =  |  5054 + 6859 = 11913 ; 11913 - 3489 = 8424 ; 8424 - 4654 = 3770 ; 3770 - 3580 = 190  |  190  |  State the final answer to the following arithmetic problem: 5054 + 6859 - 3489 - 4654 - 3580 = <think>5054 + 6859 = 11913 ; 11913 - 3489 = 8424 ; 8424 - 4654 = 3770 ; 3770 - 3580 = 190</think> <answer>190</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 4683 + 3631 - 1269 + 1486 + 6724 + 6678 =  |  4683 + 3631 = 8314 ; 8314 - 1269 = 7045 ; 7045 + 1486 = 8531 ; 8531 + 6724 = 15255 ; 15255 + 6678 = 21933  |  21933  |  State the final answer to the following arithmetic problem: 4683 + 3631 - 1269 + 1486 + 6724 + 6678 = <think>4683 + 3631 = 8314 ; 8314 - 1269 = 7045 ; 7045 + 1486 = 8531 ; 8531 + 6724 = 15255 ; 15255 + 6678 = 21933</think> <answer>21933</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 - 6 - 9 =  |  0 - 6 = -6 ; -6 - 9 = -15  |  -15  |  State the final answer to the following arithmetic problem: 0 - 6 - 9 = <think>0 - 6 = -6 ; -6 - 9 = -15</think> <answer>-15</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 96 + 67 + 41 - 76 - 35 =  |  96 + 67 = 163 ; 163 + 41 = 204 ; 204 - 76 = 128 ; 128 - 35 = 93  |  93  |  State the final answer to the following arithmetic problem: 96 + 67 + 41 - 76 - 35 = <think>96 + 67 = 163 ; 163 + 41 = 204 ; 204 - 76 = 128 ; 128 - 35 = 93</think> <answer>93</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 509 - 278 =  |  509 - 278 = 231  |  231  |  State the final answer to the following arithmetic problem: 509 - 278 = <think>509 - 278 = 231</think> <answer>231</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 80 + 31 - 39 - 91 + 85 - 71 =  |  80 + 31 = 111 ; 111 - 39 = 72 ; 72 - 91 = -19 ; -19 + 85 = 66 ; 66 - 71 = -5  |  -5  |  State the final answer to the following arithmetic problem: 80 + 31 - 39 - 91 + 85 - 71 = <think>80 + 31 = 111 ; 111 - 39 = 72 ; 72 - 91 = -19 ; -19 + 85 = 66 ; 66 - 71 = -5</think> <answer>-5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 74 - 35 =  |  74 - 35 = 39  |  39  |  State the final answer to the following arithmetic problem: 74 - 35 = <think>74 - 35 = 39</think> <answer>39</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3832 - 9072 + 5665 + 4551 + 6774 + 4366 =  |  3832 - 9072 = -5240 ; -5240 + 5665 = 425 ; 425 + 4551 = 4976 ; 4976 + 6774 = 11750 ; 11750 + 4366 = 16116  |  16116  |  State the final answer to the following arithmetic problem: 3832 - 9072 + 5665 + 4551 + 6774 + 4366 = <think>3832 - 9072 = -5240 ; -5240 + 5665 = 425 ; 425 + 4551 = 4976 ; 4976 + 6774 = 11750 ; 11750 + 4366 = 16116</think> <answer>16116</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 361 - 574 =  |  361 - 574 = -213  |  -213  |  State the final answer to the following arithmetic problem: 361 - 574 = <think>361 - 574 = -213</think> <answer>-213</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 6 - 1 =  |  6 - 1 = 5  |  5  |  State the final answer to the following arithmetic problem: 6 - 1 = <think>6 - 1 = 5</think> <answer>5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 8012 + 1199 - 6356 =  |  8012 + 1199 = 9211 ; 9211 - 6356 = 2855  |  2855  |  State the final answer to the following arithmetic problem: 8012 + 1199 - 6356 = <think>8012 + 1199 = 9211 ; 9211 - 6356 = 2855</think> <answer>2855</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 5 + 6 + 5 =  |  5 + 6 = 11 ; 11 + 5 = 16  |  16  |  State the final answer to the following arithmetic problem: 5 + 6 + 5 = <think>5 + 6 = 11 ; 11 + 5 = 16</think> <answer>16</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 488 + 288 =  |  488 + 288 = 776  |  776  |  State the final answer to the following arithmetic problem: 488 + 288 = <think>488 + 288 = 776</think> <answer>776</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 81 - 75 - 25 - 77 =  |  81 - 75 = 6 ; 6 - 25 = -19 ; -19 - 77 = -96  |  -96  |  State the final answer to the following arithmetic problem: 81 - 75 - 25 - 77 = <think>81 - 75 = 6 ; 6 - 25 = -19 ; -19 - 77 = -96</think> <answer>-96</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 422 - 194 + 348 + 433 =  |  422 - 194 = 228 ; 228 + 348 = 576 ; 576 + 433 = 1009  |  1009  |  State the final answer to the following arithmetic problem: 422 - 194 + 348 + 433 = <think>422 - 194 = 228 ; 228 + 348 = 576 ; 576 + 433 = 1009</think> <answer>1009</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 7780 - 2932 + 8573 + 3845 + 7194 + 6101 =  |  7780 - 2932 = 4848 ; 4848 + 8573 = 13421 ; 13421 + 3845 = 17266 ; 17266 + 7194 = 24460 ; 24460 + 6101 = 30561  |  30561  |  State the final answer to the following arithmetic problem: 7780 - 2932 + 8573 + 3845 + 7194 + 6101 = <think>7780 - 2932 = 4848 ; 4848 + 8573 = 13421 ; 13421 + 3845 = 17266 ; 17266 + 7194 = 24460 ; 24460 + 6101 = 30561</think> <answer>30561</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 37 - 48 - 55 - 16 =  |  37 - 48 = -11 ; -11 - 55 = -66 ; -66 - 16 = -82  |  -82  |  State the final answer to the following arithmetic problem: 37 - 48 - 55 - 16 = <think>37 - 48 = -11 ; -11 - 55 = -66 ; -66 - 16 = -82</think> <answer>-82</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9330 + 6998 - 5010 + 7658 =  |  9330 + 6998 = 16328 ; 16328 - 5010 = 11318 ; 11318 + 7658 = 18976  |  18976  |  State the final answer to the following arithmetic problem: 9330 + 6998 - 5010 + 7658 = <think>9330 + 6998 = 16328 ; 16328 - 5010 = 11318 ; 11318 + 7658 = 18976</think> <answer>18976</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 1398 - 9135 =  |  1398 - 9135 = -7737  |  -7737  |  State the final answer to the following arithmetic problem: 1398 - 9135 = <think>1398 - 9135 = -7737</think> <answer>-7737</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 16 + 83 - 98 + 98 - 74 =  |  16 + 83 = 99 ; 99 - 98 = 1 ; 1 + 98 = 99 ; 99 - 74 = 25  |  25  |  State the final answer to the following arithmetic problem: 16 + 83 - 98 + 98 - 74 = <think>16 + 83 = 99 ; 99 - 98 = 1 ; 1 + 98 = 99 ; 99 - 74 = 25</think> <answer>25</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3 - 1 =  |  3 - 1 = 2  |  2  |  State the final answer to the following arithmetic problem: 3 - 1 = <think>3 - 1 = 2</think> <answer>2</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 7884 + 4155 - 7610 =  |  7884 + 4155 = 12039 ; 12039 - 7610 = 4429  |  4429  |  State the final answer to the following arithmetic problem: 7884 + 4155 - 7610 = <think>7884 + 4155 = 12039 ; 12039 - 7610 = 4429</think> <answer>4429</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 4960 - 6508 =  |  4960 - 6508 = -1548  |  -1548  |  State the final answer to the following arithmetic problem: 4960 - 6508 = <think>4960 - 6508 = -1548</think> <answer>-1548</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 1 - 0 - 8 =  |  1 - 0 = 1 ; 1 - 8 = -7  |  -7  |  State the final answer to the following arithmetic problem: 1 - 0 - 8 = <think>1 - 0 = 1 ; 1 - 8 = -7</think> <answer>-7</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 + 9 - 4 =  |  0 + 9 = 9 ; 9 - 4 = 5  |  5  |  State the final answer to the following arithmetic problem: 0 + 9 - 4 = <think>0 + 9 = 9 ; 9 - 4 = 5</think> <answer>5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 + 5 - 5 - 3 + 4 + 5 =  |  0 + 5 = 5 ; 5 - 5 = 0 ; 0 - 3 = -3 ; -3 + 4 = 1 ; 1 + 5 = 6  |  6  |  State the final answer to the following arithmetic problem: 0 + 5 - 5 - 3 + 4 + 5 = <think>0 + 5 = 5 ; 5 - 5 = 0 ; 0 - 3 = -3 ; -3 + 4 = 1 ; 1 + 5 = 6</think> <answer>6</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 339 + 339 - 427 + 456 - 390 =  |  339 + 339 = 678 ; 678 - 427 = 251 ; 251 + 456 = 707 ; 707 - 390 = 317  |  317  |  State the final answer to the following arithmetic problem: 339 + 339 - 427 + 456 - 390 = <think>339 + 339 = 678 ; 678 - 427 = 251 ; 251 + 456 = 707 ; 707 - 390 = 317</think> <answer>317</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 0 - 5 =  |  0 - 5 = -5  |  -5  |  State the final answer to the following arithmetic problem: 0 - 5 = <think>0 - 5 = -5</think> <answer>-5</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3 + 5 - 5 + 5 =  |  3 + 5 = 8 ; 8 - 5 = 3 ; 3 + 5 = 8  |  8  |  State the final answer to the following arithmetic problem: 3 + 5 - 5 + 5 = <think>3 + 5 = 8 ; 8 - 5 = 3 ; 3 + 5 = 8</think> <answer>8</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 29 - 48 =  |  29 - 48 = -19  |  -19  |  State the final answer to the following arithmetic problem: 29 - 48 = <think>29 - 48 = -19</think> <answer>-19</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9975 + 8358 + 2777 + 8746 =  |  9975 + 8358 = 18333 ; 18333 + 2777 = 21110 ; 21110 + 8746 = 29856  |  29856  |  State the final answer to the following arithmetic problem: 9975 + 8358 + 2777 + 8746 = <think>9975 + 8358 = 18333 ; 18333 + 2777 = 21110 ; 21110 + 8746 = 29856</think> <answer>29856</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3513 - 1397 - 9996 + 5027 =  |  3513 - 1397 = 2116 ; 2116 - 9996 = -7880 ; -7880 + 5027 = -2853  |  -2853  |  State the final answer to the following arithmetic problem: 3513 - 1397 - 9996 + 5027 = <think>3513 - 1397 = 2116 ; 2116 - 9996 = -7880 ; -7880 + 5027 = -2853</think> <answer>-2853</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 103 - 347 - 172 =  |  103 - 347 = -244 ; -244 - 172 = -416  |  -416  |  State the final answer to the following arithmetic problem: 103 - 347 - 172 = <think>103 - 347 = -244 ; -244 - 172 = -416</think> <answer>-416</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 246 + 689 + 663 + 218 + 513 =  |  246 + 689 = 935 ; 935 + 663 = 1598 ; 1598 + 218 = 1816 ; 1816 + 513 = 2329  |  2329  |  State the final answer to the following arithmetic problem: 246 + 689 + 663 + 218 + 513 = <think>246 + 689 = 935 ; 935 + 663 = 1598 ; 1598 + 218 = 1816 ; 1816 + 513 = 2329</think> <answer>2329</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 52 + 57 =  |  52 + 57 = 109  |  109  |  State the final answer to the following arithmetic problem: 52 + 57 = <think>52 + 57 = 109</think> <answer>109</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 61 + 91 + 99 - 71 - 17 - 88 =  |  61 + 91 = 152 ; 152 + 99 = 251 ; 251 - 71 = 180 ; 180 - 17 = 163 ; 163 - 88 = 75  |  75  |  State the final answer to the following arithmetic problem: 61 + 91 + 99 - 71 - 17 - 88 = <think>61 + 91 = 152 ; 152 + 99 = 251 ; 251 - 71 = 180 ; 180 - 17 = 163 ; 163 - 88 = 75</think> <answer>75</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 189 - 577 - 414 - 534 =  |  189 - 577 = -388 ; -388 - 414 = -802 ; -802 - 534 = -1336  |  -1336  |  State the final answer to the following arithmetic problem: 189 - 577 - 414 - 534 = <think>189 - 577 = -388 ; -388 - 414 = -802 ; -802 - 534 = -1336</think> <answer>-1336</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3837 - 5865 + 5433 - 9618 + 4706 + 1398 =  |  3837 - 5865 = -2028 ; -2028 + 5433 = 3405 ; 3405 - 9618 = -6213 ; -6213 + 4706 = -1507 ; -1507 + 1398 = -109  |  -109  |  State the final answer to the following arithmetic problem: 3837 - 5865 + 5433 - 9618 + 4706 + 1398 = <think>3837 - 5865 = -2028 ; -2028 + 5433 = 3405 ; 3405 - 9618 = -6213 ; -6213 + 4706 = -1507 ; -1507 + 1398 = -109</think> <answer>-109</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 9 - 2 - 5 - 6 - 4 + 6 =  |  9 - 2 = 7 ; 7 - 5 = 2 ; 2 - 6 = -4 ; -4 - 4 = -8 ; -8 + 6 = -2  |  -2  |  State the final answer to the following arithmetic problem: 9 - 2 - 5 - 6 - 4 + 6 = <think>9 - 2 = 7 ; 7 - 5 = 2 ; 2 - 6 = -4 ; -4 - 4 = -8 ; -8 + 6 = -2</think> <answer>-2</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 1690 + 4266 - 4415 - 7512 + 2307 + 5938 =  |  1690 + 4266 = 5956 ; 5956 - 4415 = 1541 ; 1541 - 7512 = -5971 ; -5971 + 2307 = -3664 ; -3664 + 5938 = 2274  |  2274  |  State the final answer to the following arithmetic problem: 1690 + 4266 - 4415 - 7512 + 2307 + 5938 = <think>1690 + 4266 = 5956 ; 5956 - 4415 = 1541 ; 1541 - 7512 = -5971 ; -5971 + 2307 = -3664 ; -3664 + 5938 = 2274</think> <answer>2274</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 3 - 6 + 5 + 1 - 4 - 2 =  |  3 - 6 = -3 ; -3 + 5 = 2 ; 2 + 1 = 3 ; 3 - 4 = -1 ; -1 - 2 = -3  |  -3  |  State the final answer to the following arithmetic problem: 3 - 6 + 5 + 1 - 4 - 2 = <think>3 - 6 = -3 ; -3 + 5 = 2 ; 2 + 1 = 3 ; 3 - 4 = -1 ; -1 - 2 = -3</think> <answer>-3</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 2 + 2 - 0 - 3 + 9 + 1 =  |  2 + 2 = 4 ; 4 - 0 = 4 ; 4 - 3 = 1 ; 1 + 9 = 10 ; 10 + 1 = 11  |  11  |  State the final answer to the following arithmetic problem: 2 + 2 - 0 - 3 + 9 + 1 = <think>2 + 2 = 4 ; 4 - 0 = 4 ; 4 - 3 = 1 ; 1 + 9 = 10 ; 10 + 1 = 11</think> <answer>11</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 2652 - 8837 =  |  2652 - 8837 = -6185  |  -6185  |  State the final answer to the following arithmetic problem: 2652 - 8837 = <think>2652 - 8837 = -6185</think> <answer>-6185</answer>  |  
|  chain_sum  |  State the final answer to the following arithmetic problem: 5535 - 6061 - 1191 + 8823 =  |  5535 - 6061 = -526 ; -526 - 1191 = -1717 ; -1717 + 8823 = 7106  |  7106  |  State the final answer to the following arithmetic problem: 5535 - 6061 - 1191 + 8823 = <think>5535 - 6061 = -526 ; -526 - 1191 = -1717 ; -1717 + 8823 = 7106</think> <answer>7106</answer>  |  
End of preview. 
  * Contents⟨42⟩
  * Quality controls⟨43⟩
  * Not yet included⟨44⟩
  * Attribution & eval integrity⟨45⟩


#   ⟨46⟩ Shohin — training data 
Data for **Shohin** , a ~135M-parameter **verifiable-reasoning** language model (math / code / logic, English-only). Every corpus here is quality-controlled: verified, concise, and decontaminated against a fixed reasoning eval suite.
##   ⟨42⟩ Contents   
| path  | what  | source / license  |  
| --- | --- | --- |  
| `tokenizer/shohin-tok-32k.json`  | 32k BPE — single-digit numbers, byte-fallback, reserved `<think>`/`<code>` tokens  | ours  |  
| `reasoning_gym/rg_train.jsonl`  | ~560k **verified** (question, answer) items across 28 families  | Reasoning-Gym (Apache-2.0)  |  
| `reasoning_gym/rg_traces_train.jsonl`  | ~100k **verified execution-trace** documents (`<think>` worked steps `</think>`)  | ours (generated + verifier-checked)  |  
| `reasoning_gym/rg_eval.jsonl`  | held-out eval — families **and** seeds never seen in train  | Reasoning-Gym  |  
| `sft/openmath2_concise*.clean.jsonl`  | concise (≤400 tok), decontaminated math solutions  | OpenMathInstruct-2 (CC-BY-4.0)  |  
| `decontam/evalgrams.pkl`  | 13-gram set over GSM8K / GSM8K-Platinum / MATH-500 / HumanEval / MBPP  | derived  |  
##   ⟨43⟩ Quality controls 
  * **Decontamination** — every corpus is 13-gram-checked against the eval suite. OpenMathInstruct-2 measured ~0.7% contaminated → filtered out; Reasoning-Gym is decontaminated-by-construction (0.000%).
  * **Verification** — Reasoning-Gym items and every execution trace are checked by the task verifier; only correct items are kept (rejection sampling).
  * **Concise-CoT** — SFT solutions filtered to ≤400 tokens under the Shohin tokenizer (short reasoning beats long for small students).


##   ⟨44⟩ Not yet included 
The decontaminated pretrain shards (FineMath-4+, OpenWebMath, code — zstd `uint16`) are still building and will be added.
##   ⟨45⟩ Attribution & eval integrity 
Built on Reasoning-Gym (open-thought) and OpenMathInstruct-2 (NVIDIA). The **raw eval test sets are deliberately not re-hosted here** — download them from their original sources (GSM8K, MATH-500, HumanEval, MBPP, GSM8K-Platinum) to keep evaluation clean. Only the derived decontamination gram-set is included.
Copy to bucket new 

Downloads last month
    60
Total file size: 2.4 GB
System theme
Company
TOS⟨47⟩ Privacy⟨48⟩ About⟨49⟩ Careers⟨50⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
The table displays a preview with only the first rows.
