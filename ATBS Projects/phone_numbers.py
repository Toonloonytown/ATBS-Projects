def is_phone_number(number):
    if len(number) != 12: 
        return False
    for i in range(len(number)):
        if i < 3:
            if not number[i].isdecimal(): return False
        elif (i == 3):
            if (number[i] != '-'): return False
        elif (i < 7):
            if not number[i].isdecimal():
                return False
        elif (i == 8):
            if number[i] != '-': return False
        else:
            if (not number[i].isdecimal()): 
                return False
    return True

print("Phone Number Test:")
print("Is 464-888-9323 a phone number: ")
print(is_phone_number("464-888-9323"))
print("is Hello World a phone number: ")
print(is_phone_number("Hello World"))
