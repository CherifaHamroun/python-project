#coding:utf-8
import datetime
d1 = datetime.datetime(2020,3,27,21,45,42)
d2 = datetime.datetime(2020,4,29,21,45,42)
d3 = datetime.date(2020,1,1)
t1 = datetime.time(00,00,00)
#comparaison avec datetime.date possible aussi 
if d1<d2:
    print("d1 antérieure a d2")
else:
    print("d1 plus récente a d2")
print(d1)
print(d2)
print(d3)
print(d1.year)
print(d2.day)
print(d3.month)
print(type(d1),"-",type(d2),"-",type(d3))
print(t1)
print(datetime.datetime.now())
print(datetime.date.today())
now = datetime.date.today()
born = datetime.date(2010,8,7)
print(f"{now.year - born.year } ans")