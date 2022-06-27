alfabeto = input().split()
estados = input().split()

tabelaTransicoes = {}
for estado in estados:
      tabelaTransicoes[estado] = {simbolo: ' ' for simbolo in alfabeto}
      #print(tabelaTransicoes[estado])

#quantidade de transições
N = int(input())

for i in range(0, N):
      #estando no estado Ei e lendo o símbolo s
      #chega-se ao estado Ej
      Ei, s, Ej = input().split()
      tabelaTransicoes[Ei][s] = Ej;

estadoInicial = input() 
estadoFinal = input().split() 

#quantidade de cadeias
C = int(input())

resultados = []
for i in range(0, C):
      cadeia = list(input())

      estadoAtual = estadoInicial
      for simbolo in cadeia:
            estadoAtual = tabelaTransicoes[estadoAtual][simbolo]
      
      if estadoAtual in estadoFinal:
            resultados.append('Aceita')
      else:
            resultados.append('Rejeita')

for resultado in resultados:
      print(resultado)      
