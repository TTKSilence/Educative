//There are 'N' tasks, labeled from '0' to 'N-1'. 
//Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
//Given the number of tasks and a list of prerequisite pairs,
//write a method to print all possible ordering of tasks meeting all prerequisities.
using namespace std;
#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

class AllTaskSchedulingOrders{
    public:
    static void printOrders(int tasks, const vector<vector<int>>& prerequisite){   
        if (tasks<=0){
            return;
        }
        vector<int> Order;
        //1. Initialization
        unordered_map<int,int> Degree;
        unordered_map<int,vector<int>> Graph;
        for (int i=0;i<tasks;i++){
            Degree[i]=0;
            Graph[i]=vector<int>();
        }
        //2. Build the Graph, find the Degree
        for (int i=0;i<prerequisite.size();i++){
            int parent=prerequisite[i][0],child=prerequisite[i][1];
            Degree[child]++;
            Graph[parent].push_back(child);
        }
        //3. Find the sources
        vector<int> sources;
        for (auto entry:Degree){
            if (entry.second==0){
                sources.push_back(entry.first);
            }
        }

        printAllSorts(Graph,Degree,sources,Order);
    }
    //4. Sort & Print
    private:
    static void printAllSorts(unordered_map<int, vector<int>> &Graph,
                        unordered_map<int,int> &Degree,vector<int> &sources,vector<int> &Order){
        if (!sources.empty()){
            for (int node:sources){
                Order.push_back(node);
                vector<int> nextsources=sources;
                //Only remove the current source, other sources should remain for the next call.
                nextsources.erase(find(nextsources.begin(),nextsources.end(),node));
                //Update/decrement the degrees of the current source's children.
                for (auto child:Graph[node]){
                    Degree[child]--;
                    if (Degree[child]==0){
                        nextsources.push_back(child);
                    }
                }
                //Recursive call to print other orders from the remaining sources.
                printAllSorts(Graph,Degree,nextsources,Order);
                //Backtrack, remove the current source from Order; 
                //and put all of its children back in order to consider the next source.
                Order.erase(find(Order.begin(),Order.end(),node));
                for (auto child:Graph[node]){
                    Degree[child]++;
                }
            }
        }
        if (Order.size()==Degree.size()){
            for (auto num:Order){
                cout<<num<<" ";
            }
            cout<<endl;
        }           
    }
};

int main(int argc,char* argv[]){
    vector<vector<int>>prerequisite={vector<int>{0,1},vector<int>{1,2}};
    AllTaskSchedulingOrders::printOrders(3,prerequisite);
    cout<<endl;

    prerequisite={vector<int>{3,2},vector<int>{3,0},vector<int>{2,0},vector<int>{2,1}};
    AllTaskSchedulingOrders::printOrders(4,prerequisite);
    cout<<endl;

    prerequisite={vector<int>{2,5},vector<int>{0,5},vector<int>{0,4},
                vector<int>{1,4},vector<int>{3,2},vector<int>{1,3}};
    AllTaskSchedulingOrders::printOrders(6,prerequisite);
    cout<<endl;
}