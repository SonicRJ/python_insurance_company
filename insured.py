class Insured:
    data_insured = {}
    
    # konstruktor
    def __init__(self):
        self.reg_no = input("\nZadejte ID pojištěného: ")
        self.name = input("Zadejte jméno pojištěného: ")
        self.surname = input("Zadejte příjmení: ")
        self.phone = input("Zadejte telefonní číslo: ")
        self.age = input("Zadejte věk: ")
        self.get_insured()
        print("\nData byla uložena.")
        
    # get data
    def get_insured(self):
        print("\n-->Detaily pojištěného<--\n")
        print("\tReg. číslo:", self.reg_no)
        print("\tJméno:", self.name)
        print("\tPříjmení:", self.surname)
        print("\tVěk:", self.age)
        print("\tTelefonní číslo:", self.phone)
        
    # Metoda třídy je metoda, která je vázána na třídu
    # Zde jsem ji použil na celkový počet pojištěnců
    @classmethod
    def get_all_insurance(cls):
        return len(cls.data_insured)
    