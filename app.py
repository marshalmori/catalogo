from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

# Create category with curl
# curl -X POST "http://localhost:5000/category/api?category_name=MARSHAL&category_description=CAVALHEIRO"

app = Flask(__name__)

engine = create_engine('sqlite:///catalogo.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ======== Start API Endpoint ===================
@app.route('/user/api', methods=['GET', 'POST'])
def userFunction():
    if request.method == 'GET':
        return getAllUsers()
    if request.method == 'POST':
        username = request.args.get('username', '')
        email = request.args.get('email', '')
        picture = request.args.get('picture', '')
        return newUser(username, email, picture)

def getAllUsers():
    users = session.query(User).all()
    return jsonify(Users=[i.serialize for i in users])

def newUser(username, email, picture):
    user = User(username = username, email = email, picture = picture)
    session.add(user)
    session.commit()
    return jsonify(User=user.serialize)


@app.route('/user/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def userFunctionId(user_id):
    if request.method == 'GET':
        return getUser(user_id)
    if request.method == 'PUT':
        username = request.args.get('username')
        email = request.args.get('email')
        picture = request.args.get('picture')
        return updateUser(user_id, username, email, picture)
    if request.method == 'DELETE':
        return deleteUser(user_id)

def getUser(user_id):
    user = session.query(User).filter_by(id = user_id).one()
    return jsonify(User=user.serialize)

def updateUser(user_id, username, email, picture):
    updatedUser = session.query(User).filter_by(id = user_id).one()
    if username:
        updatedUser.username = username
    if email:
        updatedUser.email = email
    if picture:
        updatedUser.picture = picture
    session.add(updatedUser)
    session.commit()
    return 'Usuário de id: %s atualizado com sucesso' % user_id

def deleteUser(user_id):
    deletedUser = session.query(User).filter_by(id=user_id).one()
    session.delete(deletedUser)
    session.commit()
    return 'Usuário de id: %s foi excluido com sucesso.' % user_id

@app.route('/category/api', methods=['GET', 'POST'])
def categoryFunction():
    if request.method == 'GET':
        return getAllCategories()
    elif request.method == 'POST':
        category_name = request.args.get('category_name', '')
        category_description = request.args.get('category_description', '')
        # Tem que capturar o id do usuário e passar para o user_id
        return makeNewCategory(category_name, category_description)

def getAllCategories():
    categories = session.query(Category).all()
    return jsonify(Categories=[i.serialize for i in categories])

def makeNewCategory(category_name, category_description):
    category = Category(category_name = category_name,
                        category_description = category_description)
    session.add(category)
    session.commit()
    return jsonify(Category=category.serialize)

@app.route('/category/api/<int:category_id>', methods=['GET', 'PUT', 'DELETE'])
def categoryFunctionId(category_id):
    if request.method == 'GET':
        return getCategory(category_id)
    if request.method == 'PUT':
        category_name = request.args.get('category_name', '')
        category_description = request.args.get('category_description', '')
        return updateCategory(category_id, category_name, category_description)
    elif request.method == 'DELETE':
        return delCategory(category_id)

def getCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    return jsonify(Category=category.serialize)

def updateCategory(category_id, category_name, category_description):
    category = session.query(Category).filter_by(id = category_id).one()
    if category_name:
        category.category_name = category_name
    if category_description:
        category.category_description = category_description
    session.add(category)
    session.commit()
    return 'Categoria alterada com sucesso %s' % category_id

def delCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id = category_id).one()
    session.delete(deletedCategory)
    session.commit()
    return 'Categoria de id: %s excluída com sucesso' % category_id

# ======== End API Endpoint ===================

@app.route('/category/login')
def login():
    return render_template('login.html')

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
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/edit_category.html', category_id = category_id, category = editedCategory)

@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    deletedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(deletedCategory)
        session.commit()
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
        return redirect(url_for('showItem', category_id = category_id))
    else:
        return render_template('item/delete_item.html', category_id = category_id, item_id = item_id, categories = categories, items=deletedItem)

@app.route('/category/<int:category_id>/item/<int:item_id>/description/', methods=['GET', 'POST'])
def descriptionItem(category_id, item_id):
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template('item/description_item.html', category_id = category_id, categories = categories, item_id = item_id, item = item)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
