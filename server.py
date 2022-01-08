import eventlet
import socketio


def create_serve():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'index.html'}
    })
    @sio.event
    def connect(sid, environ):
        print('connect ', sid)
        print(environ)
        sio.emit('server', {'response': f'{sid}connect success'})

    # @sio.on('client')
    # def on_message(sid, data):
    #     print('serve received a message!111', data)
    @sio.on('client')
    def another_event(sid, data):
        print(f'serve received a message!{sid}', data)
    # @sio.event
    # def my_event(sid, data):
    #     print('message ', data)
    #     sio.emit('serve', {'response': 'connect success'})
    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)
    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

create_serve()