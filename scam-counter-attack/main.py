from chatterbox import *


test_audio = convert_to_wav('test_python.m4a')
angry_audio = convert_to_wav('angry_audio.m4a')
non_exist_audio = convert_to_wav('non_exist_audio.m4a')
happy_audio = convert_to_wav('happy_audio.m4a')

transcribe_audio('audio_files/test_python.wav')
transcribe_audio('audio_files/angry_audio.wav')
transcribe_audio('audio_files/non_exist_audio.wav')
transcribe_audio('audio_files/happy_audio.wav')

