import nltk
from nltk.corpus import brown

print('============================================= PART 01 =====================================================')
print('Constructs a lexicon that maps words of the English language to lexical categories. (1000 items)')
print('==========================================================================================================')


def construct_lexicon(words, how_many):
    temp = {}
    for word, pos in sorted(key for key in words[:how_many]):
        if word not in temp:
            temp[word] = pos

    for x in temp:
        print(f'{x:<20} {temp[x]}')


construct_lexicon(brown.tagged_words(), 1000)

print('============================================= PART 02 =====================================================')
print('Constructs a grammar that defines the structure of a sentence.')


def generate_grammar(sent, gra):
    parser = nltk.ChartParser(gra, trace=1)
    for tree in parser.parse(sent):
        print(tree)


grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> 'I' | N V Det N
VP -> V NP | VP PP
Det -> 'a' | 'in' | Det Det
N -> 'Susie' | 'shoe' | 'shine' | 'shop' | N N | N PP
V -> 'saw' | 'sitting'
P -> 'in'
""")
generate_grammar("I saw Susie sitting in a shoe shine shop".split(' '), grammar)
