#include <iostream>

void add_one_val(int x, int *x_addr)
{
    std::cout << "(1) " << (&x == x_addr) << std::endl;
    x = x + 1;
    std::cout << "(2) " << (&x == x_addr) << std::endl;
}

void add_one_ref(int &x, int *x_addr)
{
    std::cout << "(4) " << (&x == x_addr) << std::endl;
    x = x + 1;
    std::cout << "(5) " << (&x == x_addr) << std::endl;
}

int main()
{
    int a = 0;
    int b = 0;

    add_one_val(a, &a);
    std::cout << "(3) " << (a == 0) << std::endl;

    add_one_ref(b, &b);
    std::cout << "(6) " << (b == 0) << std::endl;
    return 0;
}