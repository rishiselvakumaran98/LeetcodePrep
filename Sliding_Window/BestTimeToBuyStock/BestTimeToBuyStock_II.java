package Sliding_Window.BestTimeToBuyStock;

public class BestTimeToBuyStock_II {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minPrice = Integer.MAX_VALUE;
        for(int i=0; i < prices.length; i++){
            minPrice = Math.min(minPrice, prices[i]);
            if (prices[i] > minPrice){
                maxProfit += prices[i]-minPrice;
                minPrice = prices[i]; // reset the price
            }
        }
        return maxProfit;
    }
}
