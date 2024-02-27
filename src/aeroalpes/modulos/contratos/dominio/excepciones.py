""" Excepciones del dominio de contratos

En este archivo usted encontrará los Excepciones relacionadas
al dominio de contratos

"""

from aeroalpes.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioContratosExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de contratos'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)