from chatterbox import *
import os
import numpy as np
import pandas as pd

full_convo_df = pd.DataFrame()
def file_runner(filename):
    wav_file = convert_to_wav(filename)
    volume_file = get_volume(wav_file)
    text_file = transcribe_audio(wav_file)
    sentiment_file = analyze_text(text_file)
    print(wav_file, volume_file, text_file, sentiment_file)
    return #wav_file, volume_file, text_file, sentiment_file


def run_all_audio():
    all_files = np.array(os.listdir('audio_files'))
    print('Files that will be run:', all_files)
    for i in all_files:
        if i != '.DS_Store':
            file_runner(i)


run_all_audio()