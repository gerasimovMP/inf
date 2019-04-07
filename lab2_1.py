from random import getrandbits
from random import randint


# наибольший общий делитель
def nod(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(module):
    required_set = set(num for num in range(1, module) if nod(num, module) == 1)
    for g in range(1, module):
        actual_set = set(g**powers % module for powers in range(1, module))
        if required_set == actual_set:
            return g




def toBinary(n):
    r = []
    while (n > 0):
        r.append(n % 2)
        n = n / 2
        return r

def MillerRabin(n, s = 5):  
    for j in range(1, s + 1):
            a = randint(1, n - 1)
            b = toBinary(n - 1)
            d = 1
            for i in range(len(b) - 1, -1, -1):
                x = d
                d = (d * d) % n
                if d == 1 and x != 1 and x != n - 1:
                    return True 
                if b[i] == 1:
                    d = (d * a) % n
                    if d != 1:
                        return True 
                    return False 
            
# Создание приватных ключей
alice_private = randint(1, 10)
print('Приватный ключ Алисы', alice_private)
bob_private = randint(1, 10)
print('Приватный ключ Боба', bob_private)

# Создание простого числа и его первообразного корня по модулю P
fg = True 
while fg:
    p = randint(2,100)
    if not (MillerRabin(p)):
        fg = False
    
#p = get_random_prime()
g = primitive_root(p)

print('Простое число: p =', p)
print('Первообразный корень по модулю p: g =', g)

# Создание публичных ключей
alice_public = g**alice_private % p
bob_public = g**bob_private % p

print('Публичный ключ Алисы', alice_public)
print('Публичный ключ Боба', bob_public)

alice_key = (bob_public**alice_private) % p
bob_key = (alice_public**bob_private) % p

print('Секретный ключ(Алиса/Боб):', alice_key, "==", bob_key)

