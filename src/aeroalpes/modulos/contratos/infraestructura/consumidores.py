import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from aeroalpes.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando

from aeroalpes.modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado
from aeroalpes.modulos.contratos.infraestructura.schema.v1.comandos import ComandoContrato
from aeroalpes.seedwork.infraestructura import utils
from datetime import datetime

import requests
import json

def suscribirse_a_eventos():
    cliente = None
    try:
        print('broker host')
        print(utils.broker_host())
        cliente = pulsar.Client(f'pulsar://broker:6650')
        consumidor = cliente.subscribe('eventos-contrato', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='aeroalpes-sub-eventos', schema=AvroSchema(EventoContratoCreado))

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
        cliente = pulsar.Client(f'pulsar://broker:6650')
        consumidor = cliente.subscribe('comando-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-contrato', schema=AvroSchema(ComandoContrato))
        
        
        while True:
            mensaje = consumidor.receive()
            if (mensaje.value().type == "ComandoCrearContrato"):
                print("CREAR")
                
                url = 'http://0.0.0.0:5000/contratos/contrato-comando'
                
                contrato_dto=mensaje.value().data

                payload = {
                    "fecha_inicio": contrato_dto.fecha_inicio,
                    "fecha_fin": contrato_dto.fecha_fin,
                    "monto": contrato_dto.monto,
                    "id_compania": contrato_dto.id_compania,
                    "id_inquilino": contrato_dto.id_inquilino,
                    "id_propiedad": contrato_dto.id_propiedad 
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
                print("Comando crear contrato entregado")
                consumidor.acknowledge(mensaje)

            
            

            if (mensaje.value().type == "ComandoEliminarContrato"):
                print("ELIMINAR")

                url = 'http://localhost:5001/contratos/contrato-query/'+ str(mensaje.value().data.id)

                response = requests.delete(url)
                if response.status_code == 204:
                    print(response)
                else:
                    print(f"Error: {response.status_code}")
                print("Comando eliminar contrato entregado")
                consumidor.acknowledge(mensaje)
                
                
                
                
                
            if (mensaje.value().type == "ComandoActualizarContrato"):
                print("ACTUALIZAR")

                url = 'http://localhost:5001/contratos/contrato-comando/'+ str(mensaje.value().data.id)
                contrato_dto=mensaje.value().data

                payload = {
                    "fecha_inicio": contrato_dto.fecha_inicio,
                    "fecha_fin": contrato_dto.fecha_fin,
                    "monto": contrato_dto.monto,
                    "id_compania": contrato_dto.id_compania,
                    "id_inquilino": contrato_dto.id_inquilino,
                    "id_propiedad": contrato_dto.id_propiedad 
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
                print("Comando actualizar contrato entregado")
                consumidor.acknowledge(mensaje)

        cliente.close()
        
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()