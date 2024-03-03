"""DTOs para la capa de infrastructura del dominio de inquilinos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de inquilinos

"""

from inquilinos.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()


class Inquilino(db.Model):
    __tablename__ = "inquilinos"
    id = db.Column(db.String(255), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)