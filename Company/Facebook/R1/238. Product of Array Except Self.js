/**
 * @param {number[]} nums
 * @return {number[]}
 */
let productExceptSelf = function(nums) {
  let res = [1];
  for (let i = 1; i < nums.length; i++) {
    res[i] = res[i - 1] * nums[i - 1];
  }
  let right = 1;
  for (let j = nums.length - 1; j >= 0; j--) {
    res[j] = res[j] * right;
    right = right * nums[j];
  }
  return res;
};
