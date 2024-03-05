from companias.seedwork.aplicacion.comandos import Comando
from companias.modulos.companias.aplicacion.dto import CompaniaDTO
from .base import CrearCompaniaBaseHandler
from dataclasses import dataclass, field
from companias.seedwork.aplicacion.comandos import ejecutar_commando as comando

from companias.modulos.companias.dominio.entidades import Compania
from companias.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from companias.modulos.companias.aplicacion.mapeadores import MapeadorCompania
from companias.modulos.companias.infraestructura.repositorios import RepositorioCompanias, RepositorioEventosCompanias

@dataclass
class ActualizarCompania(Comando):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    documento_identidad: str
    nombre: str
    direccion: str
    telefono: int

class ActualizarCompaniaHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: ActualizarCompania):
        print("ActualizarCompaniaHandler")
        print(comando)

        compania_dto = CompaniaDTO(
                id = comando.id
            ,   fecha_creacion = comando.fecha_creacion
            ,   fecha_actualizacion = comando.fecha_actualizacion   
            ,   documento_identidad = comando.documento_identidad
            ,   nombre = comando.nombre
            ,   direccion = comando.direccion
            ,   telefono = comando.telefono
                )

        print("compania_dto")
        print(compania_dto)

        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        print("compania:")
        print(compania)
        compania.crear_compania(compania)
        print("actualizar compania:")
        print(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias)

        print("repositorio:")
        print(repositorio)



        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, compania)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ActualizarCompania)
def ejecutar_comando_actualizar_compania(comando: ActualizarCompania):
    handler = ActualizarCompaniaHandler()
    handler.handle(comando)
    