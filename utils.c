#include "push_swap.h"

void	error_exit(void)
{
	write(2, "Error\n", 6);
	exit(1);
}

static int	ft_isspace(char c)
{
	return (c == ' ' || c == '\t' || c == '\n'
		|| c == '\r' || c == '\v' || c == '\f');
}

int	ft_atoi_safe(const char *s, int *out)
{
	long	n;
	int		sign;

	n = 0;
	sign = 1;
	while (ft_isspace(*s))
		s++;
	if (*s == '-' || *s == '+')
	{
		if (*s == '-')
			sign = -1;
		s++;
	}
	if (!(*s >= '0' && *s <= '9'))
		return (0);
	while (*s >= '0' && *s <= '9')
	{
		n = n * 10 + (*s - '0');
		if ((sign == 1 && n > INT_MAX) || (sign == -1 && -n < INT_MIN))
			return (0);
		s++;
	}
	if (*s != '\0')
		return (0);
	*out = (int)(sign * n);
	return (1);
}

int	parse_args(int argc, char **argv, t_stack *a)
{
	int		i;
	int		val;
	t_node	*cur;
	t_node	*new;

	i = 1;
	while (i < argc)
	{
		if (!ft_atoi_safe(argv[i], &val))
			return (0);
		cur = a->top;
		while (cur)
		{
			if (cur->val == val)
				return (0);
			cur = cur->next;
		}
		new = malloc(sizeof(t_node));
		if (!new)
			return (0);
		new->val = val;
		new->rank = 0;
		new->next = NULL;
		new->prev = NULL;
		if (!a->top)
		{
			a->top = new;
			a->size++;
		}
		else
		{
			t_node	*tail = a->top;
			while (tail->next)
				tail = tail->next;
			tail->next = new;
			new->prev = tail;
			a->size++;
		}
		i++;
	}
	return (1);
}

int	is_sorted(t_stack *a)
{
	t_node	*cur;

	cur = a->top;
	while (cur && cur->next)
	{
		if (cur->val > cur->next->val)
			return (0);
		cur = cur->next;
	}
	return (1);
}

void	free_stack(t_stack *s)
{
	t_node	*cur;
	t_node	*next;

	cur = s->top;
	while (cur)
	{
		next = cur->next;
		free(cur);
		cur = next;
	}
	s->top = NULL;
	s->size = 0;
}

void	assign_ranks(t_stack *a)
{
	t_node	*cur;
	t_node	*inner;
	int		rank;

	cur = a->top;
	while (cur)
	{
		rank = 0;
		inner = a->top;
		while (inner)
		{
			if (inner->val < cur->val)
				rank++;
			inner = inner->next;
		}
		cur->rank = rank;
		cur = cur->next;
	}
}

int	stack_min_rank(t_stack *s)
{
	t_node	*cur;
	int		min;

	if (!s->top)
		return (-1);
	cur = s->top;
	min = cur->rank;
	while (cur)
	{
		if (cur->rank < min)
			min = cur->rank;
		cur = cur->next;
	}
	return (min);
}

int	find_rank(t_stack *s, int rank)
{
	t_node	*cur;
	int		pos;

	cur = s->top;
	pos = 0;
	while (cur)
	{
		if (cur->rank == rank)
			return (pos);
		cur = cur->next;
		pos++;
	}
	return (-1);
}
