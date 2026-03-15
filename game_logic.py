from secret_number import seed_secret_numbers, generate_secret_number
from response import respuesta

seed =int(input("Enter a seed number:\n"))
seed_secret_numbers(seed)
numero_aleatorio = generate_secret_number()
intentos = 0
correctas = False
while not correctas:
    guess = int ( input("What is your guess?\n"))
    intentos += 1
    mensaje, correctas = respuesta(numero_aleatorio, guess)
    print(mensaje)
print(f"It took you {intentos} tries!")