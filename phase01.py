import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 

ps = PorterStemmer()

nltk.download('punkt')
nltk.download('stopwords')

text = "Magnolia is Paul Thomas Anderson's rst big movie that is as wild as it is weird. It is a quick cut, but long and slow narrative between around 10 major characters' lives. I wish it were shorter and more fast paced, but alas Anderson fails to cut down his lms to a more manageable size. However, I thoroughly enjoyed Magnolia. Its unique shots, story twists, and excellent writing keep it in check. Beautiful music and heartfelt writing collide as the intertwined lives of these various gures in society mesh for the most original lm I have seen in a long time. There is no other lm quite like Magnolia. It is like the intense crescendo of harrowing events like Requiem for a Dream with the scattered perspective narrative of Pulp Fiction. It even has moments of the surreal comedy like the Coen Brothers' The Big Lebowski or Fargo."

# Backgammon is one of the oldest known board games. Its history can be traced back nearly 5,000 years to archeological discoveries in the Middle East. It is a two player game where each player has fifteen checkers which move between twenty-four points according to the roll of two dice.

tokenized = nltk.word_tokenize(text)

tokenized_sentence = nltk.sent_tokenize(text)

distribution = FreqDist(tokenized)

stop_words =set(stopwords.words("english"))

filtered_sentence = list()  # instead of []

for word in tokenized:
    if word not in stop_words:
        filtered_sentence.append(word)


stem_words = list()
print("4)")
print("STEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEM")
for x in filtered_sentence:
    stem_words.append(ps.stem(x))
print(stem_words)

print("6)")
print("MOST COMMON STEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEM")
stem_most_common_words = FreqDist(tokenized).most_common(10)
print(stem_most_common_words)

print("2)")
print("================================================================")
print("Tokenized text. ")
print(tokenized)

print("LAST ONEEEEEE")
for x in tokenized:
  if len(x) >= 10:
    print(x)

print("3)")
print("================================================================")
print("The words that are not stop words. ")
print(filtered_sentence)

print("================================================================")
print("All the stop words of English language. ")
print(stop_words)
# Stop Word -> Gereksiz kelime
# It is just shown unneccassary words...

print("5)")
print("================================================================")
print("Basic information about words. ")
print(distribution)

print("================================================================")
print("The tokenized version of our text based on words. ")
print(tokenized)

print("================================================================")
print("Our tokenized text based on sentences. ")
print(tokenized_sentence)

print("7)")
print("VISUALIZIIIIING")