import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context

# Nesse arquivo temos 3 classes que geram o banco de dados
# com as tabelas user, category e item
Base = declarative_base()

# Classe que gera a tabela user.
class User(Base):
    '''Classe para criar os campos da tabela dos usuários'''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    email = Column(String)
    picture = Column(String)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def serialize(self):
        '''Retorna os dados de um objeto serializado'''
        return {
            'id':       self.id,
            'username': self.username,
            'email':    self.email,
            'picture':  self.picture
        }

# Classe que gera a tabela category.
class Category(Base):
    '''Classe para criar os campos da tabela das categorias'''
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(32), index=True)
    category_description = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        '''Retorna os dados de um objeto serializado'''
        return {
            'id':                   self.id,
            'category_name':        self.category_name,
            'category_description': self.category_description,
            'user_id':              self.user_id
        }

# Classe que gera a tabela item.
class Item(Base):
    '''Classe para criar os campos da tabela dos itens'''
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(32), index=True)
    item_long_description = Column(String(350))
    item_short_description = Column(String(100))
    price = Column(String(8))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        '''Retorna os dados de um objeto serializado'''
        return {
            'id': self.id,
            'item_name': self.item_name,
            'item_long_description': self.item_long_description,
            'item_short_description': self.item_short_description,
            'price': self.price,
            'user_id': self.user_id,
            'category_id': self.category_id
        }


engine = create_engine('sqlite:///catalogo.db')
Base.metadata.create_all(engine)
