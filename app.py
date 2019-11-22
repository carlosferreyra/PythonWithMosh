from ecommerce.shipping import calc_shipping
from pathlib import Path
import random

"""print("Hello World") #Imprime hola mundo
print('*'*10) #Imprime un string de 10 concatenaciones de '*'
x = input("Input :")
print("hello , " + x)
entry = input('>')
words = entry.split(' ')
emojis = {
    ":)": "😊",
    ":(": "☹"

}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)


def greet_user(name):
    print(f"Hello {name}")


class Person:
    def __init__(self,aName,aLastName,aAddress):
        self.__Name = aName
        self.__LastName = aLastName
        self.__Address = aAddress
    def GetName(self):
        return self.__Name

    def move(self):
        print("Move")

    def talk(self):
        print("Draw")



for x in range(3):
    random.random()
    random.randint(10,20)
    print(random.choice(["Juan","Pedro","Ana"]))
"""
path = Path()
for file in path.glob("*"):
    print(file)

