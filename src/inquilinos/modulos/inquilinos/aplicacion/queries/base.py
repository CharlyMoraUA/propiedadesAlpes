from inquilinos.seedwork.aplicacion.queries import QueryHandler
from inquilinos.modulos.inquilinos.infraestructura.fabricas import FabricaRepositorio, FabricaVista
from inquilinos.modulos.inquilinos.dominio.fabricas import FabricaInquilinos

class InquilinoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_inquilinos: FabricaInquilinos = FabricaInquilinos()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos  