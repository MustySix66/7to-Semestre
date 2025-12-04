import unicodedata

def limpiar_texto(texto):
    """Elimina acentos y convierte a mayúsculas."""
    if not texto:
        return ""
    texto = texto.upper()
    # Normalizar para separar acentos de letras y eliminarlos
    texto = ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))
    # Reemplazar Ñ por X (regla común en sistemas, aunque la regla oficial a veces varía)
    return texto.replace('Ñ', 'X')

def obtener_primera_vocal_interna(palabra):
    vocales = "AEIOU"
    # Empezamos desde el índice 1 (segunda letra)
    for letra in palabra[1:]:
        if letra in vocales:
            return letra
    return "X"

def generar_inicio_curp(nombre, paterno, materno):
    # 1. Limpieza de datos
    nombre = limpiar_texto(nombre)
    paterno = limpiar_texto(paterno)
    materno = limpiar_texto(materno)

    # Prevenir errores si los campos están vacíos
    if not paterno or not nombre:
        return "ERROR: Faltan datos obligatorios"

    # --- REGLA 1 y 2: Apellido Paterno ---
    letra1 = paterno[0]
    letra2 = obtener_primera_vocal_interna(paterno)

    # --- REGLA 3: Apellido Materno ---
    letra3 = materno[0] if materno else 'X'

    # --- REGLA 4: Nombre ---
    # Regla: Si el nombre es compuesto y empieza con JOSE o MARIA, se usa el segundo nombre
    # Ejemplo: Jose Antonio -> A, Maria Guadalupe -> G
    nombres_lista = nombre.split()
    letra4 = nombres_lista[0][0] # Por defecto, la primera del primer nombre
    
    nom_comunes = ["JOSE", "MARIA", "MA.", "MA", "J.", "J"]
    
    if len(nombres_lista) > 1:
        if nombres_lista[0] in nom_comunes:
            letra4 = nombres_lista[1][0]

    curp_inicial = f"{letra1}{letra2}{letra3}{letra4}"

    # --- REGLA 5: Palabras Inconvenientes ---
    # Lista oficial (resumida) de palabras que no pueden ir en la CURP
    palabras_prohibidas = {
        "BUEI", "BUEY", "CACA", "CACO", "CAGA", "CAGO", "CAKA", "CAKO",
        "COGE", "COJA", "COJE", "COJI", "COJO", "CULO", "FETO", "GUEY",
        "JOTO", "KACA", "KACO", "KAGA", "KAGO", "KOGE", "KOJO", "KULO",
        "MAME", "MAMO", "MEAR", "MEAS", "MEON", "MIAR", "MION", "MOCO",
        "MULA", "PEDA", "PEDO", "PENE", "PUTA", "PUTO", "QULO", "RATA", "RUIN"
    }

    if curp_inicial in palabras_prohibidas:
        # Se cambia la segunda letra por X
        curp_inicial = f"{curp_inicial[0]}X{curp_inicial[2]}{curp_inicial[3]}"

    return curp_inicial

# --- Ejemplos de prueba ---
print(f"Normal: {generar_inicio_curp('Sergio Alejandro', 'Avila', 'martinez')}")         # PELJ