#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to a head of the list
 * Return: 1 if cycle is present, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (!list)
		return (0);
	tmp = list->next;
	while (tmp != list)
	{
		if (tmp == NULL)
			return (0);
		tmp = tmp->next;
	}
	return (1);
}
