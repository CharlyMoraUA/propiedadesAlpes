import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
import json
import requests

from propiedades.modulos.propiedades.infraestructura.schema.v1.eventos import EventoPropiedadCreado
from propiedades.modulos.propiedades.infraestructura.schema.v1.comandos import ComandoPropiedad
from propiedades.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        print('broker host')
        print(utils.broker_host())
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-propiedad', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='propiedades-sub-eventos', schema=AvroSchema(EventoPropiedadCreado))

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
        consumidor = cliente.subscribe('comando-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-propiedad', schema=AvroSchema(ComandoPropiedad))
        
        lHost = 'http://0.0.0.0:5000'
        while True:
            mensaje = consumidor.receive()
            
            if (mensaje.value().type == "ComandoCrearPropiedad"):
                print("CREAR")
                
                url = lHost + '/propiedades/propiedad-comando'
                
                propiedad_dto=mensaje.value().data

                payload = {
                    "matricula": propiedad_dto.matricula,
                    "direccion": propiedad_dto.direccion,
                    "area": propiedad_dto.area,
                    "tipo": propiedad_dto.tipo
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
                print("Comando crear propiedad entregado")
                consumidor.acknowledge(mensaje)

                
                

            if (mensaje.value().type == "ComandoEliminarPropiedad"):
                print("ELIMINAR")

                url = lHost + '/propiedades/propiedad-query/'+ str(mensaje.value().data.id)

                response = requests.delete(url)
                if response.status_code == 204:
                    print(response)
                else:
                    print(f"Error: {response.status_code}")
                print("Comando eliminar propiedad entregado")
                consumidor.acknowledge(mensaje)
                
                
                
                
                
            if (mensaje.value().type == "ComandoActualizarPropiedad"):
                print("ACTUALIZAR")

                url = lHost + '/propiedades/propiedad-comando/'+ str(mensaje.value().data.id)
                propiedad_dto=mensaje.value().data

                payload = {
                    "matricula": propiedad_dto.matricula,
                    "direccion": propiedad_dto.direccion,
                    "area": propiedad_dto.area,
                    "tipo": propiedad_dto.tipo
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
                print("Comando actualizar propiedad entregado")
                consumidor.acknowledge(mensaje)


        cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()