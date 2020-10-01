//There are 'N' tasks, labeled from '0' to 'N-1'. 
//Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
//Given the number of tasks and a list of prerequisite pairs,
//find out if it is possible to schedule all the tasks.
using namespace std;
#include<iostream>
#include<queue>
#include<unordered_map>
#include<vector>

class TaskScheduling{
    public:
    static bool isSchedulingPossible(int tasks, const vector<vector<int>>& prerequisites){
        if (tasks<=0){
            return false;
        }
        //1. Initialization
        unordered_map<int,int> Degree;
        unordered_map<int,vector<int>> Graph;
        for(int i=0;i<tasks;i++){
            Degree[i]=0;
            Graph[i]=vector<int>();
        }
        //2. Build the graph,Find the Degree
        for(int i=0;i<prerequisites.size();i++){
            int parent=prerequisites[i][0],child=prerequisites[i][1];
            Degree[child]++;
            Graph[parent].push_back(child);
        }
        //3. Find the sources
        queue<int> sources;
        for(auto entry:Degree){
            if (entry.second==0){
                sources.push(entry.first);
            }
        }
        //4. Sort
        vector<int> Order;
        while(!sources.empty()){
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
        return Order.size()==tasks;
    }
};

int main(int argc, char* argv[]){
    bool result=TaskScheduling::isSchedulingPossible(3,
                vector<vector<int>>{vector<int>{0,1},vector<int>{1,2}});
    cout<<result<<endl;

    result=TaskScheduling::isSchedulingPossible(3,
                vector<vector<int>>{vector<int>{0,1},vector<int>{1,2},vector<int>{2,0}});
    cout<<result<<endl;

    result=TaskScheduling::isSchedulingPossible(6,vector<vector<int>>{vector<int>{2,5},
                vector<int>{0,5},vector<int>{0,4},vector<int>{1,4},vector<int>{3,2},vector<int>{1,3}});
    cout<<result<<endl;
}