import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from companias.modulos.companias.infraestructura.schema.v1.eventos import EventoCompaniaCreada
from companias.modulos.companias.infraestructura.schema.v1.comandos import ComandoCompania
from companias.seedwork.infraestructura import utils
import requests
import json

def suscribirse_a_eventos():
    cliente = None
    try:
        print('broker host')
        print(utils.broker_host())
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-compania', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='companias-sub-eventos', schema=AvroSchema(EventoCompaniaCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-compania', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-compania', schema=AvroSchema(ComandoCompania))
        
        lHost = 'http://0.0.0.0:5000'

        while True:
            mensaje = consumidor.receive()
                
            if (mensaje.value().type == "ComandoCrearCompania"):
                print("CREAR")
                
                url = lHost + '/companias/compania-comando'
                
                compania_dto=mensaje.value().data

                payload = {
                    "direccion":compania_dto.direccion, 
                    "documento_identidad":compania_dto.documento_identidad, 
                    "nombre":compania_dto.nombre, 
                    "telefono":compania_dto.telefono,
                }
                json_payload = json.dumps(payload)

                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.post(url, data=json_payload, headers=headers)

                if response.status_code == 202:
                    print(response.json())
                else:
                    print(f"Error: {response.status_code}")
                print("Comando crear compania entregado")
                consumidor.acknowledge(mensaje)

                
                

            if (mensaje.value().type == "ComandoEliminarCompania"):
                print("ELIMINAR")

                url = lHost + '/companias/compania-query/'+ str(mensaje.value().data.id)

                response = requests.delete(url)
                if response.status_code == 204:
                    print(response)
                else:
                    print(f"Error: {response.status_code}")
                print("Comando eliminar compania entregado")
                consumidor.acknowledge(mensaje)
                
                
                
                
                
            if (mensaje.value().type == "ComandoActualizarCompania"):
                print("ACTUALIZAR")

                url = lHost + '/companias/compania-comando/'+ str(mensaje.value().data.id)
                compania_dto=mensaje.value().data

                payload = {
                    "direccion":compania_dto.direccion, 
                    "documento_identidad":compania_dto.documento_identidad, 
                    "nombre":compania_dto.nombre, 
                    "telefono":compania_dto.telefono,
                }
                json_payload = json.dumps(payload)

                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.put(url, data=json_payload, headers=headers)

                if response.status_code == 202:
                    print(response.json())
                else:
                    print(f"Error: {response.status_code}")
                print("Comando actualizar compania entregado")
                consumidor.acknowledge(mensaje)

        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()