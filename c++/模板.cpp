#include <iostream>
#include <vector>
using namespace std;

template <class T>
class array
{
public:
    array(int);
    T &operator[](int);
    const T &operator[](int) const;
    int getlen() const { return length; }
    ~array();

private:
    array(){};
    int length;
    T *num;
};

template <class T>
array<T>::array(int n)
{
    num = new T[n];
    length = n;
}

template <class T>
array<T>::~array()
{
    delete[] num;
}

template <class T>
T &array<T>::operator[](int i)
{
    if (i < 0 || i >= length)
        throw string("out of bounds");
    return num[i];
}

template <class T>
const T &array<T>::operator[](int i) const
{
    if (i < 0 || i >= length)
        throw string("out of bounds");
    return num[i];
}

template <class T>
ostream &operator<<(ostream &out, const array<T> &A)
{
    for (int i = 0; i < A.getlen(); i++)
        out << A[i] << " ";
    return out;
}

int main()
{
    array<int> A(10);
    for (int i = 0; i < 10; i++)
    {
        A[i] = 2 * i;
    }
    cout << A << endl;
    return 0;
}