/*You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

*/
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int N=coins.size();
        int dp[N+1][amount+1];
        if(coins.size()==1 && amount%coins[0]!=0){
            return -1;
        }
        if(coins.size()==1 && amount%coins[0]==0){
            return amount/coins[0];
        }
        for(int i=0;i<N+1;i++){
            dp[i][0]=0;
        }
        for(int j=1;j<amount+1;j++){
            dp[0][j]=INT_MAX-1;
        }
        for(int i=1;i<N+1;i++){
            for(int j=1;j<amount+1;j++){
                if(coins[i-1]<=j){
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j]);
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        if(dp[N][amount]>=INT_MAX-1){
            return -1;
        }
        else{
            return dp[N][amount];
        }
    }
};
