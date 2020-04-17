def check_input(type_input, user):
    if type_input == "digit":
        if user.isdigit():
            return 1
        else:
            return 0
    elif type_input == "alpha":
        if user.isalpha():
            return 1
        else:
            return 0

