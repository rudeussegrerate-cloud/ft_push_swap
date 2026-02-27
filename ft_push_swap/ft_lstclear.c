/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 20:21:24 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:02:59 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void*))
{
	t_list	*liste;

	if (!lst || !del)
		return ;
	while (*lst)
	{
		liste = (*lst)->next;
		del((*lst)->content);
		free(*lst);
		*lst = liste;
	}
	*lst = NULL;
}
