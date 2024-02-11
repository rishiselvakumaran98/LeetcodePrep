package Binary_search.KokoBananas;

public class KokoBananas {
    public int minEatingSpeed(int[] piles, int h) {
        // Take the minimum banana in a pile
        // Take the maximum bananas in a pile
        // use a binary search method to find a k integer and use it to calculate the total time taken to 
        // finish the banana within h hours, if total_time > h then shift l = m-1
        // else shift r = m+1;

        // Find the min, max in a pile
        int max_val = Integer.MIN_VALUE;
        for (int i = 0; i < piles.length; i++){
            if (piles[i] > max_val){
                max_val = piles[i];
            }
        }
        int l = 0, r = max_val, k = Integer.MAX_VALUE;
        while(l <= r){
            int m = (l+r)/2;
            int total_time = 0;
            for (int i = 0; i < piles.length; i++){
                total_time += Math.ceil(piles[i]/(double)m);
            }
            if (total_time <= h){
                k = Math.min(k, m);
                r = m-1;
            }
            else {
                l = m+1;
            }
        }
        return k;
    }
}
