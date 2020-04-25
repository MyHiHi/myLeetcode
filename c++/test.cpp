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

void merge(vector<int> &s1, vector<int> &s2, vector<int> &p)
{
  int l1 = s1.size() - 1, l2 = s2.size() - 1, n = p.size() - 1;
  while (l1 >= 0 && l2 >= 0)
  {
    if (s1[l1] > s2[l2])
    {
      p[n--] = s1[l1--];
    }
    else
    {
      p[n--] = s2[l2--];
    }
  }
  while (l1 >= 0)
    p[n--] = s1[l1--];
  while (l2 >= 0)
    p[n--] = s2[l2--];
}
void merge_sort(vector<int> &p)
{
  int n = p.size();
  if (n < 2)
    return;
  int m = n / 2;
  vector<int> s1(p.begin(), p.begin() + m), s2(p.begin() + m, p.end());
  merge_sort(s1), merge_sort(s2);
  merge(s1, s2, p);
}

vector<int> quick_sort(vector<int> &p)
{
  vector<int> s1, s2;
  int t = p.size() / 2, n = p[t];
  p.erase(p.begin() + t);
  for (auto a : p)
  {
    if (a > n)
      s2.push_back(a);
    else
      s1.push_back(a);
  }
  vector<int> res;
  res.push_back(quick_sort(s1).begin(), quick_sort(s1).end());
  res.push_back(n);
  res.push_back(quick_sort(s2));
  return res;
}
int main()
{
  vector<int> p = {12, 5, 3, 2, 32, 323, 5};
  merge_sort(p);
  for (auto a : p)
  {
    cout << a << " ";
  }

  return 0;
}
