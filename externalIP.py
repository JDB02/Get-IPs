import urllib.request
#returns an external IP address

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)
