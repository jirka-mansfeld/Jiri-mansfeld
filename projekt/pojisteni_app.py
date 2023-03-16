from pojistenec import Pojistenec

class PojisteniApp:
    """
    třída se bude starat o chod programu
    """

    def __init__(self):
        self.seznam_pojistencu = []

    def vykresli(self):
        """
        funkce vykreslí na začátku cyklu obrazovku s možnostmi pro uživatele
        """
        print("-------------------------")
        print("Evidence pojištěných")
        print("-------------------------")
        print()
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

    def pridej(self):
        """
        funkce přidává a ukládá uživatele
        """
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení pojištěného:\n")
        vek = input("Zadejte věk:\n")
        telefon = input("Zadejte telefonní číslo:\n")

        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.seznam_pojistencu.append(pojistenec)

        print()
        input("Data byla uložena. Pokračujte libovolnou klávesou...")

    def vypis(self):
        """
        funkce vypisuje všechny pojištěnce
        """
        print()
        for pojistenec in self.seznam_pojistencu:
            print(pojistenec)

        print()
        input("Pokračujte libovolnou klávesou...")

    def vyhledej(self):
        """
        funkce vyhledává pojištěnce
        """
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení:\n")
        vyhledany_pojistenec = False
        print()

        for pojistenec in self.seznam_pojistencu:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                print(pojistenec)
                vyhledany_pojistenec = True

        if vyhledany_pojistenec == False:
            print()
            print("Tento pojištěnec neexistuje!")

        print()
        input("Pokračujte libovolnou klávesou...")

    def zacni(self):
        """
        funkce, která se stará o běh programu
        """
        while True:
            self.vykresli()
            vyber = int(input())

            if vyber == 1:
                self.pridej()
                continue
            elif vyber == 2:
                self.vypis()
                continue
            elif vyber == 3:
                self.vyhledej()
                continue
            elif vyber == 4:
                print("Děkuji za používání programu!")
                break
            else:
                print()
                print("Zadali jste nesprávné číslo, zkuste to znovu!")
                print("Pokračujte libovolnou klávesou...")
                input()
                continue