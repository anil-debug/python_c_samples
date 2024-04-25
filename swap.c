#include <stdio.h>
#include <stdlib.h>

int swap(int *a, int *b)
{
    // int temp;
    // temp = *a;
    // *a = *b;
    // *b = temp;
    *a = *a+*b;
    *b = *a-*b;
    *a = *a-*b;
}

int main()
{
    int x, y;
    printf("enter the element x:");
    scanf("%d",&x);
    printf("enetr the element y:");
    scanf("%d",&y);
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(&x,&y);
    printf("After swapping: x = %d, y = %d\n", x, y);
}

// #include <stdio.h>

// void swap(int *a, int *b)
// {
//     int temp;
//     temp = *a;
//     *a = *b;
//     *b = temp;
// }

// int main()
// {
//     int x, y;
//     printf("Enter the element x: ");
//     scanf("%d", &x);
//     printf("Enter the element y: ");
//     scanf("%d", &y);

//     printf("Before swapping: x = %d, y = %d\n", x, y);
//     swap(&x, &y);
//     printf("After swapping: x = %d, y = %d\n", x, y);

//     return 0;
// }
