from limites.tela import Tela
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
        while True:
            try:
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
                if ((not isinstance(codigo, int)) or
                    (not isinstance(id_reserva, int))):
                    raise ValueError
                self.close()
                return {"codigo": codigo, "id_reserva": id_reserva, "lista_itens": lista_itens}
            
            except ValueError:
                    sg.Popup("Dados incorretos! Utilize apenas inteiros para o código e id da reserva!", title = "ERRO")
                    self.close()

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_dados_pedido(self, dados_pedido):
        try:
            string_todos_pedidos = ""
            for pedido in dados_pedido:
                print(pedido)
                string_todos_pedidos += "CÓDIGO DO PEDIDO: " + str(pedido["codigo"]) + '\n'
                string_todos_pedidos += "ID DA RESERVA: " + str(pedido["id_reserva"]) + '\n'
                string_todos_pedidos += "ITENS DO PEDIDO: " + '\n' + str(pedido["itens"]) + '\n\n'

            sg.Popup('-------- LISTA DE PEDIDOS ----------', string_todos_pedidos)
        except KeyError as e:
            sg.Popup("Erro ao exibir dados do pedido: ", str(e))

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_pedido(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR PEDIDO ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o código do pedido que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('codigo:', size=(15, 1)), sg.InputText('', key='codigo')],
                    [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
                ]
                self.__window = sg.Window('Seleciona pedido').Layout(layout)

                button, values = self.open()
                codigo = values['codigo']
                if not isinstance(codigo, int):
                    raise ValueError
                self.close()
                return codigo
            except ValueError:
                sg.Popup("Insira um valor válido! O número da mesa deve ser um valor inteiro!", title = "ERRO")
                self.close()

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values