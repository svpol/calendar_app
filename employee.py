from calendar import Calendar


class Employee:
    """
    The class stores info about each employee.
    """

    def __init__(self, name, role, location, working_time_list):
        self.name = name
        self.role = role
        self.location = location
        self.working_time = Calendar.get_working_time(working_time_list)
        self.calendar = Calendar.working_time_minutes(working_time_list)


if __name__ == '__main__':

    mpopova = Employee('Maria Popova', 'accountant', 'Moscow', [[8, 50], [17, 30]])
    # print(*mpopova.working_time)
    mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [8, 50], [9, 30])
    mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [11, 0], [11, 30])
    print("Maria's available timeslots: {}".format(Calendar.get_available_timeslots(mpopova.calendar)))
    agreen = Employee('Alexander Green', 'programmer', 'Moscow', [[12, 0], [21, 0]])
    # print(*agreen.working_time)
    agreen.calendar = Calendar.book_timeslot(agreen.calendar, [17, 0], [18, 8])
    print("Alexander's available timeslots: {}".format(Calendar.get_available_timeslots(agreen.calendar)))
    sfishman = Employee('Sam Fishman', 'project manager', 'Moscow', [[10, 0], [19, 0]])
    sfishman.calendar = Calendar.book_timeslot(sfishman.calendar, [12, 0], [13, 0])
    sfishman.calendar = Calendar.book_timeslot(sfishman.calendar, [13, 30], [14, 0])
    print("Sam's available timeslots: {}".format(Calendar.get_available_timeslots(sfishman.calendar)))
    print('Common timeslots are: {}'.format(Calendar.get_common_timeslots([mpopova.calendar, agreen.calendar, sfishman.calendar])))