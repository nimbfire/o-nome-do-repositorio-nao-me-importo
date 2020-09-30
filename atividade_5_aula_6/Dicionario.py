
# Construa um algoritmo que peça ao usuário para informar o nome, a
# nota01 e a nota02 de um aluno. Guarde estas informações em um
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02)
# /2] e adicione ao dicionário. Ao final, imprima todos os dados do
# dicionário.

dic = {}

inp = input("Digite o nome do usuario:")
dic["nome"] = inp
inp = input("Digite a nota 01 do usuario:")
dic["nota01"] = inp
inp = input("Digite a nota 02 do usuario:")
dic["nota02"] = inp
dic["notaFinal"] = (int(dic["nota02"]) + int(dic["nota01"]))/2

print(dic)