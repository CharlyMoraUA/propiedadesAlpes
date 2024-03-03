""" Interfaces para los repositorios del dominio de propiedades

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de propiedades

"""

from abc import ABC
from propiedades.seedwork.dominio.repositorios import Repositorio

class RepositorioPropiedads(Repositorio, ABC):
    ...

class RepositorioEventosPropiedads(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...