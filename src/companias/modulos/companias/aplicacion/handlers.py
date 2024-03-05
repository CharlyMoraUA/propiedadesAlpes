from companias.seedwork.aplicacion.handlers import Handler
from companias.modulos.companias.infraestructura.despachadores import Despachador

class HandlerCompaniaIntegracion(Handler):

    @staticmethod
    def handle_compania_creada(evento):
        print("handler evento")
        print(evento)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-compania')

    