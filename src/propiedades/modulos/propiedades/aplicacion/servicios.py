from propiedades.seedwork.aplicacion.servicios import Servicio
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.modulos.propiedades.dominio.fabricas import FabricaPropiedads
from propiedades.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedads
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorPropiedad

from .dto import PropiedadDTO

import asyncio

class ServicioPropiedad(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedads = FabricaPropiedads()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades    
    
    def crear_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(Repositoriopropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("PROPIEDAD FABRICA")
        print(propiedad)

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())\

    def actualizar_propiedad(self, propiedad_dto: PropiedadDTO) -> PropiedadDTO:
        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        propiedad.crear_propiedad(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(Repositoriopropiedades.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("PROPIEDAD FABRICA")
        print(propiedad)

        return self.fabrica_propiedades.crear_objeto(propiedad, MapeadorPropiedad())

    def obtener_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(Repositoriopropiedades.__class__)
        return self.fabrica_propiedades.crear_objeto(repositorio.obtener_por_id(id), MapeadorPropiedad())

    def eliminar_propiedad_por_id(self, id) -> PropiedadDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(Repositoriopropiedades.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, propiedad)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()
        return self.fabrica_propiedades.crear_objeto(repositorio.eliminar_por_id(id), MapeadorPropiedad())

