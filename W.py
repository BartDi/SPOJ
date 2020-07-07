print("Wyślij wiadomość")
mess = input()
lista = mess.split()
i = 0
while i < len(lista):
    word=lista[i]
    cap=word.capitalize()
    lista[i]=cap
    i += 1
for x in lista:
    print(x, end='')
