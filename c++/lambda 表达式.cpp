/*
@File    :   lambda 表达式.cpp
@Time    :   2020/03/23 16:52:41
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   lambda 表达式.cpp
*/
/*
Lambda表达式完整的声明格式如下：
[capture list] (params list) mutable exception-> return type { function body }
*/
#include <iostream>
using namespace std;
int main()
{
  int a = 12;
  auto f = [&a](auto g) -> void {
    a++;
    g();
    cout << a << endl;
  };
  auto g = []() {
    cout << "inner..." << endl;
  };
  f(g);
  cout << "Final: "
       << a << endl;

  // auto f = [](int t) { cout << "Te" << t << endl; };
  // f(12);


  // vector<int> test = {11, 4, 4, 3, 22, 1, 2};
  // sort(test.begin(), test.end(), [](int a, int b) -> bool { return a > b; });
  // for (auto t : test)
  // {
  //   cout << t << " ";
  // }
return 0;
}
