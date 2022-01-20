import os

import eventlet
import socketio
# import pymongo as mgdb

# os.system("sudo systemctl start mongod")
# client = mgdb.MongoClient("0.0.0.0",27017)
# mydb  = client["chatDemo"]
# my_col = mydb["users"]
# def sign_up(username,password,password2):
#     if  password == password2:
#         my_col.insert_one({"username":username,"password":password})
# def sign_in(username,password):
#     x = my_col.find_one({"name":username})
#     if x is not None:
#         return x["username"] == password
#     else:
#         return False


def create_serve():
    sio = socketio.Server()
    sio.recent_msg = []
    sio.client_count = 0
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'index.html'}
    })
    @sio.event
    def connect(sid, environ):
        # print('connect', sid)
        sio.client_count +=1
        sio.emit('recent_msg',{"recent_msg":sio.recent_msg})
        sio.emit('client_count',{'client_count':sio.client_count})
        sio.emit('connection', {'response': f'{sid} connect success'})
    @sio.on('chat message')
    def another_event(sid, data):
        sio.recent_msg.append(data) #存储最近信息
        if len(sio.recent_msg)>10:  #最近10条
            sio.recent_msg.remove(sio.recent_msg[0])
        # print(len(sio.recent_msg))
        sio.emit('chat message', data)
    # @sio.on('logup')
    # def another_event(sid, data):
    #     sign_up(data["username"],data["password"],data["password2"])
    #     # sio.emit('chat message', data)
    # @sio.on('login')
    # def another_event(sid, data):
    #     if sign_in(data["username"],data["password"]):
    #         sio.emit('login',{"login_successes":True})
    #     else:
    #         sio.emit('login', {"login_successes": False})
    #         # sio.disconnect()

    @sio.event
    def disconnect(sid):
        # print('disconnect ', sid)
        sio.client_count -=1
        sio.emit('client_count', {'client_count': sio.client_count})
        sio.emit('disconnection',{'response':f'{sid} disconnect'})
    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
    @sio.event()
    def on_message():
        print('received msg')
create_serve()