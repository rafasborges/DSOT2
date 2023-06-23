import PySimpleGUI as sg
from limites.tela import Tela

class TelaCliente(Tela):
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
        if values['0'] or button in (None, 'Cancelar', 'Voltar', 'Sair'):
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
        while True:
            try:
                layout = [
                    [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
                    [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
                    [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                    [sg.Text('Número de convidados:', size=(17, 1)), sg.InputText('', key='num_convidados', size=(43, 1))],
                    [sg.Text('Idade:', size=(15, 1)), sg.InputText('', key='idade')],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

                button, values = self.open()
                if len(values['nome']) > 0:
                    nome = str(values['nome'])
                if len(values['cpf']) > 0:
                    cpf = str(values['cpf'])
                if len(values['num_convidados']) > 0:
                    num_convidados = int(values['num_convidados'])
                if len(values['idade']) > 0:
                    idade = int(values['idade'])
                else:
                    nome, cpf, num_convidados, idade = '', '', 900, 900

                variavel = values.get('', 'insight')
                if variavel != 'insight':
                    if variavel or button in (None, 'Voltar'):
                        opcao = 0
                    return opcao
                
                if button != 'Voltar' and ((self.checa_valor(nome) == True) or len(cpf) != 11 or (not isinstance(num_convidados, int)) or (not isinstance(idade, int))):
                    raise ValueError
                self.close()
                return {"nome": nome, "cpf": cpf, "num_convidados": num_convidados, "idade": idade}
            except ValueError:
                    sg.Popup("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas strings para o nome e números inteiros para a idade e número de convidados!", title = "ERRO")
                    self.close()

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_cliente(self, dados_cliente):
        sg.ChangeLookAndFeel('TealMono')
        try:
            string_todos_clientes = ""
            for dado in dados_cliente:
                string_todos_clientes = string_todos_clientes + "NOME DO CLIENTE: " + str(dado["nome"]) + '\n'
                string_todos_clientes = string_todos_clientes + "CPF DO CLIENTE: " + str(dado["cpf"]) + '\n'
                string_todos_clientes = string_todos_clientes + "NUM. DE CONVIDADOS: " + str(dado["num_convidados"]) + '\n'
                string_todos_clientes = string_todos_clientes + "IDADE: " + str(dado["idade"]) + '\n\n'

            sg.Popup('-------- LISTA DE CLIENTES ----------', string_todos_clientes, title='')

        except KeyError as e:
            sg.Popup("Erro ao exibir dados do cliente: ", str(e))
            self.__window = sg.Window('Lista de Clientes').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o CPF do cliente que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
                    [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
                ]
                self.__window = sg.Window('Seleciona cliente').Layout(layout)

                button, values = self.open()
                cpf = str(values['cpf'])
                if not isinstance(cpf, str):
                    raise ValueError
                self.close()
                return cpf
            except ValueError:
                sg.Popup("Insira um valor válido!", title = "ERRO")
                self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg, title='')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

