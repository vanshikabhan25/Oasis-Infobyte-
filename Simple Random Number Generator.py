import random
import string

print("Welcome to Python Project 1 - Simple Random Number Generator!!!")
letters = string.ascii_letters
digits = string.digits
Special_chars = string.punctuation
letters_list = list(letters)
digits_list = list(digits)
Special_list = list(Special_chars)
_letters = int(input(f"How many Letters are there in the passcode in the project 1 ? \n"))
_digits = int(input(f"How many digits are there in the passcode in the project 1 ? \n"))
_SpecialChars = int(input(f"How many Special Chars are there in the project 1 ? \n"))

Passcode = []
ResultantPasscode = []
counter_l = 0
for l in letters_list:
    Passcode.append(random.choice(letters_list))
    counter_l += 1
    if counter_l == _letters:
        break

counter_d = 0
for d in digits_list:
    Passcode.append(random.choice(digits_list))
    counter_d += 1
    if counter_d == _digits:
        break

counter_S = 0
for S in Special_list:
    Passcode.append(random.choice(Special_list))
    counter_S += 1
    if counter_S == _SpecialChars:
        break
P_count = 0
for P in Passcode:
    ResultantPasscode.append(random.choice(Passcode))
    P_count += 1
    if P_count == len(Passcode):
        break

print("".join(ResultantPasscode))
