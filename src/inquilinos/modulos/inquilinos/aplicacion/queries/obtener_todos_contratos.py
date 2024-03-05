from inquilinos.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery

class ObtenerTodoInquilinos(Query):
    ...

class ObtenerTodosInquilinosHandler(QueryHandler):

    def handle() -> ResultadoQuery:
        ...