from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from dataclasses import dataclass
from .base import ContratoQueryBaseHandler
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
import uuid

@dataclass
class EliminarContrato(Query):
    id: str

class EliminarContratoHandler(ContratoQueryBaseHandler):

    def handle(self, query: EliminarContrato) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos)
        print("repositorio")
        print(repositorio)
        try:
            contrato =  self.fabrica_contratos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorContrato())
            repositorio.eliminar(query.id)
            return True
        except:
            return False

@query.register(EliminarContrato)
def ejecutar_query_eliminar_contrato(query: EliminarContrato):
    handler = EliminarContratoHandler()
    return handler.handle(query)