import json
import os

import eventlet
import socketio
import pymongo as mgdb


def create_serve():
    sio = socketio.Server()
    sio.recent_msg = []
    sio.client_count = 0
    app = socketio.WSGIApp(sio, static_files={'/': {'content_type': 'text/html', 'filename': 'static/index.html'}})
    sio.mgdb_client = mgdb.MongoClient("mongodb://lyy:105014@mongoAuth:27017/lyy")
    sio.mydb = sio.mgdb_client['lyy']
    sio.userinfos = sio.mydb['userinfos']
    sio.chatting_records = sio.mydb['chatting_records']

    @sio.event
    def connect(sid, environ):
        # print('connect', sid)
        sio.client_count += 1
        sio.emit('recent_msg', {"recent_msg": sio.recent_msg}, to=sid)
        sio.emit('client_count', {'client_count': sio.client_count})
        sio.emit('connection', {'response': f'{sid} connect success'})

    @sio.on('chat message')
    def another_event(sid, data):
        sio.recent_msg.append(data)  # 存储最近信息
        if len(sio.recent_msg) > 10:  # 最近10条
            sio.recent_msg.remove(sio.recent_msg[0])
        sio.emit('chat message', data)

    @sio.on("usrinfo")  # 登录时上传个人信息
    def get_usrinfo(sid, data):
        try:
            data = json.loads(data)
            sio.userinfos.insert_one({'sid': sid, 'id': data['id']})
            print(sio.userinfos.find_one({'sid': sid}))
        except TypeError:
            sio.userinfos.insert_one({'sid': sid, 'id': data['id']})
            print(sio.userinfos.find_one({'sid': sid}))
        else:
            pass

    @sio.on("personal message")  # 私人聊天
    def personal_event(sid, data):
        f = sio.userinfos.find_one({'sid': sid})
        t = sio.userinfos.find_one({'id': data['to']})
        # 得到双方信息，接下来发送给接收者
        if t is not None:
            sio.emit('personal message', data, to=t['sid'])
            sio.chatting_records.insert_one({'from': f['id'], 'to': t['id'], 'message': data['message']})
        else:
            sio.emit('personal message', {'error': 'no online'}, to=sid)

    @sio.on('get personal message')  # 私人聊天记录
    def get_personal_message(sid, data):
        fusr = sio.chatting_records.find_one({'sid': sid})
        tusr = sio.userinfos.find_one({'id': data['id']})
        f = sio.chatting_records.find({'from': fusr['id'], 'to': tusr['id']})
        t = sio.chatting_records.find({'from': tusr['id'], 'to': fusr['id']})
        for fm in f:
            sio.emit('personal message', fm['message'], to=fusr['sid'])
            sio.emit('personal message', fm['message'], to=tusr['sid'])
        for tm in t:
            sio.emit('personal message', tm['message'], to=fusr['sid'])
            sio.emit('personal message', tm['message'], to=tusr['sid'])

    @sio.event
    def disconnect(sid):
        # print('disconnect ', sid)
        x = sio.userinfos.find_one({'sid': sid})
        if x is not None:
            sio.userinfos.delete_one(x)
        sio.client_count -= 1
        sio.emit('client_count', {'client_count': sio.client_count})
        sio.emit('disconnection', {'response': f'{sid} disconnect'})

    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)

    @sio.event()
    def on_message():
        pass  # print('received msg')


create_serve()
