from limites.tela import Tela
'''

class TelaPedido(Tela):

    def tela_opcoes(self):
        print("--------- CADASTRO PEDIDO --------- ")
        print(" 1 - Incluir Pedido")
        print(" 2 - Listar Pedidos")
        print(" 3 - Excluir Pedido")
        print(" 4 - Voltar")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])
        return opcao
    

    def pega_dados_pedido(self):
        print("-------- DADOS PEDIDO ----------")
        while True:
            try:
                codigo = int(input("Código do Pedido: "))
                id_reserva = int(input("Id da Reserva que efetuou o Pedido: "))
                cod_itens= input("Código dos itens que deseja selecionar (separados por vírgula): ")
                lista_itens = [int(numero) for numero in cod_itens.split(",")]
                if ((not isinstance(codigo, int)) or
                    (not isinstance(id_reserva, int))):
                    raise ValueError
                return {"codigo": codigo, "id_reserva": id_reserva, "lista_itens": lista_itens}
            except ValueError:
                    print("Dados incorretos! Utilize apenas inteiros para o código e id da reserva!")


    def mostra_dados_pedido(self, dados_pedido):
        try:
            print("Código: ", dados_pedido["codigo"])
            print("Id da reserva: ", dados_pedido["id_reserva"])
            print("Itens: ", dados_pedido["itens"])
            print("\n")
        except KeyError as e:
            print("Erro ao exibir dados do pedido: ", str(e))
            print("\n")

    def seleciona_pedido(self):
        while True:
            codigo = input("Código do item que deseja selecionar: ")
            try:
                codigo = int(codigo)
                if not isinstance(codigo, int):
                    raise ValueError
                return codigo
            except ValueError:
                print("\nCódigo do item inválido. O código deve ser um valor inteiro.")
                print("\n") 
'''

import PySimpleGUI as sg


class TelaPedido(Tela):
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
            [sg.Text('-------- RESERVAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Pedido', "RD1", key='1')],
            [sg.Radio('Listar Pedido', "RD1", key='2')],
            [sg.Radio('Excluir Pedido', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_pedido(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- DADOS PEDIDO ----------', font=("Helvica", 25))],
            [sg.Text('Código do Pedido:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Id da Reserva que efetuou o Pedido:', size=(15, 1)), sg.InputText('', key='id_reserva')],
            [sg.Text('Código dos itens que deseja selecionar (separados por vírgula):', size=(15, 1)), sg.InputText('', key='cod_itens')],
            [sg.Cancel('Cancelar'), sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        id_reserva = values['id_reserva']
        cod_itens = values['cod_itens']
        lista_itens = [int(numero) for numero in cod_itens.split(",")]

        self.close()
        return {"codigo": codigo, "id_reserva": id_reserva, "lista_itens": lista_itens}

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_dados_pedido(self, dados_pedido):
        string_todos_pedidos = ""
        for pedido in dados_pedido:
            print(pedido)
            string_todos_pedidos += "CÓDIGO DO PEDIDO: " + str(pedido["codigo"]) + '\n'
            string_todos_pedidos += "ID DA RESERVA: " + str(pedido["id_reserva"]) + '\n'
            string_todos_pedidos += "ITENS DO PEDIDO: " + str(pedido["itens"]) + '\n\n'
            # string_todos_pedidos += "ITENS DO PEDIDO: " + '\n'
            # for i in range(len(pedido["itens"])):
            #     string_todos_pedidos += str(pedido["itens"][i]) + '\n'

        sg.Popup('-------- LISTA DE PEDIDOS ----------', string_todos_pedidos)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_pedido(self):
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- SELECIONAR PEDIDO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do pedido que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona pedido').Layout(layout)

        button, values = self.open()
        codigo = values['codigo']
        self.close()
        return codigo

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values