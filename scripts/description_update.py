import sys

file_date = str(sys.argv[2])

year  = str(sys.argv[1])
month = int(file_date.split('_')[0])
day   = int(file_date.split('_')[1])

#c = changelog
#d = description log

c_path = '/home/brendon/Documents/changelogs/' + year + '/' + file_date
d_path = '/home/brendon/Documents/changelogs/description_logs/' + year

with open(c_path, 'r') as c_log:
    description = c_log.readline()
    description = description[7:-1]   #This removes the "NOTES: " preface and the newline

d_all = list()              #contains only the dates on the lines
d_entire_contents = list()  #contatins the entire contents

with open(d_path, 'a+') as d_log:  #Creates description log if does not exist
    d_log.seek(0)                       #Move cursor to beginning of file
    for line in d_log:
        d_entire_contents.append(line)
        d_all.append(line.split()[0][:-1])  #This gets the date and removes the ':'



#dont forget to seperate the item in d_all to the month and date using .split('_')
#when using year, month, day, they are strings, convert to int for comparison

"""
    current date < stored date : move on to next entry
    current date = stored date : now iterate by days (same structure as all of this)
    current date > stored date : place entry at previous position (.insert())
    (above shouldn't happen unless manually creating changelog for past day)
    
    insert if does not exist, replace if it does
    
********May need to go back and read everything into buffer to write back
"""

finding_date = True
loc = 0  #location to input (line number, list element)
d_size = len(d_all)

while finding_date and loc < d_size:

    file_month = int(d_all[loc][0:2])

    if month == file_month:
    
        file_day = int(d_all[loc][3:5])
        
        if day == file_day:
            finding_date = False
            d_entire_contents[loc] = file_date + ': ' + description + '\n'
        
        elif file_day > day:
            finding_date = False
            d_entire_contents.insert(loc, file_date + ': ' + description + '\n')
            
        else:
            loc += 1
            
    elif file_month > month:
        finding_date = False
        d_entire_contents.insert(loc, file_date + ': ' + description + '\n')
    
    else:  #file_month < month
        loc += 1


if loc >= d_size:
    d_entire_contents.append(file_date + ': ' + description + '\n')

while '\n' in d_entire_contents:    #remove any unwanted newlines
    d_entire_contents.remove('\n')

with open(d_path, 'w') as log_d:
    log_d.writelines(d_entire_contents)



