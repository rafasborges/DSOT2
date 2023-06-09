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
      sg.ChangeLookAndFeel('TealMono')
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
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_cliente(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Número de convidados:', size=(15, 1)), sg.InputText('', key='num_convidados')],
        [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
        [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
      ]
      self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

      button, values = self.open()
      nome = values['nome']
      cpf = values['cpf']
      num_convidados = values['num_convidados']
      idade = values['idade']


      self.close()
      return {"nome": nome, "cpf": cpf, "num_convidados": num_convidados, "idade": idade}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_cliente(self, dados_cliente):
      string_todos_clientes = ""
      for dado in dados_cliente:
        string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + dados_cliente["nome"] + '\n'
        string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dados_cliente["cpf"]) + '\n'
        string_todos_clientes = string_todos_clientes + "NUM. DE CONVIDADOS: " + str(dados_cliente["num_convidados"]) + '\n'
        string_todos_clientes = string_todos_clientes + "IDADE: " + str(dados_cliente["idade"]) + '\n\n'

      sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
      sg.ChangeLookAndFeel('TealMono')
      layout = [
        [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
        [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Helvica", 15))],
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

