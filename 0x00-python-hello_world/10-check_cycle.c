#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to a head of the list
 * Return: 1 if cycle is present, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL || list->next == NULL)
		return (0);

	head = list->next;
	tail = list->next->next;

	while (head && tail && head->next)
	{
		if (head == tail)
        {
            return (1);
        }
        head = head->next;
        tail = tail->next->next;
	}
	return (0);
}
