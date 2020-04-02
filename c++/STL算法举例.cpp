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
int main()
{

  vector<int> num(10);
  generate(begin(num), num.end(), rand);
  replace_if(
      num.begin(), num.end(), [](int t) { return t % 2 != 0; }, 0);
  sort(num.begin(), num.end(), [](int t, int f) { return t > f; });
  for_each(num.begin(), num.end(), [](int t) { cout << t << " "; });

  return 0;
}
