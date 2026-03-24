#!/bin/bash
read -p "Введите массу (кг, целое): " WEIGHT
read -p "Введите рост (м): " HEIGHT
bmi=$((WEIGHT/HEIGHT**2))
echo "ИМТ: $bmi"
