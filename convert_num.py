def roman_to_int(numeral):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0

    for char in reversed(numeral.upper()):
        value = roman_dict[char]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value

    return total

numeral_input = input("Enter the roman numerals you want to convert: ")
result = roman_to_int(numeral_input)
print(f"The roman numerals you entered translates to: {result}!")


