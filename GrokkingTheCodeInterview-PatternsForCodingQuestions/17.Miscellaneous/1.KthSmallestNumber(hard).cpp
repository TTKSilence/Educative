//Given an unsorted array of numbers, find Kth smallest number in it.
//Note: it is the Kth smallest number in the sorted order, not the Kth distinct element.
using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>

class KthSmallestNumber{
    public:
    static int findKthSmallestNumber(vector<int> &nums, int k){
        return findKthSmallestNumberRec(nums,k,0,nums.size()-1);
    }
    /*Using Partition Scheme of QuickSort*/
    static int findKthSmallestNumberRec(vector<int> &nums,int k,int start,int end){
        int pivot=partition(nums,start,end);

        if (pivot==k-1){
            return nums[pivot];
        }

        if (pivot>k-1){
            return findKthSmallestNumberRec(nums,k,start,pivot-1);
        }

        return findKthSmallestNumberRec(nums,k,pivot+1,end);
    }

    private:
    static int partition(vector<int> &nums, int low, int high){
        if (low==high){
            return low;
        }
        /*
        //Using Randomized Partition Scheme of QuickSort
        srand(time(0));
        int pivotIndex=low+rand()%(high-low);
        swap(nums,pivotIndex,high);
        */

        /*
        //Using the Median of Medians*/
        int median=medianOfMedians(nums,low,high);
        for (int i=low;i<high;i++){
            if (nums[i]==median){
                swap(nums,i,high);
                break;
            }
        }

        int pivot=nums[high];
        //All elements less than 'pivot' will be swaped before the index 'low'
        for (int i=low;i<high;i++){
            if (nums[i]<pivot){
                swap(nums,low++,i);
            }
        }
        //Put the pivot in its correct place, remember nums[high] is the pivot
        swap(nums,low,high);
        return low;
    }

    static void swap(vector<int> &nums, int i, int j){
        int temp=nums[i];
        nums[i]=nums[j];
        nums[j]=temp;
    }

    static int medianOfMedians(vector<int> &nums, int low, int high){
        int n=high-low+1;
        //if there are less than 5 elements, ignore the partition algorithm
        if(n<5){
            return nums[low];
        }
        int numOfPartitions=n/5; //the number of '5 elements'
        vector<int> medians(numOfPartitions);
        for (int i=0;i<numOfPartitions;i++){
            int partitionStart=low+i*5;  //the starting index of the current '5 elements'
            sort(nums.begin()+partitionStart,nums.begin()+partitionStart+5); //Sort the '5 elements
            medians[i]=nums[partitionStart+2];  //Get the middle element (or the median)
        }
        return partition(medians,0,numOfPartitions-1);
    }
};

int main(int argc, char *argv[]){
    vector<int> vec={1,5,12,2,11,5};
    int result=KthSmallestNumber::findKthSmallestNumber(vec,3);
    cout<<result<<endl;

    result=KthSmallestNumber::findKthSmallestNumber(vec,4);
    cout<<result<<endl;

    vec={1,5,12,12,11,-1};
    result=KthSmallestNumber::findKthSmallestNumber(vec,4);
    cout<<result<<endl;
}