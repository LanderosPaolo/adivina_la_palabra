# Importar función choice del modulo random 
from random import choice
# Importamos el diccionario que contiene las palabras secretas
import palabras

# Guardamos en variables la categoría y palabra secreta
categoria_secreta = choice(list(palabras.palabra_secreta))
palabra_secreta = choice(list(palabras.palabra_secreta[categoria_secreta]))
print(categoria_secreta)
print(palabra_secreta)

# Creamos una variable que irá formando la palabra y una que mantendrá las otras ocultas
letras_adivinadas = ['_'] * len(palabra_secreta)
letras_ocultas = list(palabra_secreta)

# Creamos la variable que saludara y dará inicio al juego
def inicio_del_juego():
    # Preguntamos el nombre del usuario
    nombre_usuario = input('Ingresa tu nombre: ')
    # Guardamos la respuesta del usuario y la pasamos a minúscula para evitar problemas
    respuesta_usuario = input(f"""- Hola {nombre_usuario}.
Bienvenido/a al juego del ahorcado. ¿quieres jugar?
si/no: """).strip().lower()
    # Un bucle en caso de que conteste algo distinto a si o no
    while respuesta_usuario not in ['si', 'no']:
            respuesta_usuario = input(f"""- Hola {nombre_usuario}.
Necesito saber si quieres jugar o no
si/no: """).strip().lower()
    # Ejecutamos la función letra_usuario, en caso de querer jugar
    letra_usuario(respuesta_usuario, nombre_usuario)

# Creamos la función para comenzar el juego
def letra_usuario(respuesta, nombre):
    vidas = 6
    if(respuesta == 'si'):
        print(f"""- Muy bien, comencemos, te recuerdo que tienes 6 vidas.
{nombre} te daré dos pistas, la palabra tiene un largo de {len(palabra_secreta)} letras
la palabra se encuentra en la categoría {categoria_secreta}""")
        letras_adivinadas = ['_'] * len(palabra_secreta)
        letras_ocultas = list(palabra_secreta)
        # Crear un conjunto para almacenar letras acertadas
        letras_acertadas = set()  
        
        # El juego durará hasta que se acaben las vidas o se complete la palabra
        while vidas > 0:
            letra = input('- Dime una letra cualquiera: ')
            while not letra.isalpha() or len(letra) != 1:
                letra = input(f"""{nombre}, te recuerdo que debes ingresar 1 letra
Dime una letra cualquiera: """)
            # Se le avisa al jugador si ya adivino esa letra
            if letra in letras_acertadas:
                print(f"- Ya adivinaste la letra {letra}")
            elif letra in letras_ocultas:
                print(f"""- Has acertado la letra {letra}""")
                letras_acertadas.add(letra)
                # Bucle for para ir mostrando las letras adivinadas
                for i, l in enumerate(letras_ocultas):
                    # Si l es igual a la letra del jugador se actualiza la lista, al mismo tiempo se reemplaza por un _
                    # para demostrar que ya no es una letra oculta
                    if l == letra:
                        letras_adivinadas[i] = letra
                        letras_ocultas[i] = '_'
                # Se imprime la palabra con las letras adivinadas
                print(' '.join(letras_adivinadas))
                # Si no quedan letras en la palabra oculta, el juego termina felicitando al jugador
                if not '_' in letras_adivinadas:
                    print(f"¡¡Felicidades {nombre}, has adivinado la palabra!!")
                    break
            else:
                # Cada vez que falle al adivinar la letra se le descuenta 1 vida
                vidas -= 1
                # Si las vidas son 0, se le da un aviso de que perdió y se muestra la palabra
                if vidas == 0:
                    print(f"""- Era tu última oportunidad, una lástima!
La palabra era '{palabra_secreta}'""")
                else:
                    # En caso de no acertar se le da un aviso con la cantidad de vidas que quedan
                    print(f"""- No has acertado
{nombre}, te quedan {vidas} vidas""")
    # En caso de que no quiera jugar, se le da un aviso
    else:
        print('Que pena, vuelve luego')

inicio_del_juego()