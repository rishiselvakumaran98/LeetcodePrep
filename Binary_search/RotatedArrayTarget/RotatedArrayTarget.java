package Binary_search.RotatedArrayTarget;

public class RotatedArrayTarget {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        // Make sure nums1 is the smaller array and nums2 is larger array
        if (m > n){
            return findMedianSortedArrays(nums2, nums1);
        }

        int total = m+n;
        int half = (total+1)/2;
        double result = 0.0;
        int l = 0, r = m;
        while(l<=r){
            int i = l+(r-l)/2;
            int j = half-i;
            int left1 = i > 0 ? nums1[i-1] : Integer.MIN_VALUE;
            int right1 = i < m ? nums1[i] : Integer.MAX_VALUE;
            int left2 = j > 0 ? nums2[j-1] : Integer.MIN_VALUE;
            int right2 = j < n ? nums2[j] : Integer.MAX_VALUE;

            // Correct Partition
            if (left1 <= right2 && left2 <= right1){
                if (total % 2 == 0){
                    result = (Math.max(left1, left2) + Math.min(right1, right2))/2.0;
                } else {
                    result = Math.max(left1, left2);
                }
                break;
            }
            else if (left1 > right2){
                r = i-1; 
            }
            else {
                l = i+1;
            }
        }
        return result;
    }
}
