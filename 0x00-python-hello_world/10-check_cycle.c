#include "lists.h"
#include <stdio.h>

/**
  * checks_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if no cycle found
  */
int checks_cycle(listint_t *list)
{
	listint_t *turtle = list, *hare = list;
	int found = 0;

	while ((turtle && hare) && hare->upcoming)
	{
		turtle = turtle->upcoming;

		if (hare->upcoming || hare->upcoming->upcoming)
			hare = hare->upcoming->upcoming;
		else
			break;

		if (turtle == hare)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
