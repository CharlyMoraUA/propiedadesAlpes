from companias.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from companias.seedwork.aplicacion.queries import ejecutar_query as query
from companias.modulos.companias.infraestructura.repositorios import RepositorioCompanias
from dataclasses import dataclass
from .base import CompaniaQueryBaseHandler
from companias.modulos.companias.aplicacion.mapeadores import MapeadorCompania
import uuid

@dataclass
class ObtenerCompania(Query):
    id: str

class ObtenerCompaniaHandler(CompaniaQueryBaseHandler):

    def handle(self, query: ObtenerCompania) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias)
        compania =  self.fabrica_companias.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorCompania())
        return QueryResultado(resultado=compania)

@query.register(ObtenerCompania)
def ejecutar_query_obtener_compania(query: ObtenerCompania):
    handler = ObtenerCompaniaHandler()
    return handler.handle(query)