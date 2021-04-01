import socket

sock = socket.socket()
sock.bind(('', 9090))
print('сервер запущен')
sock.listen(1)
conn, addr = sock.accept()
users = []

print('connected:', addr)

while True:
    data = conn.recv(1024)
    
    user_id = addr[1]
    data = data.decode()
    

    if '<nick_check>' in data:
        user_nick = data.split('>=')[1]
        if user_nick not in users:
            users.append(user_nick)
            conn.send('<nick_check_true>'.encode())
            continue
        else:
            conn.send('<nick_check_false>'.encode())
            continue
    if not data:
        break
    conn.send(data.encode())

conn.close()
print('сервер выключен')

