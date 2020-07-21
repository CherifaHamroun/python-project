#coding:utf-8
"""
Sockets : logiciels se chargeant de permettre la communication
soit au seins d'une meme machine ou + distantes 
sans se soucier de la maniere dont est gérée le réseau
interface de connexion avec différents modes
Modes :
        TCP : connecté la cnxn est établie une bonne fois pour
            toute et puis communiquer et les infos sont vérifiées
            ie recevoir tte l'info jusqu'à clore ou couper la cnxn 
        UDP : non-connecté plus rapide pas de vérification du tt 
            a chaque communication il faudra donner les infos
            du destinataireet pas de vérification de réception 
            des données 
"""
import socket 
#Le client se connecte au server et puis ces deux la communiquent
host,port = ("127.0.0.1",5566)
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    socket.connect((host,port))
    print("Client connecté")
    data = "Bonjoour je suis le client"
    #encodage des données en utf-8 a l'envoie
    data = data.encode("utf8")
    socket.sendall(data) #send pas sur que ce sera envoyé integralement
except ConnectionRefusedError: #ConnectionRefusedError 
    print("Connexion échouée")
finally:
    socket.close()