# working from old calls to find frequently used keywords, scam scripts,
# overall sentiment values, specific scammer phrases and their appropriate response,
from response import *
import os
import pandas as pd

word_box = pd.DataFrame()

def analyze_past_calls():
    past_calls_list = os.listdir('train_calls/')
    print('Training calls to be analyzed:', past_calls_list)
    for i in past_calls_list:
        if i != '.DS_Store:':
            org_train = open('train_calls/' + i, encoding = "latin-1").read().lower()  # type str
            string_train = org_train.replace('\n', ' ') #remove new lines

            words_spoken_list = string_train.split(' ') #split words by spacing
            while '' in words_spoken_list:
                words_spoken_list.remove('')#remove whitespace

            train_sentences = org_train.split('\n') #split word groupings by new line
            while '' in train_sentences:
                train_sentences.remove('') #removing whitespace


    for i in train_sentences:
        analyze_text(i)

    words_spoken_series = pd.Series(words_spoken_list).value_counts()
    print(words_spoken_list)
    print(words_spoken_series)

analyze_past_calls()