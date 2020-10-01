//There are 'N' tasks, labeled from '0' to 'N-1'. 
//Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
//Given the number of tasks and a list of prerequisite pairs,
//find out the ordering of tasks we should pick to finish all tasks.
using namespace std;
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

class TaskSchedulingOrder{
    public:
    static vector<int> findOrder(int tasks, const vector<vector<int>>& prerequisite){
        
        if (tasks<=0){
            return vector<int> ();
        }
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
        queue<int> sources;
        for (auto entry:Degree){
            if (entry.second==0){
                sources.push(entry.first);
            }
        }
        //4. Sort
        vector<int> Order;
        while (!sources.empty()){
            int node=sources.front();
            sources.pop();
            Order.push_back(node);
            for (auto child:Graph[node]){
                Degree[child]--;
                if (Degree[child]==0){
                    sources.push(child);
                }
            }
        }
        //5. Judgement
        if (Order.size()!=tasks) {
            return vector<int>();
            }
        return Order;
    }
};

int main(int argc,char* argv[]){
    vector<int> result=TaskSchedulingOrder::findOrder(3,
                vector<vector<int>>{vector<int>{0,1},vector<int>{1,2}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;

    result=TaskSchedulingOrder::findOrder(3,
                vector<vector<int>>{vector<int>{0,1},vector<int>{1,2},vector<int>{2,0}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;

    result=TaskSchedulingOrder::findOrder(6,vector<vector<int>>{vector<int>{2,5},
                vector<int>{0,5},vector<int>{0,4},vector<int>{1,4},vector<int>{3,2},vector<int>{1,3}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;
}