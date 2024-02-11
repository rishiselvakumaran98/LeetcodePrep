package Sliding_Window.BestTimeToBuyStock;

public class BestTimeToBuyStock {
    public int maxProfit(int[] prices) {
        int maxProfit=0;
        // maximizing profit is when we buy on low price and sell it at higher price
        int minPrice = Integer.MAX_VALUE;
        for(int i=0; i< prices.length; i++){
            minPrice = Math.min(minPrice, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i]-minPrice);
        }
        return maxProfit;
    }
}
