#include <stdio.h>
#include <stdbool.h>
#include "lists.h"

/**
* check_cycle - Function that checks if a singly linked list has a cycle in it
* @head: pointer passed in function
* Return: true if there is a cycle, false otherwise
*/
int check_cycle(listint_t *head)
{
listint_t *slow = head;
listint_t *fast = head;
for (; fast != NULL && fast->next != NULL;)
{
slow = slow->next;
fast = fast->next->next;
while (slow == fast)
return (true);
}
return (false);
}
