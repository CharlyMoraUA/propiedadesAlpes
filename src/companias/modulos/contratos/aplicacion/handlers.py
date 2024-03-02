from companias.modulos.contratos.dominio.eventos import ContratoCreado
from companias.seedwork.aplicacion.handlers import Handler
from companias.modulos.contratos.infraestructura.despachadores import Despachador

class HandlerContratoIntegracion(Handler):

    @staticmethod
    def handle_contrato_creado(evento):
        print("handler evento")
        print(evento)
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contrato')

"""     @staticmethod
    def handle_contrato_firmado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contrato')

    @staticmethod
    def handle_contrato_procesado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-contrato') """


    