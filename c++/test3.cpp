#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int m, n;
    cin >> m >> n;
    vector<vector<int>> nums(m, vector<int>(n));
    for (int i = 0; i < m; i++)
    {
        // vector<int> a;
        for (int j = 0; j < n; j++)
        {
            cin >> nums[i][j];
        }
        // nums.push_back(a);
    }
    int k;
    cin >> k;
    int i = m - 1, j = 0;
    while (i >= 0 && j < n)
    {
        int y = nums[i][j];
        if (y == k)
        {
            cout << "true";
            return 0;
        }
        if (y < k)
            j++;
        else
            i--;
    }
    cout << "false";

    return 0;
}