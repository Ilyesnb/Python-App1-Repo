list_name=[]
input_name="init"
while input_name!="":
    input_name=input("nom : ")
    if(input_name!=""):
        list_name.append(input_name)
print("nombre de noms : ",len(list_name))
#deuxsieme methode
print("nombre de noms : ",list_name.__len__())
# join
print("nombre de noms : "," ;".join(list_name))

# deuxieme methode 

list_name= []
input_name= ""
while True :
    input_name=input("nom: ")
    if(input_name==''):
        break
    list_name.append(input_name)
print("nombre des noms: ",len(list_name))
print("liste des noms: "," ".join(list_name))