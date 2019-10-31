/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
let addBinary = function(a, b) {
  a = a.split("").reverse().join("");
  b = b.split("").reverse().join("");
  let res = "";
  let aP = 0;
  let bP = 0;
  let forward = 0;
  while (aP < a.length || bP < b.length) {
    let numA = isNaN(Number(a[aP])) ? 0 : Number(a[aP]);
    let numB = isNaN(Number(b[bP])) ? 0 : Number(b[bP]);
    let result = numA +  numB + forward;
    if (result === 0){
      res += 0;
      forward = 0;
    } else if (result === 1) {
      res += 1;
      forward = 0;
    } else if (result === 2) {
      res += 0;
      forward = 1;
    } else {
      res += 1;
      forward = 1;
    }
    aP++;
    bP++;
  }
  res += forward === 0 ? 0 : 1;
  return res.split("").reverse().join("");
};

a = "1010";
b = "1011";

console.log(addBinary(a, b));
