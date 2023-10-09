#include "lists.h"

/**
 * get_middle - find the middle of a linked list
 * @head: a pointer to the first node of the list
 * Return: a pointer to the middle node
 */
listint_t *get_middle(listint_t **head)
{
	listint_t *fast, *slow;

	fast = *head;
	slow = *head;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	return (slow);
}

/**
 * reverse_half - reverse a list
 * @middle: a pointer to the first node
 * Return: a pointer to the new head of the list
 */

listint_t *reverse_half(listint_t **middle)
{
	listint_t *current = *middle, *previous = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	return (previous);
}

/**
 * is_palindrome - checks if a list is palindrome
 * @head: a pointer to the first node of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle, *current = *head;

	middle = get_middle(head);
	middle = reverse_half(&middle);

	while (middle != NULL && current != NULL)
	{
		if (middle->n != current->n)
			return (0);
		middle = middle->next;
		current = current->next;
	}
	return (1);
}
