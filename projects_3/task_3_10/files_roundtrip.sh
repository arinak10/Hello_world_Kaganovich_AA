#!/bin/bash
for i in {1..10}; do
 touch "test$i.txt"
done
echo "Файлы успешно созданы"
i=10
while [ "$i" -ge 1 ]; do 
 rm "test$i.txt"
i=$((i - 1))
done
echo "Файлы успешно удалены"
