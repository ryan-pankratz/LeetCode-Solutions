/*
 * A solution file for the LeetCode Container with most water problem in C#.
 */

public class Solution {
    public int MaxArea(int[] height) {
        int k = 0;
        int l = height.Length - 1;
        int maxArea = 0;

        while (k != l) {
            if (maxArea < Math.Min(height[k], height[l]) * (l - k)) {
                maxArea = Math.Min(height[k], height[l]) * (l - k);
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