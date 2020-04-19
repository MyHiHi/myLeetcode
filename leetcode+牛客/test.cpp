#include <iostream>
#include <string>
using namespace std;
// string strAdd(string a, string b)
// {
//   int carry = 0, i = a.size() - 1, j = b.size() - 1;
//   string ans = "";
//   while (i >= 0 || j >= 0)
//   {
//     int p1 = i >= 0 ? a[i--] - '0' : 0, p2 = j >= 0 ? b[j--] - '0' : 0;
//     int v = (p1 + p2 + carry);
//     carry =v/ 10, ans = to_string(v % 10) + ans;
//   }
//   return carry == 1 ? "1" + ans : ans;
// }

string strAdd(string a, string b)
{
  int carry = 0, i = a.size() - 1, j = b.size() - 1, p1 = 0, p2 = 0, v = 0;
  string ans = "";
  while (i >= 0 || j >= 0)
  {
    p1 = (i >= 0) ? a[i--] - '0' : 0, p2 = (j >= 0) ? b[j--] - '0' : 0;
    v = (p1 + p2 + carry);
    carry = v / 10, ans = to_string(v % 10) + ans;
  }
  return carry == 1 ? "1" + ans : ans;
}


/***
 * #include <iostream>
#include <string>
#include <vector>
using namespace std;
string strAdd(string a, string b)
{
  int carry = 0, i = a.size() - 1, j = b.size() - 1, p1 = 0, p2 = 0, v = 0;
  string ans = "";
  while (i >= 0 || j >= 0)
  {
    if (i<0){
        ans=to_string(b[j--]-'0'+carry)+ans,carry=0;
    }
     else  if (j<0){
        ans=to_string(a[i--]-'0'+carry)+ans,carry=0;
    }else{
         int v=a[i--]-'0'+b[j--]-'0'+carry;
         carry=v/10,ans=to_string(v%10)+ans;
     }
  }
  return carry == 1 ? "1" + ans : ans;
}
int main(){
    int n;
    cin>>n;
    string *dp=new string[n+1];
    dp[0]="1",dp[1]="1",dp[2]="2";
    for (int t=3;t<n+1;t++){
        dp[t]=strAdd(dp[t-1],dp[t-2]);
     
    }
    cout<<dp[n];
}
 * /
int main()
{
  // int n;
  // cin >> n;
  // string *dp = new string[n + 1];
  // dp[0] = "0", dp[1] = "1", dp[2] = "2";
  // for (int t = 3; t < n + 1; t++)
  // {
  //   dp[t] = strAdd(dp[t - 1], dp[t - 2]);
  //   cout << "# " << dp[t] << endl;
  // }
  cout << strAdd("123123214321432423423", "783442131312312312312323122") << endl;
  // cout << dp[n];
}