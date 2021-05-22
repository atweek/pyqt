NAME =  main
SRC_DESC = ./src_qt/main.py
SRC_BOT = ./src_tg/bot.py

all: $(NAME)

$(NAME):
	pyinstaller --onefile --noconsole $(SRC_DESC)
	mv build ./app
	mv dist ./app
	mv main.spec ./app

py:
	python3 $(SRC_BOT) &
	python3 $(SRC_DESC)

run:
	python3 $(SRC_BOT) &
	./app/dist/main

kill:
	ps -ale | pgrep  python3 | xargs kill

ui:
	sh src_qt/disigner/ui.sh


#clean:
#	@rm -f app/*
#
fclean: clean
	@rm -rf app/*

re: fclean all

.PHONY: clean fclean all re