from statistics import mean
import more_itertools


employees = {
    'aslam@example.com': {
        'first_name': 'Aslam',
        'last_name': 'Khan',
        'age': '23',
        'designation': 'software engineer',
        'last_three_scores': [9,3,4]
    },
    'arif@example.com': {
        'first_name': 'Ali',
        'last_name': 'Arif',
        'age': '30',
        'designation': 'software engineer',
        'last_three_scores': [10,8,4]
    },
    'ahsan@example.com': {
        'first_name': 'Ahsan',
        'last_name': 'Ameen',
        'age': '18',
        'designation': 'project manager',
        'last_three_scores': [5,3,2]
    },
    'zain@example.com': {
        'first_name': 'Zain',
        'last_name': 'Malik',
        'age': '32',
        'designation': 'designer',
        'last_three_scores': [5,4,1]
    }
}

def print_employees_by_email():
    print()
    print('(1) Sorted According to Email:\n ')
    myKeys = list(employees.keys())
    myKeys.sort()
    sorted_dict = {i: employees[i] for i in myKeys}
    print(sorted_dict)
    print()



def print_employees_by_age():
    print()
    print('(2) Sorted According to Age in ascending order:\n ')
    list_sorted: list = sorted(employees.items(), key = lambda x:x[1]['age'])
    sorted_dict = dict(list_sorted)
    print(sorted_dict)
    print()



def print_employees_by_age_descending():
    print()
    print('(3) Sorted According to Age in descending order :\n ')
    list_sorted: list = sorted(employees.items(), key = lambda x:x[1]['age'],reverse=True)
    sorted_dict = dict(list_sorted)
    print(sorted_dict)
    print()
    

def print_employees_by_full_name():
    print()
    print('(4) Sorted According to Full Name:\n ')
    list_sorted: list = sorted(employees.items(), key = lambda x:x[1]['first_name'] + x[1]['last_name'])
    sorted_dict = dict(list_sorted)
    print(sorted_dict)


def print_employees_by_full_name_length():
    print()
    print("(5) Sorted According to Full Name Length:\n ")
    list_sorted: list  = sorted(employees.items(), key = lambda x:len(x[1]['first_name'] + x[1]['last_name']))
    sorted_dict = dict(list_sorted)
    print(sorted_dict)


def print_employees_by_avg_last_month_scores():
    print()
    print("(6) Sorted According to last 3 month scores:\n")
    list_sorted = sorted(employees.items(), key=lambda x: mean(x[1]['last_three_scores']))
    sorted_dict = dict(list_sorted)
    first_n = list(sorted_dict.items())[0:3]
    print(first_n)


def print_employee_designations():
    print()
    print("(7) Employee Designations:\n")
    target = "designation"
    res = [val[target] for key, val in employees.items() if target in val]
    res = set(res)
    print('\n'.join(res))



def print_comma_seperated_string():
    print()
    print("(8) Comma Seperated String containing emails of employees:\n ")
    keys_str = ','.join(employees.keys())
    print(keys_str)
    

def main():

    print_employees_by_email()
    print_employees_by_age()
    print_employees_by_age_descending()
    print_employees_by_full_name()
    print_employees_by_full_name_length()
    print_employees_by_avg_last_month_scores()
    print_employee_designations()
    print_comma_seperated_string()

if __name__ == '__main__':
    main()
    