from flask import Blueprint, render_template, request
from aula03a07.dao.modelo_dao import Modelo, ModeloDAO
from aula03a07.dao.montadora_dao import MontadoraDAO

bp_md = Blueprint('md', __name__)


@bp_md.route('/form_create')
def form_create():
    dao = MontadoraDAO()
    lst = dao.selecionar_tudo()
    return render_template('/md/form_create.html', msg="", display="none", lst=lst)


@bp_md.route('/create', methods=['POST'])
def create():
    # Preencher com dados de montadora vindos do formulário
    m = Modelo()
    m.nme_modelo = request.form['nme_modelo']
    m.cod_montadora = request.form['cod_montadora']

    # Salvando a novo Modelo
    dao = ModeloDAO()
    dao.inserir(m)
    if m.idt_modelo is None:
        msg = 'Erro ao inserir modelo. Procure o administrador do sistema'
    else:
        msg = f'Modelo número {m.idt_modelo} inserido com sucesso.'

    # Recarregar montadoras no formulário para novo modelo
    dao = MontadoraDAO()
    lst = dao.selecionar_tudo()

    return render_template('/md/form_create.html', msg=msg, display="block", lst=lst)


@bp_md.route('/read')
def read():
    # Buscar as montadoras para listar em uma tabela
    dao = ModeloDAO()
    lst = dao.selecionar_tudo()

    if not lst:
        msg = 'Não há modelos na base de dados.'
    else:
        msg = f'Listados {len(lst)} modelos da base de dados.'

    return render_template('/md/read.html', msg=msg, lst=lst)
