from limites.tela import Tela

'''
class TelaCliente(Tela):
                    
    def tela_opcoes(self):
        print("--------- CADASTRO CLIENTE --------- ")
        print(" 1 - Incluir Cliente")
        print(" 2 - Alterar Cliente")
        print(" 3 - Listar Clientes")
        print(" 4 - Excluir Cliente")
        print(" 5 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
        return opcao
    
    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        while True:
            try:
                nome = input("Nome: ")
                cpf = input("CPF: ")
                num_convidados = int(input("Número de convidados: "))
                idade = int(input("Idade: "))
                if ((self.checa_valor(nome) == True) or
                    len(cpf) != 11 or
                    (not isinstance(num_convidados, int)) or
                     (not isinstance(idade, int))):
                    raise ValueError
                return {"nome": nome, "cpf": cpf, "num_convidados": num_convidados, "idade": idade}
            except ValueError:
                print("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números inteiros para a idade e número de convidados!")
            
    def mostra_cliente(self, dados_cliente):
        try:
            print("NOME DO CLIENTE: ", dados_cliente["nome"])
            print("CPF DO CLIENTE: ", dados_cliente["cpf"])
            print("IDADE DO CLIENTE: ", dados_cliente["idade"])
            print("NÚMERO DE CONVIDADOS DO CLIENTE: ", dados_cliente["num_convidados"])
        except KeyError as e:
            print("Erro ao exibir dados do cliente:", str(e))
        print("\n")


    def seleciona_cliente(self):        
        while True:
            cpf_lido = input("CPF do cliente que deseja selecionar: ")
            try:
                cpf = str(cpf_lido)
                if not isinstance(cpf, str):
                    raise ValueError
                return cpf
            except ValueError:
                print("\nInsira um valor válido!")
                print("\n")
'''
import PySimpleGUI as sg


class TelaCliente():
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
      sg.ChangeLookAndFeel('DarkTeal4')
      layout = [
        [sg.Text('-------- CLIENTES ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Incluir Cliente', "RD1", key='1')],
        [sg.Radio('Alterar Cliente', "RD1", key='2')],
        [sg.Radio('Listar Cliente', "RD1", key='3')],
        [sg.Radio('Excluir Cliente', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de livros').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_amigo(self):
      sg.ChangeLookAndFeel('DarkTeal4')
      layout = [
        [sg.Text('-------- DADOS AMIGO ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Telefone:', size=(15, 1)), sg.InputText('', key='telefone')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Sistema de livros').Layout(layout)

      button, values = self.open()
      nome = values['nome']
      telefone = values['telefone']
      cpf = values['cpf']

      self.close()
      return {"nome": nome, "telefone": telefone, "cpf": cpf}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_amigo(self, dados_amigo):
      string_todos_amigos = ""
      for dado in dados_amigo:
        string_todos_amigos = string_todos_amigos + "NOME DO AMIGO: " + dado["nome"] + '\n'
        string_todos_amigos = string_todos_amigos + "FONE DO AMIGO: " + str(dado["telefone"]) + '\n'
        string_todos_amigos = string_todos_amigos + "CPF DO AMIGO: " + str(dado["cpf"]) + '\n\n'

      sg.Popup('-------- LISTA DE AMIGOS ----------', string_todos_amigos)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_amigo(self):
      sg.ChangeLookAndFeel('DarkTeal4')
      layout = [
        [sg.Text('-------- SELECIONAR AMIGO ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do amigo que deseja selecionar:', font=("Helvica", 15))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
      ]
      self.__window = sg.Window('Seleciona amigo').Layout(layout)

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

