from propiedades.seedwork.aplicacion.queries import QueryHandler
from propiedades.modulos.propiedades.infraestructura.fabricas import FabricaRepositorio
from propiedades.modulos.propiedades.dominio.fabricas import FabricaPropiedads

class PropiedadQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_propiedades: FabricaPropiedads = FabricaPropiedads()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades  