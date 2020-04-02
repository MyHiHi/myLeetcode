#include <iostream>
#include <cmath>
using namespace std;
// inline void p(int a[])
// {
//   a[1] = 123;
// }
enum index
{
  underflow,
  overflow
};
int array_index(int *a, int n, int i)
{
  if (i < 0)
    throw underflow;
  if (i >= n)
    throw overflow;
  return a[i];
}
int main()
{
  // const int a = 12.98;
  // const int *p = &a;
  // int *c = const_cast<int *>(p);
  // *c = 123.89;
  // cout << a << " " << *p << " " << *c << endl;
  // cout << &a << " " << p << " " << c << endl;
  // int s[2] = {1, 4};
  // p(s);
  // cout << s[1];
  // int *p = new int[2];
  // cout << p + 3 << " " << p + 4;
  // delete[] p;
  int *A = new int[5];
  for (int t = 0; t < sizeof(A) / sizeof(int); t++)
  {
    A[t] = t;
    cout << A[t] << endl;
  }
  cout << " " << sizeof(A) / sizeof(int) << endl;
  try
  {
    cout << array_index(A, 5, 14) << endl;
    cout << array_index(A, 5, -1) << endl;
    cout << array_index(A, 5, 2) << endl;
  }
  catch (index e)
  {

    if (e == underflow)
    {
      cerr << "underflow" << endl;
    }
    else if (e == overflow)
    {
      cerr << "overflow" << endl;
    }
    exit(-1);
  }
  catch (bad_alloc)
  {
    cerr << "alloc failure" << endl;
  }
  return 0;
}
