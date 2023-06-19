from DAOs.dao import DAO
from entidade.mesa import Mesa

#cada entidade terá uma classe dessa, implementação bem simples.
class ItemCardapioDAO(DAO):
    def __init__(self):
        super().__init__('mesas.pkl')

    def add(self, itemcardapio: ItemCardapio):
        if((itemcardapio is not None) and isinstance(itemcardapio, ItemCardapio) and isinstance(itemcardapio.codigo_item, int)):
            super().add(itemcardapio.codigo_item,itemcardapio)

    def update(self, itemcardapio: ItemCardapio):
        if((itemcardapio is not None) and isinstance(itemcardapio, ItemCardapio) and isinstance(itemcardapio.codigo_item, int)):
            super().update(itemcardapio.numero, itemcardapio)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)