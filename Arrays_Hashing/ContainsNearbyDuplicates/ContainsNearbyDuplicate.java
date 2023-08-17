package Arrays_Hashing;

import java.util.HashMap;

public class ContainsNearbyDuplicate {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // start from i and traverse until k
        HashMap<Integer, Integer> visited = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (!visited.containsKey(nums[i])){
                visited.put(nums[i], i);
            } else {
                int j = visited.get(nums[i]);
                if (Math.abs(i-j) <= k){
                    return true;
                } else {
                    // update the key and value to current index
                    visited.put(nums[i], i);
                }
            }
        }
        return false;
    }
}
