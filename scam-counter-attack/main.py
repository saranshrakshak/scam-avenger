from chatterbox import *

def sentiment_runner(filename):
    test_audio = convert_to_wav(filename)
    text_audio = transcribe_audio(test_audio)
    return analyze_text(text_audio)

sentiment_runner('yelling_test.m4a')
sentiment_runner('quiet_test.m4a')
sentiment_runner('long_yelling.m4a')
