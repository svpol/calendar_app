from calendar import Calendar


class Employee:

    def __init__(self, name, role, location, working_time):
        self.name = name
        self.role = role
        self.location = location
        self.working_time = Calendar.get_working_time(working_time)
        self.calendar = Calendar.get_working_time(working_time)


if __name__ == '__main__':

    mpopova = Employee('Maria Popova', 'accountant', 'Moscow', [[8, 50], [17, 30]])
    print(*mpopova.working_time)

