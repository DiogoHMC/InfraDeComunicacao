all: redes

CC = clang
override CFLAGS += -g -Wno-everything -pthread -lm

SRCS = $(redes find . -name '.ccls-cache' -type d -prune -o -type f -name '*.c' -print)
HEADERS = $(redes find . -name '.ccls-cache' -type d -prune -o -type f -name '*.h' -print)

redes: $(SRCS) $(HEADERS)
	$(CC) $(CFLAGS) $(SRCS) -o "$@"

redes-debug: $(SRCS) $(HEADERS)
	$(CC) $(CFLAGS) -O0 $(SRCS) -o "$@"

clean:
	rm -f redes redes-debug

run-server:
	osascript -e 'tell app "Terminal" to do script "cd Documents/InfraDeComunicacao && python3 server/server.py"'

run-client:
	osascript -e 'tell app "Terminal" to do script "cd Documents/InfraDeComunicacao && python3 client/client.py"'

start:
	make run-server & make run-client
