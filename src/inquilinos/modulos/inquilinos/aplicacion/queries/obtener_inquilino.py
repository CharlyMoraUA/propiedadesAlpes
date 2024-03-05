from inquilinos.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from inquilinos.seedwork.aplicacion.queries import ejecutar_query as query
from inquilinos.modulos.inquilinos.infraestructura.repositorios import RepositorioInquilinos
from dataclasses import dataclass
from .base import InquilinoQueryBaseHandler
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilino
import uuid

@dataclass
class ObtenerInquilino(Query):
    id: str

class ObtenerInquilinoHandler(InquilinoQueryBaseHandler):

    def handle(self, query: ObtenerInquilino) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos)
        inquilino =  self.fabrica_inquilinos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorInquilino())
        return QueryResultado(resultado=inquilino)

@query.register(ObtenerInquilino)
def ejecutar_query_obtener_inquilino(query: ObtenerInquilino):
    handler = ObtenerInquilinoHandler()
    return handler.handle(query)