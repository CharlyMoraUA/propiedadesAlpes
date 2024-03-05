from inquilinos.seedwork.aplicacion.dto import Mapeador as AppMap
from inquilinos.seedwork.dominio.repositorios import Mapeador as RepMap
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.modulos.inquilinos.dominio.objetos_valor import nombre, telefono
from datetime import datetime
from .dto import InquilinoDTO
import uuid

from datetime import datetime

class MapeadorInquilinoDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> InquilinoDTO:
        inquilino_dto = InquilinoDTO(str(uuid.uuid4()),externo.get("nombre"),externo.get("telefono"))
        return inquilino_dto

    def dto_a_externo(self, dto: InquilinoDTO) -> dict:
        return dto.__dict__

class MapeadorInquilino(RepMap):

    def obtener_tipo(self) -> type:
        return Inquilino.__class__

    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:
        _id = str(entidad.id)
        nombre = entidad.nombre
        telefono = entidad.telefono
        
        return InquilinoDTO(_id, nombre, telefono)

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        inquilino = Inquilino()
        inquilino.id = dto.id
        inquilino.nombre = dto.nombre
        inquilino.telefono = dto.telefono
        
        return inquilino