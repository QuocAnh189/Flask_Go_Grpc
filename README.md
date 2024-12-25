# EventHub

===========================================================

# 1. How to run the app (Development Environment)

Go (version 1.23.2) - Python (version 3.8.10)

1. Clone the repo and cd into it
2. Rename or copy `.env.example` file to `.env` (Get AccessKey at `https://api.countrylayer.com`)
3. Download the necessary python libraries in the python/app.py directory
4. Install gRPC packages for Python
   `pip install grpcio grpcio-tools`
5. Download the necessary go libraries in the server/main.go directory
6. Install gRPC packages for Golang
   `go get -u google.golang.org/grpc`
   `golang.org/x/net/context`
7. In your terminal run `python -m grpc_tools.protoc -I. --python_out=client --grpc_python_out=client countries proto`
8. In your terminal run `protoc -I . --go_out=. --go-grpc_out=. countries.proto`
9. In your terminal `cd server` at server folder , run `go run main.go` to start grpc server.
10. In your terminal `cd client` at client folder , run `python app.py` to start client.

### POSTMAN DEMO :

![imagedemo](https://res.cloudinary.com/dadvtny30/image/upload/v1735112521/portfolio/lvwvijnmrd1bdtbicbd8.png)

## Author Contact

Contact me with any questions!<br>

Email: anquoc18092003@gmail.com
Facebook: https://www.facebook.com/tranphuocanhquoc2003

<p style="text-align:center">Thank You so much for your time !!!</p>
