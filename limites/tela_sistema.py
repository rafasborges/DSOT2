from limites.tela import Tela

'''
class TelaSistema(Tela):

    def tela_opcoes(self):
        print(" ===================================")
        print("|       SISTEMA RESTAURANTE         |")
        print(" ===================================")
        print("------------ RESTAURANTE ------------")
        print("1 - Mesas")
        print("2 - Itens do cardápio")
        print("3 - Funcionários")
        print("-------------- SISTEMA --------------")
        print("4 - Clientes")
        print("5 - Reservas")
        print("6 - Pedidos")
        print("------------ RELATÓRIOS -------------")
        print("7 - Relatório Valor Total")
        print("8 - Relatório Total Clientes")
        print("9 - Relatório Total Reservas")
        print("10 - Relatório Mais Pedidos")
        print("-------------------------------------")
        print("11 - Finalizar o dia")
        print("0 - Finalizar sistema")
        print("-------------------------------------")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        return opcao
'''

import PySimpleGUI as sg

class TelaSistema(Tela):
    def __init__(self):
        self.__window = None
        self.init_components()

# fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
# precisa chamar self.init_components() aqui para o caso de chamar essa janela uma 2a vez. Não é possível reusar layouts de janelas depois de fechadas.
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        if values['9']:
            opcao = 9
        if values['10']:
            opcao = 10
        if values['11']:
            opcao = 11
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    # def init_components(self):
    #     #sg.theme_previewer()
    #     sg.ChangeLookAndFeel('TealMono')
    #     layout = [
    #         [sg.Text('Bem vindo ao Sistema de Restaurante!', font=("Helvica",25))],
    #         [sg.Text('ESCOLHA SUA OPÇÃO:', font=("Helvica",15)), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.Text('RELATÓRIOS', font=("Helvica",15))],
    #         #[sg.Text('RESTAURANTE', font=("Helvica",25))],
    #         [sg.Radio('Mesas',"RD1", key='1')],
    #         [sg.Radio('Itens do cardápio',"RD1", key='2')],
    #         [sg.Radio('Funcionários',"RD1", key='3')],
    #         #[sg.Text('SISTEMA', font=("Helvica",25))],
    #         [sg.Radio('Clientes',"RD1", key='4')],
    #         [sg.Radio('Reservas',"RD1", key='5')],
    #         [sg.Radio('Pedidos',"RD1", key='6')],
    #         #[sg.Text('RELATÓRIOS', font=("Helvica",15))],
    #         [sg.Radio('Relatório Valor Total',"RD1", key='7')],
    #         [sg.Radio('Relatório Total Clientes',"RD1", key='8')],
    #         [sg.Radio('Relatório Total Reservas',"RD1", key='9')],
    #         [sg.Radio('Relatório Mais Pedidos',"RD1", key='10')],
    #         [sg.Text('ENCERRAR', font=("Helvica",15))],
    #         [sg.Radio('Finalizar o dia',"RD1", key='11')],
    #         [sg.Radio('Finalizar sistema',"RD1", key='0')],
    #         [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
    #     ]
    #     self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    def init_components(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('Bem vindo ao Sistema de Restaurante!', font=("Helvica",25))],
            [sg.Text('ESCOLHA SUA OPÇÃO:', font=("Helvica",15)), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.T(""), sg.Text('RELATÓRIOS', font=("Helvica",15))],
            [sg.Radio('Mesas',"RD1", key='1'), sg.Text(" " * 60), sg.Radio('Relatório Valor Total',"RD1", key='7')],
            [sg.Radio('Itens do cardápio',"RD1", key='2'), sg.Text(" " * 45), sg.Radio('Relatório Total Clientes',"RD1", key='8')],
            [sg.Radio('Funcionários',"RD1", key='3'), sg.Text(" " * 51), sg.Radio('Relatório Total Reservas',"RD1", key='9')],
            [sg.Radio('Clientes',"RD1", key='4'), sg.Text(" " * 58), sg.Radio('Relatório Mais Pedidos',"RD1", key='10')],
            [sg.Radio('Reservas',"RD1", key='5')],
            [sg.Radio('Pedidos',"RD1", key='6')],
            [sg.Text('ENCERRAR', font=("Helvica",15))],
            [sg.Radio('Finalizar o dia',"RD1", key='11')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)