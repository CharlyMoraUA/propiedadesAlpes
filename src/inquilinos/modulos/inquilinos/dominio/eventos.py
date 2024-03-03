from __future__ import annotations
from dataclasses import dataclass, field
from inquilinos.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

import uuid

@dataclass
class InquilinoCreado(EventoDominio):
    id_inquilino: uuid.UUID = None
    nombre: str = None
    telefono: int = None