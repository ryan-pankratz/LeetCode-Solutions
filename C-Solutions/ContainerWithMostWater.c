/*
 * A solution file for the LeetCode Container with most water problem in C.
 */

int maxArea(int* height, int heightSize){
    int k = 0;
    int l = heightSize - 1;
    int maxArea = 0;

    while (k != l) {
        if (maxArea < minimum(height[k], height[l]) * (l - k)) {
            maxArea = minimum(height[k], height[l]) * (l - k);   
        }

        if (height[k] < height[l])
            k += 1;
        else
            l -= 1;
    }
    return maxArea;
}

int minimum(int a, int b) {
    if (a > b) return b;
    return a;
}