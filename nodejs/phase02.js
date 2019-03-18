const natural = require("natural")
const util = require('util')
const nGram = require('n-gram')
const fs = require('fs')

let text = ''
let stopWords = []

try {
  text = fs.readFileSync('../file.txt', 'utf8').toString()
  stopWords = fs.readFileSync('../stopWords.txt', 'utf-8').toString().split()[0]
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
  return tokenizeText.filter(x => !stopWords.includes(x)).filter(x => isNaN(x))
}

const preProcessed = preprocess(text)

console.log('=============================================PART 01 =====================================================')
console.log('Tokenize version of the text that does not contain neither any stop words nor any punctuations')
console.log('==========================================================================================================')
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

console.log('=============================================PART 02 =====================================================')
console.log('Number of the occurrences of the frequent words')
console.log('==========================================================================================================')
mostFrequent(preProcessed, 5).forEach((val) => console.log(val))

displayNgrams = (preProcessed, n) => {
  const NGrams = natural.NGrams;
  return n == 2 ? NGrams.bigrams(preProcessed) : NGrams.trigrams(preProcessed)
}

console.log('=============================================PART 03 =====================================================')
console.log('Displays n grams only as many as the desired n.')
console.log('==========================================================================================================')
displayNgrams(preProcessed, 2).forEach((val) => console.log(val))

mostFreqBiGram = (freq_bi_gram, number_of_bi_gram) => {
  let map = new Map()

  displayNgrams(preProcessed, 2).forEach(x => {
    let str = x[0] + ' ' + x[1]
    map.has(str) ? map.set(str, map.get(str) + 1) : map.set(str, 1)
  })

  return [...map].filter((x) => x[1] == freq_bi_gram).slice(0, number_of_bi_gram)
}

console.log('=============================================PART 04 =====================================================')
console.log('Bi grams with the given frequency rate.')
console.log('==========================================================================================================')
console.log('frequency = 4, n = 1')
mostFreqBiGram(4,1).forEach(x => console.log(x))
console.log('frequency = 2, n = 3')
mostFreqBiGram(2,3).forEach(x => console.log(x))
console.log('frequency = 1, n = 5')
mostFreqBiGram(1,5).forEach(x => console.log(x))

// tagGivenText = (text) => {

// }

// console.log(tagGivenText(file))