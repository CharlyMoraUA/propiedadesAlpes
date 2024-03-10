from aeroalpes.seedwork.infraestructura.vistas import Vista
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.config.db import db
from .dto import Contrato as ContratoDTO

class VistaContrato(Vista):
    def obtener_todos(self):
        contratos_dto = db.session.query(ContratoDTO).all()
        contratos = list()

        for contrato_dto in contratos_dto:
            contratos.append(Contrato(id=contrato_dto.id, 
                fecha_creacion=contrato_dto.fecha_creacion, 
                fecha_actualizacion=contrato_dto.fecha_actualizacion,
                fecha_inicio=contrato_dto.fecha_inicio,
                fecha_fin=contrato_dto.fecha_fin,
                id_compania=contrato_dto.id_compania,
                id_inquilino=contrato_dto.id_inquilino,
                id_propiedad=contrato_dto.id_propiedad,
                monto=contrato_dto.monto
                ))
        
        return contratos

    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs) -> [Contrato]:
        params = dict()

        if id:
            params['id'] = str(id)
        
        if estado:
            params['estado'] = str(estado)
        
        if id_cliente:
            params['id_cliente'] = str(id_cliente)
            
        return db.session.query(ContratoDTO).filter_by(**params)
