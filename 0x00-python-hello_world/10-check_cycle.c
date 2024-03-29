#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *previous;
	listint_t *p2;

	p2 = list;
	previous = list;
	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;

		if (list == p2)
		{
			list = previous;
			previous =  p2;
			while (1)
			{
				p2 = previous;
				while (p2->next != list && p2->next != previous)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
