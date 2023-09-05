print("Hola Usuario!")
print("Vamos a llenar un tanque con agua!")
print("Que capacidad quiere que el tanque tenga?")
v=int(input())
print("El tanque de agua tiene una capacidad de", v ,"ml")
u="si"
vs=0
while u!="no":
    print("Ingrese la cantidad de ml que quiere vertir en el tanque")
    ex=int(input())
    vs=ex+vs
    if vs>=v:
      break
    print("Ahora el tanque tiene", vs, "ml de agua!")
    print("Quiere seguir?")
    u=input()
    up=u.lower()
    if u=="no":
     break
    else:
     continue
if vs>=v:
 print("Ha llenado o superado la capacidad del tanque!")
if vs>v:
  print("El tanque se lleno y se rebalzo, hay", (vs-v), "ml sobrantes!")
else:
  print("El tanque quedo con", vs, "ml de agua!")