#include <iostream>
#include <string>
#include <queue>
using namespace std;
int main()
{
  int t[] = {2, 4, 12, 5, 23, 1};
  priority_queue<int> p(t, t + 6);
  while (!p.empty())
  {
    cout << p.top() << endl;
    p.pop();
  }
  return 0;
}