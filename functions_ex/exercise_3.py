def password_checker(password):
    special_characters = ['!', '#', '$', '%', '&']
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_characters = False

    if len(password) < 12:
        return False

    for character in password:
        if character.isalpha():
            if character.isupper():
                has_upper = True
            if character.islower():
                has_lower = True
        elif character in special_characters:
            has_special_characters = True
        elif character.isdigit():
            has_digit = True

    return has_upper and has_lower and has_special_characters and has_digit


    # if not any(char.isupper() for char in password):
    #     return False
    # if not any(char.islower() for char in password):
    #     return False
    # if not any(char.isalpha() for char in password):
    #     return False
    # if not any(char.isdigit() for char in password):
    #     return False
    # if not any(char in special_characters for char in password):
    #     return False
    #
    # return True

assert(password_checker('8&tSD%EmKke$8rs#')) == True
assert(password_checker('agP#9Y0fUo%i')) == True
assert(password_checker('2v$tqj&x$&1qN4ZYgk')) == True
assert(password_checker('kENb#lv77')) == False
assert(password_checker('770xbi#&!n3e')) == False
assert(password_checker('vfJLD!Nt#Ul')) == False

pwd_tocheck = input("Please provide a password to check: ")
while not password_checker(pwd_tocheck):
    print('This password does not meet the criteria.')
    print()
    pwd_tocheck = input("Please provide a new password to check: ")
print('This password is ok!')
