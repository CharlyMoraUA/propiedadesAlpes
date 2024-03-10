from dataclasses import dataclass
from companias.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from companias.seedwork.aplicacion.queries import ejecutar_query as query
from companias.modulos.companias.dominio.entidades import Compania
from companias.modulos.companias.aplicacion.dto import CompaniaDTO
from .base import CompaniaQueryBaseHandler

class ObtenerTodosCompanias(Query):
    ...
class ObtenerTodosCompaniasHandler(CompaniaQueryBaseHandler):
    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        companias_dto = []
        vista = self.fabrica_vista.crear_objeto(Compania)
        companias = vista.obtener_todos()

        for compania in companias:
            dto = CompaniaDTO(
                id = compania.id,
                fecha_creacion=compania.fecha_creacion.strftime(self.FORMATO_FECHA),
                fecha_actualizacion=compania.fecha_actualizacion.strftime(self.FORMATO_FECHA),
                documento_identidad=compania.documento_identidad,
                nombre=compania.nombre,
                direccion=compania.direccion,
                telefono=compania.telefono
            )
            companias_dto.append(dto)
        
        return QueryResultado(resultado=companias_dto)

@query.register(ObtenerTodosCompanias)
def ejecutar_query_obtener_compania(query: ObtenerTodosCompanias):
    handler = ObtenerTodosCompaniasHandler()
    return handler.handle(query)