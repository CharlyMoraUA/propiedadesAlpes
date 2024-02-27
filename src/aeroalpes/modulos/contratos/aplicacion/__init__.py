from pydispatch import dispatcher

from .handlers import HandlerContratoIntegracion

from aeroalpes.modulos.contratos.dominio.eventos import ContratoCreado

dispatcher.connect(HandlerContratoIntegracion.handle_contrato_creado, signal=f'{ContratoCreado.__name__}Integracion')
""" dispatcher.connect(HandlerContratoIntegracion.handle_contrato_firmado, signal=f'{ContratoFirmado.__name__}Integracion')
dispatcher.connect(HandlerContratoIntegracion.handle_contrato_procesado, signal=f'{ContratoProcesado.__name__}Integracion') """