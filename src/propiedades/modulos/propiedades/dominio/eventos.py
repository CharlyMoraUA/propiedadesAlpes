from __future__ import annotations
from dataclasses import dataclass, field
from propiedades.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

import uuid

@dataclass
class PropiedadCreado(EventoDominio):
    id_propiedad: uuid.UUID = None
    estado: str = None
    matricula: datetime = None