#include <iostream>
using namespace std;
class Student
{
private:
  double price;

public:
  inline void setPrice(double r);
  inline double getPrice();

protected:
  void print()
  {
    cout << "sdf" << endl;
  }
};
void Student::setPrice(double r)
{
  price = r;
}
double Student::getPrice()
{
  return price;
}
int main()
{
  Student stu;
  stu.setPrice(12.967545353535353);
  cout << stu.getPrice() << endl;
  Student *p = new Student;
  p->setPrice(190);
  cout << p->getPrice() << endl;
}