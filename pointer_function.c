#include <stdio.h>
#include <stdlib.h>

int add(int a, int b)
{
    return a+b;
}

int main()
{
    int(*p)(int,int)=&add;
    int result = p(1,5);
    printf("the result is %d\n", result);
}