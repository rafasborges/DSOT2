from DAOs.dao import DAO
from entidades.pedido import Pedido

#cada entidade terá uma classe dessa, implementação bem simples.
class PedidoDAO(DAO):
    def __init__(self):
        super().__init__('pedidos.pkl')
        self.__total_pedidos = []

    def add(self, pedido: Pedido):
        if((pedido is not None) and isinstance(pedido, Pedido) and isinstance(pedido.codigo, int)):
            super().add(pedido.codigo, pedido)

    def update(self, pedido: Pedido):
        if((pedido is not None) and isinstance(pedido, Pedido) and isinstance(pedido.codigo, int)):
            super().update(pedido.codigo, pedido)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
    
    def add_total(self, pedido: Pedido):
        if((pedido is not None) and isinstance(pedido, Pedido) and isinstance(pedido.codigo, int)):
            self.__total_pedidos.append(pedido)

    @property
    def total_pedidos(self):
        return self.__total_pedidos