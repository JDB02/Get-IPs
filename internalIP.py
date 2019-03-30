import socket
#Returns an internal IP address
#This assumes you have an internet access, and that there is no local proxy.

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
