#lista de elementos en modo clave-valor
#diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
#diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Mexico"}
#Arreglos asociativos

persona = {"nombre": "Juan",
            "edad": 25, 
            "Pais": "Colombia"}

#Son modificables pero no se acumulan los valores

# persona["edad"] = 26 #Modifica el valor de la clave "edad"

persona["apodo"] = "Juancho" #Agrega una nueva clave con su valor

"""
print(persona.keys()) #Imprime las claves del diccionario
print(persona.values()) #Imprime los valores del diccionario
print(persona.items()) #Imprime las claves y valores del diccionario
"""

#for key, value in persona.items():
    #print(f"La clave es {key} y el valor es {value}")

print ("direccion" in persona) #Verifica si la clave "direccion" existe en el diccionario   