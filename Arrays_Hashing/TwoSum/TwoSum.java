package Arrays_Hashing;

import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target){
        HashMap<Integer, Integer> visited = new HashMap<>();
        int[] return_arr = new int[2];
        for(int i = 0 ; i< nums.length; i ++){
            int other_num = target-nums[i];
            if(visited.containsKey(other_num)){
                int j = visited.get(other_num);
                return_arr[0] = i;
                return_arr[1] = j;
                return return_arr;
            }
            else{
                visited.put(nums[i], i);
            }
        }
        return_arr[0] = -1;
        return_arr[1] = -1;
        return return_arr;
    }
}
