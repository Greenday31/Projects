import array as arr
#Ejercicios del curso de logica de programacion base python.

#Ejercicio 1 imprimir un texto de una variable o puede ser solo direcamente del print.

message='We can write first the variable with the text then print it'
print(message)
print('')

#Ejercicio 2 Operaciones basicas.

value1 = 3
value2 = 4
value3 = 8
value4 = 6

ressum = value1 + value4
resminus = value3 - value2
resmul= value3 * value4
resdiv = value4 / value1

print(ressum,resminus,resmul,resdiv)
print('')

#Ejercicio 3 Variables, Integers y strings ya pueden ser definidos arriba son lo mismo, el valor boolean se asigna como siempre,
#el valor float solo se ace igual que un integer.

#Valores alfanumericos, se hace como en todos los lenguajes de programacion.

valal =input("Hello bitch whats ur name : ")

print("My name is....",valal)
print('')

#Valores en blanco para que mas adelante se les asigne el valor acorde  a la accion realizada. Realmente es lo mismo de arriba pero declarando vacio y despues adquiere el valor

vl1 = str()
vl2 = int()
vl1=input("Favorite Song? ")
vl2=input("Favorite Number? ")

print("My favorite song is ",vl1)
print("My favorite number is ",vl2)

print('')

#Ejercicio 4 if, else statement.

age = int(input("How old are u? "))

if ( (age) > 25 ):
    print("Pinche vejete kulikagao")
else:
    print("Pinche morrillo mekillo")

print('')
#Now Example con elif
age2 = int(input("How old are u? "))
if ( 12 > (age2) > 1 ):
    print("Pinche bb")
elif ((age2) > 13):
    print("Pinche morrillo mekillo")
else: 
    print("Morido")

print('')

#Ejercicio 5 Switch statement, SE REALIZA DE LA SIGUIENTE FORMA PERO NECESITA UN PYTHON MAS ACTUALIZADO.

#option = str(input("Choose an option: "))
#match option:
#    case "yes":
#       print("Sex")
#    case "no":
#       print("Nosex")

#Ejercicio 6 Array 

#Declaracion del array

a =arr.array('i',[3,1,1])

#Impresion del array

for i in range (0,2):
    print (a[i],end = "")
print('')

#Insertar un nuevo dato al array

a.insert(2,9)

#Print el array actualizado
print("Updated: ")

for i in (a):
    print(i,end="")

#Ejercicio 7 Loops

print('')

bands = ["Queen","Greenday","Maroon 5"]
singers = ["FM","BJ","Al"]

for x in bands :
    for y in singers:
        print(x,y)

print('')

i2= 1
while i2 < 5:
    print(i2)
    i2+=1
else:
    print("Ya se acabo carnalito ya no es menor que 5 ")

print('')

#Ejercicio 8 Functions
#Functions: Something you want
#Arguments: Specifics of functions
#Analogy: Ordering food for delivery
# The ability to include argument allows the function to be used for many purposes

teeth= input("Tas listo para lavarte el ocico de puerka? ")
alarm= input("Ya pusiste tu alarma huevon?")

#Function para saber si ya todo esta completo
def listopamimir(teeth,alarm):
    if(teeth == 'si' and alarm == 'si'):
        print("A momir")
    else:
        print("Apurarte que aun no puedes momir")

#Function que no requiere argumentos de entrada.
def complete():
    print("Listo el chequeo de la mimicion")

#We call booth functions
listopamimir(teeth,alarm)
complete()

#Otro ejercicio de functions pero mas elaborado

def total():
    done = "N"
    global count 
    count = 0
    while done != "S":
        people = int(input("Cuantas puercas hay en la sala del cinuki? "))
        count = (people+count)
        done = input("Ya se lleno esta chingadera S o N")

total()
print("Gente en la sala: ", count)
    
print('')

#Ejercicio 8 Recursion

def sumaloca(begin):

    print(begin)

    next = begin + 10

    if next < 100:
        sumaloca(next)
sumaloca(10)


