from inquilinos.seedwork.infraestructura.vistas import Vista
from inquilinos.modulos.inquilinos.dominio.entidades import Inquilino
from inquilinos.config.db import db
from .dto import Inquilino as InquilinoDTO

class VistaInquilino(Vista):
    def obtener_todos(self):
        inquilinos_dto = db.session.query(InquilinoDTO).all()
        inquilinos = list()

        for inquilino_dto in inquilinos_dto:
            inquilinos.append(Inquilino(id=inquilino_dto.id, 
                nombre=inquilino_dto.nombre, 
                telefono=inquilino_dto.telefono,
                ))
        
        return inquilinos

    def obtener_por(self, id=None, estado=None, id_cliente=None, **kwargs) -> [Inquilino]:
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(InquilinoDTO).filter_by(**params)