#!/bin/bash
echo "Выше 80: "
awk '$2 > 80 {print $1}' students.txt
echo "Ниже 70: "
awk '$2 < 70 {print $1}' students.txt
echo "Первая строка: " 
awk 'NR==1' students.txt
