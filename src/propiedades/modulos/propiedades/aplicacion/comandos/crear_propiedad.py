from propiedades.seedwork.aplicacion.comandos import Comando
from propiedades.modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import CrearPropiedadBaseHandler
from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedad
from propiedades.modulos.propiedades.infraestructura.repositorios import RepositorioPropiedads, RepositorioEventosPropiedads

@dataclass
class CrearPropiedad(Comando):
    id: str
    matricula: str
    direccion: str
    area: float
    tipo: str

class CrearPropiedadHandler(CrearPropiedadBaseHandler):
    
    def handle(self, comando: CrearPropiedad):
        print("CrearPropiedadDaniel")
        print(comando)

        propiedad_dto = PropiedadDTO(
                id = comando.id
            ,   matricula = comando.matricula
            ,   direccion = comando.direccion   
            ,   area = comando.area
            ,   tipo = comando.tipo
                )

        print("CrearPropiedadHandler")
        print(propiedad_dto)

        propiedad: Propiedad = self.fabrica_propiedades.crear_objeto(propiedad_dto, MapeadorPropiedad())
        print("propiedad:")
        print(propiedad)
        propiedad.crear_propiedad(propiedad)
        print("crear propiedad:")
        print(propiedad)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPropiedads)
        #repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosPropiedads)

        print("repositorio:")
        print(repositorio)



        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, propiedad)
        # UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearPropiedad)
def ejecutar_comando_crear_propiedad(comando: CrearPropiedad):
    handler = CrearPropiedadHandler()
    handler.handle(comando)
    