import nltk
from nltk.collocations import BigramCollocationFinder
from nltk import ngrams
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd

df = pd.read_csv("../Reviews.csv")
saved_column = df['Text']

for file in saved_column:

    def pre_process(text):
        tokenize = nltk.word_tokenize(text)
        tokenize = [x.lower() for x in tokenize if x.isalpha()]

        stop_words = set(stopwords.words("english"))
        filtered_sentence = list()

        for word in tokenize:
            if word not in stop_words:
                filtered_sentence.append(word)

        return filtered_sentence


    pre_process_file = pre_process(file)

    print('=============================================PART 01 =====================================================')
    print('Tokenize version of the text that does not contain neither any stop words nor any punctuations')
    print('==========================================================================================================')
    print(*pre_process_file, sep='\n')


    def most_frequent(tokenize_text, how_many):
        stem_words = list()
        for x in tokenize_text:
            stem_words.append(PorterStemmer().stem(x))
        return FreqDist(stem_words).most_common(how_many)


    print('=============================================PART 02 =====================================================')
    print('Number of the occurrences of the frequent words')
    print('==========================================================================================================')
    print(most_frequent(pre_process_file, 10))


    def display_n_grams(tokenize_text, how_many):
        return ngrams(tokenize_text, how_many)


    print('=============================================PART 03 =====================================================')
    print('Displays n grams only as many as the desired n.')
    print('==========================================================================================================')
    print(*list(display_n_grams(pre_process_file, 2)), sep='\n')


    def most_freq_bi_gram(freq_bi_gram, number_of_bi_gram):
        bi_gram = FreqDist(display_n_grams(pre_process_file, 2)) \
            .most_common(len(list(display_n_grams(pre_process_file, 2))))
        result = list()
        temp = 0

        for x in bi_gram:
            if x[1] == freq_bi_gram and temp < number_of_bi_gram:
                result.append(x[0])
                temp += 1

        return result


    print('=============================================PART 04 =====================================================')
    print('Bi grams with the given frequency rate.')
    print('==========================================================================================================')
    print('frequency = 4, n = 1')
    print(most_freq_bi_gram(4, 1))

    print('frequency = 2, n = 3')
    print(most_freq_bi_gram(2, 3))

    print('frequency = 1, n = 5')
    print(most_freq_bi_gram(1, 5))


    def probable_occur(bi_gram):
        bi_gram_measures = nltk.collocations.BigramAssocMeasures()
        finder = BigramCollocationFinder.from_documents(bi_gram)
        return sorted(finder.nbest(bi_gram_measures.pmi, 10))  # raw_freq


    print('=============================================PART 05 =====================================================')
    print('Top 10 bi grams.')
    print('==========================================================================================================')
    print(*probable_occur(display_n_grams(pre_process_file, 2)), sep='\n')  # ask teacher about some wrong examples


    def score_bi_gram(bi_gram):
        bi_gram_measures = nltk.collocations.BigramAssocMeasures()
        finder = BigramCollocationFinder.from_documents(bi_gram)
        finder.apply_freq_filter(2)
        scored = finder.score_ngrams(bi_gram_measures.pmi)
        return scored


    print('=============================================PART 06 =====================================================')
    print('Score information of the bi grams that are equal to or more frequent than 2.')
    print('==========================================================================================================')
    print(*score_bi_gram(display_n_grams(pre_process_file, 2)), sep='\n')


    def tag_given_text(text):
        tokenize = nltk.word_tokenize(text)
        return nltk.pos_tag(tokenize)


    print('=============================================PART 07 =====================================================')
    print('Produces a list of words.')
    print('==========================================================================================================')
    print(tag_given_text(file))


    def num_of_tags(tagged_text):
        stat = {}
        for x in tagged_text:
            if x[1] in stat:
                stat[x[1]] += 1
            else:
                stat[x[1]] = 1
        return sorted(stat.items(), key=lambda y: y[1], reverse=True)[:10]


    print('=============================================PART 08 =====================================================')
    print('Most common tags.')
    print('==========================================================================================================')
    print(num_of_tags(tag_given_text(file)))


    def get_specified_tag(tagged_text, tag):
        define_text = list()
        for k, v in tagged_text:
            if tag in v:
                define_text.append(k)
        return define_text


    print('=============================================PART 09 =====================================================')
    print('Displays the words in descending order for the specified tag.')
    print('==========================================================================================================')
    print(get_specified_tag(tag_given_text(file), 'NN'))


    def list_word_occurrences_information(text):
        tokenize = nltk.word_tokenize(text)
        tokenize = [word.lower() for word in tokenize if word.isalpha()]
        sorted_freq = sorted(((value, key) for (key, value) in FreqDist(tokenize).items()), reverse=True)

        freq_percent = []
        words = []
        for i in sorted_freq:
            freq_percent.append(i[0] * 100 / len(tokenize))
            words.append(i[1])

        index = []
        for i in range(1, len(freq_percent) + 1):
            index.append(i)

        temp = []
        for i in index:
            temp.append(i * freq_percent[i - 1] / 100)

        count = []
        for i in sorted_freq:
            count.append(i[0])

        rank_df = pd.DataFrame(data={'Rank': index})
        words_df = pd.DataFrame(data={'Word': words})
        counts_df = pd.DataFrame(data={'Counts': count})
        freq_df = pd.DataFrame(data={'Frequency': freq_percent})
        freq_rank_df = pd.DataFrame(data={'Freq X Rank': temp})
        data_frame_result = pd.concat([rank_df, words_df, counts_df, freq_df, freq_rank_df], axis=1)

        return data_frame_result


    print('=============================================PART 10 =====================================================')
    print('List all the words with number of occurrences information')
    print('==========================================================================================================')
    print(list_word_occurrences_information(file))
