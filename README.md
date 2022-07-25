# seperator_for_csv

This program helps to parse out date and time from a timestamp in the ISO format. It uses the software library in Python called Panda to seperate out time and date from the timestamp.

We first read in the file, parse out the date and time information and then save the date in DD-MM-YYYY format and the time in HH:MM:SS. It drops out all the other unnecesary information and stores the time and date as new columns within a new CSV file.
