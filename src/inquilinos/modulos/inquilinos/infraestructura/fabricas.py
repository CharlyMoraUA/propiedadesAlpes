""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de inquilinos

"""

from dataclasses import dataclass, field
from inquilinos.seedwork.dominio.fabricas import Fabrica
from inquilinos.seedwork.dominio.repositorios import Repositorio
from inquilinos.modulos.inquilinos.dominio.repositorios import RepositorioProveedores, RepositorioInquilinos, RepositorioEventosInquilinos
from .repositorios import RepositorioProveedoresSQLAlchemy, RepositorioInquilinosSQLAlchemy, RepositorioEventosInquilinoSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioInquilinos:
            return RepositorioInquilinosSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosInquilinos:
            return RepositorioEventosInquilinoSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')