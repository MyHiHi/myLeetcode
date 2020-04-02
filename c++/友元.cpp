/*
@File    :   友元.cpp
@Time    :   2020/03/15 23:24:56
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   友元.cpp
*/
/*
*/
#include <iostream>
using namespace std;
class Time
{
public:
  void displa(Student s)
  {
    cout << s.age << "***" << s.value << endl;
  };
};
class Student
{
private:
  int age;
  int value;

public:
  ~Student(){};
  Student(int a, int v) : age(a), value(v) {}
  friend void display(const Student s);
  friend Time;
};
void display(const Student s)
{
  cout << s.age << "---" << s.value << endl;
}

int main()
{
  Student s(12, 1);
  display(s);
  Time t;
  t.displa(s);
  return 0;
}
