from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.dominio.objetos_valor import Fecha_inicio, Fecha_fin, Monto
from datetime import datetime
from .dto import ContratoDTO
import uuid

from datetime import datetime

class MapeadorContratoDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        fecha_creacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_actualizacion = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_inicio = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        fecha_fin = datetime.strptime("2025-02-25T05:12:58Z", '%Y-%m-%dT%H:%M:%SZ')
        contrato_dto = ContratoDTO(str(uuid.uuid4()),fecha_creacion,fecha_actualizacion,fecha_inicio,fecha_fin,externo.get('id_compania'),externo.get('id_inquilino'),externo.get('id_propiedad'),externo.get('monto'))
        print("contrato_dto3")
        print(contrato_dto)
        print("EXTERNO")
        print(externo)

        return contrato_dto

    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__

class MapeadorContrato(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
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
        
        return ContratoDTO(_id, fecha_creacion, fecha_actualizacion, fecha_inicio, fecha_fin, id_compania, id_inquilino, id_propiedad, monto)

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato()
        print("dto_a_entidad_aplicacion:")
        print(contrato)
        contrato.id = dto.id
        contrato.fecha_inicio = dto.fecha_inicio
        contrato.fecha_fin = dto.fecha_fin
        contrato.id_compania = dto.id_compania
        contrato.id_inquilino = dto.id_inquilino
        contrato.id_propiedad = dto.id_propiedad
        contrato.monto = dto.monto
        
        return contrato