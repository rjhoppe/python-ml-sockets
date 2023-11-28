import socket
# For serializing
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 9999))

try:
  test_obj = {'key1': 'value1', 'key2': 'value2'}
  serialized = pickle.dumps(test_obj)
  client.sendall(serialized)
  print('Job done.')
finally:
  client.close()
