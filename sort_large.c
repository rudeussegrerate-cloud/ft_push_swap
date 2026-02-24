#include "push_swap.h"

static int	find_max_pos(t_stack *s, int *max_rank_out)
{
	t_node	*cur;
	int		pos;
	int		max_pos;
	int		max_rank;

	cur = s->top;
	pos = 0;
	max_pos = 0;
	max_rank = cur->rank;
	while (cur)
	{
		if (cur->rank > max_rank)
		{
			max_rank = cur->rank;
			max_pos = pos;
		}
		cur = cur->next;
		pos++;
	}
	if (max_rank_out)
		*max_rank_out = max_rank;
	return (max_pos);
}

static int	find_min_pos(t_stack *s, int *min_rank_out)
{
	t_node	*cur;
	int		pos;
	int		min_pos;
	int		min_rank;

	cur = s->top;
	pos = 0;
	min_pos = 0;
	min_rank = cur->rank;
	while (cur)
	{
		if (cur->rank < min_rank)
		{
			min_rank = cur->rank;
			min_pos = pos;
		}
		cur = cur->next;
		pos++;
	}
	if (min_rank_out)
		*min_rank_out = min_rank;
	return (min_pos);
}

/*
** Find the target position in A (circular sorted) for inserting element
** with the given rank. Returns the position where the element should be
** inserted (i.e., rotate A by this many ra ops to put it in place after pa).
*/
static int	target_in_a(t_stack *a, int rank)
{
	int		max_rank;
	int		min_rank;
	int		min_pos;
	int		i;
	int		pos;
	t_node	*cur;

	find_max_pos(a, &max_rank);
	min_pos = find_min_pos(a, &min_rank);
	if (rank > max_rank || rank < min_rank)
		return (min_pos);
	i = 0;
	while (i < a->size)
	{
		pos = (min_pos + i) % a->size;
		cur = a->top;
		while (pos-- > 0)
			cur = cur->next;
		if (cur->rank > rank)
			return ((min_pos + i) % a->size);
		i++;
	}
	return (min_pos);
}

/*
** Calculate the minimum cost to bring element at b_pos in B and
** a_pos target in A simultaneously, considering rr/rrr combined ops.
*/
static int	calc_cost(int a_pos, int a_size, int b_pos, int b_size)
{
	int	a_fwd;
	int	a_rev;
	int	b_fwd;
	int	b_rev;
	int	costs[4];
	int	min;
	int	i;

	a_fwd = a_pos;
	a_rev = a_size - a_pos;
	b_fwd = b_pos;
	b_rev = b_size - b_pos;
	costs[0] = (a_fwd > b_fwd) ? a_fwd : b_fwd;
	costs[1] = (a_rev > b_rev) ? a_rev : b_rev;
	costs[2] = a_fwd + b_rev;
	costs[3] = a_rev + b_fwd;
	min = costs[0];
	i = 1;
	while (i < 4)
	{
		if (costs[i] < min)
			min = costs[i];
		i++;
	}
	return (min + 1);
}

/*
** Execute the best combined rotation for a_pos rotations in A and
** b_pos rotations in B, then pa.
*/
static void	execute_move(t_stack *a, t_stack *b, int a_pos, int b_pos)
{
	int	a_fwd;
	int	a_rev;
	int	b_fwd;
	int	b_rev;
	int	costs[4];
	int	best;
	int	common;
	int	i;

	a_fwd = a_pos;
	a_rev = a->size - a_pos;
	b_fwd = b_pos;
	b_rev = b->size - b_pos;
	costs[0] = (a_fwd > b_fwd) ? a_fwd : b_fwd;
	costs[1] = (a_rev > b_rev) ? a_rev : b_rev;
	costs[2] = a_fwd + b_rev;
	costs[3] = a_rev + b_fwd;
	best = 0;
	i = 1;
	while (i < 4)
	{
		if (costs[i] < costs[best])
			best = i;
		i++;
	}
	if (best == 0)
	{
		common = (a_fwd < b_fwd) ? a_fwd : b_fwd;
		i = common;
		while (i-- > 0)
			rr(a, b);
		i = a_fwd - common;
		while (i-- > 0)
			ra(a);
		i = b_fwd - common;
		while (i-- > 0)
			rb(b);
	}
	else if (best == 1)
	{
		common = (a_rev < b_rev) ? a_rev : b_rev;
		i = common;
		while (i-- > 0)
			rrr(a, b);
		i = a_rev - common;
		while (i-- > 0)
			rra(a);
		i = b_rev - common;
		while (i-- > 0)
			rrb(b);
	}
	else if (best == 2)
	{
		while (a_fwd-- > 0)
			ra(a);
		while (b_rev-- > 0)
			rrb(b);
	}
	else
	{
		while (a_rev-- > 0)
			rra(a);
		while (b_fwd-- > 0)
			rb(b);
	}
	pa(a, b);
}

/*
** Count elements in stack with rank in [lo, hi].
*/
static int	count_in_range(t_stack *s, int lo, int hi)
{
	t_node	*cur;
	int		count;

	cur = s->top;
	count = 0;
	while (cur)
	{
		if (cur->rank >= lo && cur->rank <= hi)
			count++;
		cur = cur->next;
	}
	return (count);
}

/*
** Push elements to B in chunks (bidirectional scan).
** Checks both top and bottom of A to reduce rotation count.
*/
static void	push_chunks_to_b(t_stack *a, t_stack *b, int chunk_size)
{
	int	n;
	int	chunk_min;
	int	chunk_max;
	int	to_push;

	n = a->size;
	chunk_min = 0;
	while (a->size > 3)
	{
		chunk_max = chunk_min + chunk_size - 1;
		if (chunk_max >= n)
			chunk_max = n - 1;
		to_push = count_in_range(a, chunk_min, chunk_max);
		if (a->size - to_push < 3)
			to_push = a->size - 3;
		while (to_push > 0 && a->size > 3)
		{
			if (a->top->rank >= chunk_min && a->top->rank <= chunk_max)
			{
				pb(a, b);
				to_push--;
			}
			else if (bottom(a)->rank >= chunk_min
				&& bottom(a)->rank <= chunk_max)
				rra(a);
			else
				ra(a);
		}
		chunk_min = chunk_max + 1;
	}
}

/*
** Turk insertion: for each element in B, find cheapest insertion into A,
** execute it, until B is empty.
*/
static void	turk_insert(t_stack *a, t_stack *b)
{
	t_node	*cur;
	int		b_pos;
	int		a_pos;
	int		cost;
	int		best_cost;
	int		best_b_pos;
	int		best_a_pos;

	while (b->size > 0)
	{
		cur = b->top;
		b_pos = 0;
		best_cost = -1;
		best_b_pos = 0;
		best_a_pos = 0;
		while (cur)
		{
			a_pos = target_in_a(a, cur->rank);
			cost = calc_cost(a_pos, a->size, b_pos, b->size);
			if (best_cost == -1 || cost < best_cost)
			{
				best_cost = cost;
				best_b_pos = b_pos;
				best_a_pos = a_pos;
			}
			cur = cur->next;
			b_pos++;
		}
		execute_move(a, b, best_a_pos, best_b_pos);
	}
}

/*
** Rotate A until the minimum rank is at the top (final sort pass).
*/
static void	rotate_min_to_top(t_stack *a)
{
	int	min_pos;

	min_pos = find_min_pos(a, NULL);
	if (min_pos <= a->size / 2)
	{
		while (min_pos-- > 0)
			ra(a);
	}
	else
	{
		min_pos = a->size - min_pos;
		while (min_pos-- > 0)
			rra(a);
	}
}

void	sort_large(t_stack *a, t_stack *b)
{
	int	n;
	int	chunk_size;

	n = a->size;
	if (n <= 100)
		chunk_size = 20;
	else
		chunk_size = n / 8;
	push_chunks_to_b(a, b, chunk_size);
	if (a->size == 3)
		sort_three(a);
	else if (a->size == 2)
		sort_two(a);
	turk_insert(a, b);
	rotate_min_to_top(a);
}
