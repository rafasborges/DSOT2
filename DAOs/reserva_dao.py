from DAOs.dao import DAO
from entidade.reserva import Reserva

#cada entidade terá uma classe dessa, implementação bem simples.
class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reservas.pkl')

    def add(self, reserva: Reserva):
        if((reserva is not None) and isinstance(reserva, Reserva) and isinstance(reserva.id, int)):
            super().add(reserva.id, reserva)

    def update(self, reserva: Reserva):
        if((reserva is not None) and isinstance(reserva, Reserva) and isinstance(reserva.id, int)):
            super().update(reserva.id, reserva)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)