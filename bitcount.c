#include <stdio.h>

// Function to count the number of bits set to 1 and 0
void countBits(int num) {
    int onesCount = 0; // Initialize the count of 1 bits to 0
    int zerosCount = 0; // Initialize the count of 0 bits to 0

    while (num > 0) {
        // Use bitwise AND with 1 to check the least significant bit
        if (num & 1) {
            onesCount++; // If the bit is 1, increment onesCount
        } else {
            zerosCount++; // If the bit is 0, increment zerosCount
        }
        // Right-shift the number to check the next bit
        num >>= 1;
    }

    printf("Number of 1 bits: %d\n", onesCount);
    printf("Number of 0 bits: %d\n", zerosCount);
}

int main() {
    int num = 0b11011010101; // Example input (replace with your integer)

    countBits(num);

    return 0;
}
