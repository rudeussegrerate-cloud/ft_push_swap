/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 20:20:33 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:02:53 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_push_swap.h"

void	ft_lstadd_back(stack **lst, stack *new)
{
	stack	*liste;

	liste = *lst;
	if (!lst || !new)
		return ;
	if (*lst == NULL)
	{
		*lst = new;
		return ;
	}
	while (liste)
	{
		if (liste->next == NULL)
			break ;
		liste = liste->next;
	}
	liste->next = new;
	new->next = NULL;
}
