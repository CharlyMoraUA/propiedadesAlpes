from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedads
from dataclasses import dataclass
from .base import CrearPropiedadBaseHandler
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando as comando
import uuid

@dataclass
class EliminarPropiedad(Comando):
    id: str

class EliminarPropiedadHandler(CrearPropiedadBaseHandler):

    def handle(self, comando: EliminarPropiedad):
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedads)
        try:
            repositorio.eliminar(comando.id)
            return True
        except:
            return False

@comando.register(EliminarPropiedad)
def ejecutar_comando_eliminar_propiedad(comando: EliminarPropiedad):
    handler = EliminarPropiedadHandler()
    return handler.handle(comando)