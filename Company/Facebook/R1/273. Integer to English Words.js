const BILLION = 1000000000;
const MILLION = 1000000;
const THOUSAND = 1000;

function smallHundred(num) {
  const lv1 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(" ");
  const lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split(" ");
  const lv3 = "Hundred".split(" ");
  let numStr = String(num);
  while (numStr.length < 3) {
    numStr = '0' + numStr;
  }
  let res = '';
  if (numStr[0] !== '0') {
    res += lv1[Number(numStr[0]) - 1] + " " + lv3[0] + " ";
  }
  if (numStr[1] !== '0') {
    if (numStr[1] === '1') {
      res += lv1[Number(numStr[1] + numStr[2]) - 1];
    } else {
      if (numStr[2] !== '0') {
        res += lv2[Number(numStr[1]) - 2] + " " + lv1[Number(numStr[2]) - 1];
      } else {
        res += lv2[Number(numStr[1]) - 2];
      }
    }
  } else {
    if (numStr[2] !== '0') {
      res += lv1[Number(numStr[2]) - 1];
    }
  }
  return res.trim();
}
/**
 * @param {number} num
 * @return {string}
 */
let numberToWords = function(num) {
  const lv4 = "Thousand Million Billion".split(" ");
  if (num === 0) return "Zero";
  let res = "";
  if (Math.floor(num / BILLION) !== 0) {
    res += smallHundred(Math.floor(num / BILLION)) + " " + lv4[2] + " ";
    num = num % BILLION;
  }
  if (Math.floor(num / MILLION) !== 0) {
    res += smallHundred(Math.floor(num / MILLION)) + " " + lv4[1] + " ";
    num = num % MILLION;
  }
  if (Math.floor(num / THOUSAND) !== 0) {
    res += smallHundred(Math.floor(num / THOUSAND)) + " " + lv4[0] + " ";
    num = num % THOUSAND;
  }
  res += smallHundred(num);
  return res.trim();
};

console.log(numberToWords(211));

