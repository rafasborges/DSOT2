from limites.tela import Tela
import PySimpleGUI as sg


class TelaReserva(Tela):
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
        if values['0'] or button in (None, 'Cancelar', 'Voltar', 'Sair'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('TealMono')
        layout = [
            [sg.Text('-------- RESERVAS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Reserva', "RD1", key='1')],
            [sg.Radio('Listar Reserva', "RD1", key='2')],
            [sg.Radio('Excluir Reserva', "RD1", key='3')],
            [sg.Radio('Calcular valor total de uma Reserva', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Voltar'), sg.Cancel('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_reserva(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
          try:
            layout = [
                [sg.Text('-------- DADOS RESERVA ----------', font=("Helvica", 25))],
                [sg.Text('Id da reserva:', size=(15, 1)), sg.InputText('', key='id')],
                [sg.Text('Número da Mesa:', size=(15, 1)), sg.InputText('', key='mesa_num')],
                [sg.Text('CPF do cliente:', size=(15, 1)), sg.InputText('', key='cliente_cpf')],
                [sg.Text('Nome do funcionário:', size=(15, 1)), sg.InputText('', key='funcionario_nome')],
                [sg.Cancel('Voltar'), sg.Button('Confirmar')]
            ]
            self.__window = sg.Window('Sistema de Restaurante').Layout(layout)
            button, values = self.open()
            if len(values['id']) > 0:
              id = int(values['id'])
            if len(values['mesa_num']) > 0:
              mesa_num = int(values['mesa_num'])
            if len(values['cliente_cpf']) > 0:
              cliente_cpf = str(values['cliente_cpf'])
            if len(values['funcionario_nome']):
              funcionario_nome = str(values['funcionario_nome'])
            else:
               id, mesa_num, cliente_cpf, funcionario_nome = 0, 0, '', ''
            
            variavel = values.get('0', 'insight')

            if variavel != "insight":
                if variavel or button in (None, 'Voltar'):
                  opcao = 0
                return opcao
            
            if button != 'Voltar' and ((not isinstance(id, int)) or 
                (not isinstance(mesa_num, int)) or
                (self.checa_valor(funcionario_nome) == True)
                or len(cliente_cpf) != 11):
              raise ValueError
            self.close()
            return {"id": id, "mesa_num": mesa_num, "cliente_cpf": cliente_cpf, "funcionario_nome": funcionario_nome}
          except ValueError:
            sg.Popup("Dados incorretos! O CPF deve conter 11 dígitos! Utilize apenas inteiros para o id e número da mesa e string para o nome do funcionário!", title = "ERRO")
            self.close()
          
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_reserva(self, dados_reserva):
      try:
        string_todas_reservas = ""
        for reserva in dados_reserva:
            string_todas_reservas = string_todas_reservas + "ID DA RESERVA: " + str(reserva["id_reserva"]) + '\n'
            string_todas_reservas = string_todas_reservas + "NÚMERO DA MESA: " + str(reserva["num_mesa"]) + '\n'
            string_todas_reservas = string_todas_reservas + "NOME DO CLIENTE: " + str(reserva["nome_cliente"]) + '\n'
            string_todas_reservas = string_todas_reservas + "NOME DO FUNCIONÁRIO: " + str(reserva["nome_funcionario"]) + '\n\n'

        sg.Popup('-------- LISTA DE RESERVAS ----------', string_todas_reservas, title='')
      except KeyError as e:
        sg.Popup("Erro ao exibir dados da reserva: ", str(e))


    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_reserva(self):
        sg.ChangeLookAndFeel('TealMono')

        while True:
          try:
            layout = [
                [sg.Text('-------- SELECIONAR RESERVA ----------', font=("Helvica", 25))],
                [sg.Text('Digite o id da reserva que deseja selecionar:', font=("Helvica", 15))],
                [sg.Text('Id:', size=(15, 1)), sg.InputText('', key='id')],
                [sg.Button('Voltar'), sg.Cancel('Confirmar')]
            ]
            self.__window = sg.Window('Seleciona reserva').Layout(layout)

            button, values = self.open()
            id_reserva = int(values['id'])
            if not isinstance(id_reserva, int):
              raise ValueError
            self.close()
            return id_reserva
          except ValueError:
            sg.Popup("Insira um valor válido! O número da reserva deve ser um valor inteiro!", title = "ERRO")
            self.close()
    
    def mostra_ganho_reserva(self, id_reserva, total):
      sg.Popup(("Valor total da reserva " + str(id_reserva) + ": R$ " + str(total)), title= 'Total')

    def mostra_mensagem(self, msg):
        sg.popup("", msg, title='')

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values