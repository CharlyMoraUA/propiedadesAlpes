from inquilinos.seedwork.aplicacion.dto import Mapeador as AppMap
from inquilinos.seedwork.dominio.repositorios import Mapeador as RepMap
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.modulos.inquilinos.dominio.objetos_valor import Fecha_inicio, Fecha_fin, Monto
from datetime import datetime
from .dto import InquilinoDTO
import uuid

from datetime import datetime

class MapeadorInquilinoDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> InquilinoDTO:
        fecha_creacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_actualizacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_inicio = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_fin = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        inquilino_dto = InquilinoDTO(str(uuid.uuid4()),fecha_creacion,fecha_actualizacion,fecha_inicio,fecha_fin,externo.get('id_compania'),externo.get('id_inquilino'),externo.get('id_propiedad'),externo.get('monto'))
        print("inquilino_dto3")
        print(inquilino_dto)
        print("EXTERNO")
        print(externo)

        return inquilino_dto

    def dto_a_externo(self, dto: InquilinoDTO) -> dict:
        return dto.__dict__

class MapeadorInquilino(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Inquilino.__class__

    def entidad_a_dto(self, entidad: Inquilino) -> InquilinoDTO:
        print("entidad_a_dto_aplicacion")
        print(entidad)
        _id = str(entidad.id)
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        fecha_inicio = entidad.fecha_inicio.strftime(self._FORMATO_FECHA)
        fecha_fin = entidad.fecha_fin.strftime(self._FORMATO_FECHA)
        print("entidad.id_compania")
        print(entidad.id_compania)
        id_compania = entidad.id_compania
        id_inquilino = entidad.id_inquilino 
        id_propiedad = entidad.id_propiedad
        monto = float(entidad.monto)
        
        return InquilinoDTO(_id, fecha_creacion, fecha_actualizacion, fecha_inicio, fecha_fin, id_compania, id_inquilino, id_propiedad, monto)

    def dto_a_entidad(self, dto: InquilinoDTO) -> Inquilino:
        inquilino = Inquilino()
        print("dto_a_entidad_aplicacion:")
        print(inquilino)
        inquilino.id = dto.id
        inquilino.fecha_inicio = dto.fecha_inicio
        inquilino.fecha_fin = dto.fecha_fin
        inquilino.id_compania = dto.id_compania
        inquilino.id_inquilino = dto.id_inquilino
        inquilino.id_propiedad = dto.id_propiedad
        inquilino.monto = dto.monto
        
        return inquilino