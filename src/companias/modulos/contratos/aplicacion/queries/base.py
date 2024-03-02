from companias.seedwork.aplicacion.queries import QueryHandler
from companias.modulos.contratos.infraestructura.fabricas import FabricaRepositorio
from companias.modulos.contratos.dominio.fabricas import FabricaContratos

class ContratoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos  