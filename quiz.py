#!/usr/bin/env python3
# BY rvpmin
# LICENSE GNU/GPL

#Simple quiz

def validate_True_False(text):
    text = text.lower()
    if ('falso' in text) or ('verdadero' in text):
        return True
        # print('Respuesta valida')
    else:
        return False


print('El Sol y la Luna tienen el mismo radio aparente?')
print('[Falso/Verdadero]')


answer = False

while not answer:
    text = input('>')
    text = text.lower()
    if validate_True_False(text):
        if 'verdadero' in text:
            print('Respuesta correcta!')
        else:
            print('Respuesta incorrecta :(')
    else:
        answer = False
#tarea: hacer otra pregunta con 4 opciones :p
