#include <stddef.h>
#include "lists.h"
/**
* is_palindrome - function that checks if singly linked list is a palindrome
* @head: pointer passed in function
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head;
listint_t *prev = NULL, *next = NULL;
listint_t *first_half = *head, *second_half = NULL;
int is_palindrome = 1;
if (*head == NULL || (*head)->next == NULL)
return (is_palindrome);
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev = slow;
slow = slow->next;
}
if (fast != NULL)
{
slow = slow->next;
}
prev->next = NULL;
while (slow != NULL)
{
next = slow->next;
slow->next = second_half;
second_half = slow;
slow = next;
}
while (second_half != NULL)
{
if (first_half->n != second_half->n)
{
is_palindrome = 0;
break;
}
first_half = first_half->next;
second_half = second_half->next;
}
prev->next = NULL;
while (second_half != NULL)
{
next = second_half->next;
second_half->next = prev->next;
prev->next = second_half;
second_half = next;
}
return (is_palindrome);
}
