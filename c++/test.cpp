#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int main()
{
  string p = ":asdfefe";
  if (p.find('t') == -1)
    cout << "No";
  else if (p.find('t') == -1)
    cout << "No1";
  cout << "end";
  p[0] = "1";
  cout << p;
}