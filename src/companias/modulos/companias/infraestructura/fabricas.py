""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de companias

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de companias

"""

from dataclasses import dataclass, field
from companias.seedwork.dominio.fabricas import Fabrica
from companias.seedwork.dominio.repositorios import Repositorio
from companias.modulos.companias.dominio.repositorios import RepositorioProveedores, RepositorioCompanias, RepositorioEventosCompanias
from .repositorios import RepositorioProveedoresSQLAlchemy, RepositorioCompaniasSQLAlchemy, RepositorioEventosCompaniaSQLAlchemy
from .excepciones import ExcepcionFabrica
from companias.seedwork.infraestructura.vistas import Vista
from companias.modulos.companias.infraestructura.vistas import VistaCompania
from companias.modulos.companias.dominio.entidades import Compania

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioCompanias:
            return RepositorioCompaniasSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosCompanias:
            return RepositorioEventosCompaniaSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
        
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Compania:
            return VistaCompania()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')