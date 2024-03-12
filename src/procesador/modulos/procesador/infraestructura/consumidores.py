import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from procesador.modulos.procesador.infraestructura.schema.v1.eventos import EventoProcesadorCreado
from procesador.modulos.procesador.infraestructura.schema.v1.comandos import ComandoCrearProcesador
from procesador.seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        print('broker host')
        print(utils.broker_host())
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')

        # topics = ['eventos-propiedad', 'eventos-compania', 'eventos-inquilino', 'eventos-contrato']
        topics = ['persistent://public/default/eventos-propiedad', 
        'persistent://public/default/eventos-compania',
        'persistent://public/default/eventos-inquilino',
        'persistent://public/default/eventos-contrato'
        ]
        consumidor = cliente.subscribe(topics, consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sub-eventos-procesador', schema=AvroSchema(EventoProcesadorCreado))

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
        consumidor = cliente.subscribe('comandos-propiedad', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='propiedades-sub-comandos-procesador', schema=AvroSchema(ComandoCrearProcesador))

        while True:
            mensaje = consumidor.receive()
            print(f'====================================================================')
            print(f'====================================================================')
            print(f'====================================================================')
            print(f'Comando recibido: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()