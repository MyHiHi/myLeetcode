#include <iostream>
#include <vector>
using namespace std;
int main()
{
  vector<int> nums;
  int num;
  while (getchar() != ']')
  {
    cin >> num;
    nums.push_back(num);
  }
  int size = nums.size();
  int i = 0, a = nums[0];
  while (1)
  {
    i += a;
    cout << "*****: " << i << " " << a << endl;
    if (i < 0 || i >= size)
    {
      cout << "true";
      return 0;
    }
    if (nums[i] == 0)
    {
      cout << "false";
      return 0;
    }
    a = nums[i];
    nums[i] = 0;
  }
  return 0;
}