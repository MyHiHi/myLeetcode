/*
@File    :   struct.cpp
@Time    :   2020/03/15 18:55:41
@Author  :   Zhang tao 
@Version :   1.0
@Desc    :   struct.cpp
*/
/*
*/
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
class node
{
public:
  int value;
  string name;
  int age;
  // const int before;
  // node() : before(12){};
  node(){};
  node(int v, int age = 12, string n = "admin");
  node(int v) : value(v)
  {
    cout << "init finished!" << endl;
  }
  // node(int v)
  // {
  //   cout << "create...." << endl;
  //   value = v;
  // }
  void display()
  {
    cout << value << endl;
  }
};
node::node(int v, int a, string n) : value(v), age(a), name(n)
{
}
struct book
{
public:
  void setprice(double a);
  double getprice();

private:
  double price;
};
node &createNode(int value)
{
  static node b;
  b.value = value;
  return b;
}
void dis(node n)
{
  n.display();
}
int main()
{
  node f(11, 14);
  f.display();
  cout << f.name << endl;
  // node f(123);
  // node *f = new node(222);
  // f->display();
  // node f = createNode(12);
  // f.display();
  // dis(f);
  // node *c = new node;
  // c->value = 123.78;
  // c->display();

  // book p;
  // p.price=12;
}
