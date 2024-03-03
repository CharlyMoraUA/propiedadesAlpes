""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de propiedades

"""

from propiedades.config.db import db
from propiedades.modulos.propiedades.dominio.repositorios import RepositorioPropiedads, RepositorioProveedores, RepositorioEventosPropiedads
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.modulos.propiedades.dominio.fabricas import FabricaPropiedads
from .dto import Propiedad as PropiedadDTO
from .mapeadores import MapeadorPropiedad
from uuid import UUID

class RepositorioProveedoresSQLAlchemy(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Propiedad:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Propiedad):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioPropiedadsSQLAlchemy(RepositorioPropiedads):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedads = FabricaPropiedads()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        # TODO
        raise NotImplementedError

    def agregar(self, propiedad: Propiedad):
        propiedad_dto = self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())
        db.session.add(propiedad_dto)

    def actualizar(self, propiedad: Propiedad):
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(propiedad.id)).one()
        propiedad_dto.id = propiedad.id
        propiedad_dto.matricula = propiedad.matricula
        propiedad_dto.direccion = propiedad.direccion
        propiedad_dto.area = propiedad.area
        propiedad_dto.tipo = propiedad.tipo #ATENCION
        db.session.commit()

    def eliminar(self, propiedad_id: UUID):
        db.session.query(PropiedadDTO).filter_by(id=str(propiedad_id.id)).delete()
        db.session.commit()

    
class RepositorioEventosPropiedadSQLAlchemy(RepositorioEventosPropiedads):

    def __init__(self):
        self._fabrica_vuelos: FabricaPropiedads = FabricaPropiedads()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Propiedad:
        propiedad_dto = db.session.query(PropiedadDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())

    def obtener_todos(self) -> list[Propiedad]:
        raise NotImplementedError

    def agregar(self, evento):
        propiedad_evento = self.fabrica_propiedad.crear_objeto(evento, MapeadorPropiedad())

        parser_payload = JsonSchema(propiedad_evento.data.__class__)
        json_str = parser_payload.encode(propiedad_evento.data)

        evento_dto = EventosPropiedad()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_propiedad)
        evento_dto.fecha_evento = evento.fecha_evento
        evento_dto.version = str(propiedad_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(propiedad_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Propiedad):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError