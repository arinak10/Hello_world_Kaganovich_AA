#!/bin/bash
df -h | awk 'NR > 1 {print $1, $5} $5 > 90 {print "предупреждение"}' 
