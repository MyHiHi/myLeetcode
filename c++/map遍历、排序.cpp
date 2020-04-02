/*
@File    :   test.cpp
@Time    :   2020/03/25 10:28:18
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/

#include <iostream>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef pair<int, int> PAIR;
bool sortByV(pair<int, int> a, pair<int, int> b)
{
  return a.second > b.second;
}
int main()
{
  map<int, int> nums;
  nums[12] = 1;
  nums[4] = 120;
  nums.insert(pair<int, int>(34, 14));
  // 排序
  vector<PAIR> vec(begin(nums), end(nums));
  sort(vec.begin(), vec.end(), [](PAIR a, PAIR b) { return a.second > b.second; }); //排序
  for_each(vec.begin(), end(vec), [](auto s) { cout << s.first << " " << s.second << endl; });
  // map<int, int>::iterator t = begin(nums);
  // while (t != end(nums))
  // {
  //   cout << t->first << " " << t->second << endl;
  //   t++;
  // }
  // for (int t = 0; t < nums.size(); t++)
  // {
  //   cout << nums[t] << endl;
  // }
  return 0;
}
