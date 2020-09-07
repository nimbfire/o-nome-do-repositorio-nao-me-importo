from No import No

class Lista:

  def __init__(self):
    self.inicio = None
    self.tamanho = 0

  def __len__(self):
    return self.tamanho

  def __str__(self):
    if self.inicio:
      retorno = "\033[96m----------------------------------------------------------------------------------------------------------------------------------------------|\033[00m\n"
      retorno += "\033[96m{: ^34} \033[00m|\033[96m {: ^30s}\033[00m | \033[96m{: ^34s}\033[00m | \033[96m{: ^34s} |\033[00m\n".format('endereço do nó', 'dado','proximo', 'anterior')
      no_auxiliar = self.inicio

      while( no_auxiliar.proximo ):
        retorno += "{}   |\033[96m{:<30}\033[00m  | {} | {}\n".format(no_auxiliar, no_auxiliar.dado , no_auxiliar.proximo, no_auxiliar.anterior)
        no_auxiliar = no_auxiliar.proximo

      retorno += "{}   |\033[96m{:<30}\033[00m  |               {}               | {}\n".format(no_auxiliar, no_auxiliar.dado , no_auxiliar.proximo, no_auxiliar.anterior)
      return retorno

    else:

      return "Lista vazia"

  def adicionar(self, valor):
    '''
    Adiciona um valor ao fim da lista
    '''
    if self.inicio:
      #eh uma lista com valores.
      no_auxiliar = self.inicio
      while( no_auxiliar.proximo ):
        no_auxiliar = no_auxiliar.proximo
      no_auxiliar.proximo = No(valor, no_auxiliar)

    else:
      #eh uma lista vazia
      self.inicio = No(valor, None)

    self.tamanho += 1

  def inserirOrdenado(self, valor):
    '''
    Adicionar um valor na proxima posição ordenada.
    Exemplo, a lista possui[ 1,2,3,10] e se passa o valor 4, ele deve ser aciionado antes do valor 10
    '''
    if self.inicio == None:
      no = No(valor)
      self.inicio = no

    else:
      print('im here')
      anterior = self.inicio

      while anterior:
        proximo = anterior.proximo

        print('while anterior im here')
        print(anterior.dado, ' < ', valor)
        if anterior and anterior.dado < valor:
          if proximo == None:
            no = No(valor)
            no.proximo = anterior.proximo
            anterior.proximo = no
            break
          elif proximo.dado > valor:
            no = No(valor)
            no.proximo = anterior.proximo
            anterior.proximo = no
            break
          else:
            anterior = anterior.proximo
            print("pula pro proximo node    2")
          

        else:
          anterior = anterior.proximo
          print("pula pro proximo node    1 ")
      
    self.tamanho += 1

  def inserir(self, posicao, valor):
    '''
    Adicionar um valor em uma posição específica na lista.
    '''
    if posicao == 0:
      no = No(valor)
      no.proximo = self.inicio
      self.inicio = no
    else:
      anterior = self.inicio
      for i in range( posicao - 1):
        if anterior:
          anterior = anterior.proximo
      no = No(valor)
      no.proximo = anterior.proximo
      anterior.proximo = no
    self.tamanho += 1

  def imprimir(self):
    aux = self.inicio
    while (aux):
      print(aux.dado, '\n')
      aux = aux.proximo

  def excluir(self, valor):
    '''
    Exclui elemento da lista que possua o valor dado
    '''
    # if self.tamanho == 0:
    #   print("A lista esta vazia")
    #   return false
    # elif self.tamanho == 1:
    #   if self.inicio.dado == valor
    #     self.inicio = None
    #   else:
    #     print("valor não encontrado")
    # else:
    #   aux = inicio



