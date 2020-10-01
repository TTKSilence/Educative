//Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number 'S'.
using namespace std;
#include<iostream>
#include<vector>
class SubserSum{
    public:
    bool Exist(const vector<int> &num,int sum){
        int n=num.size();
        /*Solution1 - Bottom-up DP
        vector<vector<bool>> dp(n,vector<bool>(sum+1));
        for (int i=0;i<n;i++){
            dp[i][0]=true;
        }
        for (int s=1;s<sum;s++){
            dp[0][s]=(num[0]<=s? true:false);
        }
        for (int i=1;i<n;i++){
            for (int s=1;s<=sum;s++){
                if(dp[i-1][s]){
                    dp[i][s]=dp[i-1][s];
                }else if(num[i]<=s){
                    dp[i][s]=dp[i-1][s-num[i]];
                }
            }
        }
        return dp[n-1][sum];
        */
       /*Solution2 - Bottom-up DP- time complexity improved*/
       vector<bool> dp(sum+1);
       dp[0]=true;
       for (int s=1;s<=sum;s++){
           dp[s]=(num[0]<=s?true:false);
       }
       for (int i=1;i<n;i++){
           for(int s=sum;s>=0;s--){
               //if dp[s], then we can get the sum without num[i]. So just jump over to see the next num.
               if(!dp[s] && s>=num[i]){
                   dp[s]=dp[s-num[i]];
               }
           }
       }
       return dp[sum];
    }
};

int main(int argc,char *argv[]){
    SubserSum ss;
    vector<int> num={1,2,3,7};
    cout<<ss.Exist(num,6)<<endl;
    num={1,2,7,1,5};
    cout<<ss.Exist(num,10)<<endl;
    num={1,3,4,8};
    cout<<ss.Exist(num,6)<<endl;
}