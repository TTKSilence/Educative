//Given a set of positive numbers, 
//find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
using namespace std;
#include <iostream>
#include <vector>
/*Solution1-Basic
class PartitionSet{
    public:
    bool canPartition(const vector<int> &num){
        int sum=0;
        for (int i=0;i<num.size();i++){
            sum+=num[i];
        }
        if (sum%2!=0){
            return false;
        }
        return  this -> canPartitionRecursive(num,sum/2,0);
        }
    
    private:
    bool canPartitionRecursive(const vector<int> &num, int sum, int currentindex){
        if (sum==0){
            return true;
        }
        if (num.empty() || currentindex>=num.size()){
            return false;
        }
        if (num[currentindex]<=sum){
            if (canPartitionRecursive(num,sum-num[currentindex],currentindex+1)){
                return true;
            }
        }
        return  canPartitionRecursive(num,sum,currentindex+1);
    }

};
*/

/*Solution2-Top-down DP with memorization'''
class PartitionSet{
    public:
    bool canPartition(const vector<int> &num){
        int sum=0;
        for (int i=0;i<num.size();i++){
            sum+=num[i];
        }
        if (sum%2!=0){
            return false;
        }
        vector<vector<int>> dp(num.size(),vector<int>(sum/2 +1,-1));
        return this -> canPartitionRecursive(dp,num,sum/2,0);
    }

    private:
    bool canPartitionRecursive(vector<vector<int>> &dp, const vector<int> &num, 
                                int sum, int currentindex){
        if (sum==0){
            return true;
        }
        if (num.empty() || currentindex >=num.size()){
            return false;
        }
        if (dp[currentindex][sum]==-1){
            if (num[currentindex]<=sum){
                if (canPartitionRecursive(dp,num,sum-num[currentindex],currentindex+1)){
                    dp[currentindex][sum]=1;
                    return true;
                }
            }
            dp[currentindex][sum]=canPartitionRecursive(dp,num,sum,currentindex+1) ? 1 : 0;
        }
        return dp[currentindex][sum]==1 ? true:false;
    }
};
*/

/*Solution3- Bottom-up DP*/
class PartitionSet{
    public:
    bool canPartition(const vector<int> &num){
        int n = num.size();
        int sum=0;
        for (int i=0;i<n;i++){
            sum+=num[i];
        }
        if (sum%2!=0){
            return false;
        }
        sum/=2;
        vector<vector<bool>> dp(n,vector<bool>(sum+1));
        for (int i=0;i<n;i++){
            dp[i][0]=true;
        }
        for (int s=1;s<=sum;s++){
            dp[0][s]=(num[0]==s?true:false);
        }
        for (int i=1;i<n;i++){
            for (int s=1;s<=sum;s++){
                if (dp[i-1][s]){
                    dp[i][s]=dp[i-1][s];
                }else if (num[i]<=s){
                    dp[i][s]=dp[i-1][s-num[i]];
                }
            }
        }
        return dp[n-1][sum];
    }
};

int main(int argc,char *argv[]){
    PartitionSet ps;
    vector<int> num={1,2,3,4};
    cout<<ps.canPartition(num)<<endl;
    num={1,1,3,4,7};
    cout<<ps.canPartition(num)<<endl;
    num={1,2,3,5};
    cout<<ps.canPartition(num)<<endl;
}

