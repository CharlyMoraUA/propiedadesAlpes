from dataclasses import dataclass
from inquilinos.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from inquilinos.seedwork.aplicacion.queries import ejecutar_query as query
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.modulos.inquilinos.aplicacion.dto import InquilinoDTO
from .base import InquilinoQueryBaseHandler

class ObtenerTodosInquilinos(Query):
        ...
class ObtenerTodosInquilinosHandler(InquilinoQueryBaseHandler):
    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        inquilinos_dto = []
        vista = self.fabrica_vista.crear_objeto(Inquilino)
        inquilinos = vista.obtener_todos()

        for inquilino in inquilinos:
            dto = InquilinoDTO(
                id = inquilino.id,
                nombre=inquilino.nombre,
                telefono=inquilino.telefono
            )
            inquilinos_dto.append(dto)
        
        return QueryResultado(resultado=inquilinos_dto)

@query.register(ObtenerTodosInquilinos)
def ejecutar_query_obtener_inquilino(query: ObtenerTodosInquilinos):
    handler = ObtenerTodosInquilinosHandler()
    return handler.handle(query)