import socket
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make sure this is a tuple in both the server and client files
server.bind(('127.0.0.1', 9999))

# Allows 1 connection
server.listen(1)

# Will keep running until conn interrupted
while True:
  print('Waiting for connection')
  client, addr = server.accept()

  try:
    print('Connected')

    data = b''
    while True:
      chunk = client.recv(4096)
      if not chunk:
        break
      data += chunk

    received_object = pickle.loads(data)
    print(f'Object received: {received_object}')


  finally:
    client.close()