#coding:utf-8
import sqlite3

#Gestion d'erreurs
try :
    #Connexion à la BDD
    connection = sqlite3.connect("BddTrainning.db") #erreur de bdd inexistante

    #Création du curseur itérateur
    cursor = connection.cursor()

    #Lecture depuis la BDD
    my_user_name = ("Jason",)
    cursor.execute("SELECT * FROM t_users WHERE user_name = ?",my_user_name)
    result = cursor.fetchone()[1] #erreur de none objet trouvé si on change le Jason
    print(f"Le nom de l'utilisateur est : {result}")

    #Création d'enregistrement
    cursor = connection.cursor()
    new_user = (cursor.lastrowid,"Collete",25)
    cursor.execute("INSERT INTO t_users VALUES(?,?,?)",new_user)
    connection.commit()
    print("Le nouvel utilisateur est ajouté")

    #executemany()
    cursor = connection.cursor()
    new_user = [(cursor.lastrowid,"Caly",25),(cursor.lastrowid,"Emy",12)]
    cursor.executemany("INSERT INTO t_users VALUES(?,?,?)",new_user)
    connection.commit()
    print("Les nouveaux utilisateurs sont ajoutés")

    #fetchall()
    req = cursor.execute("SELECT *FROM t_users")
    """print(req.fetchall())
    print("fetchall terminé")"""
    for row in req .fetchall():
        print(row[1])


except Exception as e:
    print("Erreur",e)
    connection.rollback()
finally:
    connection.close()

#Random information 
#print(type(connection))
#print(type(cursor))