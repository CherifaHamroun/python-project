#coding:utf-8
import cgi 
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>réponse</title>
</head>
<body>

"""
print(html)
try:
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"<p>Bonjour {username}</p>")
        html="""
        </body>
        </html>
            """
        print("<script>alert('ok')</script>")
        print(html)
    else :
        raise Exception("<p>Pseudo non trouvé</p>")
except:
    print("pseudo non transmis")

