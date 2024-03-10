import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback
from aeroalpes.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando

from aeroalpes.modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado
from aeroalpes.modulos.contratos.infraestructura.schema.v1.comandos import ComandoCrearContrato, ComandoEliminarContrato, ComandoActualizarContrato
from aeroalpes.seedwork.infraestructura import utils
from datetime import datetime

import requests
import json

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
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
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comando-crear-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-crear-contrato', schema=AvroSchema(ComandoCrearContrato))
        consumidor_eliminar = cliente.subscribe('comando-eliminar-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-eliminar-contrato', schema=AvroSchema(ComandoEliminarContrato))
        consumidor_actualizar = cliente.subscribe('comando-actualizar-contrato', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-actualizar-contrato', schema=AvroSchema(ComandoActualizarContrato))
        print("Si está llegando?")
        mensajeCrear = consumidor.receive()
        mensajeEliminar = consumidor_eliminar.receive()
        #mensajeActualizar = consumidor_actualizar.receive()

        url = 'http://localhost:5001/contratos/contrato-comando'

        if (mensajeCrear and mensajeCrear.value().type == "ComandoCrearContrato"):
            print(f'Comando recibido: {mensajeCrear.value().type}')

            contrato_dto=mensajeCrear.value().data

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
            print("Comando entregado:")
            consumidor.acknowledge(mensajeCrear)
            cliente.close()

        elif (mensajeEliminar and mensajeEliminar.value().type == "ComandoEliminarContrato"):
            print(f'Comando recibido: {mensajeEliminar.value().type}')

            url = 'http://localhost:5001/contratos/contrato-query/'+ str(mensajeEliminar.value().data.id)

            response = requests.delete(url)
            if response.status_code == 204:
                print(response)
            else:
                print(f"Error: {response.status_code}")
            print("Comando eliminar contrato entregado:")
            consumidor.acknowledge(mensajeEliminar)
            cliente.close()
        """ elif (mensajeActualizar and mensajeActualizar.value().type == "ComandoActualizarContrato"):
            print(f'Comando recibido: {mensajeActualizar.value().type}')
            print("Que pasa:")

            url = 'http://localhost:5001/contratos/contrato-comando/'+ str(mensajeActualizar.value().idContrato)
            contrato_dto=mensajeActualizar.value().data

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
            print("Comando entregado:")
            consumidor.acknowledge(mensajeActualizar)
            cliente.close() """

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()