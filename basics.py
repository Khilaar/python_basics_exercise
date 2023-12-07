
#String checker
"""
def is_string(word):
    if type(word) is str:
        print("Its a string")
    else:
        print("Its not a string")

is_string("0")

"""


#Spaces and Digits
"""
def is_only_string(arg):
    if type(arg) == str:
        if arg.isalpha():
            return True
        else:
            return False
    else:
        return False

print(is_only_string("ab c"))
"""


#Number yooo? I made to many ifs but it is what it is
"""
def is_alphanumeric(arg):
    if isinstance(arg, list):
        return False
    elif type(arg) == dict:
        return False
    elif type(arg) == int or float and type(arg) != str:
        return False
    elif type(arg) == str:
        if arg.isdigit():
            return True
        else:
            return False


print(is_alphanumeric(9))
"""


#Lists & Tuples
"""
def is_tuple(arg):
    test = type(arg) is tuple or type(arg) is list
    print(test)

is_tuple("15")
"""


#Same Type
"""
def check_same_type(arg):
    first = arg[0]
    if len(arg) < 2:
        return True
    else:
        for i, el in enumerate(arg):
            if el != first:
                return False
            elif i == len(arg) -1:
                return True
            else:
                continue


print(check_same_type(["a", "a", "a", "0"]))
"""


#Sort and Remove Duplicates
"""
def sort_that(arg, arg2):
    new_string = ""
    for letter in arg:
        if letter not in new_string:
            new_string += letter
        else:
            continue

    for letter in arg2:
        if letter not in new_string:
            new_string += letter
        else:
            continue
    print(sorted(new_string))

sort_that("bdzac", "def")
"""



#Digits Converter
"""
def converter(arg):
    strigified = str(arg)
    new_list = []
    for el in strigified:
        new_list.append(el)
    new_list = sorted(new_list)[::-1]
    print(new_list)


converter(11145855511231)
"""


#Count Repetitions!
"""
def count_reps(arg):
    new_dict = {}
    for el in arg:
        new_dict[el] = 0
    for el in arg:
        new_dict[el] += 1
    print(new_dict)


count_reps(["janik", "Miachael", "Luca", "Luca", "Luca", "Luca"])
"""


#Cat and Mouse
"""
def cat_mouse(arg):
    for i, el in enumerate(arg):
        if el == "C":
            if arg[i+1] == "m":
                print("catched mouse 1 jump")
            elif arg[i+2] == "m":
                print("catched mouse 2 jumps")
            elif arg[i + 3] == "m":
                print("catched mouse 3 jumps")
            else:
                print("Not catched")

cat_mouse("..C..m")
"""


#Split the Bill
"""
group = {
    'Amy': 20,
    'Bill': 15,
    'Chris': 10,
    "Luca": 10
}

def split_bill(arg):
    total = sum(arg.values())
    price_each = total / len(arg)
    for key, value in group.items():
        arg[key] = (value - price_each) * -1
    print(arg)
split_bill(group)
"""


#Exponentiation
"""
def expone(base, exponent):
    if exponent == 0:
        return 1
    else:
        exponed = base * expone(base, exponent -1)
        return exponed
print(expone(5,3))
"""

#Zero Sum
"""
def zero_sum(arg):
    zero_summer = []
    for i, el in enumerate(arg):
        for j, ele in enumerate(arg):
            if el + ele == 0:
                to_append = sorted([i, j])
                if to_append not in zero_summer:
                    zero_summer.append(to_append)
    print(zero_summer)

zero_sum([2,4,5,-2,-4,9])
"""


#Letter Counter
"""
def letter_counter(arg):
    upper_list = []
    lower_list = []

    for letter in arg:
        if letter.isupper():
            upper_list.append(letter)
        elif letter.islower():
            lower_list.append(letter)

    print("Upper case letters", len(upper_list))
    print("Lower case letters", len(lower_list))
letter_counter("Hello World")
"""


#Bank Account
"""
def net_amount(arg):
    total = 0

    for el in arg:
        if el[0] == "D":
            total += float(el[2:])
        elif el[0] == "W":
            total -= float(el[2:])
    print(total)

net_amount(["D 300", "D 300", "W 200", "D 100", "D 400"])
"""


#Insane dict
"""
import random
def insane_dict(arg):
    count = 0
    my_dictionary = {}
    if 9 < arg < 1001:
        while count <= arg:
            count += 1
            random_number = random.randint(1, 1000)
            my_dictionary[random_number] = random_number * random_number
        print(my_dictionary)
    else:
        print("Please type a number between 10 and 1000")


insane_dict(15)
"""


#Number to text
import inflect
def number_word(arg):
    p = inflect.engine()
    print(p.number_to_words(arg))

number_word(79)


