#include <stdio.h>
#include <stdlib.h>

// Function to convert decimal number to binary string
char* decimalToBinary(int num) {
    static char binary[9]; // 8 bits + null terminator
    for (int i = 7; i >= 0; i--) {
        binary[7 - i] = ((num >> i) & 1) + '0'; // Extract the bit and convert to ASCII
    }
    binary[8] = '\0'; // Null-terminate the string
    return binary;
}

int main() {
    int a;

    printf("enter the decimal number for shifting");
    scanf("%d",&a);
    // 12 * 2 * 2 * 2
    int leftShiftResult = a << 3;
    printf("The value of left shift operator is: %d (Binary: %s)\n", leftShiftResult, decimalToBinary(leftShiftResult));
    
    // 12 / 2 / 2 / 2
    int rightShiftResult = a >> 3;
    printf("The value of right shift operator is: %d (Binary: %s)\n", rightShiftResult, decimalToBinary(rightShiftResult));
    
    return 0;
}
