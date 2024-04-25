#include <stdio.h>
#include <stdlib.h>

int main() {
    int *array;
    int arraySize = 5;

    array = (int*)malloc(arraySize * sizeof(int));

    if (array == NULL) {
        printf("Memory allocation failed");
        return 1;
    }

    printf("Enter %d elements for the array:\n", arraySize);
    for (int i = 0; i < arraySize; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    printf("Array elements:\n");
    for (int i = 0; i < arraySize; i++) {
        printf("%d\n", array[i]);
    }

    free(array);
    printf("Memory has been freed.\n");

    return 0;
}
