import nltk
from nltk.corpus import brown

print('=============================================PART 01 =====================================================')
print('Constructs a lexicon that maps words of the English language to lexical categories. (1000 items)')
print('==========================================================================================================')

def constructLexicon():
    temp = {}
    for word, pos in sorted(key for key in brown.tagged_words()[:1000]):
        if word not in temp:
            temp[word] = pos

    for x in temp:
        print(f'{x:<20} {temp[x]}')


constructLexicon()

print('=============================================PART 02 =====================================================')
print('Constructs a grammar that denes the structure of a sentence.')
print('==========================================================================================================')
grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
def genarateGrammer(sent):
    parser = nltk.ChartParser(grammar, trace = 1)
    for tree in parser.parse(sent):
        print(tree)



example_sentence = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
genarateGrammer(example_sentence)