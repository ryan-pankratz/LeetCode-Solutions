int search(int* nums, int numsSize, int target){
    if (numsSize == 1) {
        if (*nums == target) {
            return 0;
        }
        else {
            return -1;
        }
    }

    int index = numsSize / 2;
    int *mid = nums + index;

    if (*mid == target) {
        return index;
    }
    else if (*mid < target) {
        if (numsSize % 2 != 0) {
            numsSize = (numsSize / 2) + 1;
        }
        else {
            numsSize = numsSize / 2;
        }

        int val = search(mid, numsSize, target);

        if (val == -1) {
            return -1;
        }

        return index + val;
    }
    else {
        return search(nums, numsSize / 2, target);
    }
}