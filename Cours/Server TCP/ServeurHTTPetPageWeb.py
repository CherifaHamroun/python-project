#coding:utf-8
import http.server
import socketserver

port = 80
adress =("",port)
handler= http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress,handler)
print(f"Le server a démarré sur le port {port}")
httpd.serve_forever()