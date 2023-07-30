# importando a fila
from lib.queue import Queue

# Cria uma fila vazia
fila = Queue() 

# Insere algumas pessoas na fila

fila.enqueue('Leotildes')
fila.enqueue('Orizimbo')
fila.enqueue('Valdisney')
fila.enqueue('Orozimbo')

print(fila)

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

fila.enqueue('Marcinéia')
print(fila)

proximo = fila.peek()
print(f"Próximo a ser atendido: {proximo}")
print(fila)