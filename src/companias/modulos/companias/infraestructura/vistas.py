from companias.seedwork.infraestructura.vistas import Vista
from companias.modulos.companias.dominio.entidades import Compania
from companias.config.db import db
from .dto import Compania as CompaniaDTO

class VistaCompania(Vista):
    def obtener_todos(self):
        companias_dto = db.session.query(CompaniaDTO).all()
        companias = list()

        for compania_dto in companias_dto:
            companias.append(Compania(id=compania_dto.id, 
                estado=compania_dto.estado, 
                documento_identidad=compania_dto.documento_identidad,
                nombre=compania_dto.nombre,
                direccion=compania_dto.direccion,
                telefono=compania_dto.telefono,
                ))
        
        return companias

    def obtener_por(self, id=None, **kwargs) -> [Compania]:
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(CompaniaDTO).filter_by(**params)