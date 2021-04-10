import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port=9090
while True:
    try:
        s.bind(('', port))
        print('Сервер запущен ')
        break
    except OSError:
        port += 1


users = {}

while True:
    data, addr = s.recvfrom(1024)

    if data == '':
        continue

    user_id = addr[1]
    data = data.decode()
    if data == 'join_cl':
        print('Клиент ',user_id,' присоединился')
        s.sendto('Последнее сообщение: '.encode(), addr)
        with open('log.txt') as file:
            for line in (file.readlines()[-15:]):
                s.sendto(line.encode(), addr)
        continue

    if '<n_ch>' in data:
        user_nick = data.split('>=')[1]
        if user_nick not in users.values():
            users.setdefault(addr, user_nick)
            s.sendto('<n_ch_t>'.encode(), addr)
            continue
        else:
            s.sendto('<n_ch_f>'.encode(), addr)
            continue

    data = str((users.get(addr), data))
    print(data, file=open('log.txt', "a"))
    for user in users:
        if user != addr:
            s.sendto(data.encode(), user)
            
