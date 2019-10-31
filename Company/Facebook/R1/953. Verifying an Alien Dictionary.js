/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
let isAlienSorted = function(words, order) {
  let alpha = {};
  for (let i = 0; i < order.length; i ++) {
    alpha[order[i]] = i;
  }
  let res = true;
  for (let i = 1; i < words.length; i ++) {
    let preWord = words[i - 1];
    let curWord = words[i];
    let j = 0;
    while (preWord[j] && curWord[j]) {
      if (alpha[preWord[j]] > alpha[curWord[j]]) {
        res = false;
      } else if (alpha[preWord[j]] < alpha[curWord[j]]) {
        break;
      }
      j += 1;
    }
    if (preWord[j] && !curWord[j]){
      res = false;
    }
  }
  return res;
};
