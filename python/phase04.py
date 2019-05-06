import nltk
from nltk.corpus import stopwords
import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# MAIN
df = pd.read_csv("Reviews.csv")
rr = pd.read_csv("Train.csv")
texts_train = df['Text']
score_train = df['Score']
score_test = rr['Score']
texts_test = rr['Text']


def word_extraction(sentence):
    stop_words = set(stopwords.words("english"))
    ignore = stop_words
    words = re.sub("[^\w]", " ", sentence).split()
    cleaned_text = [w.lower() for w in words if w not in ignore]
    cleaned_text = [x.lower() for x in cleaned_text if x.isalpha()]
    return cleaned_text


def tokenize(sentences):
    words = []
    for sentence in sentences:
        w = word_extraction(sentence)
        words.extend(w)

    words = sorted(list(set(words)))
    return words


def generate_bow(allsentences):
    vocab = tokenize(allsentences)
    print("Word List for Document \n{0} \n".format(vocab));

    for sentence in allsentences:
        words = word_extraction(sentence)
        bag_vector = np.zeros(len(vocab))
        for w in words:
            for i, word in enumerate(vocab):
                if word == w:
                    bag_vector[i] += 1

        print("{0}\n{1}\n".format(sentence, np.array(bag_vector)))


generate_bow(texts_train)
# generate_bow(allsentences[8:10])

vectorizer = CountVectorizer()
training_features = vectorizer.fit_transform(texts_train)
test_features = vectorizer.transform(texts_test)

# print(training_features.toarray())

# Training
model = LinearSVC()
model.fit(training_features, score_train)
y_pred = model.predict(test_features)

# Evaluation
acc = accuracy_score(score_test, y_pred)

print("Accuracy on the IMDB dataset: {:.2f}".format(acc * 100))


# classifier = GaussianNB()
# classifier.fit(texts_train, score_train)
#
# y_pred = classifier.predict(texts_test)
#
# cm = confusion_matrix(texts_test, y_pred)
#
# # print(cm)