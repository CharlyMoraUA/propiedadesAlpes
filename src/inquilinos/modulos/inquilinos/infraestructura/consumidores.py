import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoInquilino
from inquilinos.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-inquilino', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='inquilinos-sub-eventos', schema=AvroSchema(EventoInquilinoCreado))

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
        consumidor = cliente.subscribe('comando-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='aeroalpes-sub-comando-inquilino', schema=AvroSchema(ComandoInquilino))
        mensaje = consumidor.receive()
        
        print("TIPO COMANDO: ")
        print(str(mensaje.value().type))
        
        print("TIPO COMANDO 2: ")
        print(mensaje.value().type)
        
        print("TIPO COMANDO 3: ")
        print(mensaje.value())

       
        if (mensaje.value().type == "ComandoCrearInquilino"):
            print("CREAR")
            
            url = 'http://localhost:5003/inquilinos/inquilino-comando'
            
            inquilino_dto=mensaje.value().data

            payload = {
                "nombre":inquilino_dto.nombre, 
                "telefono":inquilino_dto.telefono,
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
            print("Comando crear inquilino entregado")
            consumidor.acknowledge(mensaje)
            cliente.close()

            
            

        if (mensaje.value().type == "ComandoEliminarInquilino"):
            print("ELIMINAR")

            url = 'http://localhost:5003/inquilinos/inquilino-query/'+ str(mensaje.value().data.id)

            response = requests.delete(url)
            if response.status_code == 204:
                print(response)
            else:
                print(f"Error: {response.status_code}")
            print("Comando eliminar inquilino entregado")
            consumidor.acknowledge(mensaje)
            cliente.close()
            
            
            
            
            
        if (mensaje.value().type == "ComandoActualizarInquilino"):
            print("ACTUALIZAR")

            url = 'http://localhost:5003/inquilinos/inquilino-comando/'+ str(mensaje.value().data.id)
            inquilino_dto=mensaje.value().data

            payload = {
                "nombre":inquilino_dto.nombre, 
                "telefono":inquilino_dto.telefono,
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
            print("Comando actualizar inquilino entregado")
            consumidor.acknowledge(mensaje)
            cliente.close()

    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()