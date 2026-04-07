from caesar_cipher import encrypt

COMMON_ITALIAN = ["di", "il", "che", "è", "e", "la", "a", "per", "in", "un"]
COMMON_ENGLISH = ["the", "and", "of", "to", "a", "in", "is", "it", "you", "that"]
COMMON_LATIN = ["et", "in", "est", "te", "se", "ad", "non", "ut", "de", "cum", "ave", "per", "sed", "at", "ex"]

def riconoscimento(risultati):
    punteggio_massimo = 0
    tupla_migliore = None
    for chaive, testo in risultati:
        punteggio = 0
        for parola in testo.split():
            if parola.lower() in COMMON_ITALIAN or parola.lower() in COMMON_ENGLISH or parola.lower() in COMMON_LATIN:
                punteggio += 1
        if punteggio > punteggio_massimo:
            punteggio_massimo = punteggio
            tupla_migliore = (chaive, testo)
    return tupla_migliore

def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    risultati = []
    for i in range(26):
        risultati.append((i, encrypt(ciphertext, i)))
    return risultati

def main():
    ciphertext = input("Scrivi la frase da rompere: ")
    risultati = brute_force(ciphertext)
    print("Ecco i possibili risultati")
    for chiave, testo in risultati:
        print(f"Chiave {chiave:2d}: {testo}")
    chiave_migliore, testo_migliore = riconoscimento(risultati)
    print(f"\nIl match più probabile è\nChiave {chiave_migliore}: {testo_migliore}")

if __name__ == "__main__":
    main()