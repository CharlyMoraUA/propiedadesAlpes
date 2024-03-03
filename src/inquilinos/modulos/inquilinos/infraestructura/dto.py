"""DTOs para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de inquilinos

"""

from inquilinos.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

# class Inquilino(db.Model):
#     __tablename__ = "inquilinos"
#     id = db.Column(db.String(255), primary_key=True)
#     fecha_creacion = db.Column(db.DateTime, nullable=False)
#     fecha_actualizacion = db.Column(db.DateTime, nullable=False)
#     fecha_inicio = db.Column(db.DateTime, nullable=False)
#     fecha_fin = db.Column(db.DateTime, nullable=False)
#     id_compania = db.Column(db.Integer, nullable=True)
#     id_inquilino = db.Column(db.Integer, nullable=True)
#     id_propiedad = db.Column(db.Integer, nullable=True)
#     monto = db.Column(db.Float, nullable=False)

class Inquilino(db.Model):
    __tablename__ = "inquilinos"
    id = db.Column(db.String(255), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)