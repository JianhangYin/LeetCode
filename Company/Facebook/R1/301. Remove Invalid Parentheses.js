function helper(inputStr, ans, lastI, lastJ, comArray) {
  let stackValue = 0;
  for (let i = lastI; i <= inputStr.length; i++) {
    if (inputStr[i] === comArray[0]) stackValue += 1;
    if (inputStr[i] === comArray[1]) stackValue -= 1;
    if (stackValue >= 0) continue;
    for (let j = lastJ; j <= i; j++) {
      if (inputStr[j] === comArray[1] && (j === lastJ || inputStr[j - 1] !== comArray[1])) {
        helper(inputStr.slice(0, j) + inputStr.slice(j + 1, inputStr.length), ans, i, j, comArray);
      }
    }
    return;
  }
  let reverseStr = inputStr.split("").reverse().join("");
  if (comArray[0] === '(') {
    helper(reverseStr, ans, 0, 0, [')', '(']);
  } else {
    ans.push(reverseStr);
  }
}
/**
 * @param {string} s
 * @return {string[]}
 */
let removeInvalidParentheses = function(s) {
  let ans = [];
  helper(s, ans, 0, 0, ['(', ')']);
  return ans;
};


const result = removeInvalidParentheses("()())()");
console.log(result);


