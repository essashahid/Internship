def convert_to_roman(roman_num):
    roman_to_english: dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

    if roman_num in roman_to_english:
        return roman_to_english[roman_num]
    else:
        return 0


def convert_to_english_numbers(english_num):
    english_to_roman: dict = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 50: "L", 100: "C"
    }

    if english_num in english_to_roman:
        return english_to_roman[english_num]
    else:
        return 0


def find_largest_num_less_than_num(num):
    roman_to_decimal = {100: 100, 50: 50, 10: 10, 9: 9, 5: 5, 4: 4, 1: 1}

    for key in sorted(roman_to_decimal.keys(), reverse=True):
        if num >= roman_to_decimal[key]:
            return roman_to_decimal[key]

    return 0


def convert_roman_to_english(roman_num):
    count = convert_to_roman(roman_num)

    if count:
        return count

    for i in range(len(roman_num)):
        try:
            if convert_to_roman(roman_num[i]) >= convert_to_roman(roman_num[i+1]):
                count += convert_to_roman(roman_num[i])
            else:
                count -= convert_to_roman(roman_num[i])
        except IndexError:
            count += convert_to_roman(roman_num[-1])

    return count


def convert_english_to_roman(english_num):
    roman_num = ""

    while english_num != 0:
        largest_num = find_largest_num_less_than_num(english_num)
        roman_num += convert_to_english_numbers(largest_num)
        english_num -= largest_num

    return roman_num


def process_test_cases():

    test_case_count = int(input())

    for _ in range(test_case_count):

        expression = input().upper()

        roman_operand1, roman_operand2 = expression.split("+")

        integer_operand1 = convert_roman_to_english(roman_operand1)
        integer_operand2 = convert_roman_to_english(roman_operand2)

        sum_of_integers = integer_operand1 + integer_operand2
        roman_result = convert_english_to_roman(sum_of_integers)

        print(roman_result)


process_test_cases()
