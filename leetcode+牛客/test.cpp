/*
@File    :   test.cpp
@Time    :   2020/04/06 13:24:47
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <string>
using namespace std;
int main()
{
  int size;
  string s;
  cin >> size;
  cin.ignore();
  getline(cin, s);
  cout << "s: " << s << endl;
  int k = size / 3;
  int t = 0, step = 0, mid = 2 * (k - step) - 1;
  while (t < size)
  {
    // cout << "step: " << step << " " << k << endl;
    if (step < k)
    {
      for (int i = 0; i < step; i++)
        cout << " ";
      cout << s[t++];
      for (int i = 0; i < mid; i++)
        cout << " ";
      cout << s[t++] << endl;
      mid -= 2;
      step++;
    }
    else
    {
      for (int i = 0; i < step; i++)
        cout << " ";
      cout << s[t++] << endl;
    }
  }
  return 0;
}
