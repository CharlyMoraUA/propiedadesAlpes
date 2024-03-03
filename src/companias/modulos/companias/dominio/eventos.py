from __future__ import annotations
from dataclasses import dataclass, field
from companias.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

import uuid

@dataclass
class CompaniaCreada(EventoDominio):
    id_compania: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None