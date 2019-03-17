import nltk
from nltk.collocations import *
from nltk import ngrams
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

# df = pd.read_csv("Reviews.csv")
# saved_column = df['Text']

file = open('file.txt', 'r', encoding="utf8").read()


def pre_process(text):
    tokenize = nltk.word_tokenize(text)
    tokenize = [word.lower() for word in tokenize if word.isalpha()]

    stop_words = set(stopwords.words("english"))
    filtered_sentence = list()

    for word in tokenize:
        if word not in stop_words:
            filtered_sentence.append(word)

    return filtered_sentence


print('==========================================================================================================')
print('=============================================PART 01 =====================================================')
print('Tokenize version of the text that does not contain neither any stop words nor any punctuations')
print(*pre_process(file), sep='\n')
print('==========================================================================================================')


def most_frequent(tokenize_text, how_many):
    stem_words = list()
    for x in tokenize_text:
        stem_words.append(PorterStemmer().stem(x))
    return FreqDist(stem_words).most_common(how_many)


print('==========================================================================================================')
print('=============================================PART 02 =====================================================')
print('Number of the occurrences of the frequent words')
print(most_frequent(pre_process(file), 10))
print('==========================================================================================================')


def display_n_grams(tokenize_text, how_many):
    return ngrams(tokenize_text, how_many)


print('==========================================================================================================')
print('=============================================PART 03 =====================================================')
print('Displays n grams only as many as the desired n.')
print(*list(display_n_grams(pre_process(file), 2)), sep='\n')
print('==========================================================================================================')


def most_freq_bi_gram(freq_bi_gram, number_of_bi_gram):
    bi_gram = FreqDist(display_n_grams(pre_process(file), 2))\
        .most_common(len(list(display_n_grams(pre_process(file), 2))))
    result = list()
    temp = 0

    for x in bi_gram:
        if x[1] == freq_bi_gram and temp < number_of_bi_gram:
            result.append(x[0])
            temp += 1

    return result


print('==========================================================================================================')
print('=============================================PART 04 =====================================================')
print('Bi grams with the given frequency rate.')
print('frequency = 4, n = 1')
print(most_freq_bi_gram(4, 1))

print('frequency = 2, n = 3')
print(most_freq_bi_gram(2, 3))

print('frequency = 1, n = 5')
print(most_freq_bi_gram(1, 5))
print('==========================================================================================================')


def probable_occur(bi_gram):
    bi_gram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_documents(bi_gram)
    return sorted(finder.nbest(bi_gram_measures.pmi, 10))  # raw_freq


print('==========================================================================================================')
print('=============================================PART 05 =====================================================')
print('Top 10 bi grams.')
print(*probable_occur(display_n_grams(pre_process(file), 2)), sep='\n')  # ask teacher about some wrong examples
print('==========================================================================================================')


def score_bi_gram(bi_gram):
    bi_gram_measures = nltk.collocations.BigramAssocMeasures()
    finder = BigramCollocationFinder.from_documents(bi_gram)
    finder.apply_freq_filter(2)
    scored = finder.score_ngrams(bi_gram_measures.pmi)
    return scored


print('==========================================================================================================')
print('=============================================PART 06 =====================================================')
print('Score information of the bi grams that are equal to or more frequent than 2.')
print(*score_bi_gram(display_n_grams(pre_process(file), 2)), sep='\n')
print('==========================================================================================================')


def tag_given_text(text):
    tokenize = nltk.word_tokenize(text)
    return nltk.pos_tag(tokenize)


print('==========================================================================================================')
print('=============================================PART 07 =====================================================')
print('Produces a list of words.')
print(tag_given_text(file))
print('==========================================================================================================')


def num_of_tags(tagged_text):
    stat = {}
    for k, v in tagged_text:
        if v in stat:
            stat[v] += 1
        else:
            stat[v] = 1
    return sorted(stat.items(), key=lambda x: x[1], reverse=True)[:10]


print('==========================================================================================================')
print('=============================================PART 08 =====================================================')
print('Most common tags.')
print(num_of_tags(tag_given_text(file)))
print('==========================================================================================================')

# def getSpecifiedTag(tagged_text,tag):
#
#
# getSpecifiedTag(tag_given_text(file), 'NN')
