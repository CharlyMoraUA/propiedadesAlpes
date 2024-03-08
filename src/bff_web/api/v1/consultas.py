
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    contrato: "Contrato" = strawberry.field(resolver=obtener_contrato)