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

    public int longestConsecutive_alternative(int[] nums) {
        // Keep a hashSet to store num 
        // Iterate through nums, if the current num-1 is already in hashSet
        // then keep iterating and incrementing count
        // if num -1 not in hashset then reset count=1
        // By default add num into hashSet
        HashSet<Integer> visited = new HashSet<>();
        for (int n: nums){
            visited.add(n);
        }
        int maxCount = 0;
        for (int n: nums){
            int count = 1;
            // check if the current number is first in sequence
            if(!visited.contains(n-1)){
                // check how long the sequence is
                int i = n+1;
                while (visited.contains(i)){
                    count++;
                    i++;
                }
            }
            maxCount = Math.max(count, maxCount);
        }
        return maxCount;
    }
}
