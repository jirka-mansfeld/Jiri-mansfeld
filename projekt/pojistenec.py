
class Pojistenec:
    """
    třída pojištěnců, kteří si založí pojistění
    """

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self.__jmeno = jmeno
        self.__prijmeni = prijmeni
        self.__vek = vek
        self.__telefon = telefonni_cislo

    def __str__(self):
        """
        :return: vrací textovou podobu instancí
        """
        return f"{self.__jmeno.ljust(10, ' ')}" \
               f"{self.__prijmeni.ljust(12, ' ')}" \
               f"{self.__vek.ljust(8, ' ')}" \
               f"{self.__telefon}"


