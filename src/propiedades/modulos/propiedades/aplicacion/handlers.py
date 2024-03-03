from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado
from propiedades.seedwork.aplicacion.handlers import Handler
from propiedades.modulos.propiedades.infraestructura.despachadores import Despachador

class HandlerPropiedadIntegracion(Handler):

    @staticmethod
    def handle_propiedad_creado(evento):
        print("handler evento")
        print(evento)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-propiedad')




    