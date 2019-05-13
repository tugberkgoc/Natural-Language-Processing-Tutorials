import numpy as np
import re


def tokenize_sentences(sentence):
    words = []
    for s in sentence:
        w = extract_words(s)
        words.extend(w)

    words = sorted(list(set(words)))
    return words


def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^\w]", " ", sentence).split()  # nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned


def bagofwords(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i, word in enumerate(words):
            if word == sw:
                bag[i] += 1

    return np.array(bag)


sentences = ["Machine learning is great", "Natural Language Processing is a complex field",
             "Natural Language Processing is used in machine learning"]
vocabulary = tokenize_sentences(sentences)
print(bagofwords("Machine learning is great", vocabulary))

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer="word", tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
train_data_features = vectorizer.fit_transform(sentences)
print(vectorizer.transform(["Machine learning is great"]).toarray())
