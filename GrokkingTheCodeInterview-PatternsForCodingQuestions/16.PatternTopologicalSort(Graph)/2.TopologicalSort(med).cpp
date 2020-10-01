//Topological Sort of a directed graph (a graph with unidirectional edges) 
//is a linear ordering of its vertices such that
//for every directed edge (U,V) from vertex U to vertex V, U comes before V in the ordering.
//Given a directed graph, find the topological ordering of its vertices.
using namespace std;
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

class TopologicalSort{
    public:
    static vector<int> sort(int vertices, const vector<vector<int>>& edge) {
        vector<int> sortedOrder;
        if (vertices<=0){
            return sortedOrder;
        }
        //1. Initialization
        unordered_map<int,int> inDegree;  //the order/degree in the graph 
        unordered_map<int,vector<int>> graph; //to store the edges from every vectex 
        for (int i=0;i<vertices;i++){
            inDegree[i]=0;
            graph[i]=vector<int>();
        }
        //2. Build the graph, and find the inDegree 
        for (int i=0;i<edge.size();i++){
            int parent=edge[i][0],child=edge[i][1]; 
            graph[parent].push_back(child);   //update all the 'child's of the 'parent'
            inDegree[child]++;  //update the degree of 'child' in the whole graph
        }
        //3. Find all original sources
        queue<int> sources;
        for (auto entry: inDegree){
            if (entry.second==0){    //the degree of all the original sources equals 0
                sources.push(entry.first);  
            }
        }
        //4. Sort
        while (!sources.empty()){
            int vertex=sources.front();
            sources.pop();
            sortedOrder.push_back(vertex);  //Store the current sources
            vector<int> children=graph[vertex]; 
            for (auto child:children){    //remove the current sources, 
                inDegree[child]--;         //and update the degrees to get the next sources.
                if (inDegree[child]==0){   
                    sources.push(child);
                }
            }
        }

        if (sortedOrder.size()!=vertices){    //Which means this is not a Direct Acyclic Graph (DAG), 
            cout<<"Not a DAG. No topological-sort result."<<endl;
            return vector<int>();            //there is no solution to a topological/linear order.
        }

        return sortedOrder;
    }
};

int main(int argc, char* argv[]){
    vector<int> result=
        TopologicalSort::sort(4,vector<vector<int>>{vector<int>{3,2},vector<int>{3,0},
                                vector<int>{2,0},vector<int>{2,1}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;

    result=TopologicalSort::sort(5,vector<vector<int>>{vector<int>{4,2},vector<int>{4,3},
                                vector<int>{2,0},vector<int>{2,1},vector<int>{3,1}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;

    result=TopologicalSort::sort(5,vector<vector<int>>{vector<int>{4,2},vector<int>{4,3},
                            vector<int>{2,0},vector<int>{2,1},vector<int>{3,1},vector<int>{0,4}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;

    result=TopologicalSort::sort(7,vector<vector<int>>{vector<int>{6,4},vector<int>{6,2},
                                vector<int>{5,3},vector<int>{5,4},vector<int>{3,0},
                                vector<int>{3,1},vector<int>{3,2},vector<int>{4,1}});
    for (auto num:result){
        cout<<num<<" ";
    }
    cout<<endl;
}
