/*
@File    :   test.cpp
@Time    :   2020/04/24 21:10:04
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  vector<int> p = {12, 5, 3, 2, 32, 323, 5};
  int t = p.size() / 2;
  vector<int> s1(p.begin(), p.begin() + t),
      s2(p.begin() + t, p.end());
  for (auto a : s2)
  {
    cout << a << " ";
  }

  return 0;
}
