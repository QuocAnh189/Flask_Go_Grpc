package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"time"

	"flask_go_grpc/golang/countries"

	"github.com/gin-gonic/gin"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

// gRPC client request
func searchCountry(ctx *gin.Context) {
	// Kết nối với gRPC server
	conn, err := grpc.NewClient("localhost:3000", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": fmt.Sprintf("could not connect to server: %v", err)})
		return
	}
	defer conn.Close()

	client := countries.NewCountryClient(conn)

	countryName := ctx.Param("country")

	// Tạo request gRPC
	req := &countries.CountryRequest{Name: countryName}

	// Gọi server gRPC
	ctxTimeout, cancel := context.WithTimeout(context.Background(), time.Second*20)
	defer cancel()

	resp, err := client.Search(ctxTimeout, req)
	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{"error": fmt.Sprintf("Error while calling Search: %v", err)})
		return
	}

	// Trả về kết quả từ gRPC
	ctx.JSON(http.StatusOK, gin.H{
		"name":       resp.Name,
		"alpha2Code": resp.Alpha2Code,
		"alpha3Code": resp.Alpha3Code,
		"capital":    resp.Capital,
		"region":     resp.Region,
	})
}

func test() {
	r := gin.Default()

	r.GET("/v1/countries/search/:country", searchCountry)

	if err := r.Run(":5000"); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
