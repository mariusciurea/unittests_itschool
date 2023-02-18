"""module with functions that need to be tested"""


def employee_details(name, age, email, amount, nb_working_days):
    if type(nb_working_days) != int:
        raise TypeError('Provide an integer')

    if nb_working_days == 0:
        raise ZeroDivisionError('You cannot divide by 0')

    hourly_income = amount/(nb_working_days * 8)
    return f'Welcome {name}. Your age is {age} years old.' \
           f'Your email address: {email} ' \
           f'and hourly income: {hourly_income}'


if __name__ == '__main__':
    print(employee_details('Marius', 31, 'mciurea@gmail.com', 5000, 21))