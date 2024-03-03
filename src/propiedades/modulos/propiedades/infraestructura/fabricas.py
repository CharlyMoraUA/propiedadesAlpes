""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de propiedades

"""

from dataclasses import dataclass, field
from propiedades.seedwork.dominio.fabricas import Fabrica
from propiedades.seedwork.dominio.repositorios import Repositorio
from propiedades.modulos.propiedades.dominio.repositorios import RepositorioProveedores, RepositorioPropiedads, RepositorioEventosPropiedads
from .repositorios import RepositorioProveedoresSQLAlchemy, RepositorioPropiedadsSQLAlchemy, RepositorioEventosPropiedadSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioPropiedads:
            return RepositorioPropiedadsSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosPropiedads:
            return RepositorioEventosPropiedadSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')