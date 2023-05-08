class RomanNumerals:
    @staticmethod
    def to_roman(val):
        # Define a dictionary of Roman numeral symbols and their decimal values
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        # Initialize an empty string to store the Roman numeral representation
        roman_numeral = ''
        # Loop through the Roman numeral symbols and their corresponding decimal values
        for numeral, symbol in roman_numerals.items():
            # Add the symbol to the Roman numeral representation as many times as possible
            while val >= numeral:
                roman_numeral += symbol
                val -= numeral
        return roman_numeral

    @staticmethod
    def from_roman(roman_num):
        # Define a dictionary of Roman numeral symbols and their decimal values
        roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        # Initialize the decimal value to 0
        decimal_value = 0
        # Loop through the Roman numeral characters and their corresponding decimal values
        for i in range(len(roman_num)):
            # Get the decimal value of the current symbol
            value = roman_numerals[roman_num[i]]
            # If the next symbol has a greater value, subtract the current value
            if i + 1 < len(roman_num) and roman_numerals[roman_num[i + 1]] > value:
                decimal_value -= value
            # Otherwise, add the current value to the total
            else:
                decimal_value += value
        return decimal_value
