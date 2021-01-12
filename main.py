import random

name = input ("please type your name / por favor escribe to nombre: ")
language = input (f'{name} , English or Español? ')

if language == 'english' :
   mood = input (f'hello {name}, how are you? ') 
   if mood == 'good' :
     positive = input (f'I am so happy to hear you are {mood} {name}! You dont need me then, bye!' )
   if mood == 'bad' :
     negative = input ('oh no! I am sorry :( can i make you feel better?! ' )
   if negative == 'yes' :
     joke = input ('knock knock! ' )
   if joke == 'whos there?' :
     boo = input ('boo ')
   if boo == 'boo who?' : 
     better = input ('oh no! dont cry! it was to make you feel better :D did it work?? ')
   if better == 'yes' :
     happy = input (f'i am glad i could help {name}!' )
   if better == 'no' :
     more = input (f'here is another joke {name}, why was 6 afraid of 9? ')
   if more == 'why?' :
     punchline = input ('because 9, 8, 7! do you feel better now? ')
   if punchline == 'no' :
     funny = input('heres another joke, what do you call a pig who does karate? ')
   if punchline == 'yes' :
     happy2 = input(f'glad i could help {name}! come back if you need more laughs :D GOODBYE! ')
   if funny == 'what?' :
     final_joke = input('a porkchop! you should be feeling better now! Goodbye :D ' )
   if punchline == 'yes' :
     happy2 = input(f'glad i could help {name}! come back if you need more laughs :D GOODBYE! ')

 
if language == 'espanol' :
    mood2 = input (f'hola {name}, como estas? ' )
if mood2 == 'bien':
   positive2 = input (f'Que feliz estoy de escuchar que estas {mood2} {name}! Entonces no me necesitas, adios!' )
if mood2 == 'mal' :
  negative2 = input ('o no! lo siento :( puedo aserte sentir mejor? ' )
if negative2 == 'si' :
  joke2 = input ('porque lloraba el libro de matematicas? ')
if joke2 == 'porque?' :
  better2 = input ('porque tenia muchos problemas :D. te sientes mejor? ')
if better2 == 'si' :
  happy2 = input(f'que bueno que logre ayudar{name}!')
if better2 == 'no' :
  more2 = input (f'aqui va orto chiste {name}, porque fue la computadora al doctor? ')
if more2 == 'porque?' :
  punchline2 = input ('porque tenia un virus! te sientes mejor? ')
if punchline2 == 'no' :
  funny2 = input('entonces te cuento otro chiste, que le dice un semaforo a orto? ')
if punchline2 == 'si' :
  happy3 = input(f'que bueno que  pude ayudar {name}! regresa despues si quieres reir mas :D ADIOS! ')
if funny2 == 'que?' :
  final_joke2 = input('no me mires que me estoy cambiando! deverias de sentirte mejor ahora! Hasta luego :D ' )
if punchline2 == 'si' :
  happy3 = input(f'deverias de sentirte mejor ahora {name}! Hasta luego! ')
 
    
