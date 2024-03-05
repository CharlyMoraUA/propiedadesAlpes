""" Excepciones del dominio de inquilinos

En este archivo usted encontrará los Excepciones relacionadas
al dominio de inquilinos

"""

from inquilinos.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioInquilinosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de inquilinos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)