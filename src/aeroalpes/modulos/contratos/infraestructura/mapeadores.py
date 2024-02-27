""" Mapeadores para la capa de infrastructura del dominio de contratos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.modulos.contratos.dominio.objetos_valor import Fecha_inicio, Fecha_fin, Monto
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from .dto import Contrato as ContratoDTO
import uuid

class MapeadorContrato(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        print("entidad_a_dto_infra")
        print(entidad)
        contrato_dto = ContratoDTO()
        contrato_dto.fecha_creacion = entidad.fecha_creacion
        contrato_dto.fecha_actualizacion = entidad.fecha_actualizacion
        contrato_dto.id = entidad.id
        contrato_dto.fecha_inicio = entidad.fecha_inicio 
        contrato_dto.fecha_fin = entidad.fecha_fin
        contrato_dto.id_propiedad = entidad.id_propiedad
        contrato_dto.id_inquilino = entidad.id_inquilino
        contrato_dto.id_compania = entidad.id_compania
        contrato_dto.monto = float(entidad.monto)

        return contrato_dto

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        print("dto_a_entidad_infra")
        print(ContratoDTO)
        contrato = Contrato(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        contrato.fecha_inicio = dto.fecha_inicio
        contrato.fecha_fin = dto.fecha_fin
        contrato.id_propiedad = dto.id_propiedad
        contrato.id_inquilino = dto.id_inquilino
        contrato.id_compania = dto.id_compania
        contrato.monto = dto.monto
        
        return contrato