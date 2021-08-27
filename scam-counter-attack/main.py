# main file for running audio files located in audio_files/
# ROOT ORIGIN IS MASTER NOT MAIN (GIT)
import glob
from chatterbox import *
import os
import numpy as np
import pandas as pd
from response import *

call_df = pd.DataFrame(columns=['scam_audio', 'scam_volume', 'scam_text', 'scam_sentiment'])

def file_runner(filename, info_print):
    global call_df
    wav_file = convert_to_wav(filename)

    if filename.endswith('.m4a'):
        os.remove('audio_files/' + filename)
    if call_df['scam_audio'].str.contains(wav_file).any():
        print('Skip Reprocessing')
        return
    else:
        volume_file = get_volume(wav_file)
        text_file = transcribe_audio(wav_file)
        sentiment_file = analyze_text(text_file)
        dict_row = {'scam_audio': wav_file, 'scam_volume': volume_file, 'scam_text': text_file,
                    'scam_sentiment': sentiment_file}
        call_df = call_df.append(dict_row, ignore_index=True)
        if info_print: show_file_info(wav_file, text_file, sentiment_file)
        return dict_row

# run all files in audio_files
def run_all_audio(info_print):
    all_files = np.array(os.listdir('audio_files'))
    all_files = all_files[all_files != '.DS_Store']
    print(len(all_files), 'files will be run:', all_files)
    for i in all_files:
        file_runner(i, info_print)

# get newest file added to audio_files
def newest_file():
    new_file = max(glob.glob('audio_files/*'), key=os.path.getctime)
    return new_file.split('/')[1]

def show_file_info(wav_file, text_file, sentiment_file):
    print(' ------- RUNNING NEW AUDIO FILE ------- ')
    print('File: ', wav_file.split('/')[1])
    print('Conversation Transcription: ', text_file)
    print('Conversation Sentiment: ', sentiment_file)

def show_audio_df():
    print('CallDF: ', call_df, type(call_df), call_df.columns)

run_all_audio(info_print = True)