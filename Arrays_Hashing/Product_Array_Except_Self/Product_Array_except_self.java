package Arrays_Hashing;

import java.util.Arrays;

public class Product_Array_except_self {
    // More optimal solution to do in O(1) Space
    public int[] optimalSolution(int[] nums){
        // Keep two arrays left and right
        // multiply the product of the numbers in the left except self
        // multiply the product of the numbers in the right except self
        int n = nums.length;
        int[] result_array = new int[n];
        Arrays.fill(result_array, 1);
        int pre = 1; 
        int post = 1;
        for(int i = 0; i < n; i++){
            result_array[i] *= pre;
            pre *= nums[i];
            result_array[n-i-1] *= post;
            post *= nums[n-i-1];
        }
        return result_array;
    }
    
    
    public int[] solution(int[] nums){
        // Keep two arrays left and right
        // multiply the product of the numbers in the left except self
        // multiply the product of the numbers in the right except self
        int n = nums.length;
        int[] left = new int[n]; Arrays.fill(left, 1);
        int[] right = new int[n]; Arrays.fill(right, 1);
        int[] result = new int[n];

        for(int i=1; i<n; i++){
            left[i] = left[i-1]*nums[i-1];
        }
        for(int i = n-2; i >= 0; i--){
            right[i] = right[i+1]*nums[i+1];
        }
        for(int i=0; i < n; i++){
            result[i] = left[i] * right[i];
        }
        return result;
    }
}
