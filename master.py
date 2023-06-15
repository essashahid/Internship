def roman_numbers(roman_num):
    roman_numbers_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

    if roman_num in roman_numbers_dict:
        return roman_numbers_dict[roman_num]
    else:
        return 0


def english_numbers(english_num):
    english_numbers_dict = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 50: "L", 100: "C"
    }

    if english_num in english_numbers_dict:
        return english_numbers_dict[english_num]
    else:
        return 0


def find_largest_num_less_than_num(num):
    roman_numbers_dict = {100: 100, 50: 50, 10: 10, 9: 9, 5: 5, 4: 4, 1: 1}

    for key in roman_numbers_dict:
        if num >= key:
            return key

    return 0


def convert_roman_to_english(roman_num):
    count = roman_numbers(roman_num)

    if count != 0:
        return count

    for i in range(len(roman_num)):
        try:
            if roman_numbers(roman_num[i]) >= roman_numbers(roman_num[i+1]):
                count += roman_numbers(roman_num[i])
            else:
                count -= roman_numbers(roman_num[i])
        except IndexError:
            count += roman_numbers(roman_num[-1])

    return count


def convert_english_to_roman(english_num):
    roman_num = ""
    
    while english_num != 0:
        largest_num = find_largest_num_less_than_num(english_num)
        roman_num += english_numbers(largest_num)
        english_num -= largest_num

    return roman_num

test_case_input = input("Enter the number of test cases: ")
input_list = []

for i in range(int(test_case_input)):
    print("Enter test case:", i+1)
    user_input = input().upper()
    user_input_split = user_input.split("+")
    first_num = convert_roman_to_english(user_input_split[0])
    second_num = convert_roman_to_english(user_input_split[1])
    sum_of_num = first_num + second_num

    result = convert_english_to_roman(sum_of_num)
    print("Result:", result)
