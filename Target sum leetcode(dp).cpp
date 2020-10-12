 /*You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

*/
 class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int N=nums.size();
        int sum=0;
        int find;
        int zero=0;
        for(int i=0;i<N;i++){
            sum+=nums[i];
            if(nums[i]==0){
                zero++;
            }
        }
        if(S>sum){
            return 0;
        }
        if((S+sum)%2!=0){
            return 0;
        }
        find=(S+sum)/2;
        int dp[N+1][find+1];
        for(int i=0;i<N+1;i++){
            dp[i][0]=1;
        }
        for(int  j=1;j<find+1;j++){
            dp[0][j]=0;
        }
        for(int i=1;i<N+1;i++){
            for(int j=1;j<find+1;j++){
                if(nums[i-1]==0){
                    dp[i][j]=dp[i-1][j];
                }
                else if(nums[i-1]<=j){
                    dp[i][j]=dp[i-1][j-nums[i-1]] + dp[i-1][j];
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return pow(2,zero)*dp[N][find];
    }
};
