""" Interfaces para los repositorios del dominio de contratos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de contratos

"""

from abc import ABC
from inquilinos.seedwork.dominio.repositorios import Repositorio

class RepositorioContratos(Repositorio, ABC):
    ...

class RepositorioEventosContratos(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...