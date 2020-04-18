from menu import Menu

def check_digit(user):
    """ check digit """
    while True:
        if user.isdigit():
            return int(user)
        else:
            print("Digits only, retry: ", end=" ")
            user = input()


def check_alpha(user):
    """ check alpha """
    while True:
        if user.isalpha():
            return user.title()
        else:
            print("Alpha only, retry: ", end=" ")
            user = input()

def check_menu():
    """ repeat menu if invalid input option """
    options = { 1: Menu.view_salaries,
                2: Menu.total_payroll,
                3: Menu.average_salary,
                4: Menu.add_employee,
                5: Menu.perc_reduction,
                6: exit,
    }
    
    while True:
        menu_selection = input()
        menu_selection = check_digit(menu_selection)
        if menu_selection in options.keys():
            options[int(menu_selection)]()
            break
        else:
            print("Invalid digit, try again: ", end=" ")
