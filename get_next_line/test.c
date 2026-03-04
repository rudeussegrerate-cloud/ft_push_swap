#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include "get_next_line.h"

int	main()
{
	int	fd = open("get_next_line.c", O_RDONLY);
	
	if (fd < 0)
		return (1);
	printf("%s", get_next_line(fd));
	printf("%s", get_next_line(fd));
	return (0);
}
