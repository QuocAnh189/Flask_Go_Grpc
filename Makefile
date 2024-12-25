protobuf-python:
	python -m grpc_tools.protoc -I. --python_out=client --grpc_python_out=client countries.proto

protobuf-go:
	protoc -I . --go_out=. --go-grpc_out=. countries.proto

server-go:
	go run server/main.go

client-python:
	python app.py