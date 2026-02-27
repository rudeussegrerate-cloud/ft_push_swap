/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_push_swap.h                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hrandri2 <hrandri2@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/24 05:29:33 by hrandri2          #+#    #+#             */
/*   Updated: 2026/02/24 05:30:13 by hrandri2         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PUSH_SWAP_H
# define FT_PUSH_SWAP_H

# include <unistd.h>
# include <stdlib.h>

typedef struct stack
{
	void			*content;
	struct stack	*next;
}	stack;

stack	*ft_lstnew(void *content);
void	ft_lstdelone(stack *lst, void (*del)(void*));
void	ft_lstiter(stack *lst, void (*f)(void *));
void	ft_lstadd_front(stack **lst, stack *new);
void	ft_lstadd_back(stack **lst, stack *new);
stack	*ft_lstlast(stack *lst);
/*
int		ft_lstsize(t_list *lst);
void	ft_lstclear(t_list **lst, void (*del)(void*));
t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *));
*/
#endif
