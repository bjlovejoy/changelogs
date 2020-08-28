#!/bin/bash

#Here are the original alias commands:
#   alias d1="date +'%m_%d_%y' | sed 's/^0*//'"
#   alias d='nano "/home/brendon/Documents/changelogs/$(d1)"'


if (( $# > 2 ))
then
    echo "Too many arguments."
    exit 1  #operation not permitted
else
    
    if [ $# -eq 1 ]
    then
        year=$(date +'%Y')
        FILE=/home/brendon/Documents/changelogs/$year/$1
        if [ ! -f "$FILE" ]
        then
            echo "File does not exist; check year."
            echo "Do not enter the full filepath, only the changelog (arg=mm_dd)"
            exit 2  #file or directory not found
        else
            day=$1
        fi
    elif [ $# -eq 2 ]
    then
        FILE=/home/brendon/Documents/changelogs/$2/$1
        if [ ! -f "$FILE" ]
        then
            echo "File does not exist."
            echo "Do not enter the full filepath (arg1=mm_dd, arg2=yyyy)"
            exit 2  #file or directory not found
        else
            year=$2
            day=$1
        fi
    else
        year=$(date +'%Y')
        day=$(date +'%m_%d')
        today2=$(date +'%B %d, %Y')
        
        mkdir -p /home/brendon/Documents/changelogs/$year
        FILE=/home/brendon/Documents/changelogs/$year/$day
        if [ ! -f "$FILE" ]
        then
            echo "Creating today's changelog"
            echo -e "NOTES: \n\n$today2\n\n" > $FILE
        fi

    fi
    
    if [ ! -f "$FILE" ]
    then
        echo "How the hell?"
    else
        nano $FILE
    fi
    python3 -B /home/brendon/Documents/changelogs/scripts/description_update.py $year $day
    echo 'Done'
fi
