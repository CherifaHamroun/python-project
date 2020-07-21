#coding:utf-8
import cgi
#html sous forme de script 
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page</title>
</head>
<body>
    <h1>Bonjour</h1>
    <p>Une balise de paragraphe</p>
    <form method="post" action="DonneesFormulaires.py">
    <p><input type="text" name= "username">
    <input type ="submit" value="Envoyer"></p>
    </form>
</body>
</html>
"""
print(html)
