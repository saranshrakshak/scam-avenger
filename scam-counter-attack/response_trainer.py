# working from old calls to find frequently used keywords, scam scripts,
# overall sentiment values, specific scammer phrases and their appropriate response
from response import *
import os
import pandas as pd

word_box = pd.DataFrame()
past_calls_list = os.listdir('train_calls/')
past_calls_list.remove('.DS_Store')
print('Training calls to be analyzed:', past_calls_list)

def analyze_past_sentences(print_info):
    for i in past_calls_list:
        org_train = open('train_calls/' + i, encoding="latin-1").read().lower()  # type str
        train_sentences = org_train.split('\n')  # split word groupings by new line

        while '' in train_sentences:
            train_sentences.remove('')  # removing whitespace

        if print_info:
            for sentence in train_sentences:
                print('--- NEW SENTENCE ANALYSIS ---')
                print('Sentence: ', sentence)
                print('Analysis: ', analyze_text(sentence))
                print('File: ', i, '\n')

    return print('Past Sentence analysis complete for all files in train_calls/*')

# returns a word frequency count for each word in text as type series
def analyze_past_words(print_info):
    for i in past_calls_list:
        org_train = open('train_calls/' + i, encoding="latin-1").read().lower()  # type str

        string_train = org_train.replace('\n', ' ')  # remove new lines
        words_spoken_list = string_train.split(' ')  # split words by spacing

        while '' in words_spoken_list:
            words_spoken_list.remove('')  # remove whitespace

        if print_info:
            for word in words_spoken_list:
                print('--- New Word Analysis ---')
                print('Word: ', word)
                print('Analysis: ', analyze_text(word))
                print('File: ', i, '\n')

    words_freq_series = pd.Series(words_spoken_list).value_counts()
    return words_freq_series


analyze_past_sentences(print_info = True)