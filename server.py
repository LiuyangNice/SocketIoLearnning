import eventlet
import socketio


def create_serve():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'app/index.html'}
    })
    @sio.event
    def connect(sid, environ):
        print('connect', sid)
        sio.emit('connection', {'response': f'{sid} connect success'})
    @sio.on('chat message')
    def another_event(sid, data):
        sio.emit('chat message', data)
    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)
        sio.emit('disconnection',{'response':f'{sid} disconnect'})
    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    @sio.event()
    def on_message():
        print('received msg')
create_serve()