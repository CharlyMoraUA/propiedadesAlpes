from dataclasses import dataclass, field
from propiedades.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    id: str = field(default_factory=str)
    matricula: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    area: float = field(default_factory=int)
    tipo: str = field(default_factory=str)