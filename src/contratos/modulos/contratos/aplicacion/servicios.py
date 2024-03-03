from contratos.seedwork.aplicacion.servicios import Servicio
from contratos.modulos.contratos.dominio.entidades import Contrato
from contratos.modulos.contratos.dominio.fabricas import FabricaContratos
from contratos.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from contratos.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from contratos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from .mapeadores import MapeadorContrato

from .dto import ContratoDTO

import asyncio

class ServicioContrato(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos    
    
    def crear_contrato(self, contrato_dto: ContratoDTO) -> ContratoDTO:
        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        contrato.crear_contrato(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, contrato)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("CONTRATO FABRICA")
        print(contrato)

        return self.fabrica_contratos.crear_objeto(contrato, MapeadorContrato())\

    def actualizar_contrato(self, contrato_dto: ContratoDTO) -> ContratoDTO:
        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        contrato.crear_contrato(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, contrato)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        print("CONTRATO FABRICA")
        print(contrato)

        return self.fabrica_contratos.crear_objeto(contrato, MapeadorContrato())

    def obtener_contrato_por_id(self, id) -> ContratoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        return self.fabrica_contratos.crear_objeto(repositorio.obtener_por_id(id), MapeadorContrato())

    def eliminar_contrato_por_id(self, id) -> ContratoDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)
        UnidadTrabajoPuerto.registrar_batch(repositorio.eliminar, contrato)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()
        return self.fabrica_contratos.crear_objeto(repositorio.eliminar_por_id(id), MapeadorContrato())

