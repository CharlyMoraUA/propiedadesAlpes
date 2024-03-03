from dataclasses import dataclass, field
from inquilinos.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class InquilinoDTO(DTO):
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    telefono: int = field(default_factory=int)