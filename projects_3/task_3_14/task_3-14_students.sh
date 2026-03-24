#!/bin/bash
echo "Имя: "
awk '{print $1}' students.txt
echo "Оценки: "
awk '{print $2}' students.txt
echo "Номер строки и имя: "
awk '{print NR, $2}' students.txt
