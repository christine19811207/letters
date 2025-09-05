def count_letters_and_numbers(input_string):
    if not isinstance(input_string, str):
        return 0

    letter_count = 0
    number_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    return (letter_count, number_count)
def number_to_english(number):
    if not isinstance(number, (int, float)) or not (-1000 <= number <= 1000):
        return 'Not a valid input'
    if number < 0:
        return "minus " + number_to_english(abs(number))
    elif number == 0:
        return "zero"
    ones =["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 < number < 10:
        return ones[int(number)]
    elif 10 <= number < 20:
        return teens[int(number) -10]
    elif 20 <= number < 100:
        if number % 10 == 0:
            return tens[int(number) // 10]
        else:
            return tens[int(number) // 10] + "-" + ones[int(number) % 10]
    elif 100 <= number < 1000:
        hundreds_part = ones[int(number) // 100] + " hundred"
        remainder = number % 100
        if remainder == 0:
            return hundreds_part
        else:
            return hundreds_part + " " + number_to_english(remainder)
    elif number == 1000:
        return "one thousand"

