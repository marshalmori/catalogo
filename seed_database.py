#!/usr/bin/env python3
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

def populate_db(db):
    # engine = create_engine('sqlite:///catalogo.db')
    engine = create_engine('postgresql://marshal:601077@localhost/catalogo')

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)

    session = DBSession()

    # User 1 -----------------------------------
    user1 = User(username = 'José da Silva', email = 'email1@email.com', picture = 'static/images/imagem1.png' )
    session.add(user1)
    session.commit()

    category1 = Category(category_name = 'categoria1', category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user1)
    session.add(category1)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user1,
                 category = category1)
    session.add(item6)
    session.commit()

    # User 2 -----------------------------------------
    user2 = User(username = 'Pedro da Silva', email = 'email2@email.com', picture = 'static/images/imagem2.png' )
    session.add(user2)
    session.commit()

    category2 = Category(category_name = 'categoria2', category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user2)
    session.add(category2)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user2,
                 category = category2)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user2,
                 category = category2)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user2,
                 category = category2)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user2,
                 category = category2)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user2,
                 category = category2)
    session.add(item5)
    session.commit()


    # User 3 -----------------------------------------
    user3 = User(username = 'Carlos da Silva', email = 'email3@email.com', picture = 'static/images/imagem3.png' )
    session.add(user3)
    session.commit()

    category3 = Category(category_name = 'categoria3', category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user3)
    session.add(category3)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user3,
                 category = category3)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user3,
                 category = category3)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user3,
                 category = category3)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user3,
                 category = category3)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user3,
                 category = category3)
    session.add(item5)
    session.commit()


    # User 4 -----------------------------------------
    user4 = User(username = 'Paulo da Silva', email = 'email4@email.com', picture = 'static/images/imagem4.png' )
    session.add(user4)
    session.commit()

    category4 = Category(category_name = 'categoria4', category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user4)
    session.add(category4)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item6)
    session.commit()

    item7 = Item(item_name = 'item7',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user4,
                 category = category4)
    session.add(item7)
    session.commit()

    # User 5 -----------------------------------------
    user5 = User(username = 'Ana da Silva', email = 'email5@email.com', picture = 'static/images/imagem5.png' )
    session.add(user5)
    session.commit()

    category5 = Category(category_name = 'categoria5',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user5)
    session.add(category5)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item6)
    session.commit()

    item7 = Item(item_name = 'item7',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user5,
                 category = category5)
    session.add(item7)
    session.commit()


    # User 6 -----------------------------------------
    user6 = User(username = 'Carla da Silva', email = 'email6@email.com', picture = 'static/images/imagem6.png' )
    session.add(user6)
    session.commit()

    category6 = Category(category_name = 'categoria6',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user6)
    session.add(category6)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user6,
                 category = category6)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user6,
                 category = category6)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user6,
                 category = category6)
    session.add(item3)
    session.commit()


    # User 7 -----------------------------------------
    user7 = User(username = 'Tina da Silva', email = 'email7@email.com', picture = 'static/images/imagem7.png' )
    session.add(user7)
    session.commit()

    category7 = Category(category_name = 'categoria7',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user7)
    session.add(category7)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user7,
                 category = category7)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user7,
                 category = category7)
    session.add(item2)
    session.commit()


    # User 8 -----------------------------------------
    user8 = User(username = 'Tatá da Silva', email = 'email8@email.com', picture = 'static/images/imagem8.png' )
    session.add(user8)
    session.commit()

    category8 = Category(category_name = 'categoria8',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user8)
    session.add(category8)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item6)
    session.commit()

    item7 = Item(item_name = 'item7',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user8,
                 category = category8)
    session.add(item7)
    session.commit()


    # User 9 -----------------------------------------
    user9 = User(username = 'Mussum da Silva', email = 'email9@email.com', picture = 'static/images/imagem9.png' )
    session.add(user9)
    session.commit()

    category9 = Category(category_name = 'categoria9',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user9)
    session.add(category9)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item6)
    session.commit()

    item7 = Item(item_name = 'item7',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user9,
                 category = category9)
    session.add(item7)
    session.commit()


    # User 10 -----------------------------------------
    user10 = User(username = 'Didi da Silva', email = 'email10@email.com', picture = 'static/images/imagem10.png' )
    session.add(user10)
    session.commit()

    category10 = Category(category_name = 'categoria10',category_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.', user = user10)
    session.add(category10)
    session.commit()

    item1 = Item(item_name = 'item1',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item1)
    session.commit()

    item2 = Item(item_name = 'item2',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item2)
    session.commit()

    item3 = Item(item_name = 'item3',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item3)
    session.commit()

    item4 = Item(item_name = 'item4',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item4)
    session.commit()

    item5 = Item(item_name = 'item5',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item5)
    session.commit()

    item6 = Item(item_name = 'item6',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item6)
    session.commit()

    item7 = Item(item_name = 'item7',
                 item_long_description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                 item_short_description= 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.',
                 price = '2.99',
                 user = user10,
                 category = category10)
    session.add(item7)
    session.commit()
