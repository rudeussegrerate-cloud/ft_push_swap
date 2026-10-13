NAME = codexion
CC = cc
FLAG = -Wall -Wextra -Werror
SRC = main.c
OBJ = $(SRC:.c=.o)


all: $(NAME)

$(NAME): $(OBJ)
	$(CC) $(FLAG) $(SRC) -o $(NAME)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean clean

.PHONY: all clean fclean re
