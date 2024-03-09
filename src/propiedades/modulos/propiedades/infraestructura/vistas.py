from propiedades.seedwork.infraestructura.vistas import Vista
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.config.db import db
from .dto import Propiedad as PropiedadDTO

class VistaPropiedad(Vista):
    def obtener_todos(self):
        propiedades_dto = db.session.query(PropiedadDTO).all()
        propiedades = list()

        for propiedad_dto in propiedades_dto:
            propiedades.append(Propiedad(
                id=propiedad_dto.id, 
                matricula=propiedad_dto.matricula,
                direccion=propiedad_dto.direccion,
                area=propiedad_dto.area,
                tipo=propiedad_dto.tipo
                ))
        
        return propiedades

    def obtener_por(self, id=None, **kwargs) -> [Propiedad]:
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(PropiedadDTO).filter_by(**params)