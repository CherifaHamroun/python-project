#coding:utf-8
"""
cookie fichier texte que le navigateur va enregistrer
qui permet de stocker une information il aura un nom une
valeur et une date d'expiration et d'autres infos autres 
que pseudo et mdp c pas sécuurisé 
exemple theme préféré langue préférée
____________________________________________________________________________
http fonctionne a travers des entetes 
format typique des entetes pour http
nom entete: ens de valeurs(ou nom = valeur) séparés par des ; et un espace
____________________________________________________________________________
entete précise pour les coockies
chaine de caractère qui crée une cookie
format :
    Set-Cookie:pref_langue=fr; autres infos tel
    expires = date 
    path = lien ou l'utiliser 
    comment =
    domain = domaine du site (racine)
    secure : le cookie ne fonctionne que sur des cnxn https (mot a mettre tt seul)
    version
    httponly : pour ne pas etre récupéré ou exploité par du js (mot a mettre tt seul)

"""
import cgi
import http.cookies
import datetime
import os
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
expiration = datetime.datetime.now() +datetime.timedelta(days =365)
expiration =expiration.strftime("%a,%d-%b-%Y %H:%M:%S")
mycookie = http.cookies.SimpleCookie()
mycookie["pref_lang"] = "fr"
mycookie["pref_lang"]["httponly"] = True
mycookie["pref_lang"]["expires"] = expiration
#print("Set-Cookie: pref_lanf=fr; httponly")
print(mycookie.output())
print("Content-type: text/html;charset = utf-8\n")
html ="""<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page</title>
</head>
<body>
    <h1>Cookies avec python</h1>
"""
print(html)
if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else:
    print("<p>Non trouvé</p>")
try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("<br>")
    print("La langue préférée de l'user",user_lang["pref_lang"].value)
except(http.cookies.CookieError,KeyError):
    print("Non trouvé")
html="""
</body>
</html>
"""
print(html)