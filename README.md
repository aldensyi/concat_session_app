# concat_session_app

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Concatenating single-session, single-subject Nifti files into multiple-session, single-subject Nifti files for first-level GLM Analysis**

Concatenates several preprocessed single-run task fMRI images of one subject into one 4D image with nilearn concat_imgs, and joins their events files by shifting each run's onsets after the last event of the previous run. Use it to prepare multi-run data for a first-level GLM. The code reads an 'auto_resample' config key that is not a registered parameter, and writes concatenated_img.nii.gz and concatenated_events.csv rather than the standard bold.nii.gz and events.tsv names.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.810](https://doi.org/10.25663/brainlife.app.810)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `bold_singles` | `neuro/func/task` (preprocessed) | yes | Preprocessed task fMRI runs of one subject, in the order they should be concatenated. Runs must share the same voxel grid unless resampling is enabled. |
| `events_singles` | `neuro/func/events` | yes | Events files (TSV with onset and duration) matching each fMRI run, in the same order. |

| Output | Datatype | Description |
|---|---|---|
| `bold_multiple` | `neuro/func/task` | Concatenated functional MRI bold.nii file; Will be used and passed into the First Level GLM App |
| `events_multiple` | `neuro/func/events` | Combined events table with onsets shifted to the concatenated timeline (concatenated_events.csv). |

Runtime: container `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0`.

<!-- brainlife-app:end -->

Concatenating single-session, single subject Nifti files into multiple-session, single subject Nifti files
