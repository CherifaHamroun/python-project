#coding:utf-8
import math
number = -14.6
number2 = 4
number3 = 0.5
#fonctions arithmétiques
print("Entier supérieur : {}".format(math.ceil(number)))
print("Entier inférieur : {}".format(math.floor(number)))
print("Racine carrée : {} ".format(math.sqrt(math.fabs(number))))
print("{} à la puissance {} : {} ".format(number,2,math.pow(number,2)))
print("La valeur absolue de {} est : {}".format(number,math.fabs(number)))
print("La factorielle de {} est : {}".format(number2,math.factorial(number2)))
#fonctions avancées
print("Exponnentielle de {} est {} ".format(number2,math.exp(number2)))
#base i logi = plus précise
print("Logarithme de {} est {} ".format(number2,math.log10(number2)))

print("Logarithme de {} est {} ".format(number2,math.log(number2,10)))

#fonctions trigonométriques
print("Sinus de {} est : {} radian".format(number2,math.sin(number2)))
print("Cosinus de {} est : {} radian".format(number2,math.cos(number2)))
print("Tangente de {} est : {} radian".format(number2,math.tan(number2)))
print("arcSinus de {} est : {} radian".format(number3,math.asin(number3)))
print("arccosinus de {} est : {} radian".format(number3,math.acos(number3)))
print("arctangente de {} est : {} radian".format(number3,math.atan(number3)))

#Conversion de radian en degré et vice-versa
print("Degré -> Radian = {}".format(math.radians(number)))
print("Radian -> Degré = {}".format(math.degrees(number)))

mavar = 14
print("Not a number ? {}".format(math.isnan(mavar)))

print("Pi {}".format(math.pi))
print("e {}".format(math.e))