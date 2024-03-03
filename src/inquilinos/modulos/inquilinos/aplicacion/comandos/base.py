from inquilinos.seedwork.aplicacion.comandos import ComandoHandler
from inquilinos.modulos.inquilinos.infraestructura.fabricas import FabricaRepositorio
from inquilinos.modulos.inquilinos.dominio.fabricas import FabricaInquilinos

class CrearInquilinoBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_inquilinos: FabricaInquilinos = FabricaInquilinos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_inquilinos(self):
        return self._fabrica_inquilinos  
    