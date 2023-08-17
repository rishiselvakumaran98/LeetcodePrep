package Arrays_Hashing.ContainsDuplicate.Java;

import java.util.HashSet;
import java.util.Set;

public class ContainsDuplicate {
    public static boolean containsDuplicate(int[] nums) {
        // have a set to keep track of all the numbers visited in the array
        Set<Integer> visited = new HashSet<>();
        for (int num: nums){
            if(!visited.add(num)){
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[] test1 = {1,2,3,1}; // true
        int[] test2 = {1,2,3,4}; // false
        int[] test3 = {1,1,1,3,3,4,3,2,4,2}; // true
        assert (ContainsDuplicate.containsDuplicate(test1)==true);
        assert (ContainsDuplicate.containsDuplicate(test2)==false);
        assert (ContainsDuplicate.containsDuplicate(test3)==true);
    }
}
