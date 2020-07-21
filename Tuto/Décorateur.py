#coding:utf-8
"""
Notations de décorateurs:
    func = decorator(func)
    @decorator avant la fonction a décorer

"""
#lié au design patterns 
import functools
def decorator(func):
    print("--------------")
    return func
@decorator
def Hello():
    print("Hello")
#collable Hello
Hello = decorator(Hello)
print(type(Hello))
Hello()
user_logged = True
def decorator_check_access(func):
    def wrapper():
        if user_logged:
            return func()
        else:
            print("Connexion impossible")
    return wrapper
@decorator_check_access
def profile():
    print("le profile membre ")

def article():
    print("les articles")
profile()
article()

user_admin = "Jason"
def check_access_name_user(username):
    def decorator_check(func):
        @functools.wraps(func)
        def wrapper():
            #traitement
            if username == user_admin:
                return func()
            else:
                print("unknown user")
        return wrapper
    return decorator_check
@check_access_name_user("kk")
@decorator_check_access
def profile_name_user():
    """
    Accès au profil de l'user
    """
    print("Le profile name user access")
#profile_name_user = check_access_name_user("Jason")(profile_name_user)
profile_name_user()
# me donne le wrapper si on n'enleve pas le décorateur
#admin_panel = decorator_check_access(check_access_name_user(profile_name_user)) pour 2 decorateurs
help(profile_name_user)
