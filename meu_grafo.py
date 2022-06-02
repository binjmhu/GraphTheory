from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import deque


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_adjacentes(self, V=""):

        adjacentes = []

        # percorrendo todas as arestas do grafo
        for aresta in self.A:

            # se o V1 da aresta for o vertice atual, o V2 é adjacente
            if self.A[aresta].getV1() == V:
                adjacentes.append(self.A[aresta].getV2())
            # se o V2 da aresta for o vertice atual, o V1 é adjacente
            elif self.A[aresta].getV2() == V:
                adjacentes.append(self.A[aresta].getV1())

        return adjacentes

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo. O conjunto terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto com os pares de vértices não adjacentes
        '''

        # um conjunto para armazenar os vertices nao adjacentes
        nao_adjacentes = set()

        # percorrendo todos os vertices do grafo
        for no1 in self.N:

            # uma lista para armazenar os vertices adjacentes
            adjacentes = []

            # percorrendo todas as arestas do grafo
            for aresta in self.A:

                # se o V1 da aresta for o vertice atual, o V2 é adjacente
                if self.A[aresta].getV1() == no1:
                    adjacentes.append(self.A[aresta].getV2())
                # se o V2 da aresta for o vertice atual, o V1 é adjacente
                elif self.A[aresta].getV2() == no1:
                    adjacentes.append(self.A[aresta].getV1())

            # percorrendo todos os vertices novamente
            for no2 in self.N:

                # verifica se nao é um laço adicionado, e verifica se esse vertice nao é adjacente...
                # ... para poder adicionar no conjunto de nao adjacentes
                if no1 != no2 and no2 not in adjacentes:

                    # cria-se uma string no padrao "X-Y"
                    aresta1 = f'{no1}-{no2}'
                    aresta2 = f'{no2}-{no1}'

                    # verifica se os vertices ja estao no conjunto, tanto "X-Y" como o "Y-X"...
                    # ... para evitar redundancias
                    if aresta1 not in nao_adjacentes and aresta2 not in nao_adjacentes:
                        nao_adjacentes.add(aresta1)

            # limpa a lista para a proxima iteracao
            adjacentes = []

        return nao_adjacentes

    def ha_laco(self):

        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        # percorre todas as arestas do grafo
        for aresta in self.A:

            # verifica se o V1 é igual ao V2
            if self.A[aresta].getV1() == self.A[aresta].getV2():
                return True

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        # se o vértice não existir, lança uma exceção
        if V not in self.N:
            raise VerticeInvalidoException("O vértice \"" + V + "\" não existe")
        grau = 0

        # pega todas as arestas
        for a in self.A:
            # compara os vertices das arestas com V individualmente
            if self.A[a].getV1() == V:
                grau += 1
            if self.A[a].getV2() == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

        # na implementação eu irei comparar uma aresta com as demais sucessivamente

        # primeira coluna de arestas
        for a in self.A:
            paralelas = 0
            # segunda coluna de arestas
            for b in self.A:
                # se a junção de V1 + V2 de "a" for igual a V1 + V2 de "b", então é paralela
                # vale tanto para V1 + V2 como V2 + V1
                if (self.A[a].getV1() + self.A[a].getV2()) == (self.A[b].getV1() + self.A[b].getV2()) or (
                        self.A[a].getV2() + self.A[a].getV1()) == (self.A[b].getV1() + self.A[b].getV2()):
                    paralelas += 1
                if paralelas >= 2:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        # se o vertice nao existir, lança uma exceção
        if V not in self.N:
            raise VerticeInvalidoException("O vértice \"" + V + "\" não existe")

        arestas = set()

        # passando por cada aresta
        for a in self.A:
            # verifica se o seu V1 ou V2 sao o vertice passado e adiciona seu nome no conjunto
            if self.A[a].getV1() == V or self.A[a].getV2() == V:
                arestas.add(self.A[a].rotulo)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        # grafos completos nao ha laços nem paralelas

        # se houver laço ja retorna False
        if self.ha_laco():
            return False

        # se houver paralelas ja retorna False
        if self.ha_paralelas():
            return False

        # para cada vertice do grafo, verifica se seu grau é igual ao num. de vertices - 1
        for no in self.N:
            if self.grau(no) != len(self.N) - 1:
                return False

        return True

    def adj(self):

        adjacentes = []

        for v in self.N:
            for a in self.A:
                if self.A[a].v2 == v and (
                        not adjacentes.count(f'{self.A[a].v1}-{self.A[a].rotulo}-{v}') and not adjacentes.count(
                    f'{v}-{self.A[a].rotulo}-{self.A[a].v1}')):
                    adjacentes.append(f'{self.A[a].v1}-{self.A[a].rotulo}-{v}')

                elif self.A[a].v1 == v and (
                        not adjacentes.count(f'{self.A[a].v2}-{self.A[a].rotulo}-{v}') and not adjacentes.count(
                    f'{v}-{self.A[a].rotulo}-{self.A[a].v2}')):
                    adjacentes.append(f'{v}-{self.A[a].rotulo}-{self.A[a].v2}')

        return adjacentes

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass

    def dfs(self, V=""):

        # se o vertice nao existir, lança uma exceção
        if V not in self.N:
            raise VerticeInvalidoException("O vértice " + V + " não existe")

        visitado = []

        grafo = MeuGrafo(self.N[::])

        self.dfsAux(visitado, grafo, V)

        arestas = set()

        for a in grafo.A:
            arestas.add(a)

        return grafo

    def dfsAux(self, visitado, grafo, V=""):

        '''
        Função recursiva auxiliar para o dfs
        :param visitado: Lista para armazenar vertices visitados
        :param grafo: Grafo resultante
        :param V: Vertice analisado
        :return: None
        '''

        for a in self.arestas_sobre_vertice(V):

            v1 = self.A[a].getV1()
            v2 = self.A[a].getV2()

            visitado.append(V)

            if V == v1 or V == v2:

                if V == v1: analisando = v2
                else: analisando = v1

                if analisando not in visitado and a not in grafo.A:
                    visitado.append(analisando)
                    grafo.adicionaAresta(a, V, analisando)
                    self.dfsAux(visitado, grafo, analisando)

    def bfs(self, V=''):
        '''
        Provê um novo grafo após realizar o bfs
        :param V: O vértice raíz
        :return: Uma lista com o grafo bfs
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        grafo = MeuGrafo(self.N[::])

        visitado = []
        fila = []

        visitado.append(V)
        fila.append(V)

        if V not in self.N:
            raise VerticeInvalidoException

        while len(fila):
            for a in self.A:
                v1 = self.A[a].getV1()
                v2 = self.A[a].getV2()
                analisando = fila[0]

                if v1 == analisando or v2 == analisando:

                    if analisando == v1:
                        adjacente = v2
                    else:
                        adjacente = v1

                    if adjacente not in visitado:
                        fila.append(adjacente)
                        visitado.append(adjacente)
                        grafo.adicionaAresta(a, analisando, adjacente)

            fila.pop(0)

        return grafo
