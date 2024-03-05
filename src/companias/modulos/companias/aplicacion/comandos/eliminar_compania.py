from companias.seedwork.aplicacion.comandos import Comando
from companias.modulos.companias.infraestructura.repositorios import RepositorioCompanias
from dataclasses import dataclass
from .base import CrearCompaniaBaseHandler
from companias.seedwork.aplicacion.comandos import ejecutar_commando as comando
import uuid

@dataclass
class EliminarCompania(Comando):
    id: str

class EliminarCompaniaHandler(CrearCompaniaBaseHandler):

    def handle(self, comando: EliminarCompania):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias)
        try:
            repositorio.eliminar(comando.id)
            return True
        except:
            return False

@comando.register(EliminarCompania)
def ejecutar_comando_eliminar_compania(comando: EliminarCompania):
    handler = EliminarCompaniaHandler()
    return handler.handle(comando)