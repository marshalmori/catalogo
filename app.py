from flask import (Flask, render_template, request, redirect, url_for,
                   jsonify, abort, g, flash)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

# # USUÁRIO - User
# Requisição de todos os usuários  - getAllUsers()
# curl -u marshalmori@gmail.com:1234 -X GET http://localhost:5000/user/api
# Cadastro de um novo usuário padrão via API - newUserApi()
# curl -i -X POST -H "Content-Type: application/json" -d '{"username":"Marshal","email": "marshalmori@gmail.com", "password":"1234", "picture":"/home/marshal"}' http://localhost:5000/user/api
# Cadastro de um segundo usuário padrão via API - newUserApi()
# curl -i -X POST -H "Content-Type: application/json" -d '{"username":"Tsukuru","email": "tsukuru@gmail.com", "password":"tsukuru", "picture":"/home/tsukuru"}' http://localhost:5000/user/api
# Faz a requisição das informações de um usuário específico- getUser(user_id)
# curl -u marshalmori@gmail.com:1234 -i -X GET http://localhost:5000/user/api/11
# Faz update do username e picture do usuário - updateUser(user_id)
# curl -u tsukuru@gmail.com:tsukuru -i -X PUT -H "Content-Type: application/json" -d '{"username":"Tasaki", "picture":"/home/tasaki"}' http://localhost:5000/user/api/12
# Faz o delete de um usuário
# curl -u tsukuru@gmail.com:tsukuru -i -X DELETE http://localhost:5000/user/api/12

# CATEGORIA - Category
# Requisição de todas as categorias - getAllCategories()
# curl -u marshalmori@gmail.com:1234 -X GET http://localhost:5000/category/api
# Cria uma nova categoria
# curl -u marshalmori@gmail.com:1234 -i -X POST -H "Content-Type: application/json" -d '{"category_name":"Outra Categoria", "category_description":"Uma descrição qualquer aqui"}' http://localhost:5000/category/api/12
# Faz a requisição de uma categoria específica - getCategory(category_id)
# curl -u marshalmori@gmail.com:1234 http://localhost:5000/category/api/1
# Faz update na categoria e na descrição da categoria - updateCategory(category_id)
# curl -u marshalmori@gmail.com:1234 -X PUT -H "Content-Type: application/json" -d '{"category_name":"Tasaki", "category_description":"Categoria alterada para Tasaki"}' http://localhost:5000/category/api/12
# Deleta uma categoria - delCategory(category_id)
# curl -u marshalmori@gmail.com:1234 -i -X DELETE http://localhost:5000/category/api/12

# ITEM - Item
# Requisição de todos os itens
# curl -u marshalmori@gmail.com:1234 -X GET http://localhost:5000/item/api
# Requisiçao de todos os itens de uma determinada categoria
# curl -u marshalmori@gmail.com:1234 -X POST http://localhost:5000/item/api/1
# Update de um item específico - updateItem(item_id)
# curl -u marshalmori@gmail.com:1234 -X PUT -H "Content-Type: application/json" -d '{"item_name":"Tasaki", "item_long_description":"CCCCCCCCCCCCCC CCCCCCCC CCCCCCCCC CCCCCCCCCCCCCCCC CCCCCCCCCCCC CCCCCCCCCC", "item_short_description":"CCCCCC CCCCCC CCCCC CCC", "price":"70.00"}' http://localhost:5000/item/api/1
# Exclui um item específico
# curl -u marshalmori@gmail.com:1234 -X DELETE http://localhost:5000/item/api/1

app = Flask(__name__)

engine = create_engine('sqlite:///catalogo.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@auth.verify_password
def verify_password(email, password):
    user = session.query(User).filter_by(email = email).first()
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True

# ======== Start API Endpoint ===================
@app.route('/user/api', methods=['GET'])
@auth.login_required
def getAllUsers():
    users = session.query(User).all()
    return jsonify(Users=[i.serialize for i in users])

@app.route('/user/api', methods=['POST'])
def newUserApi():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    picture = request.json.get('picture')
    if email is None or password is None:
        print('Faltando argumentos: password/senha')
        abort(400)
    if session.query(User).filter_by(email = email).first() is not None:
        print('E-mail já cadastrado.')
        user = session.query(User).filter_by(email = email).first()
        return jsonify({'message': 'Usuário já cadastrado'}), 200
    user = User(username = username, email = email, picture = picture)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({'username': user.username,
                    'email': user.email,
                    'picture': user.picture}), 201

@app.route('/user/api/<int:user_id>', methods=['GET'])
@auth.login_required
def getUser(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    if not user:
        abort(400)
    return jsonify({'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'picture': user.picture})

@app.route('/user/api/<int:user_id>', methods=['PUT'])
@auth.login_required
def updateUser(user_id):
    username = request.json.get('username')
    picture = request.json.get('picture')
    updatedUser = session.query(User).filter_by(id = user_id).one()
    if username:
        updatedUser.username = username
    if picture:
        updatedUser.picture = picture
    session.add(updatedUser)
    session.commit()
    return 'Usuário de id: %s atualizado com sucesso' % user_id

@app.route('/user/api/<int:user_id>', methods=['DELETE'])
@auth.login_required
def deleteUser(user_id):
    deletedUser = session.query(User).filter_by(id=user_id).one()
    session.delete(deletedUser)
    session.commit()
    return 'Usuário de id: %s foi excluido com sucesso.' % user_id

@app.route('/category/api', methods=['GET'])
@auth.login_required
def getAllCategories():
    categories = session.query(Category).all()
    return jsonify(Categories=[i.serialize for i in categories])

@app.route('/category/api/<int:user_id>', methods=['POST'])
@auth.login_required
def makeNewCategory(user_id):
    category_name = request.json.get('category_name')
    category_description = request.json.get('category_description')
    category = Category(category_name = category_name,
                        category_description = category_description,
                        user_id = user_id)
    session.add(category)
    session.commit()
    return jsonify({'category_name': category.category_name,
                    'category_description': category.category_description,
                    'user_id': category.user_id})

@app.route('/category/api/<int:category_id>', methods=['GET'])
@auth.login_required
def getCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    return jsonify(Category=category.serialize)

@app.route('/category/api/<int:category_id>', methods=['PUT'])
@auth.login_required
def updateCategory(category_id):
    category_name = request.json.get('category_name')
    category_description = request.json.get('category_description')
    category = session.query(Category).filter_by(id = category_id).one()
    if category_name:
        category.category_name = category_name
    if category_description:
        category.category_description = category_description
    session.add(category)
    session.commit()
    return jsonify({'category_name': category.category_name,
                    'category_description': category.category_description})

@app.route('/category/api/<int:category_id>', methods=['DELETE'])
@auth.login_required
def delCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id = category_id).one()
    session.delete(deletedCategory)
    session.commit()
    return 'Categoria de id: %s excluída com sucesso' % category_id

@app.route('/item/api', methods=['GET'])
@auth.login_required
def getAllItems():
    items = session.query(Item).all()
    return jsonify(Items=[i.serialize for i in items])

@app.route('/item/api/<int:category_id>', methods=['POST'])
@auth.login_required
def getItems(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category.id).all()
    return jsonify(Items=[i.serialize for i in items])

@app.route('/item/api/<int:item_id>', methods=['PUT'])
@auth.login_required
def updateItem(item_id):
    item = session.query(Item).filter_by(id = item_id).one()
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

@app.route('/item/api/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delItem(item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    session.delete(item)
    session.commit()
    return 'O item com o id %s foi excluído com sucesso.' %item_id

# ======== End API Endpoint ===================

# Aqui tem que mudar de /category/login para somente /login
@app.route('/category/login')
def login():
    return render_template('login.html')

# @app.route('/users', methods = ['POST'])
# def newUser():
#     email = request.form['email']
#     password = request.form['password']


@app.route('/')
@app.route('/category/')
def showCategory():
    categories = session.query(Category).all()
    return render_template('category/show_category.html', categories=categories)

@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        new_category = Category(category_name=request.form['name'],
                                category_description=request.form['category_description'])
        session.add(new_category)
        session.commit()
        flash('Categoria criada com sucesso!')
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/new_category.html')

@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['category_name']:
            editedCategory.category_name = request.form['category_name']
        if request.form['category_description']:
            editedCategory.category_description = request.form['category_description']
        session.add(editedCategory)
        session.commit()
        flash('Categoria editada com sucesso!')
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/edit_category.html', category_id = category_id, category = editedCategory)

@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(deletedCategory)
        session.commit()
        flash('Categoria excluída com sucesso!')
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/delete_category.html', category_id = category_id, category = deletedCategory)

@app.route('/category/<int:category_id>/item/', methods=['GET', 'POST'])
@app.route('/category/<int:category_id>/', methods=['GET', 'POST'])
def showItem(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category.id)
    return render_template('item/show_item.html', category_id = category_id, categories = categories, category = category, items = items)

@app.route('/category/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    categories = session.query(Category).all()
    if request.method == 'POST':
        newItem = Item(item_name=request.form['name'],
                       price=request.form['price'],
                       item_long_description=request.form['long_description'],
                       item_short_description=request.form['short_description'],
                       category_id = category_id)
        session.add(newItem)
        session.commit()
        flash('Item criado com sucesso!')
        return redirect(url_for('showItem', category_id = category_id))
    else:
        return render_template('item/new_item.html', categories = categories, category_id = category_id)

@app.route('/category/<int:category_id>/item/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    categories = session.query(Category).all()
    editedItem = session.query(Item).filter_by(id = item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.item_name = request.form['name']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['long_description']:
            editedItem.item_long_description = request.form['long_description']
        if request.form['short_description']:
            editedItem.item_short_description = request.form['short_description']
        session.add(editedItem)
        session.commit()
        flash('Item editado com sucesso!')
        return redirect(url_for('showItem', category_id = category_id))
    else:
        return render_template('item/edit_item.html', category_id= category_id, item_id = item_id, categories = categories, items = editedItem)

@app.route('/category/<int:category_id>/item/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    categories = session.query(Category).all()
    deletedItem = session.query(Item).filter_by(id = item_id).one()
    if request.method == 'POST':
        session.delete(deletedItem)
        session.commit()
        flash('Item excluído com sucesso!')
        return redirect(url_for('showItem', category_id = category_id))
    else:
        return render_template('item/delete_item.html', category_id = category_id, item_id = item_id, categories = categories, items=deletedItem)

@app.route('/category/<int:category_id>/item/<int:item_id>/description/', methods=['GET', 'POST'])
def descriptionItem(category_id, item_id):
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template('item/description_item.html', category_id = category_id, categories = categories, item_id = item_id, item = item)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
