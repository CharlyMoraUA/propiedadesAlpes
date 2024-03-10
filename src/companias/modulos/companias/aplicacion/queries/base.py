from companias.seedwork.aplicacion.queries import QueryHandler
from companias.modulos.companias.infraestructura.fabricas import FabricaRepositorio, FabricaVista
from companias.modulos.companias.dominio.fabricas import FabricaCompanias

class CompaniaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_companias: FabricaCompanias = FabricaCompanias()
        self._fabrica_vista: FabricaVista = FabricaVista()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_companias(self):
        return self._fabrica_companias 