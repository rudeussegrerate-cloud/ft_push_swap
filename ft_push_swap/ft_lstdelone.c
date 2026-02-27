/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 20:21:35 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:03:02 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_push_swap.h"

void	ft_lstdelone(stack *lst, void (*del)(void*))
{
	if (!lst || !del)
		return ;
	del(lst->content);
	free (lst);
}
