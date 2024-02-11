package Dynamic_Programming.Best_Time_to_Buy_w_cooldown;

public class BestTimeToBuyWCooldown {
    public int maxProfit(int[] prices) {
        int buy = Integer.MIN_VALUE, prev_sell = 0, sell =0, prev_buy;
        for (int price: prices){
            prev_buy = buy;
            buy = Math.max(prev_sell-price, prev_buy);
            prev_sell = sell;
            sell = Math.max(prev_buy + price, prev_sell);
        }
        return sell;
    }
}
