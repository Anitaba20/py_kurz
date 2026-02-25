# 5 Operácie s číslami
# +, -, *, /, //, %, **
# Súčet				            print(2+2)
# Odpočítavanie 			    print(2-2)
# Násobenie				        print(2*2)
# Delenie				        print(2/2)
# Celočíselné delenie		    print(3//2)		notes: zaokrúhľuje smerom dole
# Zvyšok po delení			    print(3%3)
# Exponent				        print(3**2)
# Priority ako v matematike 	print(2+2*3)
# Zátvorkové priority 		    print((2+3)*3)
#
# V programovacom jazyku Python vykonávam operácie s číslami:
# súčet,
# odpočítavanie,
# násobenie,
# delenie,
# celočíselné delenie,
# zvyšok po delení,
# exponent,
# priority ako v matematike, zátvorkové priority.


# Operácie s číslami – funkcia print
# Celočíselné delenie zaokrúhľuje smerom dole.
print(36/5)
# 7.2
print(36//5)
# 7

# Zátvorkové priority
# Násobenie má prednosť pred súčtom
# (2+3*3) – 3*3 je 9 +2 = 11
print(2+3*3)

# Exponent
# 3**2 = 3 na 2=9
print(3**2)

# Zvyšok po delení
# 10/4 = 2
# 2*4 = 8, zvyšok je 2
print(10%4)


# Operácie s číslami vs DT
# Matematická operácia súčet vs DT
# matematická operácia +, rovnaké DT, float + float
print(1.5+1.5)
# 3.0

# matematická operácia +, rovnaké DT, int + int
print(2+2)
# 4

# matematická operácia +, rovnaké DT, int + float
print(2+1.5)
# 3,5

# matematická operácia +, rovnaké DT, str + str
print("36 " + "Test")
# 36 Test

# rôznde DT, integer + string – vyhodí error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(36 + "Test")