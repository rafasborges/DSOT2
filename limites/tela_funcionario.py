from limites.tela import Tela

"""
class TelaFuncionario(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO FUNCIONÁRIO --------- ")
        print(" 1 - Incluir Funcionário")
        print(" 2 - Alterar Funcionário")
        print(" 3 - Excluir Funcionário")
        print(" 4 - Listar Funcionário")
        print(" 5 - Ver salário Funcionário")
        print(" 6 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao

    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONARIO ----------")
        while True:
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                salario = float(input("Salário: "))
                if ((self.checa_valor(nome) == True) or
                    (not isinstance(salario, (int, float)) or
                    len(cpf) != 11) or
                    salario < 0):
                    raise ValueError
                return {"nome": nome.upper(), "cpf": cpf, "salario": salario}
            except ValueError:
                print("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números decimais positivos para o salário!")
    

    def mostra_funcionario(self, dados_funcionario):
        try:
            print("NOME DO FUNCIONARIO: ", dados_funcionario["nome"].upper())
            print("CPF DO FUNCIONARIO: ", dados_funcionario["cpf"])
            print("SALÁRIO DO FUNCIONARIO: ", dados_funcionario["salario"])
        except KeyError as e:
            print("Erro ao exibir dados do funcionário:", str(e))
        print("\n")

    def seleciona_funcionario(self):
        while True:
            nome_lido = input("Nome do funcionario que deseja selecionar: ").upper()
            try:
                nome = str(nome_lido)
                if not isinstance(nome, str):
                    raise ValueError
                return nome
            except ValueError:
                print("\nInsira um valor válido!")
                print("\n")
"""
import PySimpleGUI as sg

class TelaFuncionario():
    def __init__(self):
        self.__window = None
        self.init_opcoes()

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
          opcao = 1
        if values['2']:
          opcao = 2
        if values['3']:
          opcao = 3
        if values['4']:
          opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
          opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
      # sg.theme_previewer()
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- FUNCIONARIOS ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Funcionário', "RD1", key='1')],
        [sg.Radio('Alterar Funcionário', "RD1", key='2')],
        [sg.Radio('Listar Funcionário', "RD1", key='3')],
        [sg.Radio('Excluir Funcionário', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_funcionario(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- DADOS Funcionário ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Salário:', size=(15, 1)), sg.InputText('', key='salario')],
        [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

      button, values = self.open()
      nome = values['nome']
      cpf = values['cpf']
      salario = values['salario']



      self.close()
      return {"nome": nome, "cpf": cpf, "salario": salario}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_funcionario(self, dados_cliente):
      string_todos_funcionarios = ""
      for dado in dados_funcionario:
        string_todos_funcionarios = string_todos_funcionarios + "NOME DO FUNCIONARIO: " + dados_funcionario["nome"] + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "CPF DO FUNCIONARIO: " + str(dados_funcionario["cpf"]) + '\n'
        string_todos_funcionarios = string_todos_funcionarios + "SALÁRIO DO FUNCIONARIO: " + str(dados_funcionario["salario"]) + '\n'


      sg.Popup('-------- LISTA DE FUNCIONARIOS ----------', string_todos_clientes)
      #self.__window = sg.Window('Lista de Funcionários').Layout(layout)
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_funcionario(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- SELECIONAR FUNCIONÁRIO ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do funcionário que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
      ]
      self.__window = sg.Window('Seleciona cliente').Layout(layout)

      button, values = self.open()
      cpf = values['cpf']
      self.close()
      return cpf

    def mostra_mensagem(self, msg):
      sg.popup("", msg)

    def close(self):
      self.__window.Close()

    def open(self):
      button, values = self.__window.Read()
      return button, values
