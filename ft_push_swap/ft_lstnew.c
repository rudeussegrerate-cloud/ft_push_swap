/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/03 22:30:30 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:03:13 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_push_swap.h"

stack	*ft_lstnew(void *content)
{
	stack	*list;

	list = malloc(sizeof(stack));
	if (!list)
		return (NULL);
	list->content = content;
	list->next = NULL;
	return (list);
}
