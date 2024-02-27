import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.contratos.aplicacion.servicios import ServicioContrato
from aeroalpes.modulos.contratos.aplicacion.dto import ContratoDTO
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContratoDTOJson
from aeroalpes.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
from aeroalpes.modulos.contratos.aplicacion.queries.obtener_contrato import ObtenerContrato
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
from aeroalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('contratos', '/contratos')

@bp.route('/contrato', methods=('POST',))
def crear_contrato():
    try:
        contrato_dict = request.json

        map_contrato = MapeadorContratoDTOJson()
        contrato_dto = map_contrato.externo_a_dto(contrato_dict)

        sr = ServicioContrato()
        dto_final = sr.crear_contrato(contrato_dto)
        print("dto_final: ")
        print(dto_final)

        return map_contrato.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/contrato-comando', methods=('POST',))
def crear_contrato_asincrono():
    try:
        contrato_dict = request.json

        map_contrato = MapeadorContratoDTOJson()
        print("contrato_dict")
        print(contrato_dict)

        contrato_dto = map_contrato.externo_a_dto(contrato_dict)
        print("contratodto2:")
        print(contrato_dto)

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
    print("cualquier cosa")
    if id:
        query_resultado = ejecutar_query(ObtenerContrato(id))
        print(" query_resultado")
        print( query_resultado)
        map_contrato = MapeadorContratoDTOJson()
        print("map_contrato")
        print(map_contrato)
        
        return map_contrato.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]
