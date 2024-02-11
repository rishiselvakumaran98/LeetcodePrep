package Two_Pointers.TrappingRainWater;

class TrappingRainWater {
    public int trap(int[] height) {
        // Brute force approach:
        // Create a max array for the left iteration of the rain water
        // Create another max array for the right iteration
        // Now go through both the arrays and add to the sum += min(left_arr[i], right_arr[i])-height[i]
        // Return the sum
        int n = height.length, rainWater = 0;
        int[] leftMaxArray = new int[n];
        int[] rightMaxArray = new int[n];
        // Populate the leftMaxArray
        for (int i=1; i < n; i++){
            leftMaxArray[i] = Math.max(leftMaxArray[i-1], height[i-1]);
        }
        // Populate the rightMaxArray
        for (int i=n-1; i > 0; i--){
            rightMaxArray[i-1] = Math.max(rightMaxArray[i], height[i]);
        }
        // Now go through both the arrays and add to the sum += min(left_arr[i], right_arr[i])-height[i]
        for (int i=0; i<n; i++){
            int currentVal = Math.min(leftMaxArray[i], rightMaxArray[i])-height[i];
            rainWater += currentVal > 0 ? currentVal : 0;
        }
        return rainWater;
    }
    public int trap_optimized(int[] height) {
        // Optimized version: We use a Two Ptr approach starting from left and Right Ptr 
        // Check if the leftMax is lesser than the rightMax
        // Then we increment l as we start it 
        //  sub leftMax = Math.min(leftMax, height[l]);
        //  add the leftMax - height[l] to the rainwater count; 
        // Else we increment r as we start it 
        //  sub rightMax = Math.min(rightMax, height[r]);
        //  add the rightMax - height[r] to the rainwater count;
        int l =0, r = height.length-1, result = 0;
        int maxLeft=height[l], maxRight=height[r];
        while(l < r) {
            if (maxLeft < maxRight){
                l++;
                maxLeft = Math.max(maxLeft, height[l]);
                result += maxLeft-height[l];
            } else {
                r--;
                maxRight = Math.max(maxRight, height[r]);
                result += maxRight-height[r];
            }
        }
        return result;
    }
}