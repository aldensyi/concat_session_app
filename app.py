import json
import os
import pandas as pd
import numpy as np
from nilearn import image

def concat_single_event_files(tsv1: pd.DataFrame, tsv2: pd.DataFrame) -> pd.DataFrame:
    """
    Concatenates two events.tsv files into one single tsv file
    
        Parameters:
            tsv1: First events.tsv file needing to be combined
            tsv2: Second events.tsv file needing to be combined

        Returns:
            combined_tsv(DataFrame): Combined events.tsv file
    """
    # Making sure that both dataframe exist
    if not tsv1.empty and not tsv2.empty:
        last_onset = tsv1.at[len(tsv1)-1, 'onset']
        last_duration = tsv1.at[len(tsv1)-1, 'duration']
        
        old_onset = tsv2['onset'].to_list()
        new_onset = []

        for val in old_onset:
            new_onset.append(val+last_onset+last_duration)

        tsv2['onset'] = new_onset
        combined_tsv = pd.concat([tsv1,tsv2])
        combined_tsv = combined_tsv.reset_index(drop=True)
        return combined_tsv
    
    return pd.DataFrame()


def main():
    # Loading Config.json file
    with open('config.json') as f:
        config = json.load(f)

    # Creating the Directory that would store the end products
    dirc = ['bold_multiple', 'events_multiple', 'provenance']


    for directory in dirc:
        os.makedirs(directory, exist_ok=True)

    # nifti-file passed in as an array from config.json    
    concat_list_nifti = config["bold_singles"]
    concat_list_events = config["events_singles"]

    # Concatenating the nifti files
    image.concat_imgs(concat_list_nifti, auto_resample=config['auto_resample']).to_filename("./bold_multiple/concatenated_img.nii.gz")

    # Concatenating the event files
    og_file = pd.read_csv(concat_list_events[0], sep='\t', index_col=False)

    for single_tsv in concat_list_events[1:]:
        og_file = concat_single_event_files(og_file, pd.read_csv(single_tsv, sep='\t', index_col=False))

    og_file.to_csv("./events_multiple/concatenated_events.csv")

if __name__ == "__main__":
    main()