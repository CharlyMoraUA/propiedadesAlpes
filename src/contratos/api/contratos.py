import contratos.seedwork.presentacion.api as api
import json
from contratos.modulos.contratos.aplicacion.servicios import ServicioContrato
from contratos.modulos.contratos.aplicacion.dto import ContratoDTO
from contratos.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response, make_response
from contratos.modulos.contratos.aplicacion.mapeadores import MapeadorContratoDTOJson
from contratos.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from contratos.modulos.contratos.aplicacion.comandos.eliminar_contrato import EliminarContrato
from contratos.modulos.contratos.aplicacion.queries.obtener_contrato import ObtenerContrato
from contratos.modulos.contratos.aplicacion.comandos.actualizar_contrato import ActualizarContrato
from contratos.seedwork.aplicacion.comandos import ejecutar_commando
from contratos.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('contratos', '/contratos')

@bp.route('/contrato', methods=('POST',))
def crear_contrato():
    try:
        contrato_dict = request.json
        map_contrato = MapeadorContratoDTOJson()
        contrato_dto = map_contrato.externo_a_dto(contrato_dict)
        sr = ServicioContrato()
        dto_final = sr.crear_contrato(contrato_dto)
        return map_contrato.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/contrato-comando', methods=('POST',))
def crear_contrato_asincrono():
    try:
        contrato_dict = request.json
        map_contrato = MapeadorContratoDTOJson()
        contrato_dto = map_contrato.externo_a_dto(contrato_dict)
        comando = CrearContrato(contrato_dto.id, contrato_dto.fecha_creacion, contrato_dto.fecha_actualizacion, contrato_dto.fecha_inicio, contrato_dto.fecha_fin, contrato_dto.id_compania, contrato_dto.id_inquilino, contrato_dto.id_propiedad, contrato_dto.monto)
        ejecutar_commando(comando)
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/contrato', methods=('GET',))
@bp.route('/contrato/<id>', methods=('GET',))
def dar_contrato(id=None):
    if id:
        sr = ServicioContrato()
        map_contrato = MapeadorContratoDTOJson()
        return map_contrato.dto_a_externo(sr.obtener_contrato_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/contrato-query', methods=('GET',))
@bp.route('/contrato-query/<id>', methods=('GET',))
def dar_contrato_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerContrato(id))
        map_contrato = MapeadorContratoDTOJson()        
        return map_contrato.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]



@bp.route('/contrato-query/<id>', methods=('DELETE',))
def eliminar_contrato_usando_query(id=None):
    if id:
        comando = EliminarContrato(EliminarContrato(id))
        ejecutar_commando(comando)
        return make_response('', 204)
    else:
        return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 

@bp.route('/contrato-comando/<id>', methods=('PUT',))
def actualizar_contrato_asincrono(id=None):
    try:
        if id:
            contrato_dict = request.json
            map_contrato = MapeadorContratoDTOJson()
            contrato_dto = map_contrato.externo_a_dto(contrato_dict)
            comando = ActualizarContrato(id, contrato_dto.fecha_creacion, contrato_dto.fecha_actualizacion, contrato_dto.fecha_inicio, contrato_dto.fecha_fin, contrato_dto.id_compania, contrato_dto.id_inquilino, contrato_dto.id_propiedad, contrato_dto.monto)
            ejecutar_commando(comando)
            return Response('{}', status=202, mimetype='application/json')
        else:
            return [{'message': 'I HAVE TO HAVE A ID TO DELETE!'}] 
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')