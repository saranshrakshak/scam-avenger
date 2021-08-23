# install list
# pip3 install pydub
# pip3 install SpeechRecognition
# pip3 install nltk
# pip3 install ffmpeg, ffprobe, ffplay from command line
# and download from https://ffmpeg.org/download.html
# sentiment models
# nltk.download("vader_lexicon")

from pydub import AudioSegment
import speech_recognition as sr
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# changing format of incoming file from .m4a (or other) to .wav
# returns a AudioSegment object
def convert_to_wav(filename):
    filename = 'audio_files/' + filename
    file_type = filename.split(".")[1]

    if file_type != '.wav':
        new_name = filename.split(".")[0] + ".wav"
        audio = AudioSegment.from_file(filename)
        audio.export(new_name, format='wav')
        return new_name
    else:
        if os.path.exists(filename.__contains__('.wav')):
            # print('File <<', filename, '>> already converted to .wav and removed.')
            return filename.split(".")[0] + ".wav"
        else:
            # print('File <<', filename, '>> non-existent.')
            return filename.split(".")[0] + ".wav"


def get_volume(filename):
    # print('Volume score: ', AudioSegment.from_file(filename).dBFS)
    return AudioSegment.from_file(filename).dBFS


# converting spoken words to text
def transcribe_audio(wav_file):
    if not wav_file: return False
    recognizer = sr.Recognizer()
    # Import the audio file and convert to audio data
    audio_file = sr.AudioFile(wav_file)
    with audio_file as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data)


# sentiment analysis of speaker's text
def analyze_text(text_file):
    if not text_file:
        return False
    intensity = SentimentIntensityAnalyzer()
    # print('Conversation Transcription:', text_file)
    # print('Conversation Sentiment: ', intensity.polarity_scores(text_file))
    return intensity.polarity_scores(text_file)
