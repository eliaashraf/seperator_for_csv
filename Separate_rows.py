from pickle import FALSE
import pandas as pd
#import csv 
#import datetime as dt

#Read from the csv file and parse out the timestamp into "Data" 
Data = pd.read_csv('C:\\file_location\\file_name.csv', parse_dates=['Time_stamp'], infer_datetime_format=True)

#Parse out the date from the ISO timestamp and change the format from YYYY-MM-DD to DD-MM-YYYY
Data['Date'] = pd.to_datetime(Data['Time_stamp']).dt.strftime('%d/%m/%Y')

#Parse out the time from the ISO time format and drop everything except HH:MM:SS
Data['Time'] = pd.to_datetime(Data['Time_stamp']).dt.strftime('%H:%M:%S')
#print (Data["Time"])

#Write to a new file (save changes to a new file)
Data.to_csv('C:\\Users\\file_location\\file_name.csv', index=FALSE)



##timestamps = Data.Time_Stamp
##for i in timestamps:
    ##dataobj = datetime.strptime(i, "%d/%m/%Y %H:%M")

##dt['new_date'] = [i.date() for i in Data['Time_Stamp']]
##dt['new_time'] = [i.time() for i in Data['Time_Stamp']]
