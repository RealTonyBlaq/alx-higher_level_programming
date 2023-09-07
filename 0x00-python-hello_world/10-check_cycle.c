#include "lists.h"

/**
 * check_cycle - Program checks if a linked list
 * has a cycle or not.
 * @list: A listint_t list
 *
 * Return: 1 if a cycle exists, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *cheetah, *tmp;

	if (list == NULL)
		return (0);
	tmp = list;
	while (tmp != NULL)
	{
		tortoise = tmp;
		tmp = tmp->next;
		cheetah = tmp->next;
		if (cheetah == tortoise)
			return (1);
		if (cheetah == NULL || tortoise == NULL)
			return (0);
	}
	return (0);
}
