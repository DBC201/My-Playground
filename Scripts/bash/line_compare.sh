#!/bin/bash
file1="$1"
file2="$2"
if (( "${#}" > 2 )); then
	echo "Too many files to compare!"
	exit
elif [[ -z "$file1" || -z "$file2" ]]; then
	echo "Not enough parameters"
	exit
fi;
file1_lines=()
while IFS= read -r line
do
	file1_lines["${#file1_lines[@]}"]="$line"
done < "$file1"
line_counter=0
echo "$file1 | $file2"
while IFS= read -r line
do
	if [[ "${file1_lines[$line_counter]}" != "$line" ]]; then	
		echo "$(( $line_counter+1 )): ${file1_lines[$line_counter]} | $line"
	fi;
	(( line_counter+=1 )) 
done < "$file2"	
