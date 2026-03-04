#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include "get_next_line.h"

static int bufsize = 10;
static int i = 0;

char *get_next_line(int fd)
{
	int	n;
	char	*buffer;
	char	*buffertmp;
	int	start;

	start = 0;
	if (fd < 0)
		return (NULL);
	buffer = malloc(sizeof(int) * bufsize);
	if (!buffer)
		return (NULL);
	n = read(fd, buffer, bufsize);
	if (n < 0)
		return (NULL);
	buffer[n] = '\n';
	while (buffer[i] == '\n')
	{
		printf("%c", buffer[i]);
		i++;
	}
	buffertmp = ft_strdup(buffer);
	free(buffer);
	close(fd);
	return (buffertmp);
}
