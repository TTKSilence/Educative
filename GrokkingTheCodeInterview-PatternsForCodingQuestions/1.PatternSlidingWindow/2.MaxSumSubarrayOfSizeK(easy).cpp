using namespace std;
#include <iostream>
#include <vector>
class MaxSumSubarray{
    public:
    static int findSubarray(int k, const vector<int>& arr){
        int maxsum=0, cursum=0,start=0;
        for (int i=0;i<arr.size();i++){
            cursum+=arr[i];
            if (i>=k-1){
                maxsum=max(maxsum,cursum);
                cursum-=arr[start];
                start++;
            }
        }
        return maxsum;
    }
};

int main(int argc, char *argv[]){
    int result=MaxSumSubarray::findSubarray(3,vector<int>{2,1,5,1,3,2});
    cout<<result<<endl;

    result=MaxSumSubarray::findSubarray(2,vector<int>{2,3,4,1,5});
    cout<<result<<endl;
}