/*
 *  A solution file for the LeetCode Container with most water problem in Javascript.
 */

/**
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function(height) {
    let k = 0;
    let l = height.length - 1;
    let maxFoundArea = 0;

    while (k != l) {
        if (maxArea < min(height[k], height[l]) * (l - k)) {
            maxFoundArea = min(height[k], height[l]) * (l - k);
        }

        if (height[k] < height[l]) {
            k += 1;
        }
        else {
            l -= 1;
        }
    }
    return maxFoundArea;
};

function min(a, b) {
    if (a < b) {return a;}
    return b;
}

