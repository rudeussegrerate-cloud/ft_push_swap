#include "push_swap.h"

void	sort_two(t_stack *a)
{
	if (a->top->rank > a->top->next->rank)
		sa(a);
}

/*
** Sort 3 elements optimally (at most 2 operations)
** Works with any 3 distinct rank values.
*/
void	sort_three(t_stack *a)
{
	int	r0;
	int	r1;
	int	r2;

	r0 = a->top->rank;
	r1 = a->top->next->rank;
	r2 = a->top->next->next->rank;
	if (r0 < r1 && r1 < r2)
		return ;
	else if (r0 < r2 && r2 < r1)
	{
		rra(a);
		sa(a);
	}
	else if (r1 < r0 && r0 < r2)
		sa(a);
	else if (r2 < r0 && r0 < r1)
		rra(a);
	else if (r1 < r2 && r2 < r0)
		ra(a);
	else
	{
		ra(a);
		sa(a);
	}
}

/*
** Sort 4 or 5 elements: push smallest elements to B, sort 3 in A, push back.
*/
void	sort_five(t_stack *a, t_stack *b)
{
	int	min_rank;
	int	pos;

	while (a->size > 3)
	{
		min_rank = stack_min_rank(a);
		pos = find_rank(a, min_rank);
		if (pos == 0)
			pb(a, b);
		else if (pos <= a->size / 2)
		{
			while (a->top->rank != min_rank)
				ra(a);
			pb(a, b);
		}
		else
		{
			while (a->top->rank != min_rank)
				rra(a);
			pb(a, b);
		}
	}
	sort_three(a);
	while (b->size > 0)
		pa(a, b);
}

