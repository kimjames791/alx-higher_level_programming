#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @k: an integer
 * @upcoming: points to the next node
 *
 * Description: singly linked list node structure in the func
 * 
 */
typedef struct listint_s
{
	int k;
	struct listint_s *upcomimg;
} listint_t;

size_t printlist_int(const listint_t *k);
listint_t *add_nodeint(listint_t **head, const int k);
void freelist_int(listint_t *head);
int checks_cycle(listint_t *list);

#endif /* LISTS_H */
