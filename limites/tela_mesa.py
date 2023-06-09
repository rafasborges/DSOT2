from limites.tela import Tela
from limites.tela_sistema import TelaSistema

'''
class TelaMesa(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO MESAS --------- ")
        print(" 1 - Incluir Mesa")
        print(" 2 - Alterar Mesa")
        print(" 3 - Excluir Mesa")
        print(" 4 - Listar Mesas")
        print(" 5 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
        return opcao


    def pega_dados_mesa(self):
        print("-------- DADOS MESA ----------")
        while True:
            try:
                numero = int(input("Número: "))
                capacidade = int(input("Capacidade: "))
                if (not isinstance(numero, int) or
                    not isinstance(capacidade, int) or
                    numero < 0 or capacidade < 0):
                    raise ValueError
                return {"numero": numero, "capacidade": capacidade}
            except ValueError:
                print("Dados incorretos, utilize apenas números positivos para número e capacidade!")


    def mostra_dados_mesa(self, dados_mesa):
        try:
            print("NÚMERO DA MESA: ", dados_mesa["numero"])
            print("CAPACIDADE DA MESA: ", dados_mesa["capacidade"])
        except KeyError as e:
            print("Erro ao exibir dados da mesa: ", str(e))
        print("\n")


    def seleciona_mesa(self):
        while True:
            numero = input("Número da mesa que deseja selecionar: ")
            try:
                numero = int(numero)
                if not isinstance(numero, int):
                    raise ValueError
                return numero
            except ValueError:
                print("\nInsira um valor válido! O número da mesa deve ser um valor inteiro!")
                print("\n")

'''

import PySimpleGUI as sg


class TelaMesa():
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
        # Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- MESAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Mesa', "RD1", key='1')],
            [sg.Radio('Alterar Mesa', "RD1", key='2')],
            [sg.Radio('Excluir Mesa', "RD1", key='3')],
            [sg.Radio('Listar Mesa', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_mesa(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- DADOS MESA ----------', font=("Helvica", 25))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Text('Capacidade:', size=(15, 1)), sg.InputText('', key='capacidade')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

        button, values = self.open()
        numero = values['numero']
        capacidade = values['capacidade']

        self.close()
        return {"numero": numero, "capacidade": capacidade}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_dados_mesa(self, dados_mesa):
        string_todas_mesas = ""
        for mesa in dados_mesa:
            string_todas_mesas = string_todas_mesas + "NÚMERO DA MESA: " + str(mesa["numero"]) + '\n'
            string_todas_mesas = string_todas_mesas + "CAPACIDADE DA MESA: " + str(mesa["capacidade"]) + '\n\n'

        sg.Popup('-------- LISTA DE MESAS ----------', string_todas_mesas)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_mesa(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- SELECIONAR MESA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o número da mesa que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona mesa').Layout(layout)

        button, values = self.open()
        num_mesa = values['numero']
        self.close()
        return num_mesa

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
