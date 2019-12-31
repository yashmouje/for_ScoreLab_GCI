#
#  Webserver Program
#
#Importing Reqiured Modules
import http.server
import socketserver

#Address
host = "localhost"
port = 8080
#Tuple for address
address= (host, port)

#Handler
handler = http.server.SimpleHTTPRequestHandler

#Server
httpServer = socketserver.TCPServer(address, handler)  #address needed as touple

#Starting Web server
print("**************************************************")
print()
print("Web Server now running on " + host + ":" + str(port))
print()
print("**************************************************")

httpServer.serve_forever() #server keeps running

#ysm
