import eventlet
import socketio


def create_serve():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'app/index.html'}
    })
    @sio.event
    def connect(sid, environ):
        print('connect ', sid)
        sio.emit('server', {'response': f'{sid} connect success'})
    @sio.on('client')
    def another_event(sid, data):
        sio.emit('server', {'response': data})
    @sio.event
    def disconnect(sid):
        print('disconnect ', sid)
        sio.emit('server',{'response':f'{sid} disconnect'})
    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    @sio.event()
    def on_message():
        print('received msg')
create_serve()