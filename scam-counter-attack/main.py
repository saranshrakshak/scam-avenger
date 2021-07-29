from chatterbox import *
import os
import numpy as np
import pandas as pd



def file_runner(filename):
    return analyze_text(transcribe_audio(convert_to_wav(filename)))


def run_all_audio():
    all_files = np.array(os.listdir('audio_files'))
    print('Files that will be run:', all_files)
    for i in all_files:
        if i != '.DS_Store':
            file_runner(i)


run_all_audio()