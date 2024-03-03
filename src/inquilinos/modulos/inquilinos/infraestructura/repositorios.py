""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de inquilinos

"""

from inquilinos.config.db import db
from inquilinos.modulos.inquilinos.dominio.repositorios import RepositorioInquilinos, RepositorioProveedores, RepositorioEventosInquilinos
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.modulos.inquilinos.dominio.fabricas import FabricaInquilinos
from .dto import Inquilino as InquilinoDTO
from .mapeadores import MapeadorInquilino
from uuid import UUID

class RepositorioProveedoresSQLAlchemy(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Inquilino:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Inquilino):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Inquilino):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioInquilinosSQLAlchemy(RepositorioInquilinos):

    def __init__(self):
        self._fabrica_inquilinos: FabricaInquilinos = FabricaInquilinos()

    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos

    def obtener_por_id(self, id: UUID) -> Inquilino:
        inquilino_dto = db.session.query(InquilinoDTO).filter_by(id=str(id)).one()
        return self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())

    def obtener_todos(self) -> list[Inquilino]:
        # TODO
        raise NotImplementedError

    def agregar(self, inquilino: Inquilino):
        inquilino_dto = self.fabrica_inquilinos.crear_objeto(inquilino, MapeadorInquilino())
        db.session.add(inquilino_dto)

    def actualizar(self, inquilino: Inquilino):
        inquilino_dto = db.session.query(InquilinoDTO).filter_by(id=str(inquilino.id)).one()
        inquilino_dto.id = inquilino.id
        inquilino_dto.nombre = inquilino.nombre
        inquilino_dto.telefono = inquilino.telefon
        #db.session.query(InquilinoDTO).filter_by(id=str(inquilino_dto.id)).update(inquilino_dto)
        db.session.commit()

    def eliminar(self, inquilino_id: UUID):
        db.session.query(InquilinoDTO).filter_by(id=str(inquilino_id.id)).delete()
        db.session.commit()

    
class RepositorioEventosInquilinoSQLAlchemy(RepositorioEventosInquilinos):

    def __init__(self):
        self._fabrica_vuelos: FabricaInquilinos = FabricaInquilinos()

    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos

    def obtener_por_id(self, id: UUID) -> Inquilino:
        inquilino_dto = db.session.query(InquilinoDTO).filter_by(id=str(id)).one()
        return self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())

    def obtener_todos(self) -> list[Inquilino]:
        raise NotImplementedError

    def agregar(self, evento):
        inquilino_evento = self.fabrica_inquilino.crear_objeto(evento, MapeadorInquilino())

        parser_payload = JsonSchema(inquilino_evento.data.__class__)
        json_str = parser_payload.encode(inquilino_evento.data)

        evento_dto = EventosInquilino()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_inquilino)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(inquilino_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(inquilino_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Inquilino):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError