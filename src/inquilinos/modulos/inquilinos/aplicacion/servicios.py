from inquilinos.seedwork.aplicacion.servicios import Servicio
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.modulos.inquilinos.dominio.fabricas import FabricaInquilinos
from inquilinos.modulos.inquilinos.infraestructura.fabricas import FabricaRepositorio
from inquilinos.modulos.inquilinos.infraestructura.repositorios import RepositorioInquilinos
from inquilinos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorInquilino

from .dto import InquilinoDTO

import asyncio

class ServicioInquilino(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_inquilinos: FabricaInquilinos = FabricaInquilinos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos    
    
    def crear_inquilino(self, inquilino_dto: InquilinoDTO) -> InquilinoDTO:
        inquilino: Inquilino = self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())
        inquilino.crear_inquilino(inquilino)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("CONTRATO FABRICA")
        print(inquilino)

        return self.fabrica_inquilinos.crear_objeto(inquilino, MapeadorInquilino())\

    def actualizar_inquilino(self, inquilino_dto: InquilinoDTO) -> InquilinoDTO:
        inquilino: Inquilino = self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())
        inquilino.crear_inquilino(inquilino)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("CONTRATO FABRICA")
        print(inquilino)

        return self.fabrica_inquilinos.crear_objeto(inquilino, MapeadorInquilino())

    def obtener_inquilino_por_id(self, id) -> InquilinoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)
        return self.fabrica_inquilinos.crear_objeto(repositorio.obtener_por_id(id), MapeadorInquilino())

    def eliminar_inquilino_por_id(self, id) -> InquilinoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, inquilino)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()
        return self.fabrica_inquilinos.crear_objeto(repositorio.eliminar_por_id(id), MapeadorInquilino())

