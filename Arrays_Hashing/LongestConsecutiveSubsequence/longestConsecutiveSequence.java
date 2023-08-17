package Arrays_Hashing;

import java.util.HashSet;

public class longestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int i: nums){
            set.add(i);
        }
        int longest = 0;
        for(int x: nums){
            if(!set.contains(x-1)){
                int y = x+1;
                while(set.contains(y)){
                    y++;
                }
                longest = Math.max(longest, y-x);
            }
        }
        return longest;
    }
}
