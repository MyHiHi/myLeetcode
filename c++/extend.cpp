/*
@File    :   extend.cpp
@Time    :   2020/03/17 11:45:30
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   extend.cpp
*/
/*
*/
#include <iostream>
#include <string>
using namespace std;
class Person
{
public:
  Person()
  {
    cout << "Person" << endl;
    value = 1200;
  }
  int getValue()
  {
    return value;
  }
  ~Person()
  {
    cout << "Person: destoryed" << endl;
  }

private:
  int value;
  int lucky;
};
class Student : Person
{
private:
  string name;

public:
  Student()
  {
    cout << "Student" << endl;
    name = "Helen";
  }
  void display()
  {
    cout << "name: " + name << " " << getValue() << endl;
  }
  ~Student()
  {
    cout << "Student: distoryed" << endl;
  }
};
int main()
{
  Student s;
  s.display();

  return 0;
}
