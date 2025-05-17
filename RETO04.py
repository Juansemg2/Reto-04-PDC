#Reto #4 PDC

#1.Dado un numero entero, determinar si ese numero corresponde al código ASCII de una vocal minúscula.
n = int(input("Ingrese un numero entero:"))

if n == 97 or n == 101 or n == 105 or n == 111 or n == 117:
    print("El numero no es un codigo ASCII de una vocal minuscula")
else:
    print("El numero no es un codigo ASCII de una vocal minuscula")


#------------------------------------------------------------------------------

#2.Dada una cadena de longitud 1, determine si el código ASCII de primera letra de la cadena es par o no.
caracter=str(input("Ingrese un caracter:"))
caracter=ord(caracter)
if caracter%2==0:
  print("el caracter escrito es par")
else:
  print("el caracter escrito es impar")


#------------------------------------------------------------------------------

#3.Dado un caracter, construya un programa en Python para determinar si el caracter es un digito o no.
car=str(input("Ingrese un caracter:"))
car=ord(car)
if car>=48 and car<=57:
    print("El caracter es un digito numerico")
else:
    print("el caracter no es un digito numerico")


#-----------------------------------------------------------------------------

#4.Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
if num1%num2 == 0:
    print("el numero 1 es multiplo del numero 2")
else:
    print("El numero 1 no es multiplo del numero 2")


#-----------------------------------------------------------------------------

#5.Dado un número real x, construya un programa que permita determinar si el número es positivo, negativo o cero.
numero=int(input("ingrese un numero:"))
if numero > 0:
    print("El numero x es positivo")
elif numero < 0:
    print("El numero x es negativo")
else:
    print("El número x es el neutro para la suma")


#-----------------------------------------------------------------------------

#6.Dado el centro y el radio de un círculo, determinar si un punto de R2 pertenece o no al interior del círculo

centrox=float(input("ingrese la coordenada x del centro de la circunferencia: "))
centroy=float(input("Ingrese la coordenada y del centro de la circunferencia: "))
radio=float(input("Ingrese el valor del radio de la circunferencia: "))
puntox=float(input("Ingrese la coordenada en x del punto que quiere determinar: "))
puntoy=float(input("Ingrese la coordenada en y del punto que quiere determinar: "))
if (puntox-centrox)**2 + (puntoy-centroy)**2 <= radio**2:
    print("El punto (" + str(puntox) + ", " + str(puntoy) + ") pertenece al interior del círculo")
else:
    print("El punto (" + str(puntox) + ", " + str(puntoy) + ") no pertenece al interior del círculo")


#-------------------------------------------------------------------------------


#7.Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triángulo.

lado_a=float(input("Ingrese la longitud del lado a: "))
lado_b=float(input("Ingrese la longitud del lado b: "))
lado_c=float(input("Ingrese la longitud del lado c: "))
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c + lado_a > lado_b:
    print("Es posible crear un triangulo con dichas longitudes en los lados")
else:
    print("No es posible crear un triangulo con dichas longitudes en los lados")


#------------------------------------------------------------------------------

#8.Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado (Utilice match-case).

pais=str(input("Ingrese un pais de America en minusculas para retornar su capital: "))
match pais:
    case "colombia":
        print("bogota")
    case "brasil":
        print("brasilia")
    case "argentina":
        print("buenos aires")
    case "uruguay":
        print("montevideo")
    case "paraguay":
        print("asunsion")
    case "ecuador":
        print("quito")
    case "peru":
        print("lima")
    case "Venezuela":
        print("caracas")
    case "bolivia":
        print("la Paz")
    case "chile":
        print("santiago")
    case "Surinam":
        print("parabarimo")
    case "guyana":
        print("georgetown")
    case "trinidad y tobago":
        print("puerto españa")
    case "antigua y barbuda":
        print("saint john")
    case "bahamas":
        print("nasau")
    case "barbados":
        print("bridgetown")
    case "cuba":
        print("la habana")
    case "dominicana":
        print("roseau")
    case "granada":
        print("saint george")
    case "haiti":
        print("puerto principe")
    case "jamaica":
        print("kingston")
    case "republica dominicana":
        print("santo domingo")
    case "san cristobal y nieves":
        print("basseterre")
    case "san vicente y granadinas":
        print("kingstown")
    case "santa lucia":
        print("castries")
    case "canada":
        print("ottawa")
    case "estados unidos":
        print("washington dc.")
    case "mexico":
        print("ciudad de mexico")
    case "belice":
        print("belmopan")
    case "costa rica":
        print("san jose")
    case "el salvador":
        print("san salvador")
    case "guatemala":
        print("ciudad de guatemala")
    case "honduras":
        print("tegucigalpa")
    case "nicaragua":
        print("managua")
    case "panama":
        print("panama")
    case _:
        print("pais no identificado")