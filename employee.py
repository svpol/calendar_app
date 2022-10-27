from calendar import Calendar


class Employee:

    def __init__(self, name, role, location, working_time_list):
        self.name = name
        self.role = role
        self.location = location
        self.working_time = Calendar.get_working_time(working_time_list)
        self.calendar = Calendar.working_time_minutes(working_time_list)


if __name__ == '__main__':

    mpopova = Employee('Maria Popova', 'accountant', 'Moscow', [[8, 50], [17, 30]])
    print(*mpopova.working_time)
    # print(mpopova.calendar)
    mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [9, 00], [9, 30])
    # print(mpopova.calendar)
    print(Calendar.get_available_timeslots(mpopova.calendar))
    mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [11, 00], [11, 30])
    print(Calendar.get_available_timeslots(mpopova.calendar))

