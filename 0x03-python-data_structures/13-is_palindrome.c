#include "lists.h"

/**
 * is_palindrome - Checks if a linked list
 * is a palindrome
 * @head: The head pointer to the list
 *
 * Return: 1 if true, else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *forward = *head, *backward = NULL;
	listint_t *cheetah = *head, *tortoise = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (0);

	while (cheetah != NULL && cheetah->next != NULL)
	{
		tortoise = tortoise->next;
		cheetah = cheetah->next->next;
	}
	backward = reverse_list(tortoise);
	while (backward != NULL)
	{
		forward = forward->next;
		backward = backward->next;
		if (forward->n != backward->n)
			return (0);
	}
	return (1);
}

/**
 * reverse_list - Function reverses a list
 * @head: The head pointer to the list
 *
 * Return: The reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *front = NULL;
	listint_t *current = head;
	listint_t *back = NULL;

	while (current != NULL)
	{
		front = current->next;
		current->next = back;
		back = current;
		current = front;
	}
	return (back);
}
