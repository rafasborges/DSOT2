from limites.tela import Tela

'''
class TelaItemCardapio(Tela):

  def tela_opcoes(self):
    print("-------- Itens Cardápio ----------")
    print("Escolha a opcao")
    print("1 - Incluir Item")
    print("2 - Alterar Item")
    print("3 - Excluir Item")
    print("4 - Listar Itens")
    print("5 - Voltar")

    opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5])
    return opcao

  def pega_dados_item_cardapio(self):
    print("-------- DADOS ITEM CARDÁPIO ----------")
    while True:
        try:
          nome = input("Nome: ")
          descricao = input("Descrição: ")
          codigo_item = int(input("Código: "))
          preco = float(input("Preço: "))
          if ((self.checa_valor(nome) == True) or
                  (self.checa_valor(descricao) == True) or
                  not isinstance(codigo_item, int) or
                  not isinstance(preco, float)):
             raise ValueError
          return {"nome": nome.upper(), "descricao": descricao.upper(), "codigo_item": codigo_item, "preco": preco}
        except ValueError:
          print("Dados incorretos, utilize apenas números positivos em código e preço e letras em nome e descrição!")
    
  def mostra_item_cardapio(self, dados_item):
    try:
        print("NOME DO ITEM: ", dados_item["nome"])
        print("DESCRIÇÃO DO ITEM: ", dados_item["descricao"])
        print("CÓDIGO DO ITEM: ", dados_item["codigo_item"])
        print("PREÇO DO ITEM: ", dados_item["preco"])
    except KeyError as e:
        print("Erro ao exibir dados do item do cardápio:", str(e))
    print("\n")


  def mostra_item_cardapio_formatado(self, dados_item):
   print("{} - {} - {} - R$ {:.2f}".format(dados_item["codigo_item"], dados_item["nome"], dados_item["descricao"], float(dados_item["preco"])))
        

  def seleciona_item(self):
    while True:
      codigo_item = input("Código do item que deseja selecionar: ")
      try:
        codigo_item = int(codigo_item)
        if not isinstance(codigo_item, int):
          raise ValueError
        return codigo_item
      except ValueError:
        print("\nCódigo do item inválido. O código deve ser um valor inteiro.")
        print("\n")'''
    
import PySimpleGUI as sg

class TelaItemCardapio(Tela):
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
    sg.ChangeLookAndFeel('TealMono')
    layout = [
      [sg.Text('-------- ITENS DO CARDÁPIO ----------', font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio('Incluir Item', "RD1", key='1')],
      [sg.Radio('Alterar Item', "RD1", key='2')],
      [sg.Radio('Excluir Item', "RD1", key='3')],
      [sg.Radio('Listar Itens', "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
    self.__window = sg.Window('Sistema de restaurante').Layout(layout)

  def pega_dados_item_cardapio(self):
    sg.ChangeLookAndFeel('TealMono')
    while True:
      try:
        layout = [
          [sg.Text('-------- DADOS ITEM CARDÁPIO ----------', font=("Helvica", 25))],
          [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
          [sg.Text('Descrição:', size=(15, 1)), sg.InputText('', key='descricao')],
          [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo_item')],
          [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
          [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()
        nome = str(values['nome'])
        descricao = str(values['descricao'])
        codigo_item = int(values['codigo_item'])
        preco = float(values['preco'])
        if ((self.checa_valor(nome) == True) or
                  (self.checa_valor(descricao) == True) or
                  not isinstance(codigo_item, int) or
                  not isinstance(preco, float)):
             raise ValueError

        self.close()
        return {"nome": nome.upper(), "descricao": descricao.upper(), "codigo_item": codigo_item, "preco": preco}
      except ValueError:
        sg.Popup("Dados incorretos, utilize apenas números positivos em código e preço e letras em nome e descrição!", title = "ERRO")
        self.close()


  def mostra_item_cardapio(self, dados_item):
    try:
      string_todos_itens = ""
      for dado in dados_item:
        string_todos_itens = string_todos_itens + "NOME DO ITEM: " + dado["nome"] + '\n'
        string_todos_itens = string_todos_itens + "DESCRIÇÃO DO ITEM: " + dado["descricao"] + '\n'
        string_todos_itens = string_todos_itens + "CÓDIGO DO ITEM: " + str(dado["codigo_item"]) + '\n'
        string_todos_itens = string_todos_itens + "PREÇO DO ITEM: " + str(dado["preco"]) + '\n\n'

      sg.Popup('-------- LISTA DE ITENS ----------', string_todos_itens)
    except KeyError as e:
      sg.Popup("Erro ao exibir dados do cardápio: ", str(e))


  def mostra_item_cardapio_formatado(self, dados_item):
    try:
      string_todos_itens = ""
      for dado in dados_item:
          item_info = "{} - {} - {} - R$ {:.2f}".format(dado["codigo_item"], dado["nome"], dado["descricao"], float(dado["preco"]))
          string_todos_itens += item_info + '\n'

      sg.Popup('-------- LISTA DE ITENS CARDÁPIO ----------', string_todos_itens)
    except KeyError as e:
      sg.Popup("Erro ao exibir dados do cardápio: ", str(e))


  def seleciona_item(self):
    sg.ChangeLookAndFeel('TealMono')
    while True:
      try:
        layout = [
          [sg.Text('-------- SELECIONAR ITEM ----------', font=("Helvica", 25))],
          [sg.Text('Digite o código do Item que deseja selecionar:', font=("Helvica", 15))],
          [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
          [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona item').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        if not isinstance(codigo, int):
          raise ValueError
        self.close()
        return codigo
      except ValueError:
        sg.Popup("Código do item inválido. O código deve ser um valor inteiro.", title = "ERRO")
        self.close()

  def mostra_mensagem(self, msg):
    sg.popup("", msg)

  def close(self):
    self.__window.Close()

  def open(self):
    button, values = self.__window.Read()
    return button, values