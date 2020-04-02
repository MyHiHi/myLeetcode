/*
@File    :   test.cpp
@Time    :   2020/03/15 20:11:34
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   test.cpp
*/
/*
*/
#include <iostream>
#include <cstring>
using namespace std;
class T
{
private:
  int value;
  string name;
  const int md = 111;

private:
  static int count;

public:
  T() {}
  T(int value, string n = "CC") : value(value), name(n)
  {
    count++;
  }
  void display()
  {
    static int t = 0;
    t += 100;
    cout << "t: " << t << endl;
    cout << value << ":" << name << endl;
  }
  void get();
  int getV() const
  {
    cout << "Here md:" << md << endl;
    // value = 1234;
    // display();
    return value;
  }
  void setV(int v)
  {
    this->value = v;
  }

public:
  ~T()
  {
    cout << this << " " << value << " is destroyed!" << endl;
  }
};
int T::count = 0;
int main()
{
  T c;
  c.display();
  T t(12, "Dick");
  // cout << t.getV() << endl;

  t.display();
  T y(t);
  y.display();
  // y.setV(100);
  // y.display();
  // t.display();
  T t1(14);
  T t2(90);
  // cout << "count: " << t.count << endl;
  cout << sizeof(t1) << "-->" << sizeof(t2) << "__" << sizeof(T) << endl;
  // cout << T::count << endl;
  return 0;
}
