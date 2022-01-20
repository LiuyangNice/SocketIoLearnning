import socketio


def create_client():
    sio = socketio.Client()
    @sio.event
    def connect():
        print('connection established')
        sio.emit('connection', {'foo': 'bar'})
        sio.emit('login', {"username": "111","password":"123123"})
        for index in range(20):
            sio.emit("chat message",{"index":index})

    @sio.on('chat message')
    def on_message(data):
        print('client received a message!',data)
    @sio.on('recent_msg')
    def on_message(data):
        print('recent_msg',data)
    @sio.on('login')
    def on_message(data):
        print('login_data',data)
    @sio.on('connection')
    def on_message(data):
        print('client received a message!', data)
    @sio.on('client_count')
    def on_message(data):
        print('clientCount!', data)
    @sio.event
    def connect_error():
        print("The connection failed!")
        sio.disconnect()

    @sio.event
    def disconnect():
        print('disconnected from server')
        sio.disconnect()

    # sio.connect('http://127.0.0.1:5000')
    sio.connect('http://1.117.37.235:5000')
    sio.wait()

create_client()
