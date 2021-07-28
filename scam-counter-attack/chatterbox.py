# install list
# pip3 install pydub
# pip3 install SpeechRecognition
# pip3 install nltk
# pip3 install ffmpeg, ffprobe, ffplay from command line
# and download from https://ffmpeg.org/download.html
# pretrained sentiment models
# nltk.download("punkt")
# nltk.download("vader_lexicon")

import nltk
from pydub import AudioSegment
import speech_recognition as sr
import os

#changing format of incoming file from .m4a (or other) to .wav
#returns a AudioSegment object
def convert_to_wav(filename):
    filename = 'audio_files/' + filename
    new_name = filename.split(".")[0] + ".wav"

    if os.path.exists(filename):
        audio = AudioSegment.from_file(filename)
        audio.export(new_name, format='wav')
        print('Converting ', filename, 'to', new_name, '.')
        os.remove(filename) #saves space, less search time
        return AudioSegment.from_file(new_name)
    else:
        if os.path.exists(new_name):
            print('File [', filename, '] already converted and removed.')
            return AudioSegment.from_file(new_name)
        else:
            print('File [', filename, '] non-existent.')
            return False

#converting spoken words to text
def transcribe_audio(filename):
    #take in a .wav format file and convert to text
    recognizer = sr.Recognizer()
    # Import the audio file and convert to audio data
    try:
        audio_file = sr.AudioFile(filename)
        with audio_file as source:
            audio_data = recognizer.record(source)
        # Return the transcribed text
        audio_text = recognizer.recognize_google(audio_data)
        print(filename, ':', audio_text)
        return audio_text
    except:
        FileNotFoundError
        print('Keep scanning for audio.')

