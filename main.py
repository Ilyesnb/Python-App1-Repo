#declaration 
a=16
b=15
prix= 25000
chaine = 'test l\'a chaine1'
chaine = 'test l''a chaine2'
chaine = "test l'a chaine3"
# traitements
s=a*b
pf= prix*1.19
status=False


#Resultat
print("tva=",pf)
print(chaine)
print(type(status))
print(type(chaine))
print(f'type de a :',type(a))
a=int(a)
print('valeur de a :',a,'valure de b :',b)
print(f'type de a :{type(a)} et la valeur de b {b}')


#les type
n=5
f=5.5
s="une phrase ou un text"
b=True
#Afficher un nombre
print(15)
#Affiche une chaine de caractéres
print("hello world")
#Affiche une variable
message = "ceci est un test"
print(message)
#2.Passer ou ne pas passer a la ligne
print("hello",end=" ")
print("world")