
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    contratos: typing.List[Contrato] = strawberry.field(resolver=obtener_contratos)
    
    @strawberry.field
    def contrato(self, id: str) -> Contrato:
        return obtener_contrato(id)