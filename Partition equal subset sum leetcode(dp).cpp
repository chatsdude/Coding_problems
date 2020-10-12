/*Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.*/
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum%2!=0){
            return false;
        }
        int to_find=sum/2;
        int N=nums.size();
        int dp[N+1][to_find+1];
        dp[0][0]=true;
        for(int i=1;i<N+1;i++){
            dp[i][0]=false;
        }
        for(int j=1;j<to_find+1;j++){
            dp[0][j]=false;
        }
        for(int i=1;i<N+1;i++){
            for(int j=1;j<to_find+1;j++){
                if(nums[i-1]<=j){
                    dp[i][j]=dp[i-1][j-nums[i-1]] || dp[i-1][j];
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return dp[N][to_find];
    }
};
