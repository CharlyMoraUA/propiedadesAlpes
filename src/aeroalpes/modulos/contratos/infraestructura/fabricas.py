""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de contratos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de contratos

"""

from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.fabricas import Fabrica
from aeroalpes.seedwork.dominio.repositorios import Repositorio
from aeroalpes.seedwork.infraestructura.vistas import Vista
from aeroalpes.modulos.contratos.infraestructura.vistas import VistaContrato
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.dominio.repositorios import RepositorioProveedores, RepositorioContratos, RepositorioEventosContratos
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
        
@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Contrato:
            return VistaContrato()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')