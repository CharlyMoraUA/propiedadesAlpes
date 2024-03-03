from pydispatch import dispatcher

from .handlers import HandlerPropiedadIntegracion

from propiedades.modulos.propiedades.dominio.eventos import PropiedadCreado

dispatcher.connect(HandlerPropiedadIntegracion.handle_propiedad_creado, signal=f'{PropiedadCreado.__name__}Integracion')
