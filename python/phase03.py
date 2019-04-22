from nltk.corpus import brown
import nltk

import os.path
import argparse
import grammar_converter

temp = {}
for word, pos in sorted(key for key in brown.tagged_words()[:1000]):
    if word not in temp:
        temp[word] = pos

for x in temp:
    print(f'{x:<20} {temp[x]}')


groucho_grammar = grammar_converter.convert_grammar(grammar_converter.read_grammar('some-grammar.txt'))

ss = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']

parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)
