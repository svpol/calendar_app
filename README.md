# Intro

This is a calendar implementation with the following specifics:

* The calendar works within a single day.
* You can do the following manipulations:
  * See an employee's total working hours for a day.
  * See an employee's available timeslots for booking.
  * Book a timeslot.
  * See the timeslots available for all of the employees provided as a list. 

# Structure overview

There are 3 Python files:
1. calendar.py - contains the `Calendar` class responsible for all manipulations with the calendars.
2. employee.py - contains the `Employee` class to store data about employees. 
   Also there is a **script** to illustrate the work with the calendar.
3. db_emulation.py - contains the `DataBaseEmulation` class. Its functions are just placeholders, they are not truly implemented as no real database is used in the project.