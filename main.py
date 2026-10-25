import getpass


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