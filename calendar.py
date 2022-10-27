from datetime import time


DAYTIME = list(range(1440))


class Calendar:

    @staticmethod
    def _map_time_to_minutes(time_list):
        abs_miniute = time_list[0] * 60 + time_list[1]
        return abs_miniute

    @staticmethod
    def working_time_minutes(working_time_list):
        day_start = Calendar._map_time_to_minutes(working_time_list[0])
        day_end = Calendar._map_time_to_minutes(working_time_list[1])
        return DAYTIME[day_start:day_end+1]

    @staticmethod
    def get_working_time(working_time_list):
        day_start = time(working_time_list[0][0], working_time_list[0][1])
        day_end = time(working_time_list[1][0], working_time_list[1][1])
        return [day_start, day_end]

    @staticmethod
    def get_available_timeslots(calendar):
        pass

    @staticmethod
    def book_timeslot(calendar, time_start, time_end):
        time_start_minutes = Calendar._map_time_to_minutes(time_start)
        time_end_minutes = Calendar._map_time_to_minutes(time_end)
        occupied_slot = list(range(time_start_minutes, time_end_minutes+1))
        for i in occupied_slot:
            if i in calendar:
                calendar.remove(i)
        return calendar




if __name__ == '__main__':

    wl = Calendar.get_working_time([[8, 50], [17, 50]])
    print(*wl)

    # slotted = Calendar.book_timeslot(wl, [10, 30], [11, 30])
    #
    # for i in slotted:
    #     print(*i)

    print(DAYTIME)
