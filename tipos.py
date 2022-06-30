import random

def types():
    types = ["human", "no human"]

    return types

def human():
    inteligencia = random.randint(3,7)
    fuerza = random.randint(1,6)
    velocidad = random.randint(2,5)
    resistencia = random.randint(2,5)
    energia = random.randint(1,6)
    lucha =  random.randint(1,7)

    return inteligencia, fuerza, velocidad, resistencia, energia, lucha

def not_human():
    inteligencia = random.randint(4,6)
    fuerza = random.randint(1,7)
    velocidad = random.randint(1,7)
    resistencia = random.randint(3,7)
    energia = random.randint(1,7)
    lucha =  random.randint(3,6)

    return inteligencia, fuerza, velocidad, resistencia, energia, lucha