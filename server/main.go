package main

import (
	"encoding/json"
	"flask_go_grpc/server/countries"
	"io"
	"log"
	"net"
	"net/http"
	"os"

	"github.com/joho/godotenv"
	"golang.org/x/net/context"
	"google.golang.org/grpc"
)

// Server is implementation of the proto interface
type Server struct {
    countries.UnimplementedCountryServer
}

func main() {
    grpcServer := grpc.NewServer()
    var server Server
    countries.RegisterCountryServer(grpcServer, server)
    listen, err := net.Listen("tcp", "0.0.0.0:3000")
    if err != nil {
        log.Fatalf("could not listen to 0.0.0.0:3000 %v", err)
    }
    log.Println("Server starting...")
    log.Fatal(grpcServer.Serve(listen))
}

// Search function responsible for getting country information
func (Server) Search(ctx context.Context, request *countries.CountryRequest) (*countries.CountryResponse, error) {
    err := godotenv.Load("../.env")
    if err != nil {
        log.Fatal("Error loading .env file")
    }

    accessKey := os.Getenv("AccessKey")
    
    resp, err := http.Get("https://api.countrylayer.com/v2/name/" + request.Name + "?access_key=" + accessKey)

    if err != nil {
        return nil, err
    }
    defer resp.Body.Close()

    jsonData, err := io.ReadAll(resp.Body)
    if err != nil {
        return nil, err
    }

    var data []countries.CountryResponse

    if err := json.Unmarshal(jsonData, &data); err != nil {
        return nil, err
    }

	return &data[0], nil

}
