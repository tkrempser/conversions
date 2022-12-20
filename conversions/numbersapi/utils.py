from math import floor, log

ones_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

teens_dict = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

tens_dict = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

exponentials_dict = {
    0: "hundred",
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion",
    5: "quadrillion",
    6: "quintillion",
}


def convert_number_to_words(num):
    """
    Converts a given integer number to English words.

    Args:
        num (int): The integer to be converted. Must be equal to or less than 9223372036854775807 and equal to or greater than -9223372036854775807.

    Returns:
        A string describing the number as English words.
    """
    if isinstance(num, int):
        if num < 0:
            return " ".join(["negative", convert_number_to_words(-num)])
        elif num < 10:
            return ones_dict[num]
        elif num < 20:
            return teens_dict[num]
        elif num < 100:
            div, mod = divmod(num, 10)
            if mod:
                return f"{tens_dict[div]}-{convert_number_to_words(mod)}"
            else:
                return tens_dict[div]
        elif num < 1000:
            return exponential_helper(num, 100)
        elif num < 1000**2:
            return exponential_helper(num, 1000)
        elif num < 1000**3:
            return exponential_helper(num, 1000**2)
        elif num < 1000**4:
            return exponential_helper(num, 1000**3)
        elif num < 1000**5:
            return exponential_helper(num, 1000**4)
        elif num < 1000**6:
            return exponential_helper(num, 1000**5)
        elif num < 9223372036854775808:  # Django's BigIntegerField fits 64-bits numbers
            return exponential_helper(num, 1000**6)
        else:
            raise NotImplementedError("The absolute value of the given integer is greater than 9223372036854775807.")
    else:
        raise TypeError("An integer type number was not provided.")


def exponential_helper(num, magnitude):
    div, mod = divmod(num, magnitude)
    div_words = convert_number_to_words(div)
    exp = floor(log(num) / log(1000))
    if mod:
        return f"{div_words} {exponentials_dict[exp]} {convert_number_to_words(mod)}"
    else:
        return f"{div_words} {exponentials_dict[exp]}"
