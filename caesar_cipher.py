def characht(c:str, upper:bool, key:int):
    if upper==True:
        c = ord(c) - 65
        c = (c + key) % 26
        c += 65
        c = chr(c)
    else:
        c = ord(c) - 97
        c = (c + key) % 26
        c += 97
        c = chr(c)
    return c


def encrypt(text:str, key:int)->str:
    testo = list(text)
    testo_cifrato = []

    for c in testo:
        if c.isalpha() and c.isascii():
            if c.isupper()==True:
                upper = True
                testo_cifrato.append(characht(c, upper, key))
            else:
                upper = False
                testo_cifrato.append(characht(c, upper, key))

        else: testo_cifrato.append(c)
    return ''.join(testo_cifrato)

def main():

    scelta = input("Scegli se cifrare (1), decifrare (2), uscire(3): ")

    while scelta != "1" and scelta != "2" and scelta != "3":
        print("Scelta non valida")
        scelta = input("Scegli se cifrare (1), decifrare (2), uscire(3): ")

    while scelta != "3":
        testo_cifrato = []
        if scelta == "1":
            text = input("Testo da cifrare: ")
            key = int(input("Chiave: "))
            testo_cifrato = encrypt(text, key)
        else:
            text = input("Testo da decifrare: ")
            key = int(input("Chiave: "))
            key = -key
            testo_cifrato = encrypt(text, key)

        for c in testo_cifrato:
            print(c, end="")

        scelta = input("\nScegli se cifrare (1), decifrare (2), uscire(3): ")

        while scelta != "1" and scelta != "2" and scelta != "3":
            print("Scelta non valida")
            scelta = input("Scegli se cifrare (1), decifrare (2), uscire(3): ")

    print("Uscita dal programma.")

if __name__ == "__main__":
    main()