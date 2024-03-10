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
            id = " "
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCrearContrato",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-contrato", "public/default/comando-contrato")
        
        return ContratoRespuesta(mensaje="Procesando Mensaje", codigo=203)
    
    @strawberry.mutation
    async def eliminar_contrato(self, id: str, info: Info) -> ContratoRespuesta:
        payload = dict(
            fecha_inicio = "fecha_inicio",
            fecha_fin = "fecha_fin",
            id_compania = -1,
            id_inquilino = -1,
            id_propiedad = -1,
            monto = 0,
            id = id
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoEliminarContrato",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-contrato", "public/default/comando-contrato")

        return ContratoRespuesta(mensaje="Procesando Mensaje", codigo=203)

    @strawberry.mutation
    async def actualizar_contrato(self, id: str, fecha_inicio: str, fecha_fin: str, id_compania: int, id_inquilino: int, id_propiedad: int, monto: float,  info: Info) -> ContratoRespuesta:
        payload = dict(
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            id_compania = id_compania,
            id_inquilino = id_inquilino,
            id_propiedad = id_propiedad,
            monto = monto,
            id = id
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoActualizarContrato",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-contrato", "public/default/comando-contrato")
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
    
    
    
    @strawberry.mutation
    async def crear_inquilino(self, nombre: str, telefono: int,  info: Info) -> InquilinoRespuesta:
        print(f"nombre: {nombre}, telefono: {telefono}")
        
        payload = dict(
            nombre = nombre,
            telefono = telefono,
        )
        
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoInquilino",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-inquilino", "public/default/comandos-inquilino")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)
    
    
    
    
    
    @strawberry.mutation
    async def crear_compania(self, 
                              direccion: str,
                              documento_identidad: str,
                              fecha_actualizacion: datetime,
                              fecha_creacion: datetime,
                              nombre: str,
                              telefono:int,  
                              info: Info) -> CompaniaRespuesta:
        print(f"direaccion: {direccion}, documento_identidad: {documento_identidad}, fecha_actualizacion: {fecha_actualizacion}, fecha_creacion: {fecha_creacion}, nombre: {nombre}, telefono: {telefono}")
        
        payload = dict(
                direccion=direccion, 
                documento_identidad=documento_identidad, 
                fecha_actualizacion=fecha_actualizacion, 
                fecha_creacion=fecha_creacion, 
                nombre=nombre, 
                telefono=telefono
            )
        
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoCompania",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-compania", "public/default/comandos-compania")
        
        return PropiedadRespuesta(mensaje="Procesando Mensaje", codigo=203)