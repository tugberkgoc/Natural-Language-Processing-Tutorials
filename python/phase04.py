import re
import pandas as pd
from sklearn.svm import SVC
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.metrics import r2_score
from nltk.corpus import wordnet as wn
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from nltk.stem.porter import PorterStemmer
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix

# nltk.download('wordnet')

# MAIN
df = pd.read_csv("../test.csv")

reviews = df.iloc[:, 9]
scores = df.iloc[:, 6]

reviews_array = []
for i in reviews:
    reviews_array.append(i)


def clean(given_corpus):
    cleaned_text = re.sub('[^a-zA-Z]', ' ', given_corpus).lower().split()
    cleaned_corpus = [PorterStemmer().stem(word) for word in cleaned_text if
                      not word in set(stopwords.words('english'))]
    return ' '.join(cleaned_corpus)


corpus = []
for i in reviews_array:
    corpus.append(clean(i))

print('============================================= Phase 04 ====================================================')
print('Bag of Words')
print('===========================================================================================================')
cv = CountVectorizer(max_features=10000)
X = cv.fit_transform(corpus).toarray()
print(X)
y = scores

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

print('Gaussian NB')
print('===========================================================================================================')

classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_prediction_naive_bayes = classifier.predict(X_test)

print('Accuracy score for Naive Bayes')
print('===========================================================================================================')

print(accuracy_score(y_prediction_naive_bayes, y_test))
print(classification_report(y_test, y_prediction_naive_bayes))

print('Linear Regression')
print('===========================================================================================================')

clf = LinearRegression(normalize=True)
clf.fit(X_train, y_train)
y_prediction_linear = clf.predict(X_test)

print("r^2 score for Linear")
print('===========================================================================================================')

print(r2_score(y_test, y_prediction_linear))

print('SVM')
print('===========================================================================================================')

model = SVC(kernel='linear')
model.fit(X_train, y_train)
y_prediction_SVM = model.predict(X_test)

print('Confusion Matrix for SVM')
print('===========================================================================================================')

print(confusion_matrix(y_test, y_prediction_SVM))
print(accuracy_score(y_prediction_SVM, y_test))
print(classification_report(y_test, y_prediction_SVM))

print('KNN')
print('===========================================================================================================')
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, y_train)

print('Predicted test results')
print('===========================================================================================================')
y_prediction_knn = classifier.predict(X_test)

print('Making the Confusion Matrix')
print('===========================================================================================================')
cm = confusion_matrix(y_test, y_prediction_knn)

print(accuracy_score(y_prediction_knn, y_test))

print('WORD NET')
print('===========================================================================================================')

ex_01 = word_tokenize("People can understand complicated situations.")
ex_02 = word_tokenize("Monkey can not think as people do in complicated situations.")

sum_result = 0
sim_array = []

for r in ex_01:
    for s in ex_02:
        n = wn.synsets(r)
        g = wn.synsets(s)
        for i in g:
            if i is not None:
                if type(i.path_similarity(n[0])) is float:
                    sim_array.append(i.path_similarity(n[0]))
                    print(i.path_similarity(n[0]))

result_list = list(dict.fromkeys(sim_array))
print(result_list)

for i in result_list:
    sum_result = sum_result + i
