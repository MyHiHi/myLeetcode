#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int countWays(int x, int y)
{
  vector<vector<int>> dp(x, vector<int>(y));
  dp[0][0] = 1;
  for (int i = 0; i < x; i++)
    for (int j = 0; j < y; j++)
    {
      if (i == 0 && j != 0)
        dp[i][j] = 1;
      else if (j == 0 && i != 0)
        dp[i][j] = 1;
      else
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  return dp[x - 1][y - 1];
}
int main()
{
  cout << countWays(2, 2);
}