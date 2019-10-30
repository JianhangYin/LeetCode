/*
This is a test file
String, Number, Boolean, Null, Undefined, Symbol
Array, Object, Function

let x; Undefined
let x = 1; Number
let x = 'string'; String
 */

// this is a test file
const stringType = 'test';
const numberType = 666;
const booleanType = true;
const arrayType = [1, 3, 4];
const objectType = {a: 1, b: 2, c: 3};
const nullType = null;
const undefinedType = undefined;
class Pointer {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
} // just a syntactic sugar, it is a function

console.log(typeof Pointer);
console.log(typeof stringType);
console.log(typeof numberType);
console.log(typeof booleanType);
console.log(typeof arrayType);
console.log(typeof objectType);
console.log(typeof nullType);
console.log(typeof undefinedType);

console.log(stringType.constructor);
console.log(numberType.constructor);
console.log(booleanType.constructor);
console.log(arrayType.constructor);
console.log(objectType.constructor);

const numOne = 0.1;
const numTwo = 0.2;
console.log(numOne + numTwo === 0.3);
console.log((numOne * 10 + numTwo * 10) / 10 === 0.3);
/*
str.search(/Regex/)
str.replace('/Regex/, sss)
 */

// callback hell
function f1() {
  console.log('funciton 1');
}
function f2(f) {
  setTimeout(
    () => {
      console.log('function 2');
      f();
    },
    500
  )
}
function f3() {
  console.log('function 3');
}

f1();
f2(f3);
// promise
function f4() {
  return new Promise(
    resolve => {
      setTimeout(
        () => {
          console.log('function 4');
          resolve()
        },
        500
      );
    }
  );
}

f1();
f4().then(() => { f3() });
// async/await
async function f5() {
  f1();
  await f4();
  f3();
}
f5();

// array
// filter, map, sort, reduce

// filter: return a new array, which return value is true
// map: return a new array, return the new value based on the input and function
// sort: sort the array in place
// reduce: return a single value using the reducer function
// forEach: return nothing, change and process the array

a = [1, 3, 4, 5, 7];
console.log(a.reduce((total, current) => total + current, 100));

// Set new object in ES6, similar to Set in Python, using add() to insert item.





















