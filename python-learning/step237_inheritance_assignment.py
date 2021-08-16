class User:
    name = ''
    email = ''
    password = ''
    account_number = 0000

# class Employee, with inheritance from class User, includes of its own attributes.
class Employee(User):
    base_pay = 60000
    department = ''

# class Customer, with inheritance from class User, includes of its own attributes.
class Customer(User):
    mailing_address = ''
    mailing_list = True
