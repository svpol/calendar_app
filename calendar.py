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
            time_start = str(slot[0] // 60) + ':' + str(slot[0] % 60)
            time_end = str(slot[1] // 60) + ':' + str(slot[1] % 60)
            timeslots.append([time_start, time_end])
        return timeslots

    @staticmethod
    def book_timeslot(calendar, time_start, time_end):
        time_start_minutes = Calendar._map_time_to_minutes(time_start)
        time_end_minutes = Calendar._map_time_to_minutes(time_end)
        occupied_slot = list(range(time_start_minutes, time_end_minutes+1))
        for i in occupied_slot:
            if i in calendar:
                calendar.remove(i)
        return calendar
