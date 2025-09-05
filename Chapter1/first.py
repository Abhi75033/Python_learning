print("Printing jokes.....")
import pyjokes
from time import sleep

joke = pyjokes.get_jokes()

def printJokes(jokes):
    for joke in jokes:
        print(joke)
        sleep(2)

printJokes(joke)