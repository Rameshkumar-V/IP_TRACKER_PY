import socket
from pickle import loads

CLIENTS_DATA=[
    {
        'ip':'192.168.236.246',
        'name':'My system'
    },
    {
        'ip':'127.2.0.1',
        'name':'Hi system'
    },
{
        'ip':'127.2.0.2',
        'name':'Hi system 2'
    }
]

def Fetch_details(IP):

    # IP = '192.168.236.246'  # IP FOR CLIENT THEN RECEIVER
    PORT = 6000

    server_socket = socket.socket()

    try:

        server_socket.connect((IP, PORT))

    # Send a message to the client
        server_socket.send(b"Are you on?")
        response=loads(server_socket.recv(1024))
        print('Response : ',response)
    # Close the connection
        server_socket.close()
    except Exception as e:
        print('Response : ', 'OFF')
        #print(e)



for USER in CLIENTS_DATA:
    print(USER['ip'])
    print('NAME : ',USER['name'])
    Fetch_details(USER['ip'])