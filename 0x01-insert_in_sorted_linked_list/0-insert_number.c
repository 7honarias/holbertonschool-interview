#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - prints all elements of a listint_t list
 * @h: pointer to head of list
 * @number: number to insert
 * Return: new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    const listint_t *current;

    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    
    new->n = number;
    new->next = NULL;
    if (current == NULL)
        return (new);
    
    while (current != NULL)
    {
        if (number > current->n && number < current->next->n) {
            break;
        }
        current = current->next;
    }
    current->next = new;
    new->next = current->next;

    return (new);
}
