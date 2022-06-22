import socket
import logging

def write_in_file(str):
    try:
        logging.basicConfig(filename="file.log", level=logging.INFO)
        logging.info(str)
        #with open("file.txt","a") as file:
        #    file.write(str)
    except:
        print("Ошибка записи в файл")

def print_msg(msg):
    str=msg.split(" ")
    if str[3]=='00\n':
        time=str[2].split('.')
        print(f'спортсмен, нагрудный номер {str[0]} прошёл отсечку {str[1]} в {time[0]}.{time[1][0]}')
host_name='127.0.0.1'
port_name=8080
client=socket.create_connection((host_name, port_name))
while True:
    try:
        msg=client.recv(1024)
        write_in_file(msg.decode('utf-8'))
        print_msg(msg.decode('utf-8'))
    except KeyboardInterrupt:
        client.close()
