
class Pojistenec:
    """
    třída pojištěnců, kteří si založí pojistění
    """

    def __init__(self, jmeno, prijmeni, vek, telefonni_cislo):
        self._jmeno = jmeno
        self._prijmeni = prijmeni
        self._vek = vek
        self._telefon = telefonni_cislo

    def __str__(self):
        """
        :return: vrací textovou podobu instancí
        """
        return f"{self._jmeno.ljust(10, ' ')}" \
               f"{self._prijmeni.ljust(12, ' ')}" \
               f"{self._vek.ljust(8, ' ')}" \
               f"{self._telefon}"

    @property
    def jmeno(self):
        return self._jmeno

    @property
    def prijmeni(self):
        return self._prijmeni


