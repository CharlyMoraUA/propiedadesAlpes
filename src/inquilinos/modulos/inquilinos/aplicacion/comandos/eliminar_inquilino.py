from inquilinos.seedwork.aplicacion.comandos import Comando
from inquilinos.modulos.inquilinos.infraestructura.repositorios import RepositorioInquilinos
from dataclasses import dataclass
from .base import CrearInquilinoBaseHandler
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilino
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando as comando
import uuid

@dataclass
class EliminarInquilino(Comando):
    id: str

class EliminarInquilinoHandler(CrearInquilinoBaseHandler):

    def handle(self, comando: EliminarInquilino):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos)
        try:
            repositorio.eliminar(comando.id)
            return True
        except:
            return False

@comando.register(EliminarInquilino)
def ejecutar_comando_eliminar_inquilino(comando: EliminarInquilino):
    handler = EliminarInquilinoHandler()
    return handler.handle(comando)