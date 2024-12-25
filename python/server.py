from concurrent import futures
import grpc
import os
# import json
import requests
from dotenv import load_dotenv

import countries_pb2 as countries_pb2
import countries_pb2_grpc as countries_pb2_grpc

class CountryService(countries_pb2_grpc.CountryServicer):
    def search(self, request, context):
        load_dotenv()
        access_key = os.getenv("AccessKey")

        # Gửi yêu cầu đến API bên ngoài
        try:
            response = requests.get(f"https://api.countrylayer.com/v2/name/{request.name}?access_key={access_key}")
            response.raise_for_status()
            data = response.json()

            # Trả về thông tin đầu tiên từ API
            country_data = data[0]
            return countries_pb2.CountryResponse(
                name=country_data["name"],
                alpha2Code=country_data["alpha2Code"],
                alpha3Code=country_data["alpha3Code"],
                capital=country_data["capital"],
                region=country_data["region"],
            )
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return countries_pb2.CountryResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    countries_pb2_grpc.add_CountryServicer_to_server(CountryService(), server)
    server.add_insecure_port('[::]:3000')
    print("Server is starting on port 3000...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
