from flask import Flask
from flask import jsonify

app = Flask(__name__)

import grpc
import countries_pb2 as countries_pb2
import countries_pb2_grpc as countries_pb2_grpc

def obj_to_dict(obj):
    return obj.__dict__

@app.route('/<countrie>')
def countrie(countrie):
    print("Start service")
    try:
        channel = grpc.insecure_channel('localhost:3000')
        stub = countries_pb2_grpc.CountryStub(channel)
        countryRequest = countries_pb2.CountryRequest(name=countrie)
        countryResponse = stub.search(countryRequest)

        return jsonify({
            "name": countryResponse.name,
            "alpha2Code": countryResponse.alpha2Code,
            "alpha3Code": countryResponse.alpha3Code,
            "capital": countryResponse.capital,
            "region": countryResponse.region,
        })
    except Exception as e:
        print("Error:", e)
        return str(e)


if __name__ == '__main__':
    app.run()