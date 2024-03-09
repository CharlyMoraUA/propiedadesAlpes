
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    contratos: typing.List[Contrato] = strawberry.field(resolver=obtener_contratos)
    #contrato: Contrato = strawberry.field(resolver=obtener_contrato)
    @strawberry.field
    def contrato(self, id: str) -> Contrato:
        return Contrato(id=id)