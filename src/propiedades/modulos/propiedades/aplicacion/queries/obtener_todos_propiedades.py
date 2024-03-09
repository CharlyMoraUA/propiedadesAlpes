from dataclasses import dataclass
from propiedades.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from propiedades.seedwork.aplicacion.queries import ejecutar_query as query
from propiedades.modulos.propiedades.dominio.entidades import Propiedad
from propiedades.modulos.propiedades.aplicacion.dto import PropiedadDTO
from .base import PropiedadQueryBaseHandler



class ObtenerTodosPropiedades(Query):
    ...
    
    
class ObtenerTodosPropiedadesHandler(PropiedadQueryBaseHandler):
    FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def handle(self, query) -> QueryResultado:
        propiedades_dto = []
        vista = self.fabrica_vista.crear_objeto(Propiedad)
        propiedades = vista.obtener_todos()

        for propiedad in propiedades:
            dto = PropiedadDTO(
                id = propiedad.id,
                matricula=propiedad.matricula,
                direccion=propiedad.direccion,
                area=propiedad.area,
                tipo=propiedad.tipo
            )
            propiedades_dto.append(dto)
        
        return QueryResultado(resultado=propiedades_dto)

@query.register(ObtenerTodosPropiedades)
def ejecutar_query_obtener_propiedad(query: ObtenerTodosPropiedades):
    handler = ObtenerTodosPropiedadesHandler()
    return handler.handle(query)