#include "lists.h"

/**
 * insert_node - function for inserting a number into a sorted list
 * @head: pointer to the head of the list
 * @number: the number to insert
 * Return: the address of new node otherwise null on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current, *prev;

    if (!head)
        return (NULL);

    new = malloc(sizeof(listint_t));
    if (!new)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (!*head)
    {
        *head = new;
        return (new);
    }

    current = *head;
    prev = NULL;

    while (current && current->n < number)
    {
        prev = current;
        current = current->next;
    }

    if (prev == NULL)
    {
        new->next = *head;
        *head = new;
    }
    else
    {
        prev->next = new;
        new->next = current;
    }

    return (new);

}
