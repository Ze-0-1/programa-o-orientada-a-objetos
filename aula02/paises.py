# Classe que representa um pais
class Pais:
    def __init__(self):
        print('Objeto criado com sucesso')
        self.nome = ''
        self.populacao = 0

    def __del__(self):
        print('Objeto deletado com sucesso')

    def __str__(self):
        print('Você mandou me imprimir')
        return f"Pais: {self.nome} com população de {self.populacao}"

# Programa principal
if __name__ == '__main__':
   brasil = Pais()
   brasil.nome = 'Brasil'
   brasil.populacao = 220000000
   print(brasil)
   india = Pais()
   india.nome = 'India'
   india.populacao = 1417492000
   print(india)
