#include "lists.h"

/**
 * insert_node - inserts a nouv node
 * @head: head
 * @number: index of the list
 * Return: the address of the nouv node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nouv;
	listint_t *h;
	listint_t *prev;

	h = *head;
	nouv = malloc(sizeof(listint_t));

	if (nouv == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}

	nouv->n = number;

	if (*head == NULL)
	{
		nouv->next = NULL;
		*head = nouv;
	}
	else
	{
		nouv->next = h;
		if (h == *head)
			*head = nouv;
		else
			prev->next = nouv;
	}

	return (nouv);
}
