import sqlite3

from func import check_input
from menu import Menu

options = { 1: Menu.view_salaries,
            2: Menu.total_payroll,
            3: Menu.average_salary,
            4: Menu.average_salary_age,
            5: Menu.perc_reduction,
            6: exit,
}

Menu.print_menu()
flag = True
while (flag):
    menu_selection = input()
    if (check_input("digit", menu_selection)):
        menu_selection = int(menu_selection)
        if menu_selection in options.keys():
            options[int(menu_selection)]()
            flag = False
        else:
            print("Invalid digit, try again: ", end=" ")
    else:
        print("Digits only. See menu options. Retry: ", end=" ")
