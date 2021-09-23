from __future__ import print_function
from concurrent import futures
from flask import jsonify
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict
import grpc
import json


import logging
import string
import proto_message_pb2
import proto_message_pb2_grpc
import redis
from flask import Flask
from flask import request



#Inicio servidor Redis

r = redis.Redis(host="localhost", port=6379, db=0)
r.config_set('maxmemory', 524288*2)
r.config_set('maxmemory-policy', 'allkeys-lru')
r.flushall()

#-------------------------------------------------------------



#-------------------------------------------------------------

class Search(proto_message_pb2_grpc.SearchServicer):

	def GetServerResponse(self, request, context):
		#leo json, busco, obtengo lista, devuelvo
		string_busqueda = request.message;
		#CASO: No está en caché
		lista = []
		#loop
		with open('inventario.json', 'r') as file:
			data = json.load(file)
			for linea_json in data['Inventario']:
				if string_busqueda in linea_json['Nombre']:
					lista.append(linea_json)
		r.set(string_busqueda, json.dumps(lista))
		return proto_message_pb2.SearchResult(product=lista)


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	proto_message_pb2_grpc.add_SearchServicer_to_server(Search(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	app = Flask(__name__)
	lista1 = []

	@app.route('/inventario/<string:busqueda>/', methods=['GET'])
	def index(busqueda):
		resultado_cache = r.get(busqueda)
		if resultado_cache == None:
			with grpc.insecure_channel('localhost:50051') as channel:
				stub = proto_message_pb2_grpc.SearchStub(channel)
				response = stub.GetServerResponse(proto_message_pb2.SearchRequest(message=busqueda))
				if list(response.product) == []:
					return "No hay coincidencias"
				else:
					mensaje = MessageToJson(response)
					mensaje = json.loads(mensaje)
					dicc = dict()
					dicc['Resultado busqueda'] = mensaje['product']
					return dicc
		else:
			mensaje = resultado_cache.decode("utf-8")
			mensaje = json.loads(mensaje)
			dicc = dict()
			dicc['Resultado busqueda'] = mensaje
			return dicc

	app.run(host='0.0.0.0', port=81)

	server.wait_for_termination()


if __name__ == '__main__':
	logging.basicConfig()
	serve()
