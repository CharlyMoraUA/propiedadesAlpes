from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.contratos.aplicacion.dto import ContratoDTO
from .base import CrearContratoBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from aeroalpes.modulos.contratos.infraestructura.repositorios import RepositorioContratos

@dataclass
class CrearContrato(Comando):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    fecha_inicio: str
    fecha_fin: str
    id_compania: int
    id_inquilino: int
    id_propiedad: int
    monto: float

class CrearContratoHandler(CrearContratoBaseHandler):
    
    def handle(self, comando: CrearContrato):
        print("CrearContratoDaniel")
        print(comando)

        contrato_dto = ContratoDTO(
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

        print("CrearContratoHandler")
        print(contrato_dto)

        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        print("contrato:")
        print(contrato)
        contrato.crear_contrato(contrato)
        print("crear contrato:")
        print(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        print("repositorio:")
        print(repositorio)



        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, contrato)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
    