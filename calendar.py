from datetime import time


DAYTIME = list(range(1440))


class Calendar:
    """
    This class is responsible for all operations with an employee calendar: shows working hours
    and available timeslots, allows to book free timeslots.
    """

    @staticmethod
    def _map_time_to_minutes(time_list):
        """
        Maps human-readable time format of type "HH:MM" to the DAYTIME format: there are 1440 a day,
        thus, we can map any time with minute accuracy to this format.
        :param time_list: list with 2 values - hours and minutes, e.g.: 8:30 is [8, 30]
        :return: An integer, an absolute minute value for a specified time value.
        """
        abs_miniute = time_list[0] * 60 + time_list[1]
        return abs_miniute

    @staticmethod
    def working_time_minutes(working_time_list):
        """
        Returns all the time an employee is going to be at work today.
        :param working_time_list: A list of 2 lists: working day start time and working day end time.
        Each nested list contains 2 values: hours and minutes. E.g. 9:00 - 18:30 working hours will be
        [[9, 0], [18, 30]]
        :return: Working hours in DAYTIME absolute minute format, e.g. [950, 1050].
        """
        day_start = Calendar._map_time_to_minutes(working_time_list[0])
        day_end = Calendar._map_time_to_minutes(working_time_list[1])
        return DAYTIME[day_start:day_end+1]

    @staticmethod
    def get_working_time(working_time_list):
        """
        Returns an employee's working hours in the human-readable format.
        :param working_time_list: A list of 2 lists: working day start time and working day end time.
        Each nested list contains 2 values: hours and minutes. E.g. 9:00 - 18:30 working hours will be
        [[9, 0], [18, 30]]
        :return: A list of strings with time values, e.g.: ['9:00', '18:00'].
        """
        day_start = time(working_time_list[0][0], working_time_list[0][1])
        day_end = time(working_time_list[1][0], working_time_list[1][1])
        return [day_start, day_end]

    @staticmethod
    def get_available_timeslots(calendar):
        """
        Returns an employee's free timeslots available for booking.
        :param calendar: A calendar represented with a list of integers indicating available minutes.
        :return: A list of lists with available timeslots, e.g.: [['9:31', '10:59'], ['11:31', '17:30']]
        """
        available_slots = []
        timeslots = []
        c = 0
        for i in range(len(calendar) - 1):
            if calendar[i + 1] - calendar[i] > 1:
                available_slots.append([calendar[c], calendar[i]])
                c = i + 1
            elif i + 1 == len(calendar) - 1:
                available_slots.append([calendar[c], calendar[i+1]])
        for slot in available_slots:
            minute_chars_start = str(slot[0] % 60)
            if minute_chars_start in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                minute_chars_start = '0' + minute_chars_start
            minute_chars_end = str(slot[1] % 60)
            if minute_chars_end in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                minute_chars_end = '0' + minute_chars_end
            time_start = str(slot[0] // 60) + ':' + minute_chars_start
            time_end = str(slot[1] // 60) + ':' + minute_chars_end
            timeslots.append([time_start, time_end])
        return timeslots

    @staticmethod
    def book_timeslot(calendar, time_start, time_end):
        """
        Books a timeslot.
        :param calendar: A calendar represented with a list of integers indicating available minutes.
        :param time_start: The time when the interval being booked starts with. A list of 2 values: hours and
        minutes, e.g: [10, 30] for 10:30.
        :param time_end: The time when the interval being booked ends by. A list of 2 values: hours and
        minutes, e.g: [11, 20] for 11:20.
        :return: an updated calendar, where the booked time interval is absent.
        """
        time_start_minutes = Calendar._map_time_to_minutes(time_start)
        time_end_minutes = Calendar._map_time_to_minutes(time_end)
        occupied_slot = list(range(time_start_minutes, time_end_minutes+1))
        for i in occupied_slot:
            if i in calendar:
                calendar.remove(i)
        return calendar

    @staticmethod
    def get_common_timeslots(calendars):
        """
        Gets available timeslots common for all of the employees.
        :param calendars: A list of lists with employees' calenders.
        :return: A list of lists with time intervals available for all employees.
        """
        minute_intervals = list(set.intersection(*map(set, calendars)))
        timeslots = Calendar.get_available_timeslots(minute_intervals)
        return timeslots
