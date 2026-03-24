#!/bin/bash
check_root() {
 if [ "$EUID" -ne 0 ]; then
  echo "Ошибка: Этот скрипт должен быть запущен от имени суперпользователя"
  exit
 fi
}
