from datetime import time


class Calendar:

    @staticmethod
    def get_working_time(working_time):
        day_start = time(working_time[0][0], working_time[0][1])
        day_end = time(working_time[1][0], working_time[1][1])
        return [day_start, day_end]

    @staticmethod
    def get_available_timeslots(calendar):
        pass

    @staticmethod
    def book_timeslot(calendar, time_start, time_end):
        updated_calendar = []
        time_start_time = time(time_start[0], time_start[1])
        time_end_time = time(time_end[0], time_end[1])
        if time_start_time > calendar[0]:
            slot_before = [calendar[0], time_start_time]
            slot_after = [time_end_time, calendar[1]]

        pass


if __name__ == '__main__':

    wl = Calendar.get_working_time([[8, 50], [17, 50]])
    print(*wl)

    slotted = Calendar.book_timeslot(wl, [10, 30], [11, 30])

    for i in slotted:
        print(*i)
