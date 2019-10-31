function sortDistance(a, b) {
  return (Math.pow(a[0], 2) + Math.pow(a[1], 2)) - (Math.pow(b[0], 2) + Math.pow(b[1], 2))
}
/**
 * @param {number[][]} points
 * @param {number} K
 * @return {number[][]}
 */
let kClosest = function(points, K) {
  return points.sort(sortDistance).slice(0,K);
};
