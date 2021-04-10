import socket
import threading


def pr_data(sc):
    while True:
        data = sc.recv(1024)
        print(data.decode())


sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sc.connect(('localhost', 9090))
print('клиент запущен')

while True:
    nickname_inp=input('Введите Ваш ник: ')
    nickname='<n_ch>='+nickname_inp
    if nickname_inp in ('выход','exit'):
        sc.close()
        print('клиент отключен')
        break
    sc.send(nickname.encode())
    data = sc.recv(1024)
    data = data.decode()
    if data == '<n_ch_t>':
        print('Ник успешно задан, добро пожаловаь в чат, ', nickname_inp)
        break
    elif data == '<n_ch_f>':
        print('Этот ник уже занят, введите другой!')

t1 = threading.Thread(target=pr_data, args=(sc,), daemon=True)
t1.start()
sc.send('join_cl'.encode())

while True:
    data = input('Вы: ')
    sc.send(data.encode())
    if data in ('выход','exit'):
        sc.close()
        print('клиент отключен')
        break