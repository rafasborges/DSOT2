from limites.tela import Tela
import PySimpleGUI as sg

class TelaMesa(Tela):
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
        if values['0'] or button in (None, 'Cancelar', "Voltar", "Sair"):
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
            [sg.Button('Voltar'), sg.Cancel('Confirmar')]
        ]
        self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    # opção de tratamento: adicionar um if e só coletar nome e telefone se o button é 'Confirmar'
    def pega_dados_mesa(self):
        sg.ChangeLookAndFeel('TealMono')
        while True:
            try:
                layout = [
                    [sg.Text('-------- DADOS MESA ----------', font=("Helvica", 25))],
                    [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                    [sg.Text('Capacidade:', size=(15, 1)), sg.InputText('', key='capacidade')],
                    [sg.Cancel('Voltar'), sg.Button('Confirmar')]
                ]
                self.__window = sg.Window('Sistema de Restaurante').Layout(layout)

            
                button, values = self.open()
                print(button, values)
                if len(values['numero']) > 0:
                    numero = int(values['numero'])
                if len(values['capacidade']) > 0:
                    capacidade = int(values['capacidade'])
                else:
                    numero, capacidade = 0, 900
                #tentando fazer com que volte
                print(button, values)

                variavel = values.get('0', 'insight')

                if variavel != "insight":
                    if variavel or button in (None, 'Voltar'):
                        opcao = 0
                #self.close()
                    return opcao
                print(values)
                if button != "Voltar" and ((not isinstance(numero, int) or
                        not isinstance(capacidade, int) or
                        numero < 0 or capacidade < 0)):
                        raise ValueError

                self.close()
                return {"numero": numero, "capacidade": capacidade}
            except ValueError:
                    sg.Popup("Dados incorretos, utilize apenas números positivos para número e capacidade!", title = "ERRO")
                    self.close()


    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_dados_mesa(self, dados_mesa):
        sg.ChangeLookAndFeel('TealMono')

        try:
            string_todas_mesas = ""
            for mesa in dados_mesa:
                string_todas_mesas = string_todas_mesas + "NÚMERO DA MESA: " + str(mesa["numero"]) + '\n'
                string_todas_mesas = string_todas_mesas + "CAPACIDADE DA MESA: " + str(mesa["capacidade"]) + '\n\n'

            sg.Popup('-------- LISTA DE MESAS ----------', string_todas_mesas)
        except KeyError as e:
            sg.Popup("Erro ao exibir dados da mesa: ", str(e))

            button, values = self.open()
            if len(values['numero']) > 0:
                numero = int(values['numero'])
            if len(values['capacidade']) > 0:
                capacidade = int(values['capacidade'])
            else:
                numero, capacidade = 0, 900
                # tentando fazer com que volte
            print(button, values)

            variavel = values.get('0', 'insight')

            if variavel != "insight":
                if variavel or button in (None, 'Voltar'):
                    opcao = 0
                # self.close()
                return opcao
            print(values)
            if button != "Voltar" and ((not isinstance(numero, int) or
                                        not isinstance(capacidade, int) or
                                        numero < 0 or capacidade < 0)):
                raise ValueError

            self.close()
            return {"numero": numero, "capacidade": capacidade}

        except ValueError:
            sg.Popup("Dados incorretos, utilize apenas números positivos para número e capacidade!", title="ERRO")
            self.close()


    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_mesa(self):
        sg.ChangeLookAndFeel('TealMono')

        while True:
            try:
                layout = [
                    [sg.Text('-------- SELECIONAR MESA ----------', font=("Helvica", 25))],
                    [sg.Text('Digite o número da mesa que deseja selecionar:', font=("Helvica", 15))],
                    [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='numero')],
                    [sg.Button('Cancelar'), sg.Cancel('Confirmar')]
                ]
                self.__window = sg.Window('Seleciona mesa').Layout(layout)

                button, values = self.open()
                if len(values['numero']) > 0:
                    num_mesa = int(values['numero'])
                else:
                    num_mesa = 0
                if not isinstance(num_mesa, int):
                    raise ValueError
                self.close()
                return num_mesa
                variavel = values.get('0', 'insight')

                if variavel != "insight":
                    if variavel or button in (None, 'Voltar'):
                        opcao = 0
                    # self.close()
                    return opcao
                print(values)
                if button != "Voltar" and ((not isinstance(numero, int) or
                                            numero < 0 or capacidade < 0)):
                    raise ValueError

                self.close()
                return {"numero": numero}

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
