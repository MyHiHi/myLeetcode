/*
@File    :   test3.cpp
@Time    :   2020/03/30 11:04:23
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test3.cpp
*/
/*
*/
#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
  string p;
  // cin >> p;
  int val = 0;
  int size = p.size() - 1;
  // cout << bitset<10>(12) << endl;
  char g[12];
  itoa(15, g, 2);
  cout << g << endl;
  for (int t = size; t >= 0; t--)
  {
    if (p[t] == '1')
      val += int(1 << (size - t));
  }
  cout << val;

  return 0;
}
