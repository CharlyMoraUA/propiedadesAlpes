from propiedades.seedwork.infraestructura.vistas import Vista
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.config.db import db
from .dto import Propiedad as PropiedadDTO

class VistaPropiedad(Vista):
    def obtener_todos(self):
        propiedades_dto = db.session.query(PropiedadDTO).all()
        propiedades = list()

        for propieda_dto in propiedades_dto:
            propiedades.append(Propiedad(id=propieda_dto.id, 
                fecha_creacion=propieda_dto.fecha_creacion, 
                fecha_actualizacion=propieda_dto.fecha_actualizacion,
                fecha_inicio=propieda_dto.fecha_inicio,
                fecha_fin=propieda_dto.fecha_fin,
                id_compania=propieda_dto.id_compania,
                id_inquilino=propieda_dto.id_inquilino,
                id_propiedad=propieda_dto.id_propiedad,
                monto=propieda_dto.monto
                ))
        
        return propiedades

    def obtener_por(self, id=None, **kwargs) -> [Propiedad]:
        params = dict()

        if id:
            params['id'] = str(id)
            
        return db.session.query(PropiedadDTO).filter_by(**params)