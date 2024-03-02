from inquilinos.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery

class ObtenerTodoContratos(Query):
    ...

class ObtenerTodosContratosHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...