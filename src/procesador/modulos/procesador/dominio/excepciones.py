""" Excepciones del dominio de procesador

En este archivo usted encontrará los Excepciones relacionadas
al dominio de procesador

"""

from procesador.seedwork.dominio.excepciones import ExcepcionFabrica

class TipoObjetoNoExisteEnDominioProcesadorExcepcion(ExcepcionFabrica):
    def __init__(self, mensaje='No existe una fábrica para el tipo solicitado en el módulo de procesador'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)