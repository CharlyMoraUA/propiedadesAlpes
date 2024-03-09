from propiedades.modulos.propiedades.aplicacion.queries.obtener_todos_propiedades import ObtenerTodosPropiedades
import propiedades.seedwork.presentacion.api as api
import json
from propiedades.modulos.propiedades.aplicacion.servicios import ServicioPropiedad
from propiedades.modulos.propiedades.aplicacion.dto import PropiedadDTO
from propiedades.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response, make_response
from propiedades.modulos.propiedades.aplicacion.mapeadores import MapeadorPropiedadDTOJson
from propiedades.modulos.propiedades.aplicacion.comandos.crear_propiedad import CrearPropiedad
from propiedades.modulos.propiedades.aplicacion.comandos.eliminar_propiedad import EliminarPropiedad
from propiedades.modulos.propiedades.aplicacion.queries.obtener_propiedad import ObtenerPropiedad
from propiedades.modulos.propiedades.aplicacion.comandos.actualizar_propiedad import ActualizarPropiedad
from propiedades.seedwork.aplicacion.comandos import ejecutar_commando
from propiedades.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('propiedades', '/propiedades')

@bp.route('/propiedad-comando', methods=('POST',))
def crear_propiedad_asincrono():
    try:
        propiedad_dict = request.json
        map_propiedad = MapeadorPropiedadDTOJson()
        propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
        comando = CrearPropiedad(propiedad_dto.id, propiedad_dto.matricula, propiedad_dto.direccion, propiedad_dto.area, propiedad_dto.tipo)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/propiedad-query', methods=('GET',))
@bp.route('/propiedad-query/<id>', methods=('GET',))
def dar_propiedad_usando_query(id=None):
    map_propiedad = MapeadorPropiedadDTOJson() 
    if id:
        query_resultado = ejecutar_query(ObtenerPropiedad(id))
        map_propiedad = MapeadorPropiedadDTOJson()        
        return map_propiedad.dto_a_externo(query_resultado.resultado)
    else:
        query_resultado = ejecutar_query(ObtenerTodosPropiedades())
        resultados = []
        
        for propiedad in query_resultado.resultado:
            resultados.append(map_propiedad.dto_a_externo(propiedad))
        
        return resultados

@bp.route('/propiedad-query/<id>', methods=('DELETE',))
def eliminar_propiedad_usando_query(id=None):
    if id:
        comando = EliminarPropiedad(EliminarPropiedad(id))
        ejecutar_commando(comando)
        return make_response('', 204)
    else:
        return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 

@bp.route('/propiedad-comando/<id>', methods=('PUT',))
def actualizar_propiedad_asincrono(id=None):
    try:
        if id:
            propiedad_dict = request.json
            map_propiedad = MapeadorPropiedadDTOJson()
            propiedad_dto = map_propiedad.externo_a_dto(propiedad_dict)
            comando = ActualizarPropiedad(id, propiedad_dto.matricula, propiedad_dto.direccion, propiedad_dto.area, propiedad_dto.tipo)
            ejecutar_commando(comando)
            return Response('{}', status=202, mimetype='application/json')
        else:
            return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')