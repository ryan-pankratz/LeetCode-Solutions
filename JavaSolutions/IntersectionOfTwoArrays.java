import java.util.ArrayList;

class IntersectionOfTwoArrays {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> al = this._intersectionHelper(nums1, nums2);
        int[] retArr = new int[al.size()];
        for (int i = 0; i < al.size(); i++) {
            retArr[i] = al.get(i);
        }
        return retArr;
    }

    private ArrayList<Integer> _intersectionHelper(int[] nums1, int[] nums2) {
        ArrayList retVal = new ArrayList<Integer>();
        for (int num : nums1) {
            for (int num2 : nums2) {
                if (num == num2 && !retVal.contains(num))
                    retVal.add(num);
            }
        }
        return retVal;
    }
}