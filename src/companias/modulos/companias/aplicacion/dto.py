from dataclasses import dataclass, field
from companias.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class CompaniaDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    documento_identidad: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    telefono: int = field(default_factory=int)