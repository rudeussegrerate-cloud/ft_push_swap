#include "push_swap.h"

static void	swap_top(t_stack *s)
{
	int	tmp_val;
	int	tmp_rank;

	if (s->size < 2)
		return ;
	tmp_val = s->top->val;
	tmp_rank = s->top->rank;
	s->top->val = s->top->next->val;
	s->top->rank = s->top->next->rank;
	s->top->next->val = tmp_val;
	s->top->next->rank = tmp_rank;
}

void	sa(t_stack *a)
{
	swap_top(a);
	write(1, "sa\n", 3);
}

void	sb(t_stack *b)
{
	swap_top(b);
	write(1, "sb\n", 3);
}

void	ss(t_stack *a, t_stack *b)
{
	swap_top(a);
	swap_top(b);
	write(1, "ss\n", 3);
}

void	pa(t_stack *a, t_stack *b)
{
	t_node	*node;

	node = pop_node(b);
	if (!node)
		return ;
	push_node(a, node);
	write(1, "pa\n", 3);
}

void	pb(t_stack *a, t_stack *b)
{
	t_node	*node;

	node = pop_node(a);
	if (!node)
		return ;
	push_node(b, node);
	write(1, "pb\n", 3);
}

static void	rotate(t_stack *s)
{
	t_node	*node;
	t_node	*btm;

	if (s->size < 2)
		return ;
	node = pop_node(s);
	btm = bottom(s);
	btm->next = node;
	node->prev = btm;
	node->next = NULL;
	s->size++;
}

void	ra(t_stack *a)
{
	rotate(a);
	write(1, "ra\n", 3);
}

void	rb(t_stack *b)
{
	rotate(b);
	write(1, "rb\n", 3);
}

void	rr(t_stack *a, t_stack *b)
{
	rotate(a);
	rotate(b);
	write(1, "rr\n", 3);
}

static void	rev_rotate(t_stack *s)
{
	t_node	*btm;
	t_node	*prev;

	if (s->size < 2)
		return ;
	btm = bottom(s);
	prev = btm->prev;
	prev->next = NULL;
	s->size--;
	push_node(s, btm);
}

void	rra(t_stack *a)
{
	rev_rotate(a);
	write(1, "rra\n", 4);
}

void	rrb(t_stack *b)
{
	rev_rotate(b);
	write(1, "rrb\n", 4);
}

void	rrr(t_stack *a, t_stack *b)
{
	rev_rotate(a);
	rev_rotate(b);
	write(1, "rrr\n", 4);
}
