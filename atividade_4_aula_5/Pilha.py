from No import No

class Pilha:

  def __init__(self):
    self.ultima = None
    self.tamanho = 0

  def push(self, valor):
    no = No(valor, self.ultima)
    self.ultima = no
    self.tamanho += 1

  def pop(self):
    if self.ultima:
      no = self.ultima
      self.ultima = no.anterior
      self.tamanho -= 1
      return no.valor
    return None

  # Firulas

  def __len__(self):
    return self.tamanho

  def __str__(self):
    if self.ultima:
      retorno = ""
      no = self.ultima

      retorno += "[{}]".format(no.valor)

      while no.anterior:
        no = no.anterior
        retorno += "[{}]".format(no.valor)

      return retorno

    else:

      return "Pilha vazia"

