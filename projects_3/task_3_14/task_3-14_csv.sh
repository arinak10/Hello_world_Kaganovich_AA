#!/bin/bash
echo "Названия товаров: "
awk -F "," '{print $2}' data.txt
echo "Товары дороже 20: "
awk -F "," '$3 > 20 {print $2}' data.txt
echo "Общая стоимость: "
awk -F "," '{sum += $3} END {print sum}' data.txt
