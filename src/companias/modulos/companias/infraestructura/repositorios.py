""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de compañias

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de compañias

"""

from companias.config.db import db
from companias.modulos.companias.dominio.repositorios import RepositorioCompanias, RepositorioProveedores, RepositorioEventosCompanias
from companias.modulos.companias.dominio.entidades import Compania
from companias.modulos.companias.dominio.fabricas import FabricaCompanias
from .dto import Compania as CompaniaDTO
from .mapeadores import MapeadorCompania
from uuid import UUID

class RepositorioProveedoresSQLAlchemy(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Compania:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Compania):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioCompaniasSQLAlchemy(RepositorioCompanias):

    def __init__(self):
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())

    def obtener_todos(self) -> list[Compania]:
        # TODO
        raise NotImplementedError

    def agregar(self, compania: Compania):
        compania_dto = self.fabrica_companias.crear_objeto(compania, MapeadorCompania())
        db.session.add(compania_dto)

    def actualizar(self, compania: Compania):
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(compania.id)).one()
        compania_dto.id = compania_dto.id
        compania_dto.fecha_creacion = compania.fecha_creacion
        compania_dto.fecha_actualizacion = compania.fecha_actualizacion
        compania_dto.documento_identidad = compania.documento_identidad
        compania_dto.nombre = compania.nombre
        compania_dto.direccion = compania.direccion
        compania_dto.telefono = compania.telefono
        db.session.commit()

    def eliminar(self, compania_id: UUID):
        db.session.query(CompaniaDTO).filter_by(id=str(compania_id.id)).delete()
        db.session.commit()

    
class RepositorioEventosCompaniaSQLAlchemy(RepositorioEventosCompanias):

    def __init__(self):
        self._fabrica_vuelos: FabricaCompanias = FabricaCompanias()

    @property
    def fabrica_companias(self):
        return self._fabrica_companias

    def obtener_por_id(self, id: UUID) -> Compania:
        compania_dto = db.session.query(CompaniaDTO).filter_by(id=str(id)).one()
        return self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())

    def obtener_todos(self) -> list[Compania]:
        raise NotImplementedError

    def agregar(self, evento):
        compania_evento = self.fabrica_compania.crear_objeto(evento, MapeadorCompania())

        parser_payload = JsonSchema(compania_evento.data.__class__)
        json_str = parser_payload.encode(compania_evento.data)

        evento_dto = EventosCompania()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_compania)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(compania_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(compania_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, compania: Compania):
        raise NotImplementedError

    def eliminar(self, compania_id: UUID):
        raise NotImplementedError