from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from dataclasses import dataclass
from .base import CrearContratoBaseHandler
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando
import uuid

@dataclass
class EliminarContrato(Comando):
    id: str

class EliminarContratoHandler(CrearContratoBaseHandler):

    def handle(self, comando: EliminarContrato):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos)
        try:
            repositorio.eliminar(comando.id)
            return True
        except:
            return False

@comando.register(EliminarContrato)
def ejecutar_comando_eliminar_contrato(comando: EliminarContrato):
    handler = EliminarContratoHandler()
    return handler.handle(comando)