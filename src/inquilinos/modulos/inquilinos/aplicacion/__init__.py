from pydispatch import dispatcher

from .handlers import HandlerInquilinoIntegracion

from inquilinos.modulos.inquilinos.dominio.eventos import InquilinoCreado

dispatcher.connect(HandlerInquilinoIntegracion.handle_inquilino_creado, signal=f'{InquilinoCreado.__name__}Integracion')
""" dispatcher.connect(HandlerInquilinoIntegracion.handle_inquilino_firmado, signal=f'{InquilinoFirmado.__name__}Integracion')
dispatcher.connect(HandlerInquilinoIntegracion.handle_inquilino_procesado, signal=f'{InquilinoProcesado.__name__}Integracion') """