from No import No

class Lista:
  def __init__(self):
    self.inicio = None
    self.tamanho = 0

  def __len__(self):
    return self.tamanho

  def __str__(self):

    if self.inicio:
      retorno = ""
      no_auxiliar = self.inicio
      retorno += "\033[96m{}\033[00m - {}\n".format(no_auxiliar.dado, no_auxiliar.proximo)

      while( no_auxiliar.proximo ):
        retorno += "\033[96m{}\033[00m\n".format(no_auxiliar.dado)
        no_auxiliar = no_auxiliar.proximo

      return retorno

    else:
      return "Lista vazia"

  def adicionar(self, valor):
    '''
    Adiciona um valor ao fim da lista
    '''
    if self.inicio:
      no_auxiliar = self.inicio
      while( no_auxiliar.proximo ):
        no_auxiliar = no_auxiliar.proximo
      no_auxiliar.proximo = No(valor)

    else:
      self.inicio = No(valor)

    self.tamanho += 1