""" Fábricas para la creación de objetos del dominio de contratos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de contratos

"""

from .entidades import Contrato
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioContratosExcepcion
from aeroalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaContrato(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            print("FabricaContrato: ")
            print(obj)
            return mapeador.entidad_a_dto(obj)
        else:
            contrato: Contrato = mapeador.dto_a_entidad(obj)
            
            return contrato

@dataclass
class FabricaContratos(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Contrato.__class__:
            fabrica_contrato = _FabricaContrato()
            return fabrica_contrato.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioContratosExcepcion()

