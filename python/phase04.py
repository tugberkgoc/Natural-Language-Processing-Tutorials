import nltk
from nltk.corpus import stopwords
import pandas as pd
import re
import numpy as np


# PART 01
def pre_process(text):
    tokenize = nltk.word_tokenize(text)
    tokenize = [x.lower() for x in tokenize if x.isalpha()]

    stop_words = set(stopwords.words("english"))
    filtered_sentence = list()

    for word in tokenize:
        if word not in stop_words:
            filtered_sentence.append(word)

    return set(filtered_sentence)


def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^\w]", " ", sentence).split()  # nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned


def bag_of_words(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i, word in enumerate(words):
            if word == sw:
                bag[i] += 1

    return np.array(bag)


# MAIN
df = pd.read_csv("../Reviews.csv")
saved_column = df['Text']

all_words = set()

for file in saved_column[0:2]:
    pre_process_file = pre_process(file)

    # print(*pre_process_file, sep='\n')
    all_words.update(pre_process_file)

print('=============================================PART 01 =====================================================')
print('A list of vectors of features. (Bag Of Words)')
print('==========================================================================================================')
# print(set(all_words))
print(bag_of_words("Products is likely food.", all_words))
