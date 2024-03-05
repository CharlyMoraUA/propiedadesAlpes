import pulsar
from pulsar.schema import *

from procesador.modulos.procesador.infraestructura.schema.v1.eventos import EventoProcesadorCreado, ProcesadorCreadoPayload
from procesador.modulos.procesador.infraestructura.schema.v1.comandos import ComandoCrearProcesador, ComandoCrearProcesadorPayload
from procesador.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoProcesadorCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        print("publicador")
        print(evento)
        payload = ProcesadorCreadoPayload(
            id=str(evento.id_procesador)
        )
        evento_integracion = EventoProcesadorCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoProcesadorCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoCrearProcesadorPayload(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoCrearProcesador(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoCrearProcesador))
