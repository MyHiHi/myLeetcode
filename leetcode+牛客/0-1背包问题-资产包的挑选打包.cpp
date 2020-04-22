/*
@File    :   0-1背包问题-资产包的挑选打包.cpp
@Time    :   2020/04/20 17:02:31
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   0-1背包问题-资产包的挑选打包.cpp
*/
/*
题目描述
在金融资产交易中，经常涉及到资产包的挑选打包。在资产包打包过程中，每种类型的资产有固定的数量与价值，需选择某几种资产打包，使得资产包总价值最大。打包时每种资产只能整体打包，不能分割。假设现有可容纳M条资产的资产包，另外有N种资产。资产Na数量为Ta条，总价值为Va元；资产Nb数量为Tb条，总价值为Vb元；资产Nc数量为Tc条，总价值为Vc元......；资产Nn数量为Tn，总价值为Vn。编写算法，挑选哪些类型资产放入资产包可使得资产包总价值最大？
输入描述:
资产总量,资产种类,每类资产条数,每类资产价值(逗号分隔)；其中每类资产条数与每类资产价值为空格分隔。
总格式如下：
资产总量,资产种类,资产A条数 资产B条数 资产C条数,资产A价值 资产B价值 资产C价值！
举例，资产总量为12，资产种类3种，3种资产条数分别为4，5，7，三种资产价值分别是500元，600元，800元，输入如下：
12,3,4 5 7,500 600 800
资产总量和资产种类都不超过1000，资产条数不超过1000，资产价值不超过10000，所有数值均为正整数。
输出描述:
资产包中资产最大总价值
示例1
输入
12,3,4 5 7,500 600 800
输出
1400

*/
/*
0-1背包问题：动态规划，维护一张(m+1)*(n+1)的二维表,
dp[m][n]表示前n个物体占用n空间 获得的最大价值
其最大价值在于 是否取得最后一件物品所得的价值
dp[m][n] = max(dp[m-1][n],dp[m-1][n-t[i]]+v[i])
t[i]为n物品占用的空间,v[i]为n物品价值
*/

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int main()
{
  int n, m;
  char c;
// 12,3,4 5 7,500 600 800   c为,
  cin >> n >> c >> m >> c;
  int *space = new int[m + 1], *value = new int[m + 1];
  for (int i = 1; i <= m; i++)
    cin >> space[i];
  cin >> c;
  for (int i = 1; i <= m; i++)
    cin >> value[i];
  vector<vector<int>> dp(m + 1, vector<int>(n + 1));
  for (int i = 1; i <= m; i++)
    for (int j = 1; j <= n; j++)
      dp[i][j] = max(dp[i - 1][j], j >= space[i] ? dp[i - 1][j - space[i]] + value[i] : 0);
  cout << dp[m][n];
}
