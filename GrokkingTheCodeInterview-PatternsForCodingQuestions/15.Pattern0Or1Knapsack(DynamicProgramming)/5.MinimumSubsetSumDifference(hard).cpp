//Given a set of positive numbers,
//partition the set into two subsets with minimum difference between their subset sums.
using namespace std;
#include <iostream>
#include <vector>
/*Solution1-Basic
class MinSubSumDiff{
    public:
    int canPartition(const vector<int> &num){
        return this->canPartitionRecursive(num,0,0,0);
    }

    private:
    int canPartitionRecursive(const vector<int> &num, int currentindex, int sum1, int sum2){
        if (currentindex==num.size()){
            return abs(sum1-sum2);
        }
        int diff1=canPartitionRecursive(num,currentindex+1,sum1+num[currentindex],sum2);
        int diff2=canPartitionRecursive(num,currentindex+1,sum1,sum2+num[currentindex]);
        return min(diff1,diff2);
    }
};
*/

/*Solution2-Solution2- Top-down DP with memoization
class MinSubSumDiff{
    public:
    int canPartition(const vector<int> &num){  
        int sum=0;
        for (int i=0;i<num.size();i++){
            sum+=num[i];
        }
        vector<vector<int>> dp(num.size(),vector<int>(sum+1,-1));
        return this->canPartitionRecursive(dp,num,0,0,0);
    }

    private:
    int canPartitionRecursive(vector<vector<int>> &dp,const vector<int> &num,
                            int currentindex,int sum1,int sum2){
        if (currentindex==num.size()){
            return abs(sum1-sum2);
        }
        if (dp[currentindex][sum1]==-1){
            int diff1=canPartitionRecursive(dp,num,currentindex+1,sum1+num[currentindex],sum2);
            int diff2=canPartitionRecursive(dp,num,currentindex+1,sum1,sum2+num[currentindex]);
            dp[currentindex][sum1]=min(diff1,diff2);
        }
        return dp[currentindex][sum1];
    }
};
*/

/*Solution2-Solution3- Bottom-up DP*/
class MinSubSumDiff{
    public:
    int canPartition(const vector<int> &num){  
        int sum=0;
        for (int i=0;i<num.size();i++){
            sum+=num[i];
        }
        int n=num.size();
        //find if there exists a subset whose sum equals to sum/2
        vector<vector<bool>> dp(n,vector<bool>(sum/2+1,false));
        for (int i;i<n;i++){
            dp[i][0]=true;
        }
        for (int s=0;s<=sum/2;s++){
            dp[0][s]=(num[0]==s?true:false);
        }
        for (int i=1;i<n;i++){
            for (int s=1;s<=sum/2;s++){
                if (dp[i-1][s]){
                    dp[i][s]=dp[i-1][s];
                }else if (s>=num[i]){
                    dp[i][s]=dp[i-1][s-num[i]];
                }
            }
        }
        int sum1=0;
        for (int i=sum/2;i>=0;i--){
            if (dp[n-1][i]){   //find the sum value that closest to the sum/2
                sum1=i;
                break;
            }
        }
        int sum2=sum-sum1;
        return abs(sum2-sum1);
    }
};

int main(int argc, char *argv[]){
    MinSubSumDiff mssd;
    vector<int> num={1,2,3,9};
    cout<<mssd.canPartition(num)<<endl;
    num={1,2,7,1,5};
    cout<<mssd.canPartition(num)<<endl;
    num={1,2,100,3};
    cout<<mssd.canPartition(num)<<endl;
}
