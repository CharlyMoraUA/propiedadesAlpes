from contratos.seedwork.aplicacion.comandos import Comando
from contratos.modulos.contratos.aplicacion.dto import ContratoDTO
from .base import CrearContratoBaseHandler
from dataclasses import dataclass, field
from contratos.seedwork.aplicacion.comandos import ejecutar_commando as comando

from contratos.modulos.contratos.dominio.entidades import Contrato
from contratos.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from contratos.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from contratos.modulos.contratos.infraestructura.repositorios import RepositorioContratos, RepositorioEventosContratos

@dataclass
class ActualizarContrato(Comando):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    fecha_inicio: str
    fecha_fin: str
    id_compania: int
    id_inquilino: int
    id_propiedad: int
    monto: float

class ActualizarContratoHandler(CrearContratoBaseHandler):
    
    def handle(self, comando: ActualizarContrato):
        print("ActualizarContratoDaniel")
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

        print("ActualizarContratoHandler")
        print(contrato_dto)

        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        print("contrato:")
        print(contrato)
        contrato.crear_contrato(contrato)
        print("actualizar contrato:")
        print(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos)
        #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosContratos)

        print("repositorio:")
        print(repositorio)



        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, contrato)
        #UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ActualizarContrato)
def ejecutar_comando_actualizar_contrato(comando: ActualizarContrato):
    handler = ActualizarContratoHandler()
    handler.handle(comando)
    