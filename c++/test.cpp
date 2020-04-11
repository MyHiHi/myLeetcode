#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main()
{
  vector<int> p;
  while (getchar() != '\n')
  {
    int c;
    cin >> c;
    p.push_back(c);
  }
  for (auto c : p)
  {
    cout << c << "**" << endl;
  }
  return 0;
}