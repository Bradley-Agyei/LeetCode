class Solution {
    public int maxProfit(int[] prices) {
        
        int maxProfit = 0;
        int minPrice = prices[0];
        
        for (int buy = 1; buy < prices.length; buy++) {
            if ( prices[buy] < minPrice) {
                minPrice = prices[buy];
            } else  {
                maxProfit = Math.max(prices[buy] -  minPrice, maxProfit);
            }
        }
        return maxProfit;
    }
}
