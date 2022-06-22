import random
import socket
import string
host_name='127.0.0.1'
port_name=8080

def rename_var(v):
    if v>=0 and v<=9:
        return f'0{v}'
    else:
        return f'{v}'
def rename_msec(m):
    if m>=0 and m<=9:
        return f'00{m}'
    elif m>=10 and m<=99:
        return f'0{m}'
    else:
        return f'{m}'

server=socket.create_server((host_name, port_name))
server.listen(10)
while True:
    try:
        conn,address=server.accept()
        id_person=''.join(f'{random.randint(0,9)}' for i in range(4))
        id_channel=''.join(f'{random.choice(string.ascii_uppercase)}{random.choice(string.digits)}')
        group=''.join(f'{random.randint(0,9)}' for i in range(2))
        hour=rename_var(random.randint(0,24))
        min=rename_var(random.randint(0,59))
        sec=rename_var(random.randint(0,59))
        msec=rename_msec(random.randint(0,999))
        msg=f'{id_person} {id_channel} {hour}:{min}:{sec}.{msec} {group}\n'
        conn.send(msg.encode())
        print('Послание отправлено')
    except KeyboardInterrupt:
        server.close()

