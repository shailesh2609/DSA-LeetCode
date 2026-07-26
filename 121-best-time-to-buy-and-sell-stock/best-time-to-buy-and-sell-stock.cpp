class Solution {
public:
    int maxProfit(vector<int>& prices) {
    int n = prices.size();

    int minCost = prices[0];
    int profit = 0;
    for(int i = 1; i< n ; i++){
        if(prices[i] - minCost < 0){
            minCost  = prices[i];
        }
        else{
            profit = max(profit, prices[i] - minCost);
        }
    }
    return profit;   
}
};