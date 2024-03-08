from aeroalpes.seedwork.aplicacion.queries import QueryHandler
from aeroalpes.modulos.contratos.infraestructura.fabricas import FabricaRepositorio, FabricaVista
from aeroalpes.modulos.contratos.dominio.fabricas import FabricaContratos

class ContratoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()
        self._fabrica_vista: FabricaVista = FabricaVista()

    @property
    def fabrica_vista(self):
        return self._fabrica_vista

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos  