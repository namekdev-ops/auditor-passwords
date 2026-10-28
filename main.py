import getpass
import secrets
import string



def generar_password(longitud=16):
    alfabeto = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation  
    caracteres = []
    for _ in range(longitud):
        caracteres.append(secrets.choice(alfabeto))
    return "".join(caracteres)


def analizar_caracteres(password):
    tiene_minusculas = False
    tiene_mayusculas = False
    tiene_numero = False
    tiene_simbolo = False
    
    for caracter in password:
        if caracter.islower():
            tiene_minusculas = True
        if caracter.isupper():
            tiene_mayusculas = True
        if caracter.isdigit():
            tiene_numero = True
        if not caracter.isalnum() and not caracter.isspace():
            tiene_simbolo = True
            
    return {
        
        'minusculas' : tiene_minusculas,
        'mayusculas' : tiene_mayusculas,
        'numeros' : tiene_numero,
        'simbolos': tiene_simbolo,
    }
    
    
def calcular_puntaje(password, tipos):
    puntaje = 0
    if len(password) >= 16:
        puntaje += 40
    elif len(password) >=12:
        puntaje += 30
    elif len(password) >= 8:
        puntaje += 15
    if tipos["minusculas"]:
        puntaje += 10
    if tipos["mayusculas"]:
        puntaje += 10
    if tipos["numeros"]:
        puntaje += 15
    if tipos["simbolos"]:
        puntaje += 25
    if len(password) < 8:
        puntaje = min(puntaje, 30)
    return puntaje


def clasificar(puntaje):
    if puntaje >= 85:
        return 'Contrasena es muy fuerte'
    elif puntaje >= 65:
        return 'Contrasena es fuerte'
    elif puntaje >= 45:
        return 'Contrasena es media'
    elif puntaje >= 25:
        return 'Contrasena es debil'
    elif puntaje < 25:
        return 'Contrasena extremadamente debil'
    
def dar_recomendaciones(password, tipos):
    recomendaciones = []
    
    if len(password) < 12:
        recomendaciones.append('Usa al menos 12 caracteres (es mejor si son 16 o mas).')
    if not tipos["minusculas"]:
        recomendaciones.append("Agrega letras minúsculas.")    
    if not tipos["mayusculas"]:
        recomendaciones.append("Agrega letras mayusculas.")     
    if not tipos["numeros"]:
        recomendaciones.append("Agrega numeros.")
    if not tipos["simbolos"]:
        recomendaciones.append("Agrega simbolos")
    if len(recomendaciones) == 0:
        recomendaciones.append("¡Excelente! No hay mejoras obvias.")
    return recomendaciones
    
def auditar_password():
    password = getpass.getpass('Inserte su password a auditar: ')
    print(f'Tu password tiene {len(password)} caracteres')
        
    tipos = analizar_caracteres(password)
    print(tipos)
    puntaje = calcular_puntaje(password, tipos)
    nivel = clasificar(puntaje)
    print(f"Puntaje: {puntaje}/100")
    print(f"Nivel: {nivel}")
    
    recomendaciones = dar_recomendaciones(password, tipos)
    for recomendacion in recomendaciones:
        print(f"- {recomendacion}")
        
    
def menu():
    while True:
        print("\n===== AUDITOR DE CONTRASEÑAS =====")
        print("1. Auditar una contraseña")
        print("2. Generar una contraseña segura")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")
        if opcion == "1":
            auditar_password()
        elif opcion == "2":
            longitud = int(input("Longitud de la contraseña (recomendado 16 o más): "))
            print(f"Contraseña generada: {generar_password(longitud)}")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()