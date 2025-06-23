#! /bin/bash
echo "ُEnter Your Grade"
read grade

if [ $grade -ge 90 ];
then
    echo "The Grade is Excellant"
elif [ $grade -ge 80 ];
then
    echo "The Grade is Very Good"
elif [ $grade -ge 70 ];
then
    echo "Grade is Good"
elif [ $grade -ge 0 ]
then
    echo " The grade is Fail"

fi