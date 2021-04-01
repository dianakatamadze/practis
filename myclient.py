import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print('подключено к серверу ')

while True:
    nickname_inp=input('Введите Ваше имя: ')
    nickname='<nick_check>='+nickname_inp
    sock.send(nickname.encode())
    data = sock.recv(1024)
    data = data.decode()
    if data == '<nick_check_true>':
        print('Имя успешно задано, добро пожаловаь в эхо-сервер')
        break
    elif data == '<nick_check_false>':
        print('Этото имя уже занято, введите другое!')
while True:
    
    sock.send(input(f'{nickname_inp} введите сообщение: ').encode())
    data = sock.recv(1024)
    print(data.decode())
    if data.decode() in ('exit', 'выход'):
        break
sock.close()


