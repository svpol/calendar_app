This is a calendar implementation with the following specifics:

* The calendar works within a single day.
* You can do the following manipulations:
  * See an employee's total working hours for a day.
  * See an employee's available timeslots for booking.
  * Book a timeslot.
 
There are 3 Python files:
1. calendar.py - contains the Calendar class responsible for all manipulations with the calendars.
2. employee.py contains the Employee class to store data about employees. Also there is a simple script to illustrate the work with the calendar.
3. main.py - a script that accepts an employee list and then returns the time intervals available for all the listed employees.