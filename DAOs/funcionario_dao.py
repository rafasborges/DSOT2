from DAOs.dao import DAO
from entidades.funcionario import Funcionario

#cada entidade terá uma classe dessa, implementação bem simples.
class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionario.pkl')

    def add(self, funcionario: Funcionario):
        if((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.cpf, str)):
            super().add(funcionario.cpf, funcionario)

    def update(self, funcionario: Funcionario):
        if((funcionario is not None) and isinstance(funcionario, Funcionario) and isinstance(funcionario.cpf, str)):
            super().update(funcionario.cpf, funcionario)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)