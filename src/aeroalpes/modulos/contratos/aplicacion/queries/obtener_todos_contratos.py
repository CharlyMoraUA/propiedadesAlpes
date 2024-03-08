from dataclasses import dataclass
from aeroalpes.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query as query
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.aplicacion.dto import ContratoDTO
from .base import ContratoQueryBaseHandler

@dataclass
class ObtenerTodosContratos(Query):
    ...

class ObtenerTodosContratosHandler(ContratoQueryBaseHandler):

    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        contratos_dto = []
        vista = self.fabrica_vista.crear_objeto(Contrato)
        contratos = vista.obtener_todos()

        for contrato in contratos:
            dto = ContratoDTO(
                id = contrato.id,
                fecha_creacion=contrato.fecha_creacion.strftime(self.FORMATO_FECHA),
                fecha_actualizacion=contrato.fecha_actualizacion.strftime(self.FORMATO_FECHA),
                fecha_inicio=contrato.fecha_inicio.strftime(self.FORMATO_FECHA),
                fecha_fin=contrato.fecha_fin.strftime(self.FORMATO_FECHA),
                id_compania=contrato.id_compania,
                id_inquilino=contrato.id_inquilino,
                id_propiedad=contrato.id_propiedad,
                monto=contrato.monto
            )
            contratos_dto.append(dto)
        
        return QueryResultado(resultado=contratos_dto)

@query.register(ObtenerTodosContratos)
def ejecutar_query_obtener_contrato(query: ObtenerTodosContratos):
    handler = ObtenerTodosContratosHandler()
    return handler.handle(query)