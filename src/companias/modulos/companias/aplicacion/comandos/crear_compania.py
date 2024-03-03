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
class CrearCompania(Comando):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    documento_identidad: str
    nombre: str
    direccion: str
    telefono: int

class CrearCompaniaHandler(CrearCompaniaBaseHandler):
    
    def handle(self, comando: CrearCompania):
        print("CrearCompaniaHandler")
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

        print("CrearConmpaniaHandler")
        print(compania_dto)

        compania: Compania = self.fabrica_companias.crear_objeto(compania_dto, MapeadorCompania())
        compania.crear_compania(compania)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioCompanias)
        #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosContratos)

        print("repositorio:")
        print(repositorio)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, compania)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCompania)
def ejecutar_comando_crear_compania(comando: CrearCompania):
    handler = CrearCompaniaHandler()
    handler.handle(comando)
    