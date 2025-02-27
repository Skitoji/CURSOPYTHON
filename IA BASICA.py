import re
from sympy import sympify, SympifyError
import unicodedata

# Función para quitar acentos y normalizar texto
def normalizar_texto(texto):
    texto = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto if not unicodedata.combining(c)).lower().strip()

# Función para cálculos con sympy
def calcular(expresion):
    try:
        resultado = sympify(expresion)
        return f"El resultado es: {resultado}"
    except SympifyError:
        return "No pude entender esa expresión. Usa operadores como +, -, *, / o funciones como sqrt(4)."
    except Exception as e:
        return f"Error en el cálculo: {str(e)}. Intenta algo más simple."

# Función para charlar con más respuestas
def charlar(mensaje):
    mensaje_normalizado = normalizar_texto(mensaje)
    
    respuestas = {
        "hola": "¡Hola! ¿Qué tal?",
        "cómo estás": "Estoy genial, gracias por preguntar. ¿Y tú?",
        "qué haces": "Aquí estoy, charlando y resolviendo problemas. ¿En qué piensas?",
        "adiós": "¡Nos vemos! Que tengas un buen día.",
        "gracias": "¡De nada! Siempre un placer.",
        "qué eres": "Soy una IA básica creada para ayudar con cálculos y charlas. ¡Pruébame!",
        "cuál es tu nombre": "Me llaman Grok, o algo así. ¿Cómo te llamas tú?",
        "qué hora es": "No tengo reloj, pero si me dices dónde estás, puedo buscarlo.",
        "cuéntame un chiste": "¿Por qué el matemático prefería el oscuro? Porque la luz lo hacía dividir.",
        "qué piensas": "Pienso que el universo es fascinante. ¿Tú qué opinas?",
        "te amo": "¡Qué dulce! Yo también te aprecio, a mi manera robótica.",
        "estás vivo": "No exactamente, pero estoy aquí para simularlo bastante bien.",
        "cuál es el sentido de la vida": "Dicen que es 42, pero creo que es encontrar tus propias respuestas. ¿Tú qué crees?"
    }
    
    for clave, valor in respuestas.items():
        clave_normalizada = normalizar_texto(clave)
        if clave_normalizada in mensaje_normalizado:
            return valor
    return "No sé qué responder a eso. ¿Quieres charlar más o que calcule algo?"

# Función principal de la IA
def ia_basica():
    print("Hola, soy tu IA mejorada. Puedo resolver cálculos (como '2 + 3' o 'sqrt(9)') o charlar. Escribe 'salir' para terminar.")
    
    # Patrón más estricto para detectar cálculos
    patron_calculo = re.compile(r'^\s*[0-9+\-*/\(\)\.\s]+|sqrt|sin|cos|tan|log|exp', re.IGNORECASE)
    
    while True:
        entrada = input("Tú: ").strip()
        
        # Salir del programa
        if normalizar_texto(entrada) == "salir":
            print("¡Adiós! Hasta la próxima.")
            break
        
        # Verificar si es un cálculo puro (empieza con números u operadores)
        if patron_calculo.match(entrada) and not any(palabra in normalizar_texto(entrada) for palabra in ["qué", "cuál", "cómo", "dime"]):
            respuesta = calcular(entrada)
        else:
            # Si no, asumimos que es charla
            respuesta = charlar(entrada)
        
        print("IA:", respuesta)

# Inicia la IA
if __name__ == "__main__":
    # Requiere instalar sympy: pip install sympy
    ia_basica()