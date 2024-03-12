
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    contratos: typing.List[Contrato] = strawberry.field(resolver=obtener_contratos)
    
    @strawberry.field
    def contrato(self, id: str) -> Contrato:
        return obtener_contrato(id)
    
    propiedades: typing.List[Propiedad] = strawberry.field(resolver=obtener_propiedades)
    
    @strawberry.field
    def propiedad(self, id: str) -> Propiedad:
        return obtener_propiedad(id)
    
    
    inquilinos: typing.List[Inquilino] = strawberry.field(resolver=obtener_inquilinos)
    
    @strawberry.field
    def inquilino(self, id: str) -> Inquilino:
        return obtener_inquilino(id)
    
    
    companias: typing.List[Compania] = strawberry.field(resolver=obtener_companias)
    
    @strawberry.field
    def compania(self, id: str) -> Compania:
        return obtener_compania(id)