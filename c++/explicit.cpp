/*
@File    :   explicit.cpp
@Time    :   2020/03/15 19:53:17
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   explicit.cpp
*/
/*
*/
#include <iostream>
using namespace std;
class Student
{
public:
  explicit Student(char *n) : name(n) {}
  void display()
  {
    cout << "your name: " << name << endl;
  }
  Student(Student &s);

private:
  char *name;
};
Student::Student(Student &s)
{
  name = s.name;
}
int main()
{
  Student s("Mike");
  // s.display();
  Student m(s);
  m.display();
  return 0;
}
