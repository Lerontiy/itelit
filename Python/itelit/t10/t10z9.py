import math
class pl:
    def krug(self,r):
        rez=math.pi*pow(r,2)
        return rez
    def trik(self,a,b,c):
        p=(a+b+c)/2
        rez=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return rez
    def trap(self,a,b,h):
        rez=((a+b)*h)/2
        return rez
p=pl()
r=int(input("Введіть радіус круга: "))
print("Площа круга з радіусом",r,"=",p.krug(r))
print(" ")
a=int(input("Введіть сторону трикутника a: "))
b=int(input("Введіть сторону трикутника b: "))
c=int(input("Введіть сторону трикутника c: "))
print("Площа трикутника зі сторонами",a,",",b,"та",c,"=",p.trik(a,b,c))
print(" ")
a=int(input("Введіть 1 основу трапеції a: "))
b=int(input("Введіть 2 основу трапеції b: "))
h=int(input("Введіть висоту трапеції h: "))
print(" =Площа трапеції з основами ",a,",",b,"та висотою",h,"=",p.trap(a,b,h))
    
