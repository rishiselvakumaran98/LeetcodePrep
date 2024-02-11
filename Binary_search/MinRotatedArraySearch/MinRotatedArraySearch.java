package Binary_search.MinRotatedArraySearch;

public class MinRotatedArraySearch {
    public int findMin(int[] nums) {
        // if the array is sorted and is normal like nums[0] < nums[-1]
        // since we assume that the array is gonna be sorted
        // we just return the first element
        int l = 0, r = nums.length-1;
        // But in rotated array, nums[0] > nums[-1]
        // So if this condition is true we go to middle and check if nums[m] > nums[r]
        // if so we shift the middle ptr to right side of array where l = m+1
        // else we shift middle ptr to left side of array 
        while (l < r){
            int m = (l+r)/2;
            if (nums[m] > nums[r]){
                l = m+1;
            }
            else {
                r = m;
            }
        }
        return nums[l];

    }
}
