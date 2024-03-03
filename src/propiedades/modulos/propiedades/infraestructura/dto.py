"""DTOs para la capa de infrastructura del dominio de propiedades

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de propiedades

"""

from propiedades.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedades"
    id = db.Column(db.String(255), primary_key=True)
    matricula = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    area = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(255), nullable=False)


