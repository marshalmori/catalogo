from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item

app = Flask(__name__)

engine = create_engine('sqlite:///catalogo.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

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
        new_category = Category(category_name=request.form['name'])
        session.add(new_category)
        session.commit()
        return redirect(url_for('showCategory'))
    else:
        return render_template('category/new_category.html')

@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.category_name = request.form['name']
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
                       description=request.form['description'],
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
        if request.form['description']:
            editedItem.description = request.form['description']
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



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
