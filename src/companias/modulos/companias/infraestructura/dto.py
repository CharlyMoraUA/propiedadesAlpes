"""DTOs para la capa de infrastructura del dominio de companias

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de companias

"""

from companias.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Compania(db.Model):
    __tablename__ = "companias"
    id = db.Column(db.String(255), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    documento_identidad = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(32), nullable=False)


