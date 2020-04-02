/*
@File    :   test1.cpp
@Time    :   2020/03/19 19:22:17
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test1.cpp
*/
/*
*/
#include <iostream>
#include <string>
using namespace std;
class Person
{
private:
  string name;
  int value;

public:
  Person(string name1, int value1 = 1200)
  {
    name = name1;
    value = value1;
  }
  string getName()
  {
    return name;
  }
  string operator+(const string newName) const
  {
    cout << "..." << value << endl;
    return name + " with " + newName;
  }
};
int main()
{
  // Person p("Lelen");
  // cout << p + ("marL") << endl;
  // cout << p.getName() << endl;
  // string str(10, 's');
  // cout << ".... " << str << endl;
  string s = "fir";
  string s1 = "Fgiter";
  s.swap(s1);
  cout << s << " " << s1 << endl;
  // auto p = s.c_str();
  // cout << sizeof(p) / sizeof(char);
  return 0;
}
