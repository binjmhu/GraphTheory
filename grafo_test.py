import unittest
from meu_grafo import *
from bibgrafo.grafo_exceptions import *


class TestGrafo(unittest.TestCase):

    def setUp(self):

        self.g_t1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_t1.adicionaAresta('a1', 'A', 'B')
        self.g_t1.adicionaAresta('a2', 'A', 'G')
        self.g_t1.adicionaAresta('a3', 'A', 'J')
        self.g_t1.adicionaAresta('a4', 'K', 'G')
        self.g_t1.adicionaAresta('a5', 'K', 'J')
        self.g_t1.adicionaAresta('a6', 'J', 'G')
        self.g_t1.adicionaAresta('a7', 'J', 'I')
        self.g_t1.adicionaAresta('a8', 'I', 'G')
        self.g_t1.adicionaAresta('a9', 'G', 'H')
        self.g_t1.adicionaAresta('a10', 'H', 'F')
        self.g_t1.adicionaAresta('a11', 'F', 'B')
        self.g_t1.adicionaAresta('a12', 'B', 'G')
        self.g_t1.adicionaAresta('a13', 'B', 'C')
        self.g_t1.adicionaAresta('a14', 'C', 'D')
        self.g_t1.adicionaAresta('a15', 'D', 'E')
        self.g_t1.adicionaAresta('a16', 'D', 'B')
        self.g_t1.adicionaAresta('a17', 'E', 'B')

        self.g_rd1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_rd1.adicionaAresta('a1', 'A', 'B')
        self.g_rd1.adicionaAresta('a4', 'K', 'G')
        self.g_rd1.adicionaAresta('a5', 'K', 'J')
        self.g_rd1.adicionaAresta('a7', 'J', 'I')
        self.g_rd1.adicionaAresta('a9', 'G', 'H')
        self.g_rd1.adicionaAresta('a10', 'H', 'F')
        self.g_rd1.adicionaAresta('a11', 'F', 'B')
        self.g_rd1.adicionaAresta('a14', 'C', 'D')
        self.g_rd1.adicionaAresta('a15', 'D', 'E')
        self.g_rd1.adicionaAresta('a17', 'E', 'B')

        self.g_rb1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_rb1.adicionaAresta('a1', 'A', 'B')
        self.g_rb1.adicionaAresta('a2', 'A', 'G')
        self.g_rb1.adicionaAresta('a3', 'A', 'J')
        self.g_rb1.adicionaAresta('a4', 'K', 'G')
        self.g_rb1.adicionaAresta('a8', 'I', 'G')
        self.g_rb1.adicionaAresta('a9', 'G', 'H')
        self.g_rb1.adicionaAresta('a11', 'F', 'B')
        self.g_rb1.adicionaAresta('a13', 'B', 'C')
        self.g_rb1.adicionaAresta('a16', 'D', 'B')
        self.g_rb1.adicionaAresta('a17', 'E', 'B')

        self.g_r2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_r2.adicionaAresta('a2', 'A', 'B')

        self.g_rd2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_rd2.adicionaAresta('a1', 'J', 'C')
        self.g_rd2.adicionaAresta('a2', 'C', 'E')
        self.g_rd2.adicionaAresta('a4', 'P', 'C')
        self.g_rd2.adicionaAresta('a6', 'T', 'C')
        self.g_rd2.adicionaAresta('a8', 'M', 'T')
        self.g_rd2.adicionaAresta('a9', 'T', 'Z')

        self.g_rb2 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_rb2.adicionaAresta('a1', 'J', 'C')
        self.g_rb2.adicionaAresta('a2', 'C', 'E')
        self.g_rb2.adicionaAresta('a4', 'P', 'C')
        self.g_rb2.adicionaAresta('a6', 'T', 'C')
        self.g_rb2.adicionaAresta('a7', 'M', 'C')
        self.g_rb2.adicionaAresta('a9', 'T', 'Z')

    def teste_dfs(self):
        self.assertTrue(self.g_t1.dfs("A"), self.g_rd1)
        self.assertTrue(self.g_t1.dfs("A"), self.g_r2)
        self.assertTrue(self.g_t1.dfs("J"), self.g_rd2)

    def teste_bfs(self):
        self.assertTrue(self.g_t1.bfs("A"), self.g_rb1)
        self.assertTrue(self.g_t1.bfs("A"), self.g_r2)
        self.assertTrue(self.g_t1.bfs("J"), self.g_rb2)
