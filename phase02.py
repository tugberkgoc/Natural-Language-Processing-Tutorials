import nltk
from nltk.collocations import *
from nltk import ngrams
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

# df = pd.read_csv("Reviews.csv")
# saved_column = df['Text']

str = open('file.txt', 'r', encoding="utf8").read()


def preprocess(text):
  tokenized = nltk.word_tokenize(text)
  tokenized = [word.lower() for word in tokenized if word.isalpha()]

  stop_words = set(stopwords.words("english"))
  filtered_sentence = list()

  for word in tokenized:
    if word not in stop_words:
      filtered_sentence.append(word)

  return filtered_sentence


print(*preprocess(str), sep='\n')


def mostFrequent(tokenizeText, howMany):
  stem_words = list()
  for x in tokenizeText:
    stem_words.append(PorterStemmer().stem(x))
  return FreqDist(stem_words).most_common(howMany)


print(mostFrequent(preprocess(str), 10))


def displayNgrams(tokenizeText, howMany):
  return ngrams(tokenizeText, howMany)


print(*list(displayNgrams(preprocess(str), 2)), sep='\n')

print('===MostFreqBiagram===')


def mostFreqBigram(freqBiagram, numberOfBiagram):
  text = displayNgrams(preprocess(str), 2)
  biGram = FreqDist(text).most_common(len(list(text)))
  result = list()
  temp = 0

  for x in biGram:
    if x[1] == freqBiagram and temp < numberOfBiagram:
      result.append(x[0])
      temp += 1

  return result


print('frequency = 4, n = 1')
print(mostFreqBigram(4, 1))

print('frequency = 2, n = 3')
print(mostFreqBigram(2, 3))

print('frequency = 1, n = 5')
print(mostFreqBigram(1, 5))


def propableOccur(bigrams):
  bigram_measures = nltk.collocations.BigramAssocMeasures()
  finder = BigramCollocationFinder.from_documents(bigrams)
  return sorted(finder.nbest(bigram_measures.pmi, 10))  # raw_freq


print('lastone')  # ask teacher about some wrong examples
print(*propableOccur(displayNgrams(preprocess(str), 2)), sep='\n')


def scoreBiagram(bigrams):
  bigram_measures = nltk.collocations.BigramAssocMeasures()
  finder = BigramCollocationFinder.from_documents(bigrams)
  finder.apply_freq_filter(2)
  scored = finder.score_ngrams(bigram_measures.pmi)
  return scored


print('scooore')

print(*scoreBiagram(displayNgrams(preprocess(str), 2)), sep='\n')

print('POS TAGGERS')


def tagger(text):
  tokenized = nltk.word_tokenize(text)
  return nltk.pos_tag(tokenized)


print(tagger(str))

print('numofffftags')


def numOfTags(taggedText):
  stats = {}
  for k, v in taggedText:
    if v in stats:
      stats[v] += 1
    else:
      stats[v] = 1
  return sorted(stats.items(), key=lambda x: x[1], reverse=True)[:10]


print(numOfTags(tagger(str)))
