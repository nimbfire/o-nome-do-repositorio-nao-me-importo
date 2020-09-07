from Lista import Lista

print("Cria a lista")
lista = Lista()

print("\n================== \nTesta funções de print antes de preencher a lista")
print("Print de debug:")
print(lista)
print("Print normal:")
lista.print()
print("Print reverso:")
lista.printReverso()
print("\n")

print("Preenchendo a lista...")

lista.adicionar(10)
lista.adicionar(1)
lista.adicionar(30)
lista.adicionar(1330)
lista.adicionar('a')

print("\n================== \nTesta funções de print depois de preencher a lista")
print("Print de debug:")
print(lista)
print("Print normal:")
lista.print()
print("Print reverso:")
lista.printReverso()
