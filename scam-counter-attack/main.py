import glob
from chatterbox import *
import os
import numpy as np
import pandas as pd
from response import *

call_df = pd.DataFrame(columns = ['scam_audio', 'scam_volume', 'scam_text', 'scam_sentiment'])


def file_runner(filename):
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
        return dict_row


def run_all_audio():
    all_files = np.array(os.listdir('audio_files'))
    all_files = all_files[all_files != '.DS_Store']

    print(len(all_files), 'files will be run:', all_files)

    for i in all_files:
        if i != '.DS_Store':
            # print(' ------- RUNNING NEW AUDIO FILE ------- ')
            # print('File: ' + i)
            file_runner(i)


def newest_file():
    new_file = max(glob.glob('audio_files/*'), key=os.path.getctime)
    return new_file.split('/')[1]


run_all_audio()

#print('CallDF: ', call_df, type(call_df), call_df.columns)
