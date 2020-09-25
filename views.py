from flask import render_template, Flask, flash, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from config import OPENID_PROVIDERS
from database_setup import Carrier, Forwarder, Base, FreeOrder, TakenOrder
from forms import LoginForm

engine = create_engine('sqlite:///logistic.db', connect_args={'check_same_thread': False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()

app = Flask(__name__)
@app.route('/')
@app.route('/taken_orders')

def showTakenOrders():
    orders = session.query(TakenOrder).order_by(TakenOrder.id)
    return render_template("taken_orders.html", orders=orders)

@app.route('/orders')
def showFreeOrders():
    orders = session.query(FreeOrder)
    return render_template("free_orders.html", orders=orders)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = OPENID_PROVIDERS)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)