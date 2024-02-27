from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ContratoDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)
    id_compania: int = field(default_factory=int)
    id_inquilino: int = field(default_factory=int)
    id_propiedad: int = field(default_factory=int)
    monto: float = field(default_factory=float)