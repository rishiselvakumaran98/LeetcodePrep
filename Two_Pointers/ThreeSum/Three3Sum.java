package Two_Pointers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Three3Sum {
    // Creating a list of lists of integers.
    private List<List<Integer>> results = new ArrayList<List<Integer>>();
    public List<List<Integer>> threeSum(int[] nums) {
        // First we sort the arrays 
        // then we select a specific element and then pass it to a two_sum_sorted function
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2; i++){
            // avoid duplication here by skipping indexes if they are more than 0 but if [1,2,2,3,3,4] <-- skip the 2s and 3s
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            two_sum_sorted(nums, i, 0);
        }
        return results;
    }

    public void two_sum_sorted(int[] nums, int i, int target){
        int l = i+1, r = nums.length-1;
        while(l < r){
            int remaining = nums[i] + nums[l] + nums[r];
            if (remaining < target){
                l++;
            }
            else if(remaining > target){
                r--;
            }
            else{
                results.add(Arrays.asList(nums[i], nums[l], nums[r]));
                // Slip the duplications in the remaining iterations
                while(l < r && nums[l] == nums[l+1]) l++;
                while (l < r && nums[r] == nums[r-1]) r--;
                l++;
                r--;
            }
        }
    }
}
