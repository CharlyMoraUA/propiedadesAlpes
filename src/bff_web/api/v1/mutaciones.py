import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    @strawberry.mutation
    async def crear_contrato(self, fecha_inicio: str, fecha_fin: str, id_compania: int, id_inquilino: int, id_propiedad: int, monto: float,  info: Info) -> ContratoRespuesta:
        print(f"fecha_inicio: {fecha_inicio}, fecha_fin: {fecha_fin}, id_compania: {id_compania}, id_inquilino: {id_inquilino}, id_propiedad: {id_propiedad}, monto: {monto}")
        payload = dict(
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            id_compania = id_compania,
            id_inquilino = id_inquilino,
            id_propiedad = id_propiedad,
            monto = monto,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoContrato",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-contrato", "public/default/comandos-contrato")
        
        return ContratoRespuesta(mensaje="Procesando Mensaje", codigo=203)
    
    
    
    @strawberry.mutation
    async def crear_propiedad(self, area: float, direccion: str, matricula: str, tipo: str,  info: Info) -> PropiedadRespuesta:
        print(f"area: {area}, direccion: {direccion},  matricula: {matricula}, tipo: {tipo}")
        
        payload = dict(
            area = area,
            direccion = direccion,
            matricula = matricula,
            tipo = tipo
        )
        
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoPropiedad",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-propiedad", "public/default/comandos-propiedad")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)