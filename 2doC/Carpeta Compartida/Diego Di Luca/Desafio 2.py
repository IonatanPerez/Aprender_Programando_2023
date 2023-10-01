#%%
N1 = int(input("Ingrese el numero 1"))
N2 = int(input("Ingrese el numero 2"))

if N1 == N2:
    print("Ambos numeros son iguales")
else:
    print("Ambos numeros no son iguales")

# %%
condicion = input("Digame si esta lloviendo, o no esta lloviendo")

if condicion == "no esta lloviendo":
    print("Podemos ir a la plaza")
else:
    print("Nos quedaremos en casa")

# %%
lista_numeros = ["2", "4", "6"]
for n in lista_numeros:
    n_ent = int(n)    #Convertir la cadena en un número entero (str ---> int)
    resultado = n_ent + 2
    print(resultado)

# %%
n1 = int(input("Escriba un numero aqui:"))
n2 = int(input("Escriba otro numero aqui:"))
def dividir(n1,n2):
    division = n1/n2
    return division
division = dividir(n1,n2)
print(f"El resultado de esta division es: {division}")

# %%
n1 = int(input("Escriba un numero aqui:"))
n2 = int(input("Escriba otro numero aqui:"))

if n2 == 0:
    print("no se puede realizar esta operación")
else:
    dividir = n1/n2
    print(f"la division entre ambos numeros es: {dividir}")