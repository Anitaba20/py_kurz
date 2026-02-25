import dis

def pozdrav():
    print("Ahoj")

dis.dis(pozdrav)


# 3️ Ako si pozrieť vlastný bytecode 👀
#
# Môžeš použiť modul dis.
#
# Príklad:
#
# import dis
#
# def pozdrav():
#     print("Ahoj")
#
# dis.dis(pozdrav)
#
# Výstup bude vyzerať približne takto:
#
#   2          0 LOAD_GLOBAL              0 (print)
#               2 LOAD_CONST               1 ('Ahoj')
#               4 CALL_FUNCTION            1
#               6 RETURN_VALUE
#
# To je bytecode.
#
# Nie sú to ešte 0 a 1, ale inštrukcie pre Python Virtual Machine.
#
# 🔥 Mini zhrnutie
# Jazyk		    Ako funguje			        Rýchlosť
# C			    kompilovaný			        veľmi rýchly
# Python		interpretovaný + bytecode	trochu pomalší
#
