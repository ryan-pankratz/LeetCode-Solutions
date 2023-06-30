/*
 * A solution file for the LeetCode Container with most water problem in Java.
 */

class Solution {
    public int maxArea(int[] height) {
        int k = 0;
        int l = height.length - 1;
        int maxArea = 0;

        while (k != l) {
            if (maxArea < Math.min(height[k], height[l]) * (l - k)) {
                maxArea = Math.min(height[k], height[l]) * (l - k);
            }

            if (height[k] > height[l]) {
                l--;
            }
            else {
                k++;
            }
        }
        return maxArea;
    }
}
