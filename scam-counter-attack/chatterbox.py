# install list
# pip3 install pydub
# pip3 install SpeechRecognition
# pip3 install nltk
# pip3 install ffmpeg, ffprobe, ffplay from command line
# and download from https://ffmpeg.org/download.html
# sentiment models:
# nltk.download("vader_lexicon")
from pydub import AudioSegment
import speech_recognition as sr
import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#changing format of incoming file from .m4a (or other) to .wav
#returns a AudioSegment object
def convert_to_wav(filename):
    filename = 'audio_files/' + filename

    if filename.split('.')[1] == '.m4a':
        new_name = filename.split(".")[0] + ".wav"
        audio = AudioSegment.from_file(filename)
        audio.export(new_name, format='wav')
        os.remove(filename) #saves space, less search time
        return new_name
    else:
        if os.path.exists(filename):
            print('File <<', filename, '>> already converted to .wav and removed.')
            return filename
        else:
            print('File <<', filename, '>> non-existent.')
            return False

def get_volume(filename):
    return AudioSegment.from_file(filename).dBFS

#converting spoken words to text
def transcribe_audio(wav_file):
    if not wav_file: return False
    recognizer = sr.Recognizer()
    # Import the audio file and convert to audio data
    audio_file = sr.AudioFile(wav_file)
    with audio_file as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)


#sentiment analysis of speaker's text
def analyze_text(text_file):
    if not text_file: return False
    intensity = SentimentIntensityAnalyzer()
    #print('Conversation Transcription:', text_file)
    #print('Conversation Sentiment: ', intensity.polarity_scores(text_file))
    return intensity.polarity_scores(text_file)
