
CODIGOS_PAIS = {
    "Argentina": "ar",
    "Brasil": "br",
    "Francia": "fr",
    "España": "es",
    "Alemania": "de",
    "Portugal": "pt",
    "Inglaterra": "gb-eng",
    "Uruguay": "uy",
    "Mexico": "mx",
    "México": "mx",
    "Estados Unidos": "us",
    "Italia": "it",
}


def url_bandera(pais, tamano="w320"):
    
    #Devuelve la URL de la bandera de un país desde flagcdn.com.
    #de cualquier tamaño
    #Si el país no está en el diccionario, devuelve None.
    
    codigo = CODIGOS_PAIS.get(pais)
    if not codigo:
        return None
    return f"https://flagcdn.com/{tamano}/{codigo}.png"