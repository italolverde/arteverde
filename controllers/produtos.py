from flask import Blueprint, request, render_template, session, url_for, redirect, flash
from flask_login import login_required, current_user
from db.db import TB_categoria, TB_produto, session

bp_produtos = Blueprint('produtos', __name__, url_prefix='/produtos', template_folder='../templates/produtos')

@bp_produtos.route('/novo_produto', methods=['POST','GET'])
def nova_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        categoria_nome = request.form['categoria']
        cat_id = session.query(TB_categoria.id).filter(nome=categoria_nome)
        novo_produto = TB_produto(nome=nome, preco = preco, categoria_id = cat_id)
        session.add(novo_produto)
        session.commit()
        return redirect(url_for('home'))
    return render_template('cadastrocategoria.html')


@bp_produtos.route('/nova_categoria', methods=['POST','GET'])
def nova_cat():
    if request.method == 'POST':
        nome = request.form['nome']
        nova_cat = TB_categoria(nome=nome)
        session.add(nova_cat)
        session.commit()
        return redirect(url_for('home'))
    return render_template('cadastrocategoria.html')