from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from dataclasses import dataclass
from .base import ContratoQueryBaseHandler
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
import uuid

@dataclass
class ObtenerContrato(Query):
    id: str

class ObtenerContratoHandler(ContratoQueryBaseHandler):

    def handle(self, query: ObtenerContrato) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        print("repositorio")
        print(repositorio)
        contrato =  self.fabrica_contratos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorContrato())
        print("handle_contrato")
        print(contrato)
        return QueryResultado(resultado=contrato)

@query.register(ObtenerContrato)
def ejecutar_query_obtener_contrato(query: ObtenerContrato):
    handler = ObtenerContratoHandler()
    return handler.handle(query)