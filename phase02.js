const natural = require("natural");
const util = require('util')
const nGram = require('n-gram')
const fs = require('fs')

let text = ''

try {
  let data = fs.readFileSync('file.txt', 'utf8');
  text = data.toString()
} catch (e) {
  console.log('Error: ', e.stack);
  process.exit()
}

/**
 * @part 01
 * @param text
 * @returns tokenize version of the text that does not contain neither any stop words nor any punctuations
 */
preprocess = (text) => {
  let tokenizer = new natural.WordTokenizer()
  let tokenizeText = tokenizer.tokenize(text.toLowerCase())
  let stopWords = [
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "am",
    "an",
    "and",
    "any",
    "are",
    "aren't",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can't",
    "cannot",
    "could",
    "couldn't",
    "did",
    "didn't",
    "do",
    "does",
    "doesn't",
    "doing",
    "don't",
    "down",
    "during",
    "each",
    "few",
    "for",
    "from",
    "further",
    "had",
    "hadn't",
    "has",
    "hasn't",
    "have",
    "haven't",
    "having",
    "he",
    "he'd",
    "he'll",
    "he's",
    "her",
    "here",
    "here's",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "how's",
    "i",
    "i'd",
    "i'll",
    "i'm",
    "i've",
    "if",
    "in",
    "into",
    "is",
    "isn't",
    "it",
    "it's",
    "its",
    "itself",
    "let's",
    "me",
    "more",
    "most",
    "mustn't",
    "my",
    "myself",
    "no",
    "nor",
    "not",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "ought",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "shan't",
    "she",
    "she'd",
    "she'll",
    "she's",
    "should",
    "shouldn't",
    "so",
    "some",
    "such",
    "than",
    "that",
    "that's",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "there's",
    "these",
    "they",
    "they'd",
    "they'll",
    "they're",
    "they've",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "very",
    "was",
    "wasn't",
    "we",
    "we'd",
    "we'll",
    "we're",
    "we've",
    "were",
    "weren't",
    "what",
    "what's",
    "when",
    "when's",
    "where",
    "where's",
    "which",
    "while",
    "who",
    "who's",
    "whom",
    "why",
    "why's",
    "with",
    "won't",
    "would",
    "wouldn't",
    "you",
    "you'd",
    "you'll",
    "you're",
    "you've",
    "your",
    "yours",
    "yourself",
    "yourselves"
  ];
  return tokenizeText.filter(x => !stopWords.includes(x))
}

const preProcessed = preprocess(text)

console.log(util.inspect(preProcessed, {maxArrayLength: null}))

/**
 * @part 02
 * @param tokenizeWithoutStopWords
 * @param howManyWords
 * @returns Array : number of the occurrences of the frequent words
 */
mostFrequent = (tokenizeWithoutStopWords, howManyWords) => {
  let result = []
  let ps = []
  let map = new Map()
  const sortStringValues = (a, b) => (a[1] === b[1] ? 0 : a[1] > b[1] ? -1 : 1)

  tokenizeWithoutStopWords.forEach(x => ps.push(natural.PorterStemmer.stem(x)))

  ps.forEach(x => {
    map.has(x) ? map.set(x, map.get(x) + 1) : map.set(x, 1)
  })

  let lastOne = [...map].sort(sortStringValues).slice(0, howManyWords) // You can use new Map([...map].sort(sortStringValues)) to avoid creating object at the end

  lastOne.forEach((val) => {
    result.push(val)
  })

  return result
}

console.log(mostFrequent(preProcessed, 5).forEach((val) => console.log(val)))

displayNgrams = (preProcessed, n) => {
}

// console.log(displayNgrams(preProcessed, 5))