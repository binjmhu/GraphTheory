from meu_grafo import *

paraiba = MeuGrafo(['J', 'E', 'C', "T", "P", "M", "K"])

paraiba.adicionaAresta('1', 'J', 'C')
paraiba.adicionaAresta('2', 'C', 'E')
paraiba.adicionaAresta('3', 'C', 'E')
paraiba.adicionaAresta('4', 'E', 'T')
paraiba.adicionaAresta("5", 'C', "P")
paraiba.adicionaAresta("6", 'C', "M")
paraiba.adicionaAresta("7", "P", "M")
paraiba.adicionaAresta("8", "P", "K")

# print(paraiba.vertices_adjacentes("C"))
print(paraiba.dfs("K"))

print(paraiba.dfs("K"))