import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from inquilinos.modulos.inquilinos.infraestructura.schema.v1.eventos import EventoInquilinoCreado
from inquilinos.modulos.inquilinos.infraestructura.schema.v1.comandos import ComandoCrearInquilino
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
        consumidor = cliente.subscribe('comandos-inquilino', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='inquilinos-sub-comandos-inquilino', schema=AvroSchema(ComandoCrearInquilino))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()