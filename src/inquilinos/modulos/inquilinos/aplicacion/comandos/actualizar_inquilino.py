from inquilinos.seedwork.aplicacion.comandos import Comando
from inquilinos.modulos.inquilinos.aplicacion.dto import InquilinoDTO
from .base import CrearInquilinoBaseHandler
from dataclasses import dataclass, field
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando as comando

from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilino
from inquilinos.modulos.inquilinos.infraestructura.repositorios import RepositorioInquilinos, RepositorioEventosInquilinos

@dataclass
class ActualizarInquilino(Comando):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    fecha_inicio: str
    fecha_fin: str
    id_compania: int
    id_inquilino: int
    id_propiedad: int
    monto: float

class ActualizarInquilinoHandler(CrearInquilinoBaseHandler):
    
    def handle(self, comando: ActualizarInquilino):
        print("ActualizarInquilinoDaniel")
        print(comando)

        inquilino_dto = InquilinoDTO(
                id = comando.id
            ,   fecha_creacion = comando.fecha_creacion
            ,   fecha_actualizacion = comando.fecha_actualizacion   
            ,   fecha_inicio = comando.fecha_inicio
            ,   fecha_fin = comando.fecha_fin
            ,   id_compania = comando.id_compania
            ,   id_inquilino = comando.id_inquilino
            ,   id_propiedad = comando.id_propiedad
            ,   monto = comando.monto
                )

        print("ActualizarInquilinoHandler")
        print(inquilino_dto)

        inquilino: Inquilino = self.fabrica_inquilinos.crear_objeto(inquilino_dto, MapeadorInquilino())
        print("inquilino:")
        print(inquilino)
        inquilino.crear_inquilino(inquilino)
        print("actualizar inquilino:")
        print(inquilino)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioInquilinos)
        #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosInquilinos)

        print("repositorio:")
        print(repositorio)



        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, inquilino)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ActualizarInquilino)
def ejecutar_comando_actualizar_inquilino(comando: ActualizarInquilino):
    handler = ActualizarInquilinoHandler()
    handler.handle(comando)
    