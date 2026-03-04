NAME = get_next_line

CC = cc

CFLAGS = -Wall -Wextra -Werror

SRC = get_next_line.c get_next_line_utils.c get_next_line.h

OBJ = $(SRC:.c = .o)

HEADER = get_next_line.h

all: $(NAME)

$(NAME): $(OBJ)
	ar rc $(NAME) $(OBJ)

%.o: %.c $(HEADER)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
