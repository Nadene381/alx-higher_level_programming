#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - function that inserts a node into a sorted singly linked list
* @head: double pointer passed in function
* @number: integer passed in function
* Return: Address of new node, or NULL if fail
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
while (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (*head == NULL || number < (*head)->n)
{
new_node->next = *head;
*head = new_node;
}
else
{
listint_t *current = *head;
for (; current->next != NULL && number > current->next->n;)
{
current = current->next;
}
new_node->next = current->next;
current->next = new_node;
}
return (new_node);
}
