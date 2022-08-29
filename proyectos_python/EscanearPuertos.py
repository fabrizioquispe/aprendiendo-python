import sys
from socket import *
from tracemalloc import start

host = sys.argv[1]
protstrs = sys.argv[2].splist('-')

start_port =int(protstrs[0])
end_port = int(protstrs[1])

target_ip = gethostbyname(host)
opened_port = int(protstrs[1])

for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    resultado = sock.connect_ex((target_ip,port))
    if resultado ==0:
        opened_port.append(port)

print("El puerto abierto es: ")

for i in opened_port:
    print(i)