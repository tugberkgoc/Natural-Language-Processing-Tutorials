const natural = require("natural");
const d3nLine = require("d3node-linechart");
const output = require("d3node-output");

const d3 = require("d3-node")().d3;

const d3n = require("d3node-piechart");

console.log("1)");
console.log(
  "============================================================================================================================"
);
let text =
  "Magnolia is Paul Thomas Anderson’s first big movie that is as wild as it is weird. It is a quick cut, but long and slow narrative between around 10 major characters’ lives. I wish it were shorter and more fast paced, but alas Anderson fails to cut down his films to a more manageable size. However, I thoroughly enjoyed Magnolia. Its unique shots, story twists, and excellent writing keep it in check. Beautiful music and heartfelt writing collide as the intertwined lives of these various figures in society mesh for the most original film I have seen in a long time. There is no other film quite like Magnolia. It is like the intense crescendo of harrowing events like Requiem for a Dream with the scattered perspective narrative of Pulp Fiction. It even has moments of the surreal comedy like the Coen Brothers’ The Big Lebowski or Fargo.";
console.log(text);

console.log("2)");
console.log(
  "============================================================================================================================"
);
const tokenizer = new natural.WordTokenizer();
let tokenizedText = tokenizer.tokenize(text);
console.log(tokenizedText);

const stopwords = [
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

console.log("3) TEXT WITHOUT STOP WORDS"); //
console.log(
  "============================================================================================================================"
);
const textWithoutStopWords = tokenizedText.filter(x => !stopwords.includes(x));
console.log(textWithoutStopWords);

// const compare = (arr1, arr2) => {
//   const objMap = {};

//   arr1.forEach(e1 =>
//     arr2.forEach(e2 => {
//       if (e1 === e2) {
//         objMap[e1] = objMap[e1] + 1 || 1;
//       }
//     })
//   );
//   console.log(Object.keys(objMap).map(e => Number(e)));
// };

// const random = ({ min = 1, max = 10 } = {}) => {
//   return Math.floor(Math.random() * (max - min)) + min;
// };

// console.log(random({ max: 3 }));

console.log("4) PORTER STEMMER - FINDING ROOTS");
console.log(
  "============================================================================================================================"
);
const ps = [];
textWithoutStopWords.forEach(x => ps.push(natural.PorterStemmer.stem(x)));
console.log(ps);

console.log(
  "5) Display the frequency distribution information of the stemmed text."
);
const set1 = new Set([...ps]);

console.log(`FreqDist with ${set1.size} samples and ${ps.length} outcomes.`);

console.log("6) PORTER STEMMER - MOST COMMON");
console.log(
  "============================================================================================================================"
);

const map = new Map();
for (var i = 0; i < ps.length; i++) {
  if (!map.has(ps[i])) {
    map.set(ps[i], 1);
  } else {
    map.set(ps[i], map.get(ps[i]) + 1);
  }
}

const sortStringValues = (a, b) => (a[1] === b[1] ? 0 : a[1] > b[1] ? -1 : 1);

const lastOne = new Map([...map].sort(sortStringValues));

const moreThan10Letters = [];

let howMany = 0;
for (const [k, v] of lastOne.entries()) {
  if (k.length >= 10) {
    moreThan10Letters.push(k);
  }
  if (howMany < 10) {
    console.log(k, v);
    howMany++;
  }
}

console.log(
  "8) List all the words from the text which have equal or more than 10 letters."
);
console.log(moreThan10Letters);

// const data = [{ key: "tugberk", value: 123 }];

// output(
//   "output-multiline",
//   d3n({
//     data,
//     container: `<div id="container"><h2>Multiline Example</h2><div id="chart"></div></div>`,
//     lineColors: ["steelblue", "darkorange"],
//     width: 800,
//     height: 570
//   })
// );