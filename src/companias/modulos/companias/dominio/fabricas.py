""" Fábricas para la creación de objetos del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de companias

"""

from .entidades import Compania
from .excepciones import TipoObjetoNoExisteEnDominioCompaniasExcepcion
from companias.seedwork.dominio.repositorios import Mapeador, Repositorio
from companias.seedwork.dominio.fabricas import Fabrica
from companias.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass

@dataclass
class _FabricaCompania(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            print("FabricaCompania: ")
            print(obj)
            return mapeador.entidad_a_dto(obj)
        else:
            compania: Compania = mapeador.dto_a_entidad(obj)
            
            return compania

@dataclass
class FabricaCompanias(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Compania.__class__:
            fabrica_compania = _FabricaCompania()
            return fabrica_compania.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioCompaniasExcepcion()

