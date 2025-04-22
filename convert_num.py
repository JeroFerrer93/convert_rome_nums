def roman_to_int(numeral):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(numeral.upper()):
        if char not in roman_dict:
            print(f"⚠️ Carácter inválido: '{char}'")
            return None
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value

    return total

# Agregamos esta línea como introducción:
print("ℹ️ Los números romanos son:\nI = 1\nV = 5\nX = 10\nL = 50\nC = 100\nD = 500\nM = 1000\n")

numeral_input = input("📝 Ingresá los números romanos que querés convertir: ")

result = roman_to_int(numeral_input)

if result is not None:
    print(f"✅ El número decimal equivalente es: {result}!")
else:
    print("❌ Ingreso inválido. Por favor usá solo caracteres romanos válidos.")



