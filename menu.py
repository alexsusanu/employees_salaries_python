class Menu():
    @staticmethod
    def print_menu():
        print("Welcome to Employees DB")
        print(40 * "-")
        print("Please select from the following options")
        print("1.View salaries \t2.View total payroll")
        print("3.View average salary \t4.View average salary by age")
        print("5.View % reduction \t6.Exit")

    def view_salaries():
        print("selected view salaries")

    def total_payroll():
        print("selected view total payroll")

    def average_salary():
        print("selected view average salary")

    def average_salary_age():
        print("selected view salaries by age")

    def perc_reduction():
        print("selected view % reduction")

