import pulsar
from pulsar.schema import *

from aeroalpes.modulos.contratos.infraestructura.schema.v1.eventos import EventoContratoCreado, ContratoCreadoPayload
from aeroalpes.modulos.contratos.infraestructura.schema.v1.comandos import ComandoContrato
from aeroalpes.seedwork.infraestructura import utils

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        print('broker host')
        print(utils.broker_host())
        cliente = pulsar.Client(f'pulsar://broker:6650')
        publicador = cliente.create_producer(topico, schema=AvroSchema(EventoContratoCreado))
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del evento
        print("publicador")
        print(evento)
        payload = ContratoCreadoPayload(
            id=str(evento.id_contrato), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoContratoCreado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoContratoCreado))

    def publicar_comando(self, comando, topico):
        # TODO Debe existir un forma de crear el Payload en Avro con base al tipo del comando
        payload = ComandoContrato(
            id_usuario=str(comando.id_usuario)
            # agregar itinerarios
        )
        comando_integracion = ComandoContrato(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoContrato))
