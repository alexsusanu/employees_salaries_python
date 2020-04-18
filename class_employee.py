from func import check_alpha

class Employee():

    def first_name(self):
        print("Insert first name: ", end=" ")
        fname = input().title()
        check_alpha(fname)

    def last_name(self):
        print("Insert last name: ", end=" ")
        return input()

    def age(self):
        print("Insert age: ", end=" ")
        return input()


em = Employee()
em.first_name()
