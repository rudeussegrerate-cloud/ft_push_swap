#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

typedef struct s_node
{
	int				val;
	int				rank;
	struct s_node	*next;
	struct s_node	*prev;
}	t_node;

typedef struct s_stack
{
	t_node	*top;
	int		size;
}	t_stack;

/* utils.c */
void	error_exit(void);
int		ft_atoi_safe(const char *s, int *out);
int		parse_args(int argc, char **argv, t_stack *a);
int		is_sorted(t_stack *a);
void	free_stack(t_stack *s);
int		stack_min_rank(t_stack *s);
int		find_rank(t_stack *s, int rank);
void	assign_ranks(t_stack *a);

/* stack.c */
void	push_node(t_stack *s, t_node *node);
t_node	*pop_node(t_stack *s);
t_node	*peek(t_stack *s);
t_node	*bottom(t_stack *s);

/* operations.c */
void	sa(t_stack *a);
void	sb(t_stack *b);
void	ss(t_stack *a, t_stack *b);
void	pa(t_stack *a, t_stack *b);
void	pb(t_stack *a, t_stack *b);
void	ra(t_stack *a);
void	rb(t_stack *b);
void	rr(t_stack *a, t_stack *b);
void	rra(t_stack *a);
void	rrb(t_stack *b);
void	rrr(t_stack *a, t_stack *b);

/* sort_small.c */
void	sort_two(t_stack *a);
void	sort_three(t_stack *a);
void	sort_five(t_stack *a, t_stack *b);

/* sort_large.c */
void	sort_large(t_stack *a, t_stack *b);

#endif
