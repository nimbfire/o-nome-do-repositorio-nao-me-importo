# Construir um algoritmo de contenha 3 listas:
#  - Nomes de produtos
#  - Preços de cada produto
#  - Quantidades de cada produto

# Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos da lista


produtos = ['Xis', 'Torrada', 'Coca-cola']
precos = [12.00, 9.50, 6.00]
quantidades = [20, 20, 567]

def printProduto(i):
  print(produtos[i] + ' - R$:' + str(precos[i]) + ' qnt:' + str(quantidades[i]))

def removeProduto(i):
  produtos.pop(i)
  precos.pop(i)
  quantidades.pop(i)

printProduto(0)
printProduto(1)
printProduto(2)

print("Removendo um produto (a torrada)")

removeProduto(1)
printProduto(0)
printProduto(1)

