#include "push_swap.h"

void	push_node(t_stack *s, t_node *node)
{
	node->next = s->top;
	node->prev = NULL;
	if (s->top)
		s->top->prev = node;
	s->top = node;
	s->size++;
}

t_node	*pop_node(t_stack *s)
{
	t_node	*node;

	if (!s->top)
		return (NULL);
	node = s->top;
	s->top = node->next;
	if (s->top)
		s->top->prev = NULL;
	node->next = NULL;
	node->prev = NULL;
	s->size--;
	return (node);
}

t_node	*peek(t_stack *s)
{
	return (s->top);
}

t_node	*bottom(t_stack *s)
{
	t_node	*cur;

	cur = s->top;
	if (!cur)
		return (NULL);
	while (cur->next)
		cur = cur->next;
	return (cur);
}
