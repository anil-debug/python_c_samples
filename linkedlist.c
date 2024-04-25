#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* nextlink;
};

int main()
{
    struct Node* head = (struct Node*)malloc(sizeof(struct Node));
    if (head == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Exit with an error code
    }
    head->data = 25;
    head->nextlink = NULL;

    struct Node* secondnode = (struct Node*)malloc(sizeof(struct Node));
    secondnode->data = 30;
    secondnode->nextlink = NULL;
    head->nextlink = secondnode;
    struct Node* current = head;
    while (current != NULL) {
        printf("Data: %d\n", current->data);
        current = current->nextlink;
    }

    free(head);
    free(secondnode);
    
    return 0;
}