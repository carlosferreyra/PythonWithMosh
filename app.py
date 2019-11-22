"""print("Hello World") #Imprime hola mundo
print('*'*10) #Imprime un string de 10 concatenaciones de '*'
x = input("Input :")
print("hello , " + x)"""
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

class Point:
    private name =
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")
