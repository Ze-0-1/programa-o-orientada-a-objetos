'''
 Mostre todas as montadoras que estão na base de dados
 Pergunte ao usuário qual o ID da montadora que deseja excluir
 Efetivar a exclusão
'''

from aula02.montadora_dao import Montadora, MontadoraDAO

dao = MontadoraDAO()

# Mostrar
lista = dao.selecionar_tudo()
for m in lista:
    print('ID:', m.idt_montadora, ' / ', 'Sigla:', m.sgl_montadora, ' / ', 'Nome:', m.nme_montadora)

# Pergunta
print('-' * 30)
id = int(input('Digite o ID da montadora para excluir? '))

# Exclusão
dao.deletar(id)
