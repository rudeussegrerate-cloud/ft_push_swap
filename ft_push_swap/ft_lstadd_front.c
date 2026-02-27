/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 20:20:54 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:02:55 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_push_swap.h"

void	ft_lstadd_front(stack **lst, stack *new)
{
	if (!new || !lst)
		return ;
	new->next = *lst;
	*lst = new;
}
