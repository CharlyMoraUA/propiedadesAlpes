from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

import uuid

@dataclass
class ContratoCreado(EventoDominio):
    id_contrato: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None