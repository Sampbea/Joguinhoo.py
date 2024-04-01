import random
import os

number = random.randint(1, 10)

guess = input("Vamos brincar! Tente adivinhar o número de 1 a 10: ")
guess = int(guess)

if guess == number:
    print("você venceu!")
else:
    print("você errou :( . O número correto era:", number)
