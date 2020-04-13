import time
import random
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], [
    'Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]
points = 0
cantpreg=len(preguntas)
i=cantpreg
print('Inicia el juego de las preguntas')
time.sleep(2)
print('Puntaje : ', points, ' por cada respuesta correcta sumara 10 puntos !!')
print('-'*99)
print('/'*99)
for x in preguntas:
    r=random.randrange(cantpreg)
    while preguntas[r] is None:
        r=random.randrange(cantpreg)
    print('')
    print('Le ha tocado la pregunta nro..',r)
    time.sleep(2)
    print('')
    print('¿', preguntas[r][0], '?')
    print('Ingrese su respuesta ..(si o no)')
    out = str(input()).lower()
    if out == 'si':
        points += 10
        print('Respuesta correcta!! ')
        print('Su puntaje a incrementado a ..', points, ' ◄◄')
    else:
        print('Respuesta Incorrecta')
    time.sleep(2)
    print()
    preguntas[r]=None
    i-=1
    if i!= 0:
        print('-'*99)
        print('/'*99)      
        print('Vamos a la siguente pregunta')
    else:
        print('Se han acabado las preguntas..')
        time.sleep(2)
        print('Su puntaje final es de ',time.strftime('...'),' ',points,' !!!!')
if(points==30):
    print('Excelente contestaste todas las respuestas correctamente')
elif(points==0):
    print('Mas suerte la próxima..')
preguntas.clear()# borro toda la lista auque el ej no me lo pida asi..


