import os
from management import management

# Zadaváná ID musí být unikátní

os.system('cls')

if __name__ == "__main__":
    last_continue = "ano"
    while last_continue == "ano":
        management()
        last_continue = input("\nChcete pokračovat [ano/ne]?:")
        os.system('cls')
        print()
