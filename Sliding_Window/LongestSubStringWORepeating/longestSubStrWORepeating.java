package Sliding_Window.LongestSubStringWORepeating;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class longestSubStrWORepeating {
    // My own solution
    public int lengthOfLongestSubstring(String s) {
        // We use a sliding window technique that has two pointers
        // i will be the starting ptr and j will be ptr used to keep track of unique chars until we see the same
        if (s.equals("")){
            return 0;
        }
        Set<Character> substr = new HashSet<>();
        int i = 0, j = 0;
        char[] sArray = s.toCharArray();
        int maxLength = Integer.MIN_VALUE;
        while (j < sArray.length){
            if(!substr.contains(sArray[j])){
                substr.add(sArray[j]);
                j++;
            } else {
                i++;
                substr.clear();
                j=i;
            }
            maxLength = Math.max(maxLength, j-i);
        }
        return maxLength;
    }

    public int lengthOfLongestSubstring_optimal(String s) {
        if (s.length() == 0) return 0;
        Map<Character, Integer> map = new HashMap<>();
        int maxLength = Integer.MIN_VALUE;
        for(int i =0, j =0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                j = Math.max(j, map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            maxLength = Math.max(maxLength, i-j+1);
        }
        return maxLength;
    }
}
