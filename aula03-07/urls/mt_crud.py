from flask import Blueprint, render_template, request
from aula03a07.dao.montadora_dao import Montadora, MontadoraDAO

bp_mt = Blueprint('mt', __name__)


@bp_mt.route('/form_create')
def form_create():
    return render_template('/mt/form_create.html', msg="", display="none")


@bp_mt.route('/create', methods=['POST'])
def create():
    # Preencher com dados de montadora vindos do formulário
    m = Montadora()
    m.sgl_montadora = request.form['sgl_montadora']
    m.nme_montadora = request.form['nme_montadora']

    # Salvando a nova montadora
    dao = MontadoraDAO()
    dao.inserir(m)
    if m.idt_montadora is None:
        msg = 'Erro ao inserir montadora. Procure o administrador do sistema'
    else:
        msg = f'Montadora número {m.idt_montadora} inserida com sucesso.'

    return render_template('/mt/form_create.html', msg=msg, display="block")


@bp_mt.route('/read')
def read():
    # Buscar as montadoras para listar em uma tabela
    dao = MontadoraDAO()
    lst = dao.selecionar_tudo()
    if not lst:
        msg = 'Não há montadoras na base de dados.'
    else:
        msg = f'Listadas {len(lst)} montadoras da base de dados.'

    return render_template('/mt/read.html', msg=msg, lst=lst)
