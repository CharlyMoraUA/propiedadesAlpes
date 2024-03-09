import companias.seedwork.presentacion.api as api
import json
from companias.modulos.companias.aplicacion.servicios import ServicioCompania
from companias.modulos.companias.aplicacion.dto import CompaniaDTO
from companias.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response, make_response
from companias.modulos.companias.aplicacion.mapeadores import MapeadorCompaniaDTOJson
from companias.modulos.companias.aplicacion.comandos.crear_compania import CrearCompania
from companias.modulos.companias.aplicacion.comandos.eliminar_compania import EliminarCompania
from companias.modulos.companias.aplicacion.queries.obtener_compania import ObtenerCompania
from companias.modulos.companias.aplicacion.comandos.actualizar_compania import ActualizarCompania
from companias.modulos.companias.aplicacion.queries.obtener_todos_companias import ObtenerTodosCompanias
from companias.seedwork.aplicacion.comandos import ejecutar_commando
from companias.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('companias', '/companias')

@bp.route('/compania', methods=('POST',))
def crear_compania():
    try:
        compania_dict = request.json
        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)
        sr = ServicioCompania()
        dto_final = sr.crear_compania(compania_dto)
        return map_compania.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/compania-comando', methods=('POST',))
def crear_compania_asincrono():
    try:
        compania_dict = request.json
        map_compania = MapeadorCompaniaDTOJson()
        compania_dto = map_compania.externo_a_dto(compania_dict)
        comando = CrearCompania(compania_dto.id, compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.documento_identidad, compania_dto.nombre, compania_dto.direccion, compania_dto.telefono)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/compania', methods=('GET',))
@bp.route('/compania/<id>', methods=('GET',))
def dar_compania(id=None):
    if id:
        sr = ServicioCompania()
        map_compania = MapeadorCompaniaDTOJson()
        return map_compania.dto_a_externo(sr.obtener_compania_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/compania-query', methods=('GET',))
@bp.route('/compania-query/<id>', methods=('GET',))
def dar_compania_usando_query(id=None):
    map_compania = MapeadorCompaniaDTOJson()   
    if id:
        query_resultado = ejecutar_query(ObtenerCompania(id))
        map_compania = MapeadorCompaniaDTOJson()        
        return map_compania.dto_a_externo(query_resultado.resultado)
    else:
        query_resultado = ejecutar_query(ObtenerTodosCompanias())
        resultados = []

        for compania in query_resultado.resultado:
            resultados.append(map_compania.dto_a_externo(compania))
        
        return resultados



@bp.route('/compania-query/<id>', methods=('DELETE',))
def eliminar_compania_usando_query(id=None):
    if id:
        comando = EliminarCompania(EliminarCompania(id))
        ejecutar_commando(comando)
        return make_response('', 204)
    else:
        return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 

@bp.route('/compania-comando/<id>', methods=('PUT',))
def actualizar_compania_asincrono(id=None):
    try:
        if id:
            compania_dict = request.json
            map_compania = MapeadorCompaniaDTOJson()
            compania_dto = map_compania.externo_a_dto(compania_dict)
            comando = ActualizarCompania(id, compania_dto.fecha_creacion, compania_dto.fecha_actualizacion, compania_dto.documento_identidad, compania_dto.nombre, compania_dto.direccion, compania_dto.telefono)
            ejecutar_commando(comando)
            return Response('{}', status=202, mimetype='application/json')
        else:
            return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')