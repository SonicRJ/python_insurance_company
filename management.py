import os
from intro import intro
from insured import Insured

def management():
    
    print(intro)
    
    print("--> Evidence pojištěných <--\n")
    print("Vyberte si akci:")
    print("\t1 - Přidat nového pojištěného")
    print("\t2 - Vypsat všechny pojištěné")
    print("\t3 - Vyhledat pojištěného")
    print("\t4 - Konec")
    
    option = input("Zadání: ")
    
    # Vložení nového pojištěnce na základě jeho unikátního ID nebo jakéhokoli
    # unikátního registračního čísla
    if option == "1":
        os.system('cls')
        new_insured = Insured()
        Insured.data_insured[new_insured.reg_no] = new_insured
        
    # Výpis všech pojištěných
    elif option == "2":
        if Insured.data_insured:
            os.system('cls')
            print("Celkový počet pojištěných.", Insured.get_all_insurance())
            print("\nVýpis s detaily pojištěnců")
            for i, insured in enumerate(Insured.data_insured.values()):
                print("Pojištěnec - ", i + 1)
                insured.get_insured()
                print()
        else:
            print("Žádná data nejsou v evidenci")
         
    # Vyhledání pojištěného podle ID nebo registrační čísla
    elif option == "3":
        os.system('cls')
        reg_no = input("\nZadejte ID pojištěného: ")
        try:
            Insured.data_insured[reg_no].get_insured()
        except:
            print("Zadané ID neevidujeme.")
            
    # Ukončení programu
    elif option == "4":
        os.system('cls')
        exit()