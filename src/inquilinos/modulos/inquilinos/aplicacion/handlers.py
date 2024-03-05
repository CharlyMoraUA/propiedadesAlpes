from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado
from inquilinos.seedwork.aplicacion.handlers import Handler
from inquilinos.modulos.inquilinos.infraestructura.despachadores import Despachador

class HandlerInquilinoIntegracion(Handler):

    @staticmethod
    def handle_inquilino_creado(evento):
        print("handler evento")
        print(evento)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inquilino')

"""     @staticmethod
    def handle_inquilino_firmado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inquilino')

    @staticmethod
    def handle_inquilino_procesado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-inquilino') """


    