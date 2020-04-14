#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main()
{
  map<int, int> candy;
  int n = 0;
  int t;
  while (cin >> t)
  {
    candy[t]++;
    cout << "**" << candy[t] << endl;
  }

  for (auto c : candy)
  {
    int a = c.first, b = c.second;
    int people = a + 1, num = b / people, f = b % people;
    if (f != 0)
      num++;
    n += people * num;
  }
  cout << n;

  return 0;
}