#include <stdio.h>
#include "get_next_line.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	lensrc;

	i = 0;
	lensrc = ft_strlen(src);
	if (size == 0)
		return (lensrc);
	while (i < size - 1 && src[i])
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (lensrc);
}

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
