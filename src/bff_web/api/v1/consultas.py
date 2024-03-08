
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    contratos: typing.List[Contrato] = strawberry.field(resolver=obtener_contratos)