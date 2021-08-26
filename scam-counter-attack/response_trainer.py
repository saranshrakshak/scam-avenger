# working from old calls to find frequently used keywords, scam scripts,
# overall sentiment values, specific scammer phrases and their appropriate response
from response import *
import os
import pandas as pd

word_box = pd.DataFrame()
past_calls_list = os.listdir('train_calls/')
past_calls_list.remove('.DS_Store')
print('Training calls to be analyzed:', past_calls_list)


# returns a sentence for each word in text as type dataframe
def analyze_past_sentences():
    sentence_df = pd.DataFrame(columns=['sentence', 'sentiment', 'origin_file'])
    for i in past_calls_list:
        org_train = open('train_calls/' + i, encoding="latin-1").read().lower()  # type str
        train_sentences = org_train.split('\n')  # split word groupings by new line

        while '' in train_sentences: train_sentences.remove('')  # removing whitespace

        for sentence in train_sentences:
            sent_sentiment = analyze_text(sentence)
            dict_row = {'sentence': sentence, 'sentiment': sent_sentiment, 'origin_file': i}

            sentence_df = sentence_df.append(dict_row, ignore_index=True)
    print('Sentence analysis complete for all files in train_calls/*')
    return sentence_df

# returns a word frequency count & sentiment for each word in all text as type dataframe
def analyze_past_words():
    temp = pd.DataFrame()  # frame with all words from all files
    for i in past_calls_list:
        org_train = open('train_calls/' + i, encoding = 'latin-1').read().lower()  # type str
        string_train = org_train.replace('\n', ' ')  # remove new lines
        words_spoken_list = string_train.split(' ')  # split words by spacing

        while '' in words_spoken_list: words_spoken_list.remove('')  # remove whitespace


    word_series = pd.Series(data = words_spoken_list)
    word_series = word_series.value_counts()
    temp['word'] = word_series.index
    temp['frequency'] = word_series.values
    temp['sentiment'] = [analyze_text(word) for word in temp['word']]

    print('Word analysis complete for all files in train_calls/*')
    return temp

print(analyze_past_words())
print(analyze_past_sentences())