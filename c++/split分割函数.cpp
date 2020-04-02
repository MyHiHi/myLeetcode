/*
@File    :   test.cpp
@Time    :   2020/03/25 10:29:10
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;
void split(vector<string> &res, const string str, char flag = ' ')
{
  res.clear();
  istringstream iss(str);
  string temp;
  while (getline(iss, temp, flag))
  {
    res.push_back(temp);
  }
}
int main()
{
  // string str = "cat,cats,and,sand,dog";
  string str;
  getline(cin, str);
  cout << str << endl;
  vector<string> r;
  split(r, str, ',');
  for_each(r.begin(), r.end(), [](string s) { cout << s << " "; });
  return 0;
}
