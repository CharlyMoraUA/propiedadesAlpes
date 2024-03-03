""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de contratos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de contratos

"""

from dataclasses import dataclass, field
from contratos.seedwork.dominio.fabricas import Fabrica
from contratos.seedwork.dominio.repositorios import Repositorio
from contratos.modulos.contratos.dominio.repositorios import RepositorioProveedores, RepositorioContratos, RepositorioEventosContratos
from .repositorios import RepositorioProveedoresSQLAlchemy, RepositorioContratosSQLAlchemy, RepositorioEventosContratoSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioContratos:
            return RepositorioContratosSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosContratos:
            return RepositorioEventosContratoSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')