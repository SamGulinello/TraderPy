from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event

from resources.TD.td import TD
from main import TraderPy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

async_thread = Thread()
td_thread = Thread()
thread_stop_event = Event()

td = TD()
print('TD Object Created')

def getAccountData():
    while not thread_stop_event.isSet():
        number = td.getAccountValue()
        number = "${:,.2f}". format(number)
        socketio.emit('newnumber', {'number': number}, namespace='/test')

        orders = td.getOrders()
        orders=orders[0]
        print(orders)
        socketio.emit('neworder', {'order': orders["orderLegCollection"][0]["instrument"]["symbol"], 'orderType': "{}".format(orders["orderLegCollection"][0]["instruction"])}, namespace='/test')
        socketio.sleep(5)


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global async_thread
    print('Client connected')

    if not async_thread.is_alive():
        print("Starting Thread")
        async_thread = socketio.start_background_task(getAccountData)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    td_thread = socketio.start_background_task(TraderPy)
    socketio.run(app, use_reloader=False)
