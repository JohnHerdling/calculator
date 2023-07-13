#calculator
number_1 = int(input("Bitte geben Sie die erste Zahl (Ganzzahlen) ein: "))
number_2 = int(input("Bitte geben Sie die zweite Zahl (Ganzzahlen) ein: "))

calculation = input('''Sie können nun Addieren (+), Subtrahieren(-), Multiplizieren (*) und Dividieren (/).
Wählen Sie nun ihre Rechenart (Zeichen) aus: ''')

if calculation == "+":
    result = number_1 + number_2
    print(result)
if calculation == "-":
    result = number_1 - number_2
    print(result)
if calculation == "*":
    result = number_1 * number_2
    print(result)
if calculation == "/":
    result = number_1 / number_2
    print(result)




