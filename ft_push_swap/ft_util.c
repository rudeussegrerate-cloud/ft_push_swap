#include "ft_push_swap.h"
#include <stdio.h>

void	ft_sa(stack *a)
{
	void	*tmp;

	if (!a || !a->next)
		return ;
	write(1, "sa\n", 3);
	tmp = a->next->content;
	a->next->content = a->content;
	a->content = tmp;
}

void	ft_sb(stack *b)
{
	void	*tmp;

	if (!b)
		return ;
	write(1, "sb\n", 3);
	tmp = b->next->content;
	b->next->content = b->content;
	b->content = tmp;
}

void	ft_ss(stack *a, stack *b)
{
	if (!a || !b)
		return ;
	ft_sa(a);
	ft_sb(b);
	write (1, "ss\n", 3);
}

/////////////////////////////////////////////////////
//fonction d'affichage hitestena an le liste;
void	ft_print_swap(stack *stk)
{
	if (!stk)
		return ;
	while (stk)
	{
		printf("%d", *(int *)stk->content); // msolo ft_printf io;
		stk = stk->next;
	}
	write(1, "", 1);
}
////////////////////////////////////////////////

void	ft_pa(stack **a, stack **b)
{
	stack *tmp;

	if (!b || !*b)
		return ;
	write (1, "pa\n", 3);
	tmp = *b;
	*b = (*b)->next;
	ft_lstadd_front(a, tmp);
}

void	ft_pb(stack **a, stack **b)
{
	stack *tmp;

	if (!a || !*a)
		return ;
	write (1, "pb\n", 3);
	tmp = *a;
	*a = (*a)->next;
	ft_lstadd_front(b, tmp);
}

void	ft_ra(stack **a)
{
	stack *tmp;
	if (!a || !*a)
		return ;
	write (1 ,"ra\n", 3);
	tmp = *a;
	*a = (*a)->next;
	ft_lstadd_back(a, tmp);
}

void	ft_rb(stack **b)
{
	stack	*tmp;
	
	if(!b || !*b)
		return ;
	write(1, "rb\n", 3);
	tmp = *b;
	*b = (*b)->next;
	ft_lstadd_back(b, tmp);
}

void	ft_rr(stack **a, stack **b)
{
	write (1, "rr\n", 3);
	ft_ra(a);
	ft_rb(b);
}

void	ft_rra(stack **a)
{
	stack	*tmp;
	stack	*list;
	
	list = *a;
	if(!a || !*a)
		return ;
	write(1, "rra\n", 4);
	tmp = ft_lstlast(*a);
	while (list->next != tmp)
		list = list->next;
	list->next = NULL;
	tmp->next = *a;
	*a = tmp;
}


void	ft_rrb(stack **b)
{
	stack	*tmp;
	stack	*list;

	list = *b;
	if(!b || !*b)
		return ;
	write(1, "rrb\n", 4);
	tmp = ft_lstlast(*b);
	while (list->next != tmp)
		list = list->next;
	list->next = NULL;
	tmp->next = *b;
	*b = tmp;
}

void	ft_rrr(stack **a, stack **b)
{
	write(1, "rrr\n", 4);
	ft_rra(a);
	ft_rrb(b);
}


////////////////////////////////////////////////////////////
	/* test exemple */ //(fait maison ;p)
/////////////////////////////////////////////////////////////

int main()
{
    // créer les stacks a et b
    stack *a = NULL;
    stack *b = NULL;

    int	a1 = 3;
    int	b1 = 2;
    int	c = 1;

    b = ft_lstnew(&a1);
    b->next = ft_lstnew(&b1);
    b->next->next = ft_lstnew(&c);

    printf("Avant ft_pa:\n");
    printf("Stack A: ");
    ft_print_swap(a);
    printf("Stack B: ");
    ft_print_swap(b);

    // déplacer des élément
    
    // ft_rra(&b); // depend du choix :)

    printf("\nAprès ft_pa:\n");
    printf("Stack A: ");
    ft_print_swap(a);
    printf("Stack B: ");
    ft_print_swap(b);
    return 0;
}

