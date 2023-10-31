# Importar funcion choice del modulo random 
from random import choice
# importamos el diccionario que contiene las palabras secretas
import palabras

# guardamos en variables la categoria y palabra secreta
categoria_secreta = choice(list(palabras.palabra_secreta))
palabra_secreta = choice(list(palabras.palabra_secreta[categoria_secreta]))
# print(categoria_secreta)
# print(palabra_secreta)

# creamos una variable que irá formando la palabra y una que mantendra las otras ocultas
letras_adivinadas = ['_'] * len(palabra_secreta)
letras_ocultas = list(palabra_secreta)

# creamos la variable que saludara y dara inicio al juego
def inicio_del_juego():
    # preguntamos el nombre del usuario
    nombre_usuario = input('Ingresa tu nombre: ')
    # guardamos la respuesta del usuario y la pasamos a minuscula para evitar problemas
    respuesta_usuario = input(f"""- Hola {nombre_usuario}.
Bienvenido/a al juego del ahorcado, quieres jugar?
si/no: """).strip().lower()
    # un bucle en caso de que conteste algo distinto a si o no
    while respuesta_usuario not in ['si', 'no']:
            respuesta_usuario = input(f"""- Hola {nombre_usuario}.
necesito saber si quieres jugar o no
si/no: """).strip().lower()
    # ejecutamos la funcion letra_usuario, en caso de querer jugar
    letra_usuario(respuesta_usuario, nombre_usuario)

# creamos la funcion para comenzar el juego
def letra_usuario(respuesta, nombre):
    vidas = 6
    if(respuesta == 'si'):
        print(f"""-Muy bien, comencemos, te recuerdo que tienes 6 vidas.
{nombre} te dare dos pistas, la palabra tiene un largo de {len(palabra_secreta)} letras
la palabra se encuentra en la categoria {categoria_secreta}""")
        letras_adivinadas = ['_'] * len(palabra_secreta)
        letras_ocultas = list(palabra_secreta)
        
        letras_acertadas = set()  # Crear un conjunto para almacenar letras acertadas
        
        # El juego durara hasta que se acaben las vidas o se complete la palabra
        while vidas > 0:
            letra = input('- Dime una letra cualquiera: ')
            while not letra.isalpha() or len(letra) != 1:
                letra = input(f"""{nombre}, te recuerdo que debes ingresar 1 letra
Dime una letra cualquiera: """)
            if letra in letras_acertadas:
                print(f"- Ya adivinaste la letra {letra}")
            elif letra in letras_ocultas:
                print(f"""- Has acertado la letra {letra}""")
                letras_acertadas.add(letra)
                # Bucle for para ir mostrando las letras adivinadas
                for i, l in enumerate(letras_ocultas):
                    # si l es igual a la letra del jugador se actualiza la lista, al mimsmo tiempo se reemplaza por un _
                    # para demostrar que ya no es una letra oculta
                    if l == letra:
                        letras_adivinadas[i] = letra
                        letras_ocultas[i] = '_'
                # Se imprime la palabra con las letras adivinadas
                print(' '.join(letras_adivinadas))
                if not '_' in letras_adivinadas:
                    print(f"Felicidades {nombre}, has adivinado la palabra!!")
                    break
            else:
                vidas -= 1
                if vidas == 0:
                    print(f"""- Era tu última oportunidad, una lástima!
La palabra era {palabra_secreta}""")
                else:
                    print(f"""- No has acertado
{nombre}, te quedan {vidas} vidas""")
        if not letras_ocultas:
            print(f"Felicidades {nombre}, has adivinado la palabra!!")
    else:
        print('Que pena, vuelve luego')

inicio_del_juego()