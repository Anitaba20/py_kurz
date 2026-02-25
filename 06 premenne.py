# 7 Premenné (Variables)
# Pravidlá
# Premennú vytváram ja – názov, množstvo...
# Lepšie dávať premennej anglické názvy
# Pozor na názvy, ktoré ma Python zadefinované na niečo iné
# V názve premennej nemá byť medzera, v outpute bude error
#
# Premenná – do premennej, ktorú som vytvorila si uložím nejakú hodnotu
# Pr.
# name = „Anita“
# age = 45
# height = 160.2
# isDeveloper = True
#
# name, age, height, isDeveloper sú premenné, ktoré som vytvorila a potrebujem s nimi pracovať
# do každej premennej som vložila hodnotu
#
# name  je názov premennej
# „Anita“ je hodnota, DT string – preto je úvodzovkách

# Pr. 1
name = "A"
age = 45
height = 160.2
isDeveloper = True

print(name)
print(age)
print(height)
print(isDeveloper)

# output:
# Anita
# 45
# 160.2
# True

# druhý výstup: ak chcem mať v outpute aj ďalší text:
print("Meno: " + name)
print("Vek: " + str(age))
print("Výška " + str(height))
print("Je programátor: " + str(isDeveloper))

# output:
# Meno: Anita
# Vek: 45
# Výška 160.2
# Je programátor: True

# Pr. 2
number1 = 5
number2 = 10
print(number1 + number2)
# 15


number3 = 1.5
number4 =1.5
print(number3 + number4)
# 3.0