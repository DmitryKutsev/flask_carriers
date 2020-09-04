from flask import render_template, Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import Carrier, Forwarder, Base, FreeeOrder

engine = create_engine('sqlite:///logistic.db', connect_args={'check_same_thread': False})

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()

app = Flask(__name__)
@app.route('/')
@app.route('/orders')

def showFreeeOrders():
    orders = session.query(FreeeOrder).all()
    return render_template("free_orders.html", orders=orders)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)