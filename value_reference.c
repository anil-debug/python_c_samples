#include <stdio.h>
#include <stdlib.h>

// Function to swap two numbers using pass-by-value
int swap(int a, int b)
{
    printf("Before swapping the numbers are %d and %d\n", a, b);
    int temp = a;
    a = b;
    b = temp;
    printf("After swapping the numbers are %d and %d\n", a, b);
    return a; // Return the swapped value if needed
}

// Function to swap two numbers using pass-by-reference
int swap_1(int &a, int &b)
{
    printf("Before swapping the numbers are %d and %d\n", a, b);
    int temp = a;
    a = b;
    b = temp;
    printf("After swapping the numbers are %d and %d\n", a, b);
    return a; // Return the swapped value if needed
}

int main()
{
    int x = 5, y = 10;
    
    printf("Original numbers are %d and %d\n", x, y);
    
    // Using pass-by-value swap function
    int result = swap(x, y);
    printf("Returned value after swapping (pass-by-value): %d\n", result);

    // Using pass-by-reference swap function
    result = swap_1(x, y);
    printf("Returned value after swapping (pass-by-reference): %d\n", result);

    printf("Numbers after swapping in the main function are %d and %d\n", x, y);

    return 0;
}
