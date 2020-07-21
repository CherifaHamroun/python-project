#coding:utf-8
import time
"""
          localtime()
TIMESTAMP ------------>struct_time
          <------------
          mktime
--------------------------------------------------------------------------------------------------------------------------------------------
STRFTIME/
%d 
%m
%Y: année sur 4 chiffres
%y: année sur 2 chiffres
%H 
%I
%S
%p : AM/PM
%A : jour de la semaine 
%B : mois
%b : mois abrégé
%Z : fuseau horaire
"""
#TimeStamp basée sur du premier janvier 1970 à 00h00
begin = time.time()
print("Debut")
time.sleep(5)
end = time.time()
print("Fin")
#print("Temps d'exécution : {} s".format(end-begin))
print(f"Temps d'execution : {end - begin} s")
print (time.localtime())
tps = time.mktime(time.localtime())
print(tps)
my_time = time.strftime("%A %d /%m /%Y %Z")
print(my_time)