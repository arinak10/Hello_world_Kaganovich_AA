printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do 
 if [ ! -s "$file" ]; then
  continue
 fi
 sequence=grep -v "^>" "$file"
 A=$(echo "$sequence" | grep -o "A" | wc -l)
 T=$(echo "$sequence" | grep -o "T" | wc -l)
 G=$(echo "$sequence" | grep -o "G" | wc -l)
 C=$(echo "$sequence" | grep -o "C" | wc -l)
 printf "%-15s %-5d %-5d %-5d %-5d\n" "$file" "$A" "$T" "$G" "$C"
done
