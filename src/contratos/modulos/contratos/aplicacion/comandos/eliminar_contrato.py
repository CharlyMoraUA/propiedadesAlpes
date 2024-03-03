from contratos.seedwork.aplicacion.comandos import Comando
from contratos.modulos.contratos.infraestructura.repositorios import RepositorioContratos
from dataclasses import dataclass
from .base import CrearContratoBaseHandler
from contratos.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from contratos.seedwork.aplicacion.comandos import ejecutar_commando as comando
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