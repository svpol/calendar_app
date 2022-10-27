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
        available_timeslots = []
        slot_before = [calendar[0], time(time_start[0])]
        slot_after = [time(time_end[1]), calendar[1]]


if __name__ == '__main__':

    wl = Calendar.get_working_time([[8, 50], [17, 50]])
    # print(Calendar.show_working_time([[8, 50], [19, 0]]))
    print(*wl)
