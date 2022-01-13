import socketio


def create_client():
    sio = socketio.Client()
    @sio.event
    def connect():
        print('connection established')
        sio.emit('client', {'foo': 'bar'})

    @sio.on('chat message')
    def on_message(data):
        print('client received a message!',data)
    # @sio.event
    # def message(data):
    #     print('message received with ', data)
    #     sio.emit('client', {'response': 'my response'})

    @sio.event
    def connect_error():
        print("The connection failed!")
        sio.disconnect()

    @sio.event
    def disconnect():
        print('disconnected from server')
        sio.disconnect()

    sio.connect('http://127.0.0.1:5000')
    sio.wait()

create_client()
