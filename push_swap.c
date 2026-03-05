#include "push_swap.h"

int	main(int argc, char **argv)
{
	t_stack	a;
	t_stack	b;

	if (argc < 2)
		return (0);
	a.top = NULL;
	a.size = 0;
	b.top = NULL;
	b.size = 0;
	if (!parse_args(argc, argv, &a))
	{
		free_stack(&a);
		error_exit();
	}
	if (a.size == 0 || is_sorted(&a))
	{
		free_stack(&a);
		return (0);
	}
	assign_ranks(&a);
	if (a.size == 2)
		sort_two(&a);
	else if (a.size == 3)
		sort_three(&a);
	else if (a.size <= 5)
		sort_five(&a, &b);
	else
		sort_large(&a, &b);
	free_stack(&a);
	free_stack(&b);
	return (0);
}
