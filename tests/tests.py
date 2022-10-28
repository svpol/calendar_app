from calendar import Calendar
from datetime import time


def test_working_time_minutes():
    assert Calendar.working_time_minutes([[9, 0], [9, 10]]) == \
           [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550]
    return 'test_working_time_minutes paased'


def test_get_working_time():
    assert Calendar.get_working_time([[9, 0], [18, 0]]) == [time(9, 0), time(18, 0)]
    return 'test_get_working_time passed'


def test_get_available_timeslots():
    assert Calendar.get_available_timeslots(
        [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 571, 572, 573, 574, 575,
         576, 577, 578, 579, 596, 597, 598, 599, 600]) == [['9:00', '9:09'], ['9:31', '9:39'], ['9:56', '10:00']]
    return 'test_get_available_timeslots passed'


def test_book_timeslot():
    assert Calendar.book_timeslot(
        [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554,
         555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569,
         570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584,
         585, 586, 587, 588, 589, 590], [9, 10], [9, 30]) == \
           [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 571, 572, 573, 574,
            575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590]
    return 'test_book_timeslot passed'


def test_get_common_timeslots():
    assert Calendar.get_common_timeslots(
        [[540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550,
          551, 552, 553, 554, 555, 556, 557, 558, 559, 560],
         [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550],
         [545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555]]) == [['9:05', '9:10']]
    return 'test_get_common_timeslots passed'


if __name__ == '__main__':

    print(test_working_time_minutes())
    print(test_get_working_time())
    print(test_get_available_timeslots())
    print(test_book_timeslot())
    print(test_get_common_timeslots())

