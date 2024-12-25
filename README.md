# FLask_Go_Grpc

===========================================================

# 1. How to run the app (Development Environment)

Go (version 1.23.2) - Python (version 3.8.10)
Require: Check `protoc --version` or install

1. Clone the repo and cd into it
2. Rename or copy `.env.example` file to `.env` (Get AccessKey at `https://api.countrylayer.com`)
3. Download the necessary python libraries in the python directory
4. Install gRPC packages for Python `pip install grpcio grpcio-tools`
5. Download the necessary go libraries in the golang directory
6. Install gRPC packages for Golang `go get -u google.golang.org/grpc`
7. In your terminal run `python -m grpc_tools.protoc -I. --python_out=client --grpc_python_out=client countries proto`
8. In your terminal run `protoc -I . --go_out=. --go-grpc_out=. countries.proto`

## Client-Side(Golang) And Server-Side(Python)

In your terminal `cd golang` at server folder , run `go run client.go` to start client.
In your terminal `cd python` at client folder , run `python server.py` to start grpc server.

## Client-Side(Python) And Server-Side(Golang)

In your terminal `cd python` at client folder , run `python client.py` to start client.
In your terminal `cd golang` at server folder , run `go run server.go` to start grpc server.

### POSTMAN DEMO :

# Client-Side(Golang) And Server-Side(Python)

![imagedemo](https://res.cloudinary.com/dadvtny30/image/upload/v1735121556/portfolio/caogks9ulwrnjyrnjyom.png)

# Client-Side(Python) And Server-Side(Golang)

![imagedemo](https://res.cloudinary.com/dadvtny30/image/upload/v1735121542/portfolio/fclx9dppumnhlwf5sel8.png)

## Author Contact

Contact me with any questions!<br>

Email: anquoc18092003@gmail.com
Facebook: https://www.facebook.com/tranphuocanhquoc2003

<p style="text-align:center">Thank You so much for your time !!!</p>
