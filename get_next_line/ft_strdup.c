/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tusandri <tusandri@student.42antananari    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/05 15:28:08 by tusandri          #+#    #+#             */
/*   Updated: 2026/02/06 03:04:05 by tusandri         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_utils.h"

char	*ft_strdup(const char *source)
{
	char	*duptmp;
	size_t	i;
	size_t	len;

	i = 0;
	len = ft_strlen(source);
	duptmp = (char *) malloc(sizeof(char) * (len + 1));
	if (!duptmp)
		return (NULL);
	ft_strlcpy(duptmp, source, (len + 1));
	return (duptmp);
}
