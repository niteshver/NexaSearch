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
 ![](https://www.gravatar.com/avatar/e353aca7b13ff8d5ed85ac4c08d03b15?d=retro&size=100) ⟨28⟩
Skoleatlas⟨28⟩
/
benchmark-dk-interaktivt-benchmarkingunivers⟨29⟩
like 0
Follow
![⟨30⟩] Skoleatlas 1
Tasks:  Tabular Classification ⟨31⟩ Tabular Regression ⟨32⟩
Languages:  Danish ⟨33⟩
Size:  1K<n<10K ⟨34⟩
License:
cc-by-4.0
 Dataset card ⟨29⟩ Files Files and versions xet ⟨35⟩ Community ⟨36⟩
Dataset Viewer
API Embed  Duplicate⟨37⟩ Data Studio
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
Exception:    ArrowInvalid
Message:      Schema at index 1 was different: 
Personale rækkefølge sortering.Personalegruppe: string
Sum(Personaleomsætning kommune stablet søjler.Værdi): double
Kommune rækkefølge sortering.Kommune: string
Ansættelsesperiode.Rigtigt navn: string
vs
Sum(Personaleomsætning kommune.Tilgangsprocent): double
Periode rækkefølge.aar: string
Personale rækkefølge sortering.Personalegruppe: string
Kommune rækkefølge sortering.Kommune: string
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
                File "/usr/local/lib/python3.14/site-packages/datasets/iterable_dataset.py", line 564, in _iter_arrow
                  yield new_key, pa.Table.from_batches(chunks_buffer)
                                 ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
                File "pyarrow/table.pxi", line 5039, in pyarrow.lib.Table.from_batches
                File "pyarrow/error.pxi", line 155, in pyarrow.lib.pyarrow_internal_check_status
                  return check_status(status)
                File "pyarrow/error.pxi", line 92, in pyarrow.lib.check_status
                  raise convert_status(status)
              pyarrow.lib.ArrowInvalid: Schema at index 1 was different: 
              Personale rækkefølge sortering.Personalegruppe: string
              Sum(Personaleomsætning kommune stablet søjler.Værdi): double
              Kommune rækkefølge sortering.Kommune: string
              Ansættelsesperiode.Rigtigt navn: string
              vs
              Sum(Personaleomsætning kommune.Tilgangsprocent): double
              Periode rækkefølge.aar: string
              Personale rækkefølge sortering.Personalegruppe: string
              Kommune rækkefølge sortering.Kommune: string
```

Need help to make the dataset viewer work? Make sure to review how to configure the dataset viewer⟨38⟩, and open a discussion⟨39⟩ for direct support.
  * Hvad sitet faktisk er⟨40⟩
  * Parquet⟨41⟩
  * De 6 rapporter⟨42⟩
  * Mappestruktur⟨43⟩
  * Kilde og licens⟨44⟩


#   ⟨45⟩ Benchmark.dk - interaktivt benchmarkingunivers (komplet data-høst) 
Komplet høst af datamaterialet bag Indenrigs- og Sundhedsministeriets _Benchmarkingenheds_ interaktive benchmarkingunivers: <https://www.benchmark.dk/interaktivt-benchmarkingunivers>. Høstet 1. juni 2026. Del af Silkeborg Skoleatlas⟨46⟩ - 4 af de deri indeholdte skole/dagtilbud-tabeller indgår også kurateret i atlassets egen silkeborg-benchmark-national⟨47⟩-datasæt, men dette repo er den fulde, ukuraterede kilde: alle 6 temaer, alle sider, alle kommuner.
##   ⟨40⟩ Hvad sitet faktisk er 
Forsiden lister 6 temaer. Hvert tema er ikke en HTML-side med tal eller downloads - det er en indlejret Power BI "Publish to web"-rapport (`app.powerbi.com/view?r=...`). Al data ligger i disse rapporter og hentes dynamisk via Power BI's offentlige `querydata`-API. Der findes ingen CSV/Excel/JSON/PDF-downloads på selve sitet for selve benchmark-tallene (de 506 PDF-analyser i `site_mirror/` er separate, færdigskrevne rapporter, ikke kilden til de interaktive tal).
Høsten er lavet ved at rendere hver Power BI-rapport i en rigtig browser (Playwright/Chromium), indlæse hver rapport-side, opfange alle `querydata`- netværkssvar (rådata i Power BI's DSR-format), og afkode DSR til almindelige tabeller (CSV) med rigtige kolonnenavne og opslåede dimensionsværdier.
##   ⟨41⟩ Parquet 
Alle 439 tabeller i `csv_all/` og `csv/` findes nu også som `.parquet` (samme sti, `.parquet`-endelse i stedet for `.csv`) - talkolonner er konverteret til rigtige `float64`/`int64`-typer i stedet for strenge. Hver mappe har desuden en samlet `manifest.parquet` (439 rækker: report/section/display/table/rows/ cols/kommuner/columns/csv/parquet-sti) til at slå tabeller op programmatisk uden at læse `_manifest.json`.
##   ⟨42⟩ De 6 rapporter   
| Mappe  | Tema  | Power BI-sider  |  
| --- | --- | --- |  
| `1-personale`  | Personale  | 94  |  
| `2-administration`  | Administration og tværgående emner  | 6  |  
| `3-dagtilbud-skole-uddannelse`  | Dagtilbud, skole og uddannelse  | 33  |  
| `4-integration-beskaeftigelse`  | Integration og beskæftigelse  | 16  |  
| `5-aeldre-sundhed`  | Ældre og sundhed  | 55  |  
| `6-det-specialiserede-social`  | Det specialiserede socialområde  | 7  |  
##   ⟨43⟩ Mappestruktur 
  * `csv_all/` - **hovedudtrækket** : 439 datatabeller, 29.682 datarækker, 106 tabeller med alle ~98 kommuner. Hver visuals query genafspillet uden kommunefilter, så hver kommunes faktiske værdi for hvert mål er med (ikke kun standard-kommunen Albertslund).
  * `csv/` - samme 439 tabeller i rapporternes default-tilstand (kun forvalgt kommune + Landsplan) - beholdt som reference.
  * `raw/`, `raw_all/`, `raw_silkeborg/` - de rå, ufiltrerede Power BI querydata-svar (lossless), inkl. et manuelt kontrol-udtræk for Silkeborg.
  * `model/` - Power BI-modellen + skema pr. rapport (`*.model.json`, `*.schema.json`) - kilden til data-ordbogen.
  * `site_mirror/` - spejling af selve benchmark.dk-sitet, inkl. **506 PDF-analyser** (`DOKUMENTER_katalog.csv` er indekset over dem).
  * `_scripts/` - harvester + decoder (Node/Playwright + Python) for reproducerbarhed.
  * `DATA_DICTIONARY.md`, `OVERSIGT.md`, `OVERSIGT_ALL.md`, `SILKEBORG_SKOLE.md`, `QA_REPORT.md`, `BACKUP_README.md` - dokumentation fra selve høsten.


##   ⟨44⟩ Kilde og licens 
Data tilhører Indenrigs- og Sundhedsministeriets Benchmarkingenhed (benchmark.dk). Høsten her er en teknisk kopi til analysebrug under CC BY 4.0 - angiv venligst den oprindelige kilde. PDF-analyserne i `site_mirror/` er ministeriets egne, offentligt udgivne rapporter.
Genereret af `_scripts/harvest.mjs` + `_scripts/deep_harvest.mjs` + `_scripts/decode.py`/`decode_all.py`, del af Silkeborg-Skoleatlas/silkeskoleatlas⟨48⟩.
Copy to bucket new 

Downloads last month
    727
Total file size: 934 MB
System theme
Company
TOS⟨49⟩ Privacy⟨50⟩ About⟨51⟩ Careers⟨52⟩ ⟨1⟩
Website
Models⟨2⟩ Datasets⟨3⟩ Spaces⟨4⟩ Pricing⟨8⟩ Docs⟨6⟩
