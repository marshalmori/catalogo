#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import (Flask, render_template, request, redirect, url_for,
                   jsonify, abort, g, flash)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask_httpauth import HTTPBasicAuth
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response
import random
import string
import httplib2
import json
import requests

auth = HTTPBasicAuth()

app = Flask(__name__)

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalogo"

# engine = create_engine(
#                         'sqlite:///catalogo.db',
#                         connect_args={'check_same_thread': False}
#                       )
engine = create_engine('postgresql://catalog:601077@localhost/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Método para verificação do email e senha
# @auth.verify_password
# def verify_password(email, password):
#     user = session.query(User).filter_by(email=email).first()
#     if not user or not user.verify_password(password):
#         return False
#     g.user = user
#     return True

# ======== Início dos métodos da API =============================


# Retorna um JSON com os dados de todos os usuários cadastrados.
@app.route('/user/api/', methods=['GET'])
def getAllUsers():
    users = session.query(User).all()
    return jsonify(Users=[i.serialize for i in users])


# Retorna um JSON com os dados de um usuário específico.
@app.route('/user/api/<int:user_id>', methods=['GET'])
def getUser(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    if not user:
        abort(400)
    return jsonify({'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'picture': user.picture})


# Retorna um JSON com os dados de todas as categorias criadas.
@app.route('/category/api', methods=['GET'])
def getAllCategories():
    categories = session.query(Category).all()
    return jsonify(Categories=[i.serialize for i in categories])


# Método da API para criar uma nova categoria.
@app.route('/category/api/<int:user_id>', methods=['POST'])
def makeNewCategory(user_id):
    category_name = request.json.get('category_name')
    category_description = request.json.get('category_description')
    category = Category(category_name=category_name,
                        category_description=category_description,
                        user_id=user_id)
    session.add(category)
    session.commit()
    return jsonify({'category_name': category.category_name,
                    'category_description': category.category_description,
                    'user_id': category.user_id})


# Retorna um JSON com os dados de uma categoria específica.
@app.route('/category/api/<int:category_id>', methods=['GET'])
def getCategory(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    return jsonify(Category=category.serialize)


# Método da API para editar uma categoria
@app.route('/category/api/<int:category_id>', methods=['PUT'])
def updateCategory(category_id):
    category_name = request.json.get('category_name')
    category_description = request.json.get('category_description')
    category = session.query(Category).filter_by(id=category_id).one()
    if category_name:
        category.category_name = category_name
    if category_description:
        category.category_description = category_description
    session.add(category)
    session.commit()
    return jsonify({'category_name': category.category_name,
                    'category_description': category.category_description})


# Método da API para deleter uma categoria.
@app.route('/category/api/<int:category_id>', methods=['DELETE'])
def delCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id=category_id).one()
    session.delete(deletedCategory)
    session.commit()
    return 'Categoria de id: %s excluída com sucesso' % category_id


# Retorna um JSON com todos os itens das categorias.
@app.route('/item/api', methods=['GET'])
def getAllItems():
    items = session.query(Item).all()
    return jsonify(Items=[i.serialize for i in items])


# Retorna um JSON com os itens de uma categoria específica.
@app.route('/item/api/<int:category_id>', methods=['POST'])
def getItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id).all()
    return jsonify(Items=[i.serialize for i in items])


# Método da API para editar um item de uma categoria.
@app.route('/item/api/<int:item_id>', methods=['PUT'])
def updateItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    item_name = request.json.get('item_name')
    item_long_description = request.json.get('item_long_description')
    item_short_description = request.json.get('item_short_description')
    price = request.json.get('price')
    if item_name:
        item.item_name = item_name
    if item_long_description:
        item.item_long_description = item_long_description
    if item_short_description:
        item.item_short_description = item_short_description
    if price:
        item.price = price
    session.add(item)
    session.commit()
    return jsonify({'item_name': item.item_name,
                    'item_long_description': item.item_long_description,
                    'item_short_description': item.item_short_description,
                    'price': item.price})


# Método da API para excluir um item de uma categoria.
@app.route('/item/api/<int:item_id>', methods=['DELETE'])
def delItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    session.delete(item)
    session.commit()
    return 'O item com o id %s foi excluído com sucesso.' % item_id

# ======== Fim dos Métodos da API =================================


# Cria um state token antifraude e renderiza a página de Login.
@app.route('/login')
def showLogin():
    state = ''.join(
                    random.choice(
                        string.ascii_uppercase + string.digits
                    )
                    for x in range(32)
                    )
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Faz o Logout do usuário.
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash('Você não está mais logado.')
        return redirect(url_for('showCategory'))
    else:
        flash('Você ainda não está logado.')
        return redirect(url_for('showCategory'))


# Faz a conexação do usuário utilizando a conta do Google.
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    # result = json.loads(h.request(url, 'GET')[1])
    result = json.loads(h.request(url, 'GET')[1].decode('utf-8'))
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
                                json.dumps(
                                    'Current user is already connected.'
                                          ),
                                    200
                                          )
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Seja bem vindo ao CATÁLOGO, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ''' " style = "width: 100px;
                    height: 100px;
                    border-radius: 150px;
                    -webkit-border-radius: 150px;
                    -moz-border-radius: 150px;">'''
    flash("%s - Login efetuado com sucesso" % login_session['username'])
    return output


# Desconecta o usuário que estava conectado com a conta do Google.
@app.route('/gdisconnect/')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(
            json.dumps(
                'Failed to revoke token for given user.'
                    ),
                400
                    )
        response.headers['Content-Type'] = 'application/json'
        return response


# Cria novo usuário que se cadastra utilizando a conta do Google
def createUser(login_session):
    newUser = User(username=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# Retorna as informações do usuário que se cadastrou com a conta do Google
def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one_or_none()
    return user


# Retorna o id do usuário caso esteja cadastrado, senão retorna None
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


# Apresenta as categorias criadas.
@app.route('/')
@app.route('/category/')
def showCategory():
    categories = session.query(Category).all()
    if 'username' not in login_session:
        return render_template(
                                'category/public_category.html',
                                categories=categories)
    else:
        return render_template(
                                'category/show_category.html',
                                categories=categories)


# Cria uma nova categoria.
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if request.method == 'POST':
        new_category = Category(
                    category_name=request.form['name'],
                    category_description=request.form['category_description'],
                    user_id=login_session['user_id'])
        session.add(new_category)
        session.commit()
        flash('Categoria CRIADA com sucesso!')
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/new_category.html')


# Faz a edição de uma categoria.
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if editedCategory.user_id != login_session['user_id']:
        flash(
                'Você não tem autorização para EDITAR a categoria %s.'
                % editedCategory.category_name)
        return redirect(url_for('showCategory'))
    if request.method == 'POST':
        if request.form['category_name']:
            editedCategory.category_name = request.form['category_name']
        if request.form['category_description']:
            editedCategory.category_description = request.form[
                                                        'category_description'
                                                              ]
        session.add(editedCategory)
        session.commit()
        flash('Categoria EDITADA com sucesso!')
        return redirect(url_for('showCategory'))
    else:
        return render_template(
                                'category/edit_category.html',
                                category_id=category_id,
                                category=editedCategory)


# Exclui uma categoria específica.
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if deletedCategory.user_id != login_session['user_id']:
        flash(
                'Você não tem autorização para EXCLUIR a categoria %s.'
                % deletedCategory.category_name
             )
        return redirect(url_for('showCategory'))
    if request.method == 'POST':
        session.delete(deletedCategory)
        session.commit()
        flash(
                'A categoria %s foi EXCLUÍDA com sucesso.'
                % deletedCategory.category_name
             )
        return redirect(url_for('showCategory'))
    else:
        return render_template(
                                'category/delete_category.html',
                                category_id=category_id,
                                category=deletedCategory)


# Mostra os itens de uma categoria
@app.route('/category/<int:category_id>/item/', methods=['GET', 'POST'])
@app.route('/category/<int:category_id>/', methods=['GET', 'POST'])
def showItem(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id)
    creator = getUserInfo(category.user_id)
    if 'username' not in login_session:
        return render_template(
                                'item/public_item.html',
                                category_id=category_id,
                                categories=categories,
                                category=category,
                                items=items,
                                creator=creator)
    else:
        return render_template(
                                'item/show_item.html',
                                category_id=category_id,
                                categories=categories,
                                category=category,
                                items=items,
                                creator=creator)


#  Cria um novo item em uma categoria
@app.route('/category/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if login_session['user_id'] != category.user_id:
        flash(
                'Você não tem autorização para CRIAR um item na categoria %s.'
                % category.category_name
             )
        return redirect(url_for('showItem', category_id=category_id))
    if request.method == 'POST':
        newItem = Item(item_name=request.form['name'],
                       price=request.form['price'],
                       item_long_description=request.form['long_description'],
                       item_short_description=request.form[
                                                            'short_description'
                                                          ],
                       category_id=category_id,
                       user_id=category.user_id)
        session.add(newItem)
        session.commit()
        flash('O item %s foi CRIADO com sucesso.' % newItem.item_name)
        return redirect(url_for(
                                'showItem',
                                category_id=category_id))
    else:
        return render_template(
                                'item/new_item.html',
                                categories=categories,
                                category_id=category_id)


# Edita um item de um categoria
@app.route(
            '/category/<int:category_id>/item/<int:item_id>/edit/',
            methods=['GET', 'POST']
          )
def editItem(category_id, item_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if login_session['user_id'] != category.user_id:
        flash(
                'Você não tem autorização para EDITAR o item %s.'
                % editedItem.item_name
             )
        return redirect(url_for('showItem', category_id=category_id))
    if request.method == 'POST':
        if request.form['name']:
            editedItem.item_name = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['long_description']:
            editedItem.item_long_description = request.form['long_description']
        if request.form['short_description']:
            editedItem.item_short_description = request.form[
                                                            'short_description'
                                                            ]
        session.add(editedItem)
        session.commit()
        flash('O item %s foi EDITADO com sucesso!' % editedItem.item_name)
        return redirect(url_for(
                                'showItem',
                                category_id=category_id))
    else:
        return render_template(
                                'item/edit_item.html',
                                category_id=category_id,
                                item_id=item_id,
                                categories=categories,
                                items=editedItem)


# Deleta um item de uma categoria
@app.route(
            '/category/<int:category_id>/item/<int:item_id>/delete/',
            methods=['GET', 'POST']
          )
def deleteItem(category_id, item_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    deletedItem = session.query(Item).filter_by(id=item_id).one()
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    if login_session['user_id'] != category.user_id:
        flash(
                'Você não tem autorização para EXCLUIR o item %s.'
                % deletedItem.item_name
             )
        return redirect(url_for('showItem', category_id=category_id))
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash('Item EXCLUÍDO com sucesso!')
        return redirect(url_for('showItem', category_id=category_id))
    else:
        return render_template(
                                'item/delete_item.html',
                                category_id=category_id,
                                item_id=item_id,
                                categories=categories,
                                items=deletedItem)


# Mostra um item com maiores detalhes
@app.route(
            '/category/<int:category_id>/item/<int:item_id>/description',
            methods=['GET', 'POST']
          )
def descriptionItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template(
                            'item/description_item.html',
                            category_id=category_id,
                            categories=categories,
                            item_id=item_id,
                            item=item)


if __name__ == '__main__':
    # app.secret_key = 'super_secret_key'
    # app.debug = True
    app.run(host='0.0.0.0', port=5000)
