""" Interfaces para los repositorios del dominio de inquilinos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de inquilinos

"""

from abc import ABC
from inquilinos.seedwork.dominio.repositorios import Repositorio

class RepositorioInquilinos(Repositorio, ABC):
    ...

class RepositorioEventosInquilinos(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...