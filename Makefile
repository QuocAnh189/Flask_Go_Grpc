protobuf-python: 
	python -m grpc_tools.protoc -I. --python_out=client --grpc_python_out=client countries.proto
	
protobuf-go:
	protoc --go_out=. --go-grpc_out=. countries.proto

server-go:
	go run golang/client.go (client)
	go run golang/server.go (server)

client-python:
	python python/client.py (client)
	python python/server.py (server)