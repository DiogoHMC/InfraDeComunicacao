.PHONY: server client

server:
	@echo "Running server..."
	@python server/server.py

client:
	@echo "Running client..."
	@python client/client.py