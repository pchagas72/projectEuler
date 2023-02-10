#!/bin/bash

declare -i sum=0
for i in {1..1000};do
	declare -i remainderThree=$(expr $i % 3)
	declare -i remainderFive=$(expr $i % 5)
	if [ $remainderThree -eq 0 ] || [ $remainderFive -eq 0 ]
	then sum+=$i
	fi
done
echo $sum
