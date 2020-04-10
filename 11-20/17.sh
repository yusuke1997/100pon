
cut -f 1 < hightemp.txt | sort -u
echo ""
cut -f 1 < hightemp.txt | sort | uniq
