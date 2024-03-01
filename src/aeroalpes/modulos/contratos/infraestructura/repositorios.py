""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de contratos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de contratos

"""

from aeroalpes.config.db import db
from aeroalpes.modulos.contratos.dominio.repositorios import RepositorioContratos, RepositorioProveedores, RepositorioEventosContratos
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.dominio.fabricas import FabricaContratos
from .dto import Contrato as ContratoDTO
from .mapeadores import MapeadorContrato
from uuid import UUID

class RepositorioProveedoresSQLAlchemy(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Contrato:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Contrato):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioContratosSQLAlchemy(RepositorioContratos):

    def __init__(self):
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        print("contrato_dto_obtener_por_id")
        print(contrato_dto.id_compania)
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, contrato: Contrato):
        print("contrato_db")
        print(contrato)
        contrato_dto = self.fabrica_contratos.crear_objeto(contrato, MapeadorContrato())
        print("contrato-sqlite")
        print(contrato_dto)
        db.session.add(contrato_dto)

    def actualizar(self, contrato: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, contrato_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioEventosContratoSQLAlchemy(RepositorioEventosContratos):

    def __init__(self):
        self._fabrica_vuelos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        raise NotImplementedError

    def agregar(self, evento):
        contrato_evento = self.fabrica_contrato.crear_objeto(evento, MapeadorContrato())

        parser_payload = JsonSchema(contrato_evento.data.__class__)
        json_str = parser_payload.encode(contrato_evento.data)

        evento_dto = EventosContrato()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_contrato)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(contrato_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(contrato_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Contrato):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError