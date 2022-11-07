from calendar import Calendar
# from db_emulation import DataBaseEmulation
# As a real database is not implemented in the project, DataBaseEmulation functions
# will be "called" in the comments.


class Employee:
    """
    The class stores info about each employee.
    """

    def __init__(self, name, role, location, working_time_list):
        """
        Initializes a class object.
        :param name: string, employee's name.
        :param role: string, employee's role.
        :param location: string, employee's residence city.
        :param working_time_list: list, employee's working hours in the format: [[H, M], [H, M]].
        The first nested list is for the hours and minutes of working day beginning,
        The second nested list is for the hours and minutes of working day end, e.g.:
        For standard working hours 9:00 - 18:00 working_time list is [[9, 0], [18, 0]].
        """
        self.name = name
        self.role = role
        self.location = location
        self.working_time = Calendar.get_working_time(working_time_list)
        self.calendar = Calendar.working_time_minutes(working_time_list)


if __name__ == '__main__':

    try:

        mpopova = Employee('Maria Popova', 'accountant', 'Moscow', [[8, 50], [17, 30]])
        # DataBaseEmulation.db_write('Maria Popova')
        # Then mpopova object may be removed and the data about this employee should be fetched from the DB.
        # It can be applied to all objects. But none of them is stired in the database.
        # Assuming, that the object was removed:
        # mpopova_calendar = DataBaseEmulation.db_fetch('Maria Popova', ["calendar"])
        mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [8, 50], [9, 30])
        # DataBaseEmulation.db_write('Maria Popova', ["calendar"])
        # mpopova_calendar = DataBaseEmulation.db_fetch('Maria Popova', ["calendar"])
        mpopova.calendar = Calendar.book_timeslot(mpopova.calendar, [11, 0], [11, 30])
        # DataBaseEmulation.db_write('Maria Popova', ["calendar"])
        # mpopova_calendar = DataBaseEmulation.db_fetch('Maria Popova', ["calendar"])
        print("Maria's available timeslots: {}".format(Calendar.get_available_timeslots(mpopova.calendar)))
        agreen = Employee('Alexander Green', 'programmer', 'Moscow', [[12, 0], [21, 0]])
        # DataBaseEmulation.db_write('Alexander Green')
        # agreen_calendar = DataBaseEmulation.db_fetch('Alexander Green', ["calendar"])
        agreen.calendar = Calendar.book_timeslot(agreen.calendar, [17, 0], [18, 8])
        # DataBaseEmulation.db_write('Alexander Green', ["calendar"])
        # agreen_calendar = DataBaseEmulation.db_fetch('Alexander Green', ["calendar"])
        print("Alexander's available timeslots: {}".format(Calendar.get_available_timeslots(agreen.calendar)))
        sfishman = Employee('Sam Fishman', 'project manager', 'Moscow', [[10, 0], [19, 0]])
        # DataBaseEmulation.db_write('Sam Fishman')
        # sfishman_calendar = DataBaseEmulation.db_fetch('Sam Fishman', ["calendar"])
        sfishman.calendar = Calendar.book_timeslot(sfishman.calendar, [12, 0], [13, 0])
        # DataBaseEmulation.db_write('Sam Fishman', ["calendar"])
        # sfishman_calendar = DataBaseEmulation.db_fetch('Sam Fishman', ["calendar"])
        sfishman.calendar = Calendar.book_timeslot(sfishman.calendar, [13, 30], [14, 0])
        # DataBaseEmulation.db_write('Sam Fishman', ["calendar"])
        # sfishman_calendar = DataBaseEmulation.db_fetch('Sam Fishman', ["calendar"])
        print("Sam's available timeslots: {}".format(Calendar.get_available_timeslots(sfishman.calendar)))
        # mpopova_calendar = DataBaseEmulation.db_fetch('Maria Popova', ["calendar"])
        # agreen_calendar = DataBaseEmulation.db_fetch('Alexander Green', ["calendar"])
        # sfishman_calendar = DataBaseEmulation.db_fetch('Sam Fishman', ["calendar"])
        print('Common timeslots are: {}'.format(Calendar.get_common_timeslots(
            [mpopova.calendar, agreen.calendar, sfishman.calendar])))

    except TypeError:
        print('Key Type error')
