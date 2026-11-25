<h1 align="center">Concatenating NifTi and Eventfiles</h1>

<p align="center">
  Concatenating single-session, single-subject Nifti files into multiple-session, single-subject Nifti files for first-level GLM Analysis
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.810"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.810-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Concatenating single-session, single-subject Nifti files into multiple-session, single-subject Nifti files for first-level GLM Analysis**

Concatenates several preprocessed single-run task fMRI images of one subject into one 4D image with nilearn concat_imgs, and joins their events files by shifting each run's onsets after the last event of the previous run. Use it to prepare multi-run data for a first-level GLM. The code reads an 'auto_resample' config key that is not a registered parameter, and writes concatenated_img.nii.gz and concatenated_events.csv rather than the standard bold.nii.gz and events.tsv names.

| | |
|---|---|
| **Inputs** | `neuro/func/task` · `neuro/func/events` |
| **Outputs** | `neuro/func/task` · `neuro/func/events` |
| **Container** | `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0` |
| **Run it** | [doi.org/10.25663/brainlife.app.810](https://doi.org/10.25663/brainlife.app.810) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `bold_singles` | `neuro/func/task` (preprocessed) | yes | Preprocessed task fMRI runs of one subject, in the order they should be concatenated. Runs must share the same voxel grid unless resampling is enabled. |
| `events_singles` | `neuro/func/events` | yes | Events files (TSV with onset and duration) matching each fMRI run, in the same order. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `bold_multiple` | `neuro/func/task` | Concatenated functional MRI bold.nii file; Will be used and passed into the First Level GLM App |
| `events_multiple` | `neuro/func/events` | Combined events table with onsets shifted to the concatenated timeline (concatenated_events.csv). |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.810](https://doi.org/10.25663/brainlife.app.810), choose `neuro/func/task`, `neuro/func/events` from your project and press **Execute**. The results are saved to your project as `neuro/func/task`, `neuro/func/events`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "bold_singles": "/path/to/bold_singles/bold_singles",
       "events_singles": "/path/to/events_singles/events_singles",
       "events_json": "/path/to/events_singles/events_json",
       "events_csv": "/path/to/events_singles/events_csv"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Concatenating NifTi and Eventfiles. brainlife.io App. [doi:10.25663/brainlife.app.810](https://doi.org/10.25663/brainlife.app.810)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Abraham et al. Machine learning for neuroimaging with scikit-learn. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00014](https://doi.org/10.3389/fninf.2014.00014)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@aldensyi](https://github.com/aldensyi).
