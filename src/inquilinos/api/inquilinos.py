import inquilinos.seedwork.presentacion.api as api
import json
from inquilinos.modulos.inquilinos.aplicacion.servicios import ServicioInquilino
from inquilinos.modulos.inquilinos.aplicacion.dto import InquilinoDTO
from inquilinos.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response, make_response
from inquilinos.modulos.inquilinos.aplicacion.mapeadores import MapeadorInquilinoDTOJson
from inquilinos.modulos.inquilinos.aplicacion.comandos.crear_inquilino import CrearInquilino
from inquilinos.modulos.inquilinos.aplicacion.comandos.eliminar_inquilino import EliminarInquilino
from inquilinos.modulos.inquilinos.aplicacion.queries.obtener_inquilino import ObtenerInquilino
from inquilinos.modulos.inquilinos.aplicacion.comandos.actualizar_inquilino import ActualizarInquilino
from inquilinos.seedwork.aplicacion.comandos import ejecutar_commando
from inquilinos.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('inquilinos', '/inquilinos')

@bp.route('/inquilino', methods=('POST',))
def crear_inquilino():
    try:
        inquilino_dict = request.json
        map_inquilino = MapeadorInquilinoDTOJson()
        inquilino_dto = map_inquilino.externo_a_dto(inquilino_dict)
        sr = ServicioInquilino()
        dto_final = sr.crear_inquilino(inquilino_dto)
        return map_inquilino.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/inquilino-comando', methods=('POST',))
def crear_inquilino_asincrono():
    try:
        inquilino_dict = request.json
        map_inquilino = MapeadorInquilinoDTOJson()
        inquilino_dto = map_inquilino.externo_a_dto(inquilino_dict)
        comando = CrearInquilino(inquilino_dto.id, inquilino_dto.fecha_creacion, inquilino_dto.fecha_actualizacion, inquilino_dto.fecha_inicio, inquilino_dto.fecha_fin, inquilino_dto.id_compania, inquilino_dto.id_inquilino, inquilino_dto.id_propiedad, inquilino_dto.monto)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/inquilino', methods=('GET',))
@bp.route('/inquilino/<id>', methods=('GET',))
def dar_inquilino(id=None):
    if id:
        sr = ServicioInquilino()
        map_inquilino = MapeadorInquilinoDTOJson()
        return map_inquilino.dto_a_externo(sr.obtener_inquilino_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/inquilino-query', methods=('GET',))
@bp.route('/inquilino-query/<id>', methods=('GET',))
def dar_inquilino_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerInquilino(id))
        map_inquilino = MapeadorInquilinoDTOJson()        
        return map_inquilino.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]



@bp.route('/inquilino-query/<id>', methods=('DELETE',))
def eliminar_inquilino_usando_query(id=None):
    if id:
        comando = EliminarInquilino(EliminarInquilino(id))
        ejecutar_commando(comando)
        return make_response('', 204)
    else:
        return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 

@bp.route('/inquilino-comando/<id>', methods=('PUT',))
def actualizar_inquilino_asincrono(id=None):
    try:
        if id:
            inquilino_dict = request.json
            map_inquilino = MapeadorInquilinoDTOJson()
            inquilino_dto = map_inquilino.externo_a_dto(inquilino_dict)
            comando = ActualizarInquilino(id, inquilino_dto.fecha_creacion, inquilino_dto.fecha_actualizacion, inquilino_dto.fecha_inicio, inquilino_dto.fecha_fin, inquilino_dto.id_compania, inquilino_dto.id_inquilino, inquilino_dto.id_propiedad, inquilino_dto.monto)
            ejecutar_commando(comando)
            return Response('{}', status=202, mimetype='application/json')
        else:
            return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')