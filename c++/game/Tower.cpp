#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
int main(){
    string s;
    getline(cin,s);
    stringstream ss;
    ss<<s;
    int limit;
    cin>>limit;
    int t;
    vector<int> weight;
    while (ss>>t){
        weight.push_back(t);
    }
    sort(weight.begin(),weight.end());
    int res=0;
    int i=0,j=weight.size()-1;
    while (i<=j){
        if (weight[i]+weight[j]<=limit){
            i++;
            j--;
        }else{
            j--;
        }
        res++;
    }
    cout<<res<<endl;
    return 0;
}