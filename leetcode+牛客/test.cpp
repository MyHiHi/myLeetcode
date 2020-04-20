/*
@File    :   test.cpp
@Time    :   2020/04/20 09:46:06
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
using namespace std;
int clumsy(int N)
{
  int *q1 = new int[N], l1 = 0;
  for (int i = N; i >= 1; i -= 4)
  {
    int c = i - 1, y = i;
    y *= c >= 1 ? c, c-- : 1;
    y /= c >= 1 ? c : 1;
    q1[l1++] = y;
    cout << y << " ";
  }
  cout << "**" << endl;
  int ans = 0, c = q1[l1 - 1], j = 0;
  int v1 = j < l1 ? q1[j++] : 0;
  for (int i = N - 3; i >= 1; i -= 4)
  {
    int v2 = j < l1 ? q1[j++] : 0;
    ans = v1 + i - v2;
    v1 = ans;
    cout << v1 << " " << i << " " << v2 << " " << ans << "% ";
  }
  return N - 3 >= 1 ? ans : c;
}
int main()
{
  cout << clumsy(10);
  return 0;
}

int clumsy(int N) {
        int ans = 0;
        int temp = N;
        for(int i = 1 ; i < N ; ++ i){
            int cur = N - i;
            int type = i % 4;
            if(type == 0){
                ans += temp;
                temp = - cur;
            }else if(type == 1){
                temp *= cur;
            }else if(type == 2){
                temp /= cur;
            }else{
                temp += cur;
            }
        }
        ans += temp;
        return ans;
    }
