const natural = require("natural")
const util = require('util')
const nGram = require('n-gram')
const fs = require('fs')

let text = ''
let stopWords = []

try {
  text = fs.readFileSync('file.txt', 'utf8').toString()
  stopWords = fs.readFileSync('stopWords.txt', 'utf-8').toString().split()[0]
} catch (e) {
  console.log('Error: ', e.stack)
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

  tokenizeWithoutStopWords.forEach(x => ps.push(natural.PorterStemmer.stem(x)))

  ps.forEach(x => {
    map.has(x) ? map.set(x, map.get(x) + 1) : map.set(x, 1)
  })

  let lastOne = [...map].sort((a, b) => (a[1] === b[1] ? 0 : a[1] > b[1] ? -1 : 1)).slice(0, howManyWords) // You can use new Map([...map].sort(sortStringValues)) to avoid creating object at the end

  lastOne.forEach((val) => {
    result.push(val)
  })

  return result
}

mostFrequent(preProcessed, 5).forEach((val) => console.log(val))

// displayNgrams = (preProcessed, n) => {
// }

// console.log(displayNgrams(preProcessed, 5))