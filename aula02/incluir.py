from aula02.montadora_dao import Montadora, MontadoraDAO

m = Montadora()
print('Informe os dados da nova montadora de veículos')
m.sgl_montadora = input('Qual a Sigla? ')
m.nme_montadora = input('Qual o Nome? ')

dao = MontadoraDAO()
dao.inserir(m)
print('Montadora inserida com ID:', m.idt_montadora)
