package Arrays_Hashing;

import java.util.HashSet;

class Solution{
    /* 
     * Now assume there are multiple duplicates with 1<= arr[i] <= 10^9, we can find them using negative marking
     * Runtime: O(n)
     * Space: O(1)
     */
    public int findDuplicateNegMarking(int[] arr){
        for(int i = 0; i < arr.length; i++){
            int index = Math.abs(arr[i])-1;
            if(arr[index] < 0){
                return Math.abs(arr[i]);
            }
            arr[index] *= -1;
        }
        return -1;
    }

    /* 
     * Using Set to keep track of the duplicates in the array
     * Runtime: O(n)
     * Space: O(n)
     */
    public int[] findDuplicatesSet(int[] arr){
        HashSet<Integer> visited = new HashSet<>();
        int[] duplicates = new int[arr.length];
        int i=0;
        for (int num: arr){
            if(visited.contains(num)){
                duplicates[i++] = num;
            }
            else{
                visited.add(num);
            }
        }
        return duplicates;
    }

    /*
     * Use Negative marking to find the duplicates in the array
     * Runtime: O(n)
     * Space: (1)
     */  
    public int findDuplicateFastSlowPoint(int[] arr){
        int slow = arr[0];
        int fast = arr[arr[0]];
        while(slow != fast){
            slow = arr[slow];
            fast = arr[arr[fast]];
        }
        // when the cycle ends
        fast = 0;
        while(slow != fast){
            slow = arr[slow];
            fast = arr[fast];
        }
        return slow;
    }

}